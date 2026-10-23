# -*- coding: utf-8 -*-
"""Compare the script's words with the synthesiser's tokens, word for word."""
import difflib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

EP = sys.argv[1] if len(sys.argv) > 1 else "BYTE-EP09-KV"
SPEC = sys.argv[2] if len(sys.argv) > 2 else "spec_ep09_full"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

s = io.open(os.path.join(ROOT, EP + ".html"), encoding="utf-8").read()
F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", s, re.S).group(1))
tts = [t for _, t in F["words"]]
scenes = F["scenes"]

import importlib
mod = importlib.import_module(SPEC)

scr = []
for w in mod.W:
    scr.extend(w["vo"].split())


def norm(x):
    return x.lower().strip(".,;:!?\"'()[]")


print("script words %d   tts tokens %d" % (len(scr), len(tts)))

sm = difflib.SequenceMatcher(None, [norm(x) for x in scr],
                             [norm(x) for x in tts], autojunk=False)
diffs = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        continue
    diffs += 1
    print("  %-8s script=%r  tts=%r" % (tag, scr[i1:i2][:8], tts[j1:j2][:8]))
print("alignment blocks that are not equal:", diffs)

print("\nper window: script words vs tts tokens")
for i, w in enumerate(mod.W):
    vw = len(w["vo"].split())
    ws = sum(1 for t, _ in F["words"] if scenes[i]["s"] <= t < scenes[i]["e"])
    if vw != ws:
        print("  win %2d %-7s script=%d tts=%d  diff %+d"
              % (i + 1, w["layout"], vw, ws, ws - vw))
