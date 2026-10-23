# -*- coding: utf-8 -*-
r"""Regenerate the .srt and the chapters file for an already-built FUSION episode.

    python data\_regen_srt.py BYTE-LORA spec_lora_full

The shipped FUSION episodes were built by a caption writer that dropped the
last word of every window and emitted one cue per word. This rebuilds the
captions from data that is already inside the episode HTML -- the word
timings in the window.FUSION payload -- so there is no need to re-run the
text to speech pass and no need to rebuild the episode.

The caption text is always the spec's own `vo` strings, punctuation included.
The synthesiser re-tokenises what it is given ("llama.cpp" arrives as three
tokens), so the two are aligned word by word: the caption keeps the written
line and the synthesiser supplies the timing.
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

from fusion_build import CAPTION_WORDS, _align_tokens, _groups

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def srt_ts(x):
    h = int(x // 3600)
    m = int((x % 3600) // 60)
    s = x % 60
    return ("%02d:%02d:%06.3f" % (h, m, s)).replace(".", ",")


def plain(s):
    return (s or "").replace("&middot;", "·").replace("&amp;", "&") \
        .replace("&lt;", "<").replace("&gt;", ">").replace("&nbsp;", " ").strip()


def main(name, spec_name=None):
    html = os.path.join(ROOT, name + ".html")
    if not os.path.exists(html):
        print("no such episode: %s" % html)
        return 1
    src = io.open(html, encoding="utf-8").read()
    F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", src, re.S).group(1))
    scenes = F["scenes"]
    words = F["words"]

    # the spec gives us the written narration, window by window
    vos = []
    if spec_name:
        sys.path.insert(0, os.path.join(ROOT, "data"))
        import importlib
        spec = importlib.import_module(spec_name)
        vos = [w["vo"] for w in spec.W]
        kickers = [plain(w.get("kicker") or w.get("title", "")) for w in spec.W]
    if len(vos) != len(scenes):
        vos = []
        kickers = []

    cues = []
    chap = []
    for i, sc in enumerate(scenes):
        ws = [(t, w) for t, w in words if sc["s"] <= t <= sc["e"]]
        if not ws:
            continue
        vw = vos[i].split() if vos else []
        if vw:
            tok = _align_tokens(vw, ws)
            groups = _groups(len(vw), CAPTION_WORDS)
            cstart = []
            for a, b in groups:
                t = ws[tok[a]][0]
                if cstart and t <= cstart[-1]:
                    t = cstart[-1] + 0.05
                cstart.append(t)
            for c, (a, b) in enumerate(groups):
                t0 = cstart[c]
                t1 = cstart[c + 1] if c + 1 < len(cstart) else sc["e"]
                cues.append((t0, t1, " ".join(vw[a:b])))
        else:
            for j in range(0, len(ws), CAPTION_WORDS):
                grp = ws[j:j + CAPTION_WORDS]
                t0 = grp[0][0]
                t1 = ws[j + CAPTION_WORDS][0] if j + CAPTION_WORDS < len(ws) else sc["e"]
                cues.append((t0, t1, " ".join(x for _, x in grp)))
        lab = kickers[i] if kickers else "WINDOW %02d" % (i + 1)
        chap.append("%d:%02d %s %02d" % (int(sc["s"] // 60), int(sc["s"] % 60), lab, i + 1))

    lines = []
    for k, (a, b, t) in enumerate(cues, 1):
        lines.append("%d\n%s --> %s\n%s\n" % (k, srt_ts(a), srt_ts(b), t.strip()))
    srt_path = os.path.join(ROOT, name + ".srt")
    io.open(srt_path, "w", encoding="utf-8").write("\n".join(lines))

    chap_path = os.path.join(ROOT, name + "-chapters.txt")
    io.open(chap_path, "w", encoding="utf-8").write("\n".join(chap))

    spoken = len(words)
    capt = sum(len(t.split()) for _, _, t in cues)
    script_n = sum(len(v.split()) for v in vos) if vos else 0
    thin = [t for _, _, t in cues if len(t.split()) < 2]
    print("%s" % name)
    print("  .srt      : %d cues, %d words" % (len(cues), capt))
    print("  coverage  : %d of %d script words (%.2f%%)"
          % (capt, script_n or spoken, 100.0 * capt / max(1, script_n or spoken)))
    print("  spoken tokens: %d" % spoken)
    print("  script text used: %s" % ("yes" if vos else "synthesiser tokens"))
    print("  single-word cues : %d" % len(thin))
    print("  chapters  : %d" % len(chap))
    if vos and capt != script_n:
        print("  ** coverage is not 100% of the script **")
        return 1
    if not vos and capt != spoken:
        print("  ** coverage is not 100% **")
        return 1
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    rc = 0
    args = sys.argv[1:]
    if len(args) == 1 and "," in args[0]:
        args = args[0].split(",")
    i = 0
    while i < len(args):
        nm = args[i]
        sp = args[i + 1] if i + 1 < len(args) and not args[i + 1].lower().endswith(".html") else None
        rc |= main(nm, sp)
        i += 2 if sp else 1
    sys.exit(rc)
