#!/usr/bin/env python3
"""
Pre-flight validator for episode HTML.

Every bug that shipped a broken video earlier is now a hard failure here:
  * unresolved @cue@ placeholders  -> elements stuck at opacity 0 (blank video)
  * cue timeline != audio duration -> drift over the whole video
  * scene boundary not on a pause  -> cuts land mid-word
  * missing embedded audio
  * missing fonts (silent fallback to Arial)
  * a frame that renders empty

Usage:
    python scripts/check.py                # static + audio checks
    python scripts/check.py --frames       # also render 3 sample frames
"""
import base64
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EPISODES = ROOT / "episodes"

FAIL = []
WARN = []


def fail(ep, msg):
    FAIL.append(f"{ep}: {msg}")


def warn(ep, msg):
    WARN.append(f"{ep}: {msg}")


def parse_episode(html):
    m = re.search(r"window\.EPISODE\s*=\s*\{(.*?)\n\};", html, re.S)
    if not m:
        return None
    blob = m.group(1)
    total = re.search(r"total:\s*([0-9.]+)", blob)
    scenes = re.findall(r"\{\s*s:\s*([0-9.]+),\s*e:\s*([0-9.]+)\s*\}", blob)
    wipes_m = re.search(r"wipes:\s*\[([0-9.,\s]*)\]", blob)
    wipes = [float(x) for x in wipes_m.group(1).split(",")] if wipes_m and wipes_m.group(1).strip() else []
    return {
        "total": float(total.group(1)) if total else None,
        "scenes": [(float(a), float(b)) for a, b in scenes],
        "wipes": wipes,
    }


def decode_audio(html, dst):
    m = re.search(r"data:audio/mpeg;base64,([A-Za-z0-9+/=\s]+)", html)
    if not m:
        return False
    dst.write_bytes(base64.b64decode(re.sub(r"\s+", "", m.group(1))))
    return True


def probe_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    ).stdout.strip()
    return float(out) if out else 0.0


def silence_ends(path):
    o = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af",
         "silencedetect=noise=-45dB:d=0.14", "-f", "null", "-"],
        capture_output=True, text=True,
    ).stderr
    return [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", o)]


def check_static(name, html):
    ep = parse_episode(html)
    if not ep or not ep["total"]:
        fail(name, "cannot parse window.EPISODE / total")
        return None

    # 1. unresolved cue tokens
    cues = re.findall(r'data-in="([^"]*)"', html)
    bad = [c for c in cues if not re.fullmatch(r"[0-9.]+", c)]
    if bad:
        fail(name, f"{len(bad)} unresolved cue(s): {bad[:4]}")
    if not cues:
        fail(name, "no data-in cues at all")

    # 2. scene sanity
    sc = ep["scenes"]
    if len(sc) < 2:
        fail(name, "fewer than 2 scenes")
    for i, (a, b) in enumerate(sc):
        if b <= a:
            fail(name, f"scene {i+1} has end <= start ({a},{b})")
        if a < 0 or b > ep["total"] + 0.05:
            fail(name, f"scene {i+1} outside 0..{ep['total']}")
    for i in range(1, len(sc)):
        if sc[i][0] < sc[i - 1][1] - 0.01:
            fail(name, f"scene {i+1} overlaps scene {i}")

    # 3. wipes land on a cut (full cover = start + 0.285)
    starts = {round(a, 2) for a, _ in sc[1:]}
    for w in ep["wipes"]:
        if not any(abs(w + 0.285 - s) < 0.12 for s in starts):
            warn(name, f"wipe at {w:.2f}s does not align with a scene cut")

    # 3b. visual density: no still frame longer than maxGap
    mg = re.search(r"maxGap:\s*([0-9.]+)", html)
    budget = float(mg.group(1)) if mg else None
    events = []
    for i, (a, b) in enumerate(sc):
        blk = re.search(r'<section class="scene[^"]*" data-scene="%d">(.*?)</section>' % i, html, re.S)
        if not blk:
            continue
        for v in re.findall(r'data-in="([0-9.]+)"', blk.group(1)):
            events.append(a + float(v))
    events = sorted(set(events))
    if len(events) > 1:
        worst = max(q - p for p, q in zip(events, events[1:]))
        if budget is not None and worst > budget:
            fail(name, f"visual gap {worst:.2f}s exceeds declared {budget:.1f}s")
        elif budget is None and worst > 3.5:
            warn(name, f"visual gap {worst:.2f}s (declare maxGap to enforce)")

    # 4. fonts referenced by the page must exist
    fonts = set(re.findall(r"url\(['\"]?([^'\")]+\.ttf)", html))
    for f in fonts:
        p = (EPISODES / f).resolve() if not os.path.isabs(f) else Path(f)
        if not p.exists():
            fail(name, f"font missing: {f}")

    return ep


def check_audio(name, html, ep, tmpdir):
    vo = Path(tmpdir) / f"{name}.mp3"
    if not decode_audio(html, vo):
        fail(name, "no embedded audio (data URI)")
        return None
    d = probe_duration(vo)
    if d <= 0:
        fail(name, "embedded audio will not decode")
        return None
    drift = d - ep["total"]
    if abs(drift) > 0.08:
        fail(name, f"audio {d:.2f}s vs cue timeline {ep['total']:.2f}s (drift {drift:+.2f}s)")
    # 5. scene boundaries should sit on speech pauses
    ends = silence_ends(vo)
    if ends:
        worst = 0.0
        for a, _ in ep["scenes"][1:]:
            worst = max(worst, abs(a - min(ends, key=lambda e: abs(e - a))))
        if worst > 0.15:
            fail(name, f"scene boundary off a pause by {worst*1000:.0f} ms")
    return vo


def check_frames(name, html_path):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        warn(name, "playwright not installed; skipped frame check")
        return
    try:
        with sync_playwright() as p:
            try:
                b = p.chromium.launch()
            except Exception:
                b = p.chromium.launch(channel="chrome")
            pg = b.new_page(viewport={"width": 1920, "height": 1080})
            pg.goto(html_path.resolve().as_uri())
            pg.wait_for_function("!!(window.EPISODE && window.renderAt)", timeout=60000)
            total = float(pg.evaluate("window.EPISODE.total"))
            for frac in (0.1, 0.5, 0.85):
                t = total * frac
                pg.evaluate(f"window.renderAt({t})")
                shot = pg.screenshot(type="png")
                # crude "is anything drawn" test: count distinct bytes
                uniq = len(set(shot[::997]))
                if uniq < 12:
                    fail(name, f"frame at {t:.1f}s looks empty")
                    break
            b.close()
    except Exception as e:
        fail(name, f"frame check crashed: {e}")


def main():
    frames = "--frames" in sys.argv
    only = ""
    for i, a in enumerate(sys.argv):
        if a == "--only" and i + 1 < len(sys.argv):
            only = sys.argv[i + 1]
    files = sorted(EPISODES.glob("*.html"))
    if only:
        files = [f for f in files if f.stem == only]
    if not files:
        print("no episodes found")
        return 1

    with tempfile.TemporaryDirectory() as tmp:
        for f in files:
            name = f.stem
            html = f.read_text(encoding="utf-8")
            if "window.FUSION" in html:
                gate_py = ROOT / "data" / "fusion_gate.py"
                if gate_py.exists():
                    print(f"[{name}] Running 30-check FUSION Quality Gate...")
                    res = subprocess.run([sys.executable, str(gate_py), name], cwd=str(ROOT))
                    if res.returncode != 0:
                        fail(name, "FUSION quality gate failed")
                    else:
                        print(f"  {name:22} GATE PASS")
                    continue
            ep = check_static(name, html)
            if ep:
                check_audio(name, html, ep, tmp)
                if frames:
                    check_frames(name, f)
            status = "ok" if not any(x.startswith(name + ":") for x in FAIL) else "FAIL"
            print(f"  {name:22} {status}")

    print()
    for w in WARN:
        print("  WARN ", w)
    for e in FAIL:
        print("  FAIL ", e)
    print(f"\n{len(files)} episode(s): {len(FAIL)} failure(s), {len(WARN)} warning(s)")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
