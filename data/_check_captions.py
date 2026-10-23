# -*- coding: utf-8 -*-
r"""Caption and chapter audit for a built FUSION episode.

    python data\_check_captions.py BYTE-EP09-KV spec_ep09_kv

Measures the gap between the script, the spoken audio and the shipped .srt.
The rule is 100%: every word the script says must be spoken, every spoken
word must be captioned, and the caption text must be the script's own words.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-EP09-KV"
SPEC = sys.argv[2] if len(sys.argv) > 2 else None

sys.path.insert(0, os.path.join(ROOT, "data"))


def parse_srt(path):
    if not os.path.exists(path):
        return None
    raw = io.open(path, encoding="utf-8-sig").read()
    cues = []
    for block in re.split(r"\r?\n\r?\n", raw.strip()):
        lines = [x for x in block.splitlines() if x.strip()]
        if len(lines) < 2:
            continue
        m = re.match(r"(\d+):(\d+):(\d+)[,.](\d+)\s*-->\s*(\d+):(\d+):(\d+)[,.](\d+)",
                     lines[1])
        if not m:
            continue
        g = [int(x) for x in m.groups()]
        a = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000.0
        b = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000.0
        cues.append((a, b, " ".join(lines[2:])))
    return cues


def norm(s):
    """Comparable form: case, punctuation and spacing."""
    s = s.lower().replace("&middot;", " ")
    s = re.sub(r"[^a-z0-9%.\- ]+", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def words_of(s):
    """Words with trailing sentence punctuation removed, so that a caption
    saying 'afford' matches a script saying 'afford.'"""
    out = []
    for w in norm(s).split():
        out.append(w.rstrip(".,;:!?"))
    return out


print("=" * 74)
print("CAPTION AUDIT  --  %s" % NAME)
print("=" * 74)

html = os.path.join(ROOT, NAME + ".html")
src = io.open(html, encoding="utf-8").read()
F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", src, re.S).group(1))
spoken = [w for _, w in F["words"]]
total = F["total"]
print("payload: %.1fs, %d spoken words, %d windows" % (total, len(spoken), len(F["scenes"])))

# --- the script, if a spec module was named ------------------------------
script_words = None
script_by_window = None
if SPEC:
    import importlib
    m = importlib.import_module(SPEC)
    script_by_window = [w["vo"].split() for w in m.W]
    script_words = [x for win in script_by_window for x in win]

cues = parse_srt(os.path.join(ROOT, NAME + ".srt"))
if cues is None:
    print("NO .srt FILE")
else:
    cue_words = [w for _, _, t in cues for w in words_of(t)]
    print()
    print("--- coverage ---")
    print("spoken words in the payload : %d" % len(spoken))
    print("words in the .srt           : %d" % len(cue_words))
    print("captured                    : %.2f%%" % (100.0 * len(cue_words) / max(1, len(spoken))))
    if script_words:
        print("words in the script         : %d" % len(script_words))
        print("script captured by the .srt : %.2f%%"
              % (100.0 * len(cue_words) / max(1, len(script_words))))

    # --- which words are missing ------------------------------------------
    if script_words:
        sn = words_of(" ".join(script_words))
        cn = list(cue_words)
        missing = []
        j = 0
        for w in sn:
            if j < len(cn) and cn[j] == w:
                j += 1
            else:
                missing.append(w)
        print()
        print("--- word-for-word match against the script ---")
        print("script words not found in the .srt : %d" % len(missing))
        if missing:
            print("   first 20:", " ".join(missing[:20]))

    # --- text fidelity: does the caption say what the script says? -------
    if script_words:
        s_all = words_of(" ".join(script_words))
        c_all = list(cue_words)
        same = sum(1 for a, b in zip(s_all, c_all) if a == b)
        first_diff = None
        for k, (a, b) in enumerate(zip(s_all, c_all)):
            if a != b:
                first_diff = (k, a, b)
                break
        print()
        print("--- caption text fidelity ---")
        print("identical leading words : %d / %d (%.2f%%)"
              % (same, len(s_all), 100.0 * same / max(1, len(s_all))))
        if first_diff:
            k, a, b = first_diff
            print("first divergence at word %d: script=%r  caption=%r" % (k, a, b))

    # --- timing ------------------------------------------------------------
    print()
    print("--- cue timing ---")
    gaps = []
    overlaps = 0
    for k in range(1, len(cues)):
        g = cues[k][0] - cues[k - 1][1]
        gaps.append(g)
        if g < -0.001:
            overlaps += 1
    if gaps:
        gaps_sorted = sorted(gaps)
        print("cues                 : %d" % len(cues))
        print("first cue starts at  : %.3fs" % cues[0][0])
        print("last cue ends at     : %.3fs   (audio is %.3fs)" % (cues[-1][1], total))
        print("silent tail left     : %.3fs" % (total - cues[-1][1]))
        print("overlapping cues     : %d" % overlaps)
        print("gap between cues     : min %.3f  median %.3f  max %.3f"
              % (gaps_sorted[0], gaps_sorted[len(gaps_sorted) // 2], gaps_sorted[-1]))
        long = [(cues[k + 1][0] - cues[k][1], cues[k][2][:40]) for k in range(len(cues) - 1)
                if cues[k + 1][0] - cues[k][1] > 0.30]
        print("gaps over 0.30s      : %d" % len(long))
        for g, t in long[:8]:
            print("    %.2fs after %r" % (g, t))

# --- per window: is the last word of the window captioned? ---------------
if script_by_window:
    print()
    print("--- per window: last word dropped? ---")
    # a window's span in the payload
    bad = []
    for i, sc in enumerate(F["scenes"]):
        ws = [w for t, w in F["words"] if sc["s"] <= t <= sc["e"]]
        if not ws:
            continue
        cw = set(w for x in ws for w in words_of(x))
        last = words_of(ws[-1])[0] if words_of(ws[-1]) else ""
        # find it in the caption text
        capt = " ".join(words_of(t) for _, _, t in cues) if cues else ""
        if (" " + last + " ") not in (" " + capt + " "):
            bad.append((i + 1, ws[-1]))
    print("windows whose final spoken word is absent from the .srt : %d of %d"
          % (len(bad), len(F["scenes"])))
    for i, w in bad[:12]:
        print("    window %2d  final word %r" % (i, w))

# --- chapters -------------------------------------------------------------
print()
print("--- chapters ---")
for p in (NAME + "-chapters.txt", NAME + "_chapters.txt", NAME + ".chapters.txt"):
    ex = os.path.join(ROOT, p)
    print("  %-28s %s" % (p, "present" if os.path.exists(ex) else "MISSING"))
found = [f for f in os.listdir(ROOT) if f.startswith(NAME) and "chapter" in f.lower()]
print("  chapter files found:", found if found else "none")
