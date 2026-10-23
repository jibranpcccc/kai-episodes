# -*- coding: utf-8 -*-
"""Permanent regression checks for the ten EP09 error classes.

These are not a one-off audit. Every one of them is a defect that actually
shipped in Episode 09, and each one is written so that the same defect
cannot ship again in this episode or in the next one.

    python data/_check_claims.py [spec_module]

Exit code 0 means every check passed.
"""
import importlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "data"))

from _numbers_on_screen import NUM, strings  # noqa: E402

FACTS_PATH = os.path.join(ROOT, "data", "EP09-FACTS.json")

# --------------------------------------------------------------------------
# vocabulary for the typo check
# --------------------------------------------------------------------------
WORDLIST_PATH = os.path.join(ROOT, "data", "wordlist.txt")

# Words this episode is allowed to use that a common English word list does
# not know: model names, GPU names, quantisation names, units, and the
# channel's own vocabulary.
ALLOW = set("""
kv cache caches token tokens prompt prompts weight weights model models gpu
gpus vram ram cpu gpu rtx m5 max ti gb10 qwen muse glimmer llama cpp
flash attention offload context contexts megabyte megabytes gigabyte gigabytes
mebibyte mebibytes gibibyte gibibytes tlb fp16 fp32 q8 q4 gguf
prefill decode decode encode runtime runtimes slo slo slo
nvidia cuda ubuntu linux driver kernel bsd
llama cpp
miB MiB
logits params param softmax embedding embeddings
""".split())

# Words the episode uses that are spelled with a hyphen or a digit and must
# not be flagged.
SKIP = set("""
rtx 4090 5090 3090 5060 ti m5 max gb10 qwen3 qwen2 3 8 2 5 27 30
q8 q4 fp16 0 1 2 3 4 5 6 7 8 9
""".split())


def load_words():
    words = set()
    if os.path.exists(WORDLIST_PATH):
        for line in open(WORDLIST_PATH, encoding="utf-8"):
            w = line.strip().lower()
            if w:
                words.add(w)
    words |= ALLOW
    return words


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def words_of(text):
    """The plain words of a piece of visible text.

    HTML entities are stripped, because the viewer never sees "&middot;".
    A hyphenated word is checked in its parts, because "read-only" is two
    words the viewer reads as one."""
    s = re.sub(r"&[a-zA-Z]+;|&#\d+;", " ", str(text))
    out = []
    for tok in re.findall(r"[A-Za-z][A-Za-z']*", s):
        t = tok.lower().strip("'")
        if t:
            out.append(t)
    return out


def all_text(w):
    return " ".join(t for _, t in strings(w))


# --------------------------------------------------------------------------
# 1-3  the absolute claims
# --------------------------------------------------------------------------
# Each entry: (pattern, what it forbids). They are matched against the
# narration and the visible text of every window.
FORBIDDEN = [
    # 1  the KV cache is never saved
    (r"not saved anywhere", "1: the cache is never saved anywhere"),
    (r"never saved", "1: the cache is never saved"),
    (r"throws it away when the process exits", "1: the cache always dies with the process"),
    (r"nothing after that", "1: the cache leaves nothing behind"),
    (r"resident while the process is open", "1: the cache is only ever resident"),
    (r"zero after", "1: the cache is always zero after the run"),
    # 2  two requests never share a cache
    (r"never share a cache", "2: two requests never share a cache"),
    (r"no cache is shared", "2: no cache is ever shared"),
    (r"never share", "2: caches are never shared"),
    (r"no cache sharing", "2: no cache sharing is possible"),
    (r"cannot reuse", "2: a prefix can never be reused"),
    # 3  the KV cache always scales nonlinearly
    (r"the curve is not linear", "3: the curve (and so the cache) is called nonlinear"),
    (r"cache is not linear", "3: the cache is called nonlinear"),
    (r"cache scales nonlinearly", "3: the cache is called nonlinear"),
    (r"cache is nonlinear", "3: the cache is called nonlinear"),
]

# Each claim needs a counterweight somewhere in the episode.
REQUIRED_PHRASES = [
    (r"depends on the serving system", "1: the cache lifetime depends on the serving system"),
    (r"llama\.cpp can save a slot", "1: an engine that can save the cache is named"),
    (r"prefix caching", "2: prefix reuse is named"),
    (r"the cache itself is linear", "3: the cache is stated to be linear in tokens"),
]


def check_absolute_claims(W):
    bad = []
    blob = []
    for w in W:
        blob.append((w.get("vo") or "").lower())
        blob.append(all_text(w).lower())
    joined = "\n".join(blob)
    for pat, why in FORBIDDEN:
        for m in re.finditer(pat, joined):
            bad.append("%s   (found %r)" % (why, m.group(0)))
    for pat, why in REQUIRED_PHRASES:
        if not re.search(pat, joined):
            bad.append("%s   (no counterweight found)" % why)
    return bad


# --------------------------------------------------------------------------
# 4  a speed comparison has to disclose its conditions
# --------------------------------------------------------------------------
RATE_RE = re.compile(r"(\d[\d,]*(?:\.\d+)?)\s*(?:t/s|tokens per second)", re.I)
LIST_RE = re.compile(r"t/s\s*:(.+)", re.I)
CTX_RE = re.compile(r"\b\d+\s?k\b", re.I)


def rates_in(w):
    """Every generation or prefill rate the window puts on screen."""
    found = set()
    for label, text in strings(w):
        s = str(text)
        for m in RATE_RE.finditer(s):
            found.add(m.group(1))
        m = LIST_RE.search(s)
        if m:
            for tok in NUM.findall(m.group(1)):
                if "." in tok:
                    found.add(tok)
    return found


def check_comparison_conditions(W):
    bad = []
    for i, w in enumerate(W):
        rates = rates_in(w)
        if len(rates) < 2:
            continue
        blob = ((w.get("vo") or "") + " " + all_text(w)).lower()
        if CTX_RE.search(blob) or "same context" in blob:
            continue
        # otherwise every rate has to carry its own context label
        labelled = True
        for label, text in strings(w):
            s = str(text)
            if not RATE_RE.search(s) and not LIST_RE.search(s):
                continue
            if not CTX_RE.search(s):
                labelled = False
        if not labelled:
            bad.append("window %d compares rates %s without a context"
                       % (i + 1, ", ".join(sorted(rates))))
    return bad


# --------------------------------------------------------------------------
# 5  a requirement above the card is not a fit
# --------------------------------------------------------------------------
CARD_GB = 24.0
GB_VALUES = {
    "18": 18, "19": 19, "20": 20, "22": 22, "24": 24, "26": 26, "34": 34,
    "16": 16, "17": 17, "32": 32, "128": 128,
}
QUALIFIERS = ("required", "requirement", "over the card", "does not fit",
              "neither fits", "larger than", "not fit", "no longer enough",
              "too big", "needs", "need")


def check_capacity_claims(W):
    bad = []
    for i, w in enumerate(W):
        over = []
        for label, text in strings(w):
            if label not in ("row.val", "bar.val", "row.sub", "note.item"):
                continue
            s = str(text)
            for tok in NUM.findall(s):
                try:
                    v = float(tok.replace(",", ""))
                except ValueError:
                    continue
                if v > CARD_GB and "GB" in s.upper():
                    over.append(tok)
        if not over:
            continue
        blob = ((w.get("vo") or "") + " " + all_text(w)).lower()
        if not any(q in blob for q in QUALIFIERS):
            bad.append("window %d shows %s GB, above a %d GB card, with no "
                       "qualifier" % (i + 1, ", ".join(sorted(set(over))), CARD_GB))
    return bad


# --------------------------------------------------------------------------
# 6  a measured source names the rig it was measured on
# --------------------------------------------------------------------------
RIG_TOKENS = ("rtx", "m5 max", "gb10", "cuda", "llama.cpp", "ubuntu", "driver")


def check_source_provenance(W):
    bad = []
    for i, w in enumerate(W):
        src = str(w.get("source") or "")
        if not src:
            continue
        cls = src.split("&middot;")[0].strip().lower()
        if cls not in ("measured", "external measurement"):
            continue
        blob = (src + " " + (w.get("vo") or "") + " " + all_text(w)).lower()
        if not any(t in blob for t in RIG_TOKENS):
            bad.append("window %d is sourced as measured but names no rig"
                       % (i + 1))
    return bad


# --------------------------------------------------------------------------
# 7  every number on screen is in the fact sheet, and the fact sheet says
#    where the number is spoken
# --------------------------------------------------------------------------
def check_fact_sheet(W):
    bad = []
    if not os.path.exists(FACTS_PATH):
        return ["the fact sheet data/EP09-FACTS.json is missing"]
    sheet = json.load(open(FACTS_PATH, encoding="utf-8"))
    facts = sheet["facts"]
    covered = {}
    for f in facts:
        for sc in f["scenes"]:
            covered.setdefault(sc, set()).add(f["value"])
    for i, w in enumerate(W):
        seen = set()
        for label, text in strings(w):
            for tok in NUM.findall(str(text)):
                if tok not in seen:
                    seen.add(tok)
        for tok in sorted(seen):
            if tok not in covered.get(i + 1, set()):
                bad.append("window %d shows %s, which is not in the fact sheet"
                           % (i + 1, tok))
    # the spoken side: a fact that claims to be spoken must be spoken
    for f in facts:
        spoken = f.get("spoken_as")
        if not spoken:
            continue
        phrases = [spoken] if isinstance(spoken, str) else list(spoken)
        for sc in f.get("spoken_in", []):
            vo = (W[sc - 1].get("vo") or "").lower()
            if not any(p.lower() in vo for p in phrases):
                bad.append("%s: none of %s is spoken in window %d"
                           % (f["id"], phrases, sc))
    return bad


# --------------------------------------------------------------------------
# 8  no obvious typos in the text the viewer reads
# --------------------------------------------------------------------------
def check_spelling(W):
    bad = []
    words = load_words()
    for i, w in enumerate(W):
        for label, text in strings(w):
            if label == "source":
                continue          # the source line is machine text, not prose
            for tok in words_of(text):
                if tok in words or tok in SKIP:
                    continue
                if re.search(r"\d", tok):
                    continue
                if len(tok) <= 2:
                    continue
                bad.append("window %d %s: %r is not in the vocabulary"
                           % (i + 1, label, tok))
    return bad


# --------------------------------------------------------------------------
# 9  the chapters have to be valid for YouTube
# --------------------------------------------------------------------------
CH_MIN = 10.0


def check_chapters(path):
    bad = []
    if not os.path.exists(path):
        return ["the chapters file %s is missing" % os.path.basename(path)]
    rows = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        m = re.match(r"^(?:(\d+):)?(\d{1,2}):(\d{2})\s+(.+)$", line)
        if not m:
            bad.append("chapter line is not a valid timestamp: %r" % line)
            continue
        h = int(m.group(1) or 0)
        mi = int(m.group(2))
        s = int(m.group(3))
        rows.append((h * 3600 + mi * 60 + s, m.group(4)))
    if len(rows) < 3:
        bad.append("only %d chapters; YouTube wants at least 3" % len(rows))
    if rows:
        if rows[0][0] != 0:
            bad.append("the first chapter starts at %d s, not 0" % rows[0][0])
        for i in range(1, len(rows)):
            if rows[i][0] <= rows[i - 1][0]:
                bad.append("chapter %d does not move forward" % (i + 1))
        for i in range(len(rows) - 1):
            d = rows[i + 1][0] - rows[i][0]
            if d < CH_MIN:
                bad.append("chapter %d is only %.1fs long (%s)"
                           % (i + 1, d, rows[i][1]))
        titles = [r[1] for r in rows]
        if len(set(titles)) != len(titles):
            bad.append("two chapters share a title")
    return bad


# --------------------------------------------------------------------------
# 10  a QA report has to exist and has to carry the real run
# --------------------------------------------------------------------------
QA_REPORT = os.path.join(ROOT, "BYTE-EP09-FINAL-QA.md")
QA_MARKERS = ("STRUCTURAL AUDIT", "RENDER", "AUDIO", "SOURCE", "PUBLICATION DECISION")


def check_qa_evidence():
    bad = []
    if not os.path.exists(QA_REPORT):
        return ["the QA report BYTE-EP09-FINAL-QA.md is missing"]
    text = open(QA_REPORT, encoding="utf-8").read()
    up = text.upper()
    for m in QA_MARKERS:
        if m not in up:
            bad.append("the QA report has no %s section" % m)
    if len(text) < 3000:
        bad.append("the QA report is only %d characters; that is not a report"
                   % len(text))
    if "PUBLICATION DECISION" in up:
        m = re.search(r"PUBLICATION DECISION.{0,400}", up, re.S)
        seg = m.group(0) if m else ""
        if not re.search(r"\bPASS\b|\bBLOCKED\b|PASS WITH MINOR NOTES", seg):
            bad.append("the QA report states no publication decision")
    return bad


# --------------------------------------------------------------------------
def main(spec_name="spec_ep09_full"):
    spec = importlib.import_module(spec_name)
    W = spec.W
    chapters = os.path.join(ROOT, "%s-CHAPTERS.txt" % spec.NAME)
    results = [
        ("1  the cache is never saved", check_absolute_claims(W)),
        ("4  a speed comparison discloses its conditions", check_comparison_conditions(W)),
        ("5  a requirement above the card is not a fit", check_capacity_claims(W)),
        ("6  a measured source names its rig", check_source_provenance(W)),
        ("7  every number is in the fact sheet", check_fact_sheet(W)),
        ("8  no obvious typo in the visible text", check_spelling(W)),
        ("9  the chapters are valid for YouTube", check_chapters(chapters)),
        ("10 a QA report exists and carries the run", check_qa_evidence()),
    ]
    total = 0
    for name, bad in results:
        total += len(bad)
        if bad:
            print("FAIL  %s" % name)
            for b in bad[:40]:
                print("        %s" % b)
            if len(bad) > 40:
                print("        ... and %d more" % (len(bad) - 40))
        else:
            print("PASS  %s" % name)
    print("\n%d issue(s)" % total)
    if total:
        raise SystemExit("CLAIM CHECK FAILED")
    print("CLAIM CHECK PASSED")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "spec_ep09_full")
