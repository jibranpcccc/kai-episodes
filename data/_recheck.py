#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_recheck.py - "press one button and it proves everything" for a built
Byte Forensics episode.

    python data/_recheck.py BYTE-EP09-KV spec_ep09_full

Re-verifies the built deliverable (self contained html + srt + chapters)
against the spec module and prints exactly one PASS/FAIL/WARN line per
check.  Exit status is 0 when every check passed and 1 otherwise.

Standard library only.  Never crashes on a missing artifact: a missing
file becomes a FAIL line, never a traceback.
"""

from __future__ import annotations

import base64
import binascii
import html as htmllib
import importlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

# --------------------------------------------------------------------------
# configuration
# --------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

MIN_HTML_BYTES = 500 * 1024
MAX_WINDOW_SECONDS = 19.0
MAX_CUE_WORDS = 12
MIN_CUE_WORDS = 2
CAPTION_GAP_TOLERANCE_MS = 1000
LOUDNESS_MIN_LUFS = -15.0
LOUDNESS_MAX_LUFS = -13.0
TRUE_PEAK_MAX_DBFS = -1.2

CHAPTER_LINE_RE = re.compile(r"^\s*(\d{1,3}):([0-5]\d)\s+(.+?)\s+(\d{1,2})\s*$")
TS_RE = re.compile(r"(\d{1,3}:\d{2}:\d{2})([.,])(\d{1,3})")
TS_LINE_RE = re.compile(r"(\d{1,3}:\d{2}:\d{2}[.,]\d{1,3})\s*-->\s*(\d{1,3}:\d{2}:\d{2}[.,]\d{1,3})")

# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------

PUNCT = ".,;:!?\"'()[]{}—–-…«»“”‘’*/\\|"


def norm_ws(text) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def words_of(text) -> list:
    """Word tokens: whitespace split, outer punctuation stripped, lower-cased."""
    out = []
    for token in (text or "").split():
        token = token.strip(PUNCT)
        if token:
            out.append(token.lower())
    return out


def wfield(window, key, default=""):
    if isinstance(window, dict):
        value = window.get(key, default)
    else:
        value = getattr(window, key, default)
    return default if value is None else value


def fmt_bytes(n: int) -> str:
    return f"{n:,}"


def clip(text: str, limit: int = 90) -> str:
    text = norm_ws(text)
    return text if len(text) <= limit else text[: limit - 1] + "\u2026"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def is_standalone_token(markup: str, start: int, end: int) -> bool:
    """True when the token is the whole text node or the whole attribute value."""
    token = markup[start:end]
    lo = markup.rfind(">", 0, start)
    hi = markup.find("<", end)
    if lo != -1 and hi != -1 and markup[lo + 1:hi].strip() == token:
        return True
    i = start
    while i > 0 and markup[i - 1] in " \t":
        i -= 1
    if i > 0 and markup[i - 1] in "\"'":
        quote = markup[i - 1]
        if end < len(markup) and markup[end] == quote:
            j = i - 2
            while j >= 0 and markup[j] in " \t":
                j -= 1
            if j >= 0 and markup[j] == "=":
                return True
    return False


def strip_script_contents(markup: str) -> str:
    """Remove <script>/<style> bodies but keep their opening tags."""
    out = re.sub(r"<script\b([^>]*)>.*?</script>", r"<script\1>", markup, flags=re.S | re.I)
    out = re.sub(r"<style\b([^>]*)>.*?</style>", r"<style\1>", out, flags=re.S | re.I)
    return out


def visible_markup(markup: str) -> str:
    """Markup with script/style bodies and data: payload blobs removed."""
    out = re.sub(r"<script\b[^>]*>.*?</script>", " ", markup, flags=re.S | re.I)
    out = re.sub(r"<style\b[^>]*>.*?</style>", " ", out, flags=re.S | re.I)
    out = re.sub(r"data:[^\s\"'()<>]+", " ", out)
    return out


ATTR_RE = re.compile(r"([A-Za-z_:][-A-Za-z0-9_:.]*)\s*=\s*(\"([^\"]*)\"|'([^']*)'|([^\s>]+))")


def parse_attrs(chunk: str) -> dict:
    attrs = {}
    for m in ATTR_RE.finditer(chunk or ""):
        name = m.group(1).lower()
        value = m.group(3)
        if value is None:
            value = m.group(4)
        if value is None:
            value = m.group(5)
        attrs[name] = value or ""
    return attrs


def class_tokens(markup: str):
    for m in re.finditer(r"class\s*=\s*[\"']([^\"']*)[\"']", markup or "", re.I):
        for tok in m.group(1).split():
            yield tok


def has_class_token(markup: str, wanted: str) -> bool:
    for tok in class_tokens(markup):
        low = tok.lower()
        if low == wanted or low.endswith("__" + wanted) or low.endswith("-" + wanted) \
                or low.endswith("_" + wanted):
            return True
    return False


# --------------------------------------------------------------------------
# html structure helpers
# --------------------------------------------------------------------------

SECTION_TAG_RE = re.compile(r"<section\b([^>]*)>", re.I)


def find_scenes(markup: str) -> list:
    """Return one entry per <section class="scene" data-scene="N"> block."""
    tags = list(SECTION_TAG_RE.finditer(markup))
    starts = []
    for m in tags:
        attrs = parse_attrs(m.group(1))
        classes = attrs.get("class", "").split()
        if "scene" in classes or "data-scene" in attrs:
            starts.append((m, attrs))
    scenes = []
    for i, (m, attrs) in enumerate(starts):
        end = starts[i + 1][0].start() if i + 1 < len(starts) else len(markup)
        scenes.append({
            "attrs": attrs,
            "block": markup[m.end():end],
            "tag": m.group(0),
            "start": m.start(),
            "end": end,
        })
    return scenes


def split_top_level(text: str) -> list:
    """Split a JS array body on top level commas."""
    parts, depth, buf, quote = [], 0, [], None
    for ch in text:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in "\"'`":
            quote = ch
            buf.append(ch)
            continue
        if ch in "[{(":
            depth += 1
        elif ch in "]})":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append("".join(buf))
            buf = []
            continue
        buf.append(ch)
    if "".join(buf).strip():
        parts.append("".join(buf))
    return parts


def balanced_array(text: str, start: int):
    """Return the array text that starts at text[start] == '[' (quotes aware)."""
    if start >= len(text) or text[start] != "[":
        return None
    depth = 0
    quote = None
    for i in range(start, len(text)):
        ch = text[i]
        if quote:
            if ch == quote:
                quote = None
            continue
        if ch in "\"'`":
            quote = ch
            continue
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                return text[start:i + 1]
    return None


def cumulative_spans(durations):
    spans = []
    t = 0.0
    for d in durations:
        spans.append((t, t + d))
        t += d
    return spans


def extract_scene_timing(markup: str, scenes: list, windows: list):
    """Return (spans, source).  spans is a list of (start_s, end_s) or None.

    The timing data is read from the html itself, so it is available even when
    no spec module could be imported.
    """
    count = len(windows) if windows else None

    # 1. a JSON scene table: "scenes":[{"id":0,"s":0.0,"e":10.8}, ...]
    for m in re.finditer(r"\"scenes\"\s*:\s*\[", markup):
        arr = balanced_array(markup, m.end() - 1)
        if not arr:
            continue
        try:
            data = json.loads(arr)
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(data, list) or not data:
            continue
        spans = []
        for entry in data:
            if not isinstance(entry, dict):
                spans = []
                break
            start = entry.get("s", entry.get("start", entry.get("t0")))
            end = entry.get("e", entry.get("end", entry.get("t1")))
            try:
                spans.append((float(start), float(end)))
            except (TypeError, ValueError):
                spans = []
                break
        if spans:
            return spans, "html scene table (JSON scenes[])"

    # 2. a per scene duration attribute
    attrs_durs = []
    for sc in scenes:
        value = None
        for key in ("data-dur", "data-scene-dur", "data-duration", "data-seconds", "data-len"):
            if key in sc["attrs"]:
                value = sc["attrs"][key]
                break
        if value is None:
            m = re.search(r"\bdata-(?:dur|duration|scene-dur)\s*=\s*[\"']?([0-9]*\.?[0-9]+)",
                          sc["block"], re.I)
            if m:
                value = m.group(1)
        try:
            attrs_durs.append(float(value) if value is not None else None)
        except (TypeError, ValueError):
            attrs_durs.append(None)
    if attrs_durs and all(d is not None for d in attrs_durs):
        return cumulative_spans(attrs_durs), "html scene data-dur attributes"

    # 3. a JS scene table with per scene durations
    for name in ("SCENES", "scenes", "SCENE_TABLE", "sceneTable", "SCENE_DATA", "sceneData"):
        m = re.search(r"\b" + name + r"\s*=\s*\[", markup)
        if not m:
            continue
        body = balanced_array(markup, m.end() - 1)
        if body is None:
            continue
        durs = []
        for entry in split_top_level(body[1:-1]):
            dm = re.search(r"\b(?:dur|duration|secs|seconds|len|length)\s*:\s*([0-9]*\.?[0-9]+)",
                           entry, re.I)
            if dm:
                durs.append(float(dm.group(1)))
                continue
            nm = re.fullmatch(r"\s*([0-9]*\.?[0-9]+)\s*,?\s*", entry)
            if nm:
                durs.append(float(nm.group(1)))
        if durs:
            return cumulative_spans(durs), "html JS scene table (%s)" % name

    # 4. the duration is carried by the spec windows themselves
    spec_durs = []
    for w in windows:
        value = None
        for key in ("dur", "duration", "secs", "seconds", "len"):
            raw = wfield(w, key, None)
            if isinstance(raw, (int, float)) and not isinstance(raw, bool):
                value = float(raw)
                break
        if value is None:
            spec_durs = []
            break
        spec_durs.append(value)
    if spec_durs and len(spec_durs) == count:
        return cumulative_spans(spec_durs), "spec window durations (no timing data in the html)"

    # 5. fallback: count the beats of every scene
    beats = []
    for sc in scenes:
        n = len(re.findall(r"\bdata-beat\b", sc["block"], re.I))
        if n == 0:
            n = sum(1 for tok in class_tokens(sc["block"]) if "beat" in tok.lower())
        beats.append(n)
    if beats and any(b > 0 for b in beats):
        return None, "beat counts per scene (no duration data found in the html)"

    return None, "no timing data found"


def extract_audio_b64(markup: str):
    """Return (mime, payload) of the largest embedded audio data URI."""
    best = None
    for m in re.finditer(r"data:(audio/[A-Za-z0-9.+-]+);base64,", markup):
        i = m.end()
        j = i
        n = len(markup)
        while j < n:
            c = markup[j]
            if c in " \t\r\n":
                j += 1
                continue
            if c.isalnum() or c in "+/=":
                j += 1
                continue
            break
        payload = "".join(markup[i:j].split())
        if not payload:
            continue
        if best is None or len(payload) > len(best[1]):
            best = (m.group(1), payload)
    return best


# --------------------------------------------------------------------------
# caption helpers
# --------------------------------------------------------------------------

def ts_to_ms(ts: str):
    m = re.match(r"\s*(\d{1,3}):(\d{2}):(\d{2})([.,])(\d{1,3})", ts)
    if not m:
        return None
    frac = m.group(5).ljust(3, "0")
    return ((int(m.group(1)) * 60 + int(m.group(2))) * 60 + int(m.group(3))) * 1000 + int(frac)


def parse_srt(text: str):
    """Return (cues, raw_blocks)."""
    cues = []
    blocks = re.split(r"\r?\n[ \t]*\r?\n", (text or "").strip())
    for raw in blocks:
        lines = [ln.rstrip() for ln in raw.splitlines()]
        if not any(ln.strip() for ln in lines):
            continue
        idx = None
        m = re.match(r"^\s*(\d+)\s*$", lines[0])
        if m:
            idx = int(m.group(1))
            ts_line = lines[1] if len(lines) > 1 else ""
            body = lines[2:]
        else:
            ts_line = lines[0]
            body = lines[1:]
        start = end = None
        tm = TS_LINE_RE.search(ts_line)
        if tm:
            start = ts_to_ms(tm.group(1))
            end = ts_to_ms(tm.group(2))
        cues.append({
            "num": idx,
            "ts_line": ts_line.strip(),
            "start": start,
            "end": end,
            "text": " ".join(ln.strip() for ln in body if ln.strip()).strip(),
            "raw": raw,
        })
    return cues, blocks


# --------------------------------------------------------------------------
# spec loading
# --------------------------------------------------------------------------

def spec_declared_name(path: Path):
    """The NAME a spec module declares, read without importing it."""
    try:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return None
    m = re.search(r"^NAME\s*=\s*[\"']([^\"']+)[\"']", text, re.M)
    return m.group(1) if m else None


def spec_candidates(spec_arg, episode: str):
    """Spec module names to try, in order."""
    names = []
    if spec_arg:
        names.append(spec_arg)
    stem = episode
    if stem.upper().startswith("BYTE-"):
        stem = stem[5:]
    for cand in ("spec_%s" % episode.lower(), "spec_%s" % episode,
                 "spec_%s" % stem.lower().replace("-", "_")):
        if cand not in names:
            names.append(cand)
    # finally: any spec module in data/ that declares this episode name
    try:
        modules = sorted(DATA_DIR.glob("spec_*.py"))
    except OSError:
        modules = []
    for path in modules:
        if spec_declared_name(path) == episode and path.stem not in names:
            names.append(path.stem)
    return names


def load_spec(spec_arg, episode: str, scene_count=None):
    """Import the spec module that describes this artifact.

    Returns (module, module_name, note).  `note` is None when the requested
    module was used as is, otherwise it explains the substitution.
    """
    for extra in (str(DATA_DIR), str(Path(__file__).resolve().parent)):
        if extra not in sys.path:
            sys.path.insert(0, extra)
    loaded = []
    errors = []
    for name in spec_candidates(spec_arg, episode):
        try:
            loaded.append((name, importlib.import_module(name)))
        except Exception as exc:  # noqa: BLE001
            errors.append("%s (%s)" % (name, exc))
    if not loaded:
        raise ImportError("no spec module imported; tried: " + ", ".join(errors))

    def windows_of(mod):
        try:
            return list(getattr(mod, "W", None) or [])
        except Exception:  # noqa: BLE001
            return []

    primary_name, primary_mod = loaded[0]
    chosen_name, chosen_mod = primary_name, primary_mod
    if scene_count:
        for name, mod in loaded:
            if len(windows_of(mod)) == scene_count:
                chosen_name, chosen_mod = name, mod
                break

    notes = []
    if spec_arg and chosen_name != spec_arg:
        if spec_arg in [n for n, _m in loaded]:
            notes.append("spec module '%s' describes %d window(s) but the html has %d "
                         "scene(s)" % (spec_arg, len(windows_of(primary_mod)), scene_count))
        else:
            notes.append("spec module '%s' could not be imported" % spec_arg)
        notes.append("using '%s' instead" % chosen_name)
    declared = getattr(chosen_mod, "NAME", None)
    if declared and str(declared).upper() != episode.upper():
        notes.append("spec module '%s' declares NAME '%s', not '%s'"
                     % (chosen_name, declared, episode))
    return chosen_mod, chosen_name, ("; ".join(notes) if notes else None)


# --------------------------------------------------------------------------
# ffmpeg
# --------------------------------------------------------------------------

def find_ffmpeg():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    for candidate in (
        r"C:\ffmpeg\bin\ffmpeg.exe",
        r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
        str(ROOT / "tools" / "ffmpeg.exe"),
        str(ROOT / "bin" / "ffmpeg.exe"),
    ):
        if candidate and Path(candidate).exists():
            return candidate
    return None


def parse_ebur128(output: str):
    tail = output
    marker = output.rfind("Summary:")
    if marker != -1:
        tail = output[marker:]
    integrated = re.findall(r"\bI:\s*(-?\d+(?:\.\d+)?)\s*LUFS", tail)
    peak = re.findall(r"\bPeak:\s*(-?\d+(?:\.\d+)?)\s*dBFS", tail)
    i_val = float(integrated[-1]) if integrated else None
    p_val = float(peak[-1]) if peak else None
    return i_val, p_val


# --------------------------------------------------------------------------
# checks
# --------------------------------------------------------------------------

def run_all(episode: str, spec_arg, results, emit):
    """Run every check, printing one line each.  Returns the exit code."""

    def check(code, fn):
        try:
            status, message = fn()
        except Exception as exc:  # noqa: BLE001
            status, message = "FAIL", "check raised %s: %s" % (type(exc).__name__, exc)
        emit(status, code, message)

    # ---- artifact paths -------------------------------------------------
    html_path = ROOT / ("%s.html" % episode)
    srt_path = ROOT / ("%s.srt" % episode)
    chap_path = ROOT / ("%s-chapters.txt" % episode)

    html = None
    srt_text = None
    chap_text = None
    cues = []
    chap_lines = []
    scenes = []
    spans = None
    duration_source = ""

    if html_path.exists():
        html = read_text(html_path)
        scenes = find_scenes(html)

    # ---- spec -----------------------------------------------------------
    spec = None
    spec_used = None
    spec_error = None
    note = None
    try:
        spec, spec_used, note = load_spec(spec_arg, episode, len(scenes) or None)
    except Exception as exc:  # noqa: BLE001
        spec_error = str(exc)
    windows = []
    if spec is not None:
        windows = list(getattr(spec, "W", None) or [])
        if note:
            emit("WARN", "S0", note)
        emit("PASS", "S0", "spec module '%s' imported, %d windows" % (spec_used, len(windows)))
        if html is not None:
            spans, duration_source = extract_scene_timing(html, scenes, windows)
        durations = [e - s for s, e in spans] if spans else None
    else:
        emit("FAIL", "S0", "spec module could not be imported: %s" % spec_error)
        if html is not None:
            spans, duration_source = extract_scene_timing(html, scenes, windows)
        durations = [e - s for s, e in spans] if spans else None

    def no_spec():
        return "WARN", "not run: no spec module could be imported"

    # ---- A: presence and size ------------------------------------------
    def a1():
        if not html_path.exists():
            return "FAIL", "html artifact missing: %s" % html_path.name
        size = html_path.stat().st_size
        if size <= MIN_HTML_BYTES:
            return "FAIL", "html is %s bytes, expected more than %s bytes" % (
                fmt_bytes(size), fmt_bytes(MIN_HTML_BYTES))
        return "PASS", "html present and larger than 500 KB (%s bytes)" % fmt_bytes(size)

    def a2():
        if not srt_path.exists():
            return "FAIL", "caption file missing: %s" % srt_path.name
        return "PASS", "caption file present (%s bytes)" % fmt_bytes(srt_path.stat().st_size)

    def a3():
        if not chap_path.exists():
            return "FAIL", "chapter file missing: %s" % chap_path.name
        return "PASS", "chapter file present (%s bytes)" % fmt_bytes(chap_path.stat().st_size)

    check("A1", a1)
    check("A2", a2)
    check("A3", a3)

    # load the remaining artifacts once they are known to exist
    if srt_path.exists():
        srt_text = read_text(srt_path)
    if chap_path.exists():
        chap_text = read_text(chap_path)

    # ---- B: self contained html -----------------------------------------
    def b1():
        if html is None:
            return "FAIL", "no html to inspect (see A1)"
        scanned = strip_script_contents(html)
        hits = []
        for m in re.finditer(r"\bsrc\s*=\s*[\"']\s*(https?://[^\"'\s>]+)", scanned, re.I):
            hits.append(("src", m.group(1)))
        for m in re.finditer(r"<link\b[^>]*?\bhref\s*=\s*[\"']\s*(https?://[^\"'\s>]+)",
                             scanned, re.I):
            hits.append(("link href", m.group(1)))
        for m in re.finditer(r"<script\b[^>]*?\bsrc\s*=\s*[\"']\s*(https?://[^\"'\s>]+)",
                             scanned, re.I):
            hits.append(("script src", m.group(1)))
        if hits:
            shown = "; ".join("%s=%s" % (kind, url) for kind, url in hits[:5])
            more = "" if len(hits) <= 5 else " (+%d more)" % (len(hits) - 5)
            return "FAIL", "%d external resource reference(s): %s%s" % (
                len(hits), shown, more)
        return "PASS", "no external resource references (no remote src, link or script)"

    def b2():
        if html is None:
            return "FAIL", "no html to inspect (see A1)"
        found = []
        for pat, label in ((r"data:font/woff2;base64", "woff2"),
                           (r"data:application/font-woff", "woff"),
                           (r"data:font/ttf;base64", "ttf"),
                           (r"data:font/otf;base64", "otf"),
                           (r"data:application/octet-stream;base64", "octet")):
            n = len(re.findall(pat, html, re.I))
            if n:
                found.append("%s x%d" % (label, n))
        if not found:
            return "FAIL", "no base64 font payload found in the html"
        return "PASS", "base64 font payload(s) inlined: %s" % ", ".join(found)

    def b3():
        if html is None:
            return "FAIL", "no html to inspect (see A1)"
        mimes = re.findall(r"data:(audio/[A-Za-z0-9.+-]+);base64,", html)
        if not mimes:
            return "FAIL", "no embedded audio payload (data:audio/...;base64) in the html"
        payload = extract_audio_b64(html)
        size = len(payload[1]) if payload else 0
        return "PASS", "audio embedded as %s (base64 payload %s chars)" % (
            mimes[0], fmt_bytes(size))

    def b4():
        if html is None:
            return "FAIL", "no html to inspect (see A1)"
        markup = visible_markup(html)
        patterns = [
            ("{{", re.compile(r"\{\{")),
            ("}}", re.compile(r"\}\}")),
            ("__PLACEHOLDER__", re.compile(r"__PLACEHOLDER__", re.I)),
            ("TODO", re.compile(r"\bTODO\b")),
            ("FIXME", re.compile(r"\bFIXME\b")),
        ]
        # None / undefined / NaN only count as a hole when they stand alone:
        # "None of that is in the formula" is real narration, not a placeholder.
        loose = [
            ("None", re.compile(r"\bNone\b")),
            ("undefined", re.compile(r"\bundefined\b")),
            ("NaN", re.compile(r"\bNaN\b")),
        ]
        hits = []
        for label, pattern in patterns:
            for m in pattern.finditer(markup):
                lo = max(0, m.start() - 30)
                hi = min(len(markup), m.end() + 30)
                hits.append((label, norm_ws(markup[lo:hi])))
        for label, pattern in loose:
            for m in pattern.finditer(markup):
                if not is_standalone_token(markup, m.start(), m.end()):
                    continue
                lo = max(0, m.start() - 30)
                hi = min(len(markup), m.end() + 30)
                hits.append((label, norm_ws(markup[lo:hi])))
        if hits:
            shown = "; ".join("%s -> '%s'" % (label, ctx) for label, ctx in hits[:6])
            more = "" if len(hits) <= 6 else " (+%d more)" % (len(hits) - 6)
            return "FAIL", "%d unfilled placeholder token(s): %s%s" % (
                len(hits), shown, more)
        return "PASS", "no unfilled placeholder tokens in the rendered markup"

    check("B1", b1)
    check("B2", b2)
    check("B3", b3)
    check("B4", b4)

    # ---- C: structure vs the spec ---------------------------------------
    def c1():
        if html is None:
            return "FAIL", "no html to inspect (see A1)"
        if spec is None:
            return no_spec()
        if len(scenes) != len(windows):
            return "FAIL", "%d scenes in the html but %d windows in the spec" % (
                len(scenes), len(windows))
        return "PASS", "%d scenes for %d windows" % (len(scenes), len(windows))

    def c2():
        if html is None:
            return "FAIL", "no html to inspect (see A1)"
        missing = [i + 1 for i, sc in enumerate(scenes) if not has_class_token(sc["block"], "src")]
        if missing:
            shown = ", ".join(str(i) for i in missing[:6])
            more = "" if len(missing) <= 6 else " (+%d more)" % (len(missing) - 6)
            return "FAIL", "%d scene(s) without a source footer (no class=\"src\"): %s%s" % (
                len(missing), shown, more)
        return "PASS", "every scene (%d) carries a source footer" % len(scenes)

    def c3():
        if html is None:
            return "FAIL", "no html to inspect (see A1)"
        if not durations:
            return "WARN", ("no window duration data found in the html (%s); "
                            "C3 could not be measured" % duration_source)
        over = []
        for i, d in enumerate(durations):
            if d > MAX_WINDOW_SECONDS:
                over.append("window %d: %.1f s" % (i + 1, d))
        longest = max(durations)
        source_note = " (%s)" % duration_source
        if spec is not None and len(spans) != len(windows):
            source_note += " (the html carries %d scene(s) for %d spec window(s))" % (
                len(spans), len(windows))
        if over:
            return "FAIL", "window(s) longer than %g s: %s%s" % (
                MAX_WINDOW_SECONDS, "; ".join(over), source_note)
        return "PASS", "longest window %.1f s (limit %g s)%s" % (
            longest, MAX_WINDOW_SECONDS, source_note)

    def c4():
        if spec is None:
            return no_spec()
        if len(windows) < 2:
            return "PASS", "only %d window, nothing to compare" % len(windows)
        bad = []
        for i in range(len(windows) - 1):
            a = wfield(windows[i], "layout", None)
            b = wfield(windows[i + 1], "layout", None)
            if a is not None and b is not None and str(a) == str(b):
                bad.append("windows %d and %d share layout '%s'" % (i + 1, i + 2, a))
        if bad:
            shown = "; ".join(bad[:5])
            more = "" if len(bad) <= 5 else " (+%d more)" % (len(bad) - 5)
            return "FAIL", "%d consecutive layout clash(es): %s%s" % (len(bad), shown, more)
        return "PASS", "no two consecutive windows share a layout"

    def c5():
        if spec is None:
            return no_spec()
        seen = {}
        dupes = []
        for i, w in enumerate(windows):
            vo = str(wfield(w, "vo", ""))
            for sentence in re.split(r"(?<=[.!?])\s+|\n+", vo):
                toks = words_of(sentence)
                if len(toks) < 8:
                    continue
                key = " ".join(toks)
                if key in seen and seen[key] != i:
                    dupes.append("windows %d and %d: '%s'" % (
                        seen[key] + 1, i + 1, clip(sentence)))
                else:
                    seen.setdefault(key, i)
        if dupes:
            return "FAIL", "duplicated narration: %s" % "; ".join(dupes[:4])
        return "PASS", "no duplicated narration between windows"

    check("C1", c1)
    check("C2", c2)
    check("C3", c3)
    check("C4", c4)
    check("C5", c5)

    # ---- D: captions ----------------------------------------------------
    if srt_text is not None:
        cues, _blocks = parse_srt(srt_text)

    def d1():
        if srt_text is None:
            return "FAIL", "no caption file to inspect (see A2)"
        if not cues:
            return "FAIL", "caption file contains no cues"
        bad = []
        for cue in cues:
            line = cue["ts_line"]
            if not line:
                bad.append("cue %s: missing timestamp line" % cue["num"])
                continue
            if not TS_LINE_RE.search(line):
                bad.append("cue %s: malformed timestamp line '%s'" % (cue["num"], line))
                continue
            if not re.search(r"\d{1,3}:\d{2}:\d{2},\d{1,3}", line):
                bad.append("cue %s: '%s' does not use a comma before the milliseconds"
                           % (cue["num"], line))
        if bad:
            return "FAIL", "%d cue(s) with a bad timestamp format: %s" % (
                len(bad), " | ".join(bad[:3]))
        return "PASS", "all %d cues use HH:MM:SS,mmm timestamps" % len(cues)

    def d2():
        if not cues:
            return "FAIL", "no caption file to inspect (see A2)"
        bad = []
        for i in range(len(cues) - 1):
            a, b = cues[i], cues[i + 1]
            if a["end"] is None or b["start"] is None:
                continue
            if b["start"] < a["end"]:
                bad.append("cue %s ends %d ms after cue %s starts" % (
                    a["num"], a["end"] - b["start"], b["num"]))
        if bad:
            return "FAIL", "%d overlapping cue pair(s): %s" % (len(bad), "; ".join(bad[:3]))
        return "PASS", "no overlapping cues (%d cues)" % len(cues)

    def _caption_words():
        text = " ".join(c["text"] for c in cues)
        return text, words_of(text)

    def _script_words():
        text = " ".join(str(wfield(w, "vo", "")) for w in windows)
        return text, words_of(text)

    def d3():
        if not cues:
            return "FAIL", "no caption file to inspect (see A2)"
        if spec is None:
            return no_spec()
        cap_text, cap_words = _caption_words()
        scr_text, scr_words = _script_words()
        if norm_ws(cap_text).lower() == norm_ws(scr_text).lower():
            return "PASS", "caption text is word-for-word the script (%d words)" % len(cap_words)
        if cap_words == scr_words:
            return "PASS", "caption text is word-for-word the script (%d words, punctuation differs)" % \
                len(cap_words)
        for i in range(min(len(cap_words), len(scr_words))):
            if cap_words[i] != scr_words[i]:
                ctx_c = " ".join(cap_words[max(0, i - 6):i + 6])
                ctx_s = " ".join(scr_words[max(0, i - 6):i + 6])
                return "FAIL", ("caption differs from the script at word %d: "
                                "caption '%s' vs script '%s' (caption words %d, script words %d)"
                                % (i + 1, ctx_c, ctx_s, len(cap_words), len(scr_words)))
        longer = "caption" if len(cap_words) > len(scr_words) else "script"
        return "FAIL", ("caption and script differ in length: %d caption words vs %d script words "
                        "(%s has extra trailing words)" % (len(cap_words), len(scr_words), longer))

    def d4():
        if not cues:
            return "FAIL", "no caption file to inspect (see A2)"
        if spec is None:
            return no_spec()
        _cap_text, cap_words = _caption_words()
        _scr_text, scr_words = _script_words()
        if not scr_words:
            return "WARN", "the spec contains no spoken words to compare against"
        cap_count = Counter(cap_words)
        scr_count = Counter(scr_words)
        common = sum((cap_count & scr_count).values())
        coverage = 100.0 * common / len(scr_words)
        missing = list((scr_count - cap_count).elements())
        extra = list((cap_count - scr_count).elements())
        if coverage < 99.995 or missing or extra:
            parts = []
            if missing:
                parts.append("missing: %s" % " ".join(missing[:12]))
            if extra:
                parts.append("extra: %s" % " ".join(extra[:12]))
            return "FAIL", "coverage %.2f %% (%d/%d script words) - %s" % (
                coverage, common, len(scr_words), "; ".join(parts))
        return "PASS", "word coverage %.2f %% (%d/%d words)" % (
            coverage, common, len(scr_words))

    def d5():
        if not cues:
            return "FAIL", "no caption file to inspect (see A2)"
        bad = []
        max_words = 0
        for cue in cues:
            n = len(words_of(cue["text"]))
            max_words = max(max_words, n)
            if n < MIN_CUE_WORDS:
                bad.append("cue %s has %d word(s): '%s'" % (cue["num"], n, clip(cue["text"])))
            elif n > MAX_CUE_WORDS:
                bad.append("cue %s has %d words: '%s'" % (cue["num"], n, clip(cue["text"])))
        if bad:
            return "FAIL", "%d cue(s) with a bad word count: %s" % (len(bad), " | ".join(bad[:4]))
        return "PASS", "no cue is a single word or longer than %d words (longest %d)" % (
            MAX_CUE_WORDS, max_words)

    def d6():
        if not cues:
            return "FAIL", "no caption file to inspect (see A2)"
        if spec is None:
            return no_spec()
        if not spans or len(spans) != len(windows):
            return "WARN", ("window timing data does not line up with the spec "
                            "(%d scene span(s) for %d window(s)); cue/window boundaries "
                            "could not be checked" % (len(spans or []), len(windows)))
        assigned = {}
        stray = []
        for cue in cues:
            if cue["start"] is None:
                stray.append(cue)
                continue
            placed = False
            for i, (s, e) in enumerate(spans):
                if (s - 0.25) <= cue["start"] / 1000.0 < e:
                    assigned.setdefault(i, []).append(cue)
                    placed = True
                    break
            if not placed:
                stray.append(cue)
        problems = []
        if stray:
            problems.append("%d cue(s) fall outside every window" % len(stray))
        for i, (s, e) in enumerate(spans):
            group = assigned.get(i, [])
            if not group:
                problems.append("window %d has no caption cue, its words would be dropped"
                                % (i + 1))
                continue
            gap = e - group[-1]["end"] / 1000.0
            if gap > CAPTION_GAP_TOLERANCE_MS / 1000.0:
                problems.append("window %d: last cue ends %.2f s before the window ends"
                                % (i + 1, gap))
            lead = group[0]["start"] / 1000.0 - s
            if lead > CAPTION_GAP_TOLERANCE_MS / 1000.0:
                problems.append("window %d: first cue starts %.2f s after the window starts"
                                % (i + 1, lead))
            # every word of the window must be carried by that window's cues
            group_words = words_of(" ".join(c["text"] for c in group))
            window_words = words_of(str(wfield(windows[i], "vo", "")))
            if group_words != window_words:
                problems.append("window %d: its cues carry %d word(s), the window says %d"
                                % (i + 1, len(group_words), len(window_words)))
        if problems:
            return "FAIL", "; ".join(problems[:4])
        return "PASS", ("every window's last cue ends at the window boundary and carries "
                        "the window's own words")

    check("D1", d1)
    check("D2", d2)
    check("D3", d3)
    check("D4", d4)
    check("D5", d5)
    check("D6", d6)

    # ---- E: chapters ----------------------------------------------------
    if chap_text is not None:
        chap_lines = [ln.strip() for ln in chap_text.splitlines() if ln.strip()]

    # Two chapter shapes exist in this project:
    #   legacy  "M:SS <kicker> NN"  one line per window -- a per-window index
    #   grouped "M:SS <title>"      the YouTube chapter list a viewer navigates
    # The grouped shape is the deliverable, so it is the one held to the
    # YouTube rules. The legacy shape is still accepted for older episodes.
    GROUPED_LINE_RE = re.compile(r"^(?:(\d+):)?(\d{1,2}):(\d{2})\s+(.+)$")

    def detect_chapter_shape():
        if not chap_lines:
            return None
        legacy_ok = all(CHAPTER_LINE_RE.match(ln) for ln in chap_lines)
        grouped_ok = all(GROUPED_LINE_RE.match(ln) for ln in chap_lines)
        if legacy_ok and not grouped_ok:
            return "legacy"
        if grouped_ok and not legacy_ok:
            return "grouped"
        # both parse: the per-window count decides
        if legacy_ok and len(chap_lines) == len(windows):
            return "legacy"
        return "grouped"

    chap_shape = detect_chapter_shape()
    chap_stamps = []
    chap_titles = []
    chap_problems = []
    for i, line in enumerate(chap_lines):
        if chap_shape == "legacy":
            m = CHAPTER_LINE_RE.match(line)
            if not m:
                chap_problems.append("line %d does not match 'M:SS <kicker> NN': '%s'"
                                     % (i + 1, clip(line)))
                continue
            chap_stamps.append(int(m.group(1)) * 60 + int(m.group(2)))
            chap_titles.append(m.group(3).strip())
        else:
            m = GROUPED_LINE_RE.match(line)
            if not m:
                chap_problems.append("line %d is not a timestamp: '%s'"
                                     % (i + 1, clip(line)))
                continue
            chap_stamps.append(int(m.group(1) or 0) * 3600
                               + int(m.group(2)) * 60 + int(m.group(3)))
            chap_titles.append(m.group(4).strip())

    def e1():
        if chap_text is None:
            return "FAIL", "no chapter file to inspect (see A3)"
        if chap_problems:
            return "FAIL", "; ".join(chap_problems[:3])
        if chap_shape == "legacy":
            return "PASS", "one chapter line per window (%d)" % len(chap_lines)
        # grouped form: the rules a viewer can act on
        problems = []
        if len(chap_stamps) < 3:
            problems.append("only %d chapters; YouTube wants at least 3" % len(chap_stamps))
        if chap_stamps and chap_stamps[0] != 0:
            problems.append("the first chapter starts at %ds, not 0" % chap_stamps[0])
        for k in range(len(chap_stamps) - 1):
            gap = chap_stamps[k + 1] - chap_stamps[k]
            if gap <= 0:
                problems.append("chapter %d does not move forward" % (k + 1))
            elif gap < 10:
                problems.append("chapter %d is only %ds long (%s)"
                                % (k + 1, gap, chap_titles[k]))
        if len(set(chap_titles)) != len(chap_titles):
            problems.append("two chapters share a title")
        if problems:
            return "FAIL", "; ".join(problems[:3])
        shortest = min(chap_stamps[k + 1] - chap_stamps[k]
                       for k in range(len(chap_stamps) - 1))
        return "PASS", "grouped chapter list is valid for YouTube (%d chapters, shortest %ds)" % (
            len(chap_stamps), shortest)

    def e2():
        if chap_text is None:
            return "FAIL", "no chapter file to inspect (see A3)"
        if chap_shape == "legacy":
            nums = []
            for line in chap_lines:
                m = CHAPTER_LINE_RE.match(line)
                if m:
                    nums.append(int(m.group(4)))
            expected = list(range(1, len(chap_lines) + 1))
            alt = list(range(0, len(chap_lines)))
            if nums not in (expected, alt):
                return "FAIL", "chapter numbers are not sequential: %s" % ", ".join(
                    "%02d" % n for n in nums[:12])
            # kicker cross check against the spec (informational only)
            mismatches = []
            for i, line in enumerate(chap_lines):
                m = CHAPTER_LINE_RE.match(line)
                if not m or i >= len(windows):
                    continue
                kicker = None
                for key in ("kicker", "kicker_text", "label", "chapter", "headline", "head", "title"):
                    value = wfield(windows[i], key, None)
                    if isinstance(value, str) and value.strip():
                        kicker = value.strip()
                        break
                if kicker:
                    kicker = (htmllib.unescape(kicker).replace("\u2022", "\u00b7")
                              .replace("\u2027", "\u00b7")).strip()
                    if kicker.lower() != m.group(3).strip().lower():
                        mismatches.append("line %d: '%s' vs spec '%s'" % (i + 1, m.group(3), kicker))
            if mismatches:
                return "WARN", "chapter kickers differ from the spec: %s" % "; ".join(mismatches[:3])
            return "PASS", "all %d chapter lines match 'M:SS <kicker> NN'" % len(chap_lines)
        # grouped form: every title must come from the spec's own CHAPTERS list
        if spec is None:
            return no_spec()
        declared = []
        for entry in (getattr(spec, "CHAPTERS", None) or []):
            if isinstance(entry, (tuple, list)) and len(entry) >= 2:
                declared.append(str(entry[1]).strip())
            elif isinstance(entry, str):
                declared.append(entry.strip())
        if not declared:
            return "FAIL", "the spec declares no CHAPTERS list to check the file against"
        problems = []
        if len(declared) != len(chap_titles):
            problems.append("spec declares %d chapters, the file has %d"
                            % (len(declared), len(chap_titles)))
        for i, title in enumerate(chap_titles):
            want = declared[i] if i < len(declared) else None
            if want is None:
                problems.append("chapter %d has no spec entry" % (i + 1))
            elif want.lower() != title.lower():
                problems.append("chapter %d: '%s' vs spec '%s'" % (i + 1, title, want))
        if problems:
            return "FAIL", "; ".join(problems[:3])
        return "PASS", "all %d chapters match the spec's CHAPTERS list" % len(chap_titles)

    def e3():
        if chap_text is None:
            return "FAIL", "no chapter file to inspect (see A3)"
        if chap_problems:
            return "FAIL", "; ".join(chap_problems[:3])
        times = list(chap_stamps)
        nonmono = []
        for j in range(len(times) - 1):
            if times[j + 1] <= times[j]:
                nonmono.append("line %d (%d s) does not follow line %d (%d s)"
                                % (j + 2, times[j + 1], j + 1, times[j]))
        if nonmono:
            return "FAIL", "chapter times are not monotonic: %s" % "; ".join(nonmono[:3])
        return "PASS", "chapter times increase monotonically (%s ... %s)" % (
            times[0] if times else "-", times[-1] if times else "-")

    check("E1", e1)
    check("E2", e2)
    check("E3", e3)

    # ---- F: loudness ----------------------------------------------------
    tmpdir = None
    measured = {}

    def f_measure():
        """Extract the embedded audio and measure it.  Returns (i_lufs, peak_dbfs)."""
        if html is None:
            return None, None, "no html artifact to extract audio from"
        payload = extract_audio_b64(html)
        if not payload:
            return None, None, "no embedded audio payload found in the html"
        mime, b64 = payload
        try:
            raw = base64.b64decode(b64, validate=False)
        except (binascii.Error, ValueError) as exc:
            return None, None, "embedded audio is not valid base64 (%s)" % exc
        if not raw:
            return None, None, "embedded audio payload is empty"
        ext = ".mp3" if "mpeg" in mime or "mp3" in mime else (
            ".wav" if "wav" in mime else ".ogg" if "ogg" in mime else ".mp3")
        tmpdir = tempfile.mkdtemp(prefix="bf_recheck_")
        tmp = Path(tmpdir) / ("audio" + ext)
        tmp.write_bytes(raw)
        ffmpeg = find_ffmpeg()
        if not ffmpeg:
            shutil.rmtree(tmpdir, ignore_errors=True)
            return None, None, "ffmpeg is not on PATH, loudness could not be measured"
        cmd = [ffmpeg, "-hide_banner", "-nostats", "-i", str(tmp),
               "-af", "ebur128=peak=true", "-f", "null", "NUL" if os.name == "nt" else "-"]
        try:
            proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                  text=True, errors="replace",
                                  creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
            output = proc.stdout or ""
        except Exception as exc:  # noqa: BLE001
            shutil.rmtree(tmpdir, ignore_errors=True)
            return None, None, "ffmpeg could not be run (%s)" % exc
        shutil.rmtree(tmpdir, ignore_errors=True)
        i_val, p_val = parse_ebur128(output)
        if i_val is None and p_val is None:
            tail = " / ".join(line for line in output.splitlines()[-6:] if line.strip())
            return None, None, "ffmpeg produced no ebur128 summary (%s)" % clip(tail, 160)
        return i_val, p_val, None

    def f1():
        if "err" not in measured:
            measured["i"], measured["p"], measured["err"] = f_measure()
        if measured.get("err"):
            return "WARN", "integrated loudness not measured: %s" % measured["err"]
        value = measured.get("i")
        if value is None:
            return "WARN", "integrated loudness not present in the ebur128 summary"
        if LOUDNESS_MIN_LUFS <= value <= LOUDNESS_MAX_LUFS:
            return "PASS", "integrated loudness %.1f LUFS within %.1f..%.1f" % (
                value, LOUDNESS_MIN_LUFS, LOUDNESS_MAX_LUFS)
        return "FAIL", "integrated loudness %.1f LUFS outside %.1f..%.1f" % (
            value, LOUDNESS_MIN_LUFS, LOUDNESS_MAX_LUFS)

    def f2():
        if "err" not in measured:
            measured["i"], measured["p"], measured["err"] = f_measure()
        if measured.get("err"):
            return "WARN", "true peak not measured: %s" % measured["err"]
        value = measured.get("p")
        if value is None:
            return "WARN", "true peak not present in the ebur128 summary"
        if value <= TRUE_PEAK_MAX_DBFS:
            return "PASS", "true peak %.1f dBFS at or below %.1f dBFS" % (
                value, TRUE_PEAK_MAX_DBFS)
        return "FAIL", "true peak %.1f dBFS above %.1f dBFS" % (value, TRUE_PEAK_MAX_DBFS)

    check("F1", f1)
    check("F2", f2)

    # ---- G: numbers on screen -------------------------------------------
    KEYWORDS = ("score", "accuracy", "mmlu", "flan", "percent")

    def element_inner_text(markup: str, start: int, tag: str) -> str:
        """Text of the element whose opening tag ends at `start` (nesting aware)."""
        open_re = re.compile(r"<%s\b" % re.escape(tag), re.I)
        close_re = re.compile(r"</%s\s*>" % re.escape(tag), re.I)
        depth = 1
        i = start
        inner = markup[start:start + 200]
        while i < len(markup):
            nc = close_re.search(markup, i)
            if nc is None:
                break
            no = open_re.search(markup, i)
            if no is not None and no.start() < nc.start():
                depth += 1
                i = no.end()
                continue
            depth -= 1
            i = nc.end()
            if depth == 0:
                inner = markup[start:nc.start()]
                break
        return norm_ws(htmllib.unescape(re.sub(r"<[^>]+>", " ", inner)))

    def find_row_label(markup: str, value_start: int):
        """The label of the bar/rail row that owns the value element."""
        prefix = markup[:value_start]
        row_start = None
        for m in re.finditer(r"class\s*=\s*[\"']([^\"']*)[\"']", prefix):
            toks = m.group(1).split()
            if any(t == "bar" or t == "railrow" or t == "rail" or t.endswith("row")
                   or t.endswith("bar") for t in toks):
                row_start = m.end()
        if row_start is None:
            return None
        region = markup[row_start:value_start]
        label = None
        for lm in re.finditer(r"class\s*=\s*[\"']([^\"']*)[\"'][^>]*>", region):
            toks = lm.group(1).split()
            if any(t == "lab" or t == "label" or t.endswith("__lab") or t.endswith("_lab")
                   or t.endswith("-lab") or t.endswith("__label") or t.endswith("_label")
                   or t.endswith("-label") for t in toks):
                label = norm_ws(htmllib.unescape(
                    re.sub(r"<[^>]+>", " ", region[lm.end():lm.end() + 120])))
        return label

    def g1():
        if html is None:
            return "FAIL", "no html to inspect (see A1)"
        bad = []
        scanned = strip_script_contents(html)
        for m in re.finditer(r"<([A-Za-z][\w-]*)([^>]*\bclass\s*=\s*[\"']([^\"']*)[\"'][^>]*)>",
                             scanned, re.I):
            classes = m.group(3).split()
            is_val = any(tok.lower() in ("bar__val", "rail__val", "bar__value", "rail__value")
                         or tok.lower().endswith("__val") or tok.lower().endswith("__value")
                         for tok in classes)
            if not is_val:
                continue
            text = element_inner_text(scanned, m.end(), m.group(1))
            if not re.search(r"\bt\s*/\s*s\b", text, re.I):
                continue
            label = find_row_label(scanned, m.start())
            if label:
                low = label.lower()
                hit = any(k in low for k in KEYWORDS) or "%" in label
            else:
                ctx = re.sub(r"<[^>]+>", " ", scanned[max(0, m.start() - 600):m.start()])
                low = norm_ws(htmllib.unescape(ctx)).lower()
                hit = any(k in low for k in KEYWORDS)
                label = norm_ws(htmllib.unescape(ctx))[-120:]
            if hit:
                bad.append("'%s' (label '%s') carries T/S" % (clip(text, 40), clip(label, 70)))
        if bad:
            return "FAIL", "%d value(s) pair a T/S unit with a score/accuracy label: %s" % (
                len(bad), "; ".join(bad[:4]))
        return "PASS", "no score/accuracy/percent value carries a T/S unit"

    def g2():
        if html is None:
            return "FAIL", "no html to inspect (see A1)"
        if spec is None:
            return no_spec()
        tm = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
        if not tm:
            return "FAIL", "the html has no <title> element"
        actual = norm_ws(htmllib.unescape(tm.group(1)))
        expected_raw = (getattr(spec, "DOC_TITLE", None) or getattr(spec, "TITLE", None)
                        or getattr(spec, "NAME", None))
        if not expected_raw:
            return "FAIL", "the spec module exposes neither DOC_TITLE, TITLE nor NAME"
        expected = norm_ws(htmllib.unescape(str(expected_raw)))

        def fold(text):
            return (text.lower()
                    .replace("\u2022", "\u00b7").replace("\u2027", "\u00b7")
                    .replace("\u00b7", "\u00b7"))

        if fold(actual) == fold(expected):
            return "PASS", "document title matches %r ('%s')" % (
                "DOC_TITLE" if getattr(spec, "DOC_TITLE", None) else "TITLE", actual)
        return "FAIL", "document title '%s' does not match %r" % (actual, expected)

    check("G1", g1)
    check("G2", g2)

    return 1 if any(s == "FAIL" for s, _c, _m in results) else 0


# --------------------------------------------------------------------------
# entry point
# --------------------------------------------------------------------------

def main(argv):
    if len(argv) < 2:
        print("usage: python data/_recheck.py <EPISODE-NAME> [spec_module]")
        return 2

    episode = argv[1]
    spec_arg = argv[2] if len(argv) > 2 else None
    results = []

    def emit(status, code, message):
        results.append((status, code, message))
        print("[%s] %s  %s" % (status, code, message), flush=True)

    print("RECHECK %s" % episode, flush=True)
    print("-" * 72, flush=True)

    exit_code = run_all(episode, spec_arg, results, emit)

    passed = sum(1 for s, _c, _m in results if s == "PASS")
    failed = sum(1 for s, _c, _m in results if s == "FAIL")
    warned = sum(1 for s, _c, _m in results if s == "WARN")

    print("-" * 72, flush=True)
    if failed:
        print("failed: %s" % ", ".join(c for s, c, _m in results if s == "FAIL"), flush=True)
    if warned:
        print("warnings: %s" % ", ".join(c for s, c, _m in results if s == "WARN"), flush=True)
    print("RECHECK %s: %d PASS, %d FAIL" % (episode, passed, failed), flush=True)
    if warned:
        print("RECHECK %s: %d WARN" % (episode, warned), flush=True)
    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
