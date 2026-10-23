# -*- coding: utf-8 -*-
"""Print the timing of the first scenes of a built episode.

Usage: python data/_probe_start.py BYTE-EP09 [n_scenes]
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EP = sys.argv[1]
N = int(sys.argv[2]) if len(sys.argv) > 2 else 3

path = os.path.join(ROOT, EP + ".html")
html = open(path, "r", encoding="utf-8").read()

m = re.search(r"window\.FUSION\s*=\s*(\{.*?\});\s*</script>", html, re.S)
if not m:
    m = re.search(r"window\.FUSION\s*=\s*(\{.*\})\s*;?\s*\n", html, re.S)
if not m:
    raise SystemExit("FUSION object not found")
F = json.loads(m.group(1))

print("total:", F.get("total"))
print("scenes:", len(F.get("scenes", [])), " beats:", len(F.get("beats", [])))
for i, s in enumerate(F["scenes"][:N]):
    print("scene %d  %0.2f -> %0.2f  label=%r" % (i, s["s"], s.get("e", -1), s.get("label")))

print("--- first 18 beats ---")
for b in F["beats"][:18]:
    print("  %-14s %-7s at=%0.3f dur=%s" % (b.get("el"), b.get("kind"), b.get("s"), b.get("dur")))

print("--- beats in the first %d s ---" % N * 0)
for b in F["beats"]:
    if b.get("s", 0) < (F["scenes"][min(N, len(F["scenes"])) - 1].get("e") or 0):
        print("  %-14s %-7s at=%0.3f dur=%s" % (b.get("el"), b.get("kind"), b.get("s"), b.get("dur")))

print("--- first scene markup (scene 0) ---")
m2 = re.search(r'<section class="scene[^"]*"[^>]*>.*?</section>', html, re.S)
if m2:
    mk = m2.group(0)
    print("len:", len(mk))
    print(mk[:2600])
