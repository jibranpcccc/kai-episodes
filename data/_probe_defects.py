# -*- coding: utf-8 -*-
"""Verify specific defects against a built FUSION deliverable.

    python data/_probe_defects.py BYTE-LORA

Read-only. Checks the things a spec-level review cannot see because they
only exist in the RENDERED output.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-LORA"

src = io.open(os.path.join(ROOT, NAME + ".html"), encoding="utf-8").read()
secs = re.findall(r'<section class="scene" data-scene="(\d+)">(.*?)</section>', src, re.S)
print("scenes parsed:", len(secs))
body = [b for _, b in secs]

print()
print("=== CHECK 1: the bars layout hardcodes a unit suffix ===")
for i, b in enumerate(body):
    if 'class="bar bar--' in b or 'class="bar ' in b:
        print("  scene %s  bars layout" % i)
        for mm in re.finditer(r'<div class="bar__val">(.*?)</div>', b, re.S):
            txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "|", mm.group(1))).strip()
            print("      rendered:", txt)
        for mm in re.finditer(r"<small>(.*?)</small>", b, re.S):
            print("      unit suffix:", mm.group(1))

print()
print("=== CHECK 2: which scenes carry a source footer ===")
missing = []
for i, b in enumerate(body):
    if 'class="src"' not in b:
        missing.append(i)
print("  scenes WITHOUT a .src footer:", missing if missing else "none")
print("  scenes WITH    a .src footer:",
      [i for i in range(len(body)) if i not in missing])

print()
print("=== CHECK 3: which values actually get a count-up ===")
for i, b in enumerate(body):
    vals = re.findall(r'data-num>([^<]*)<', b)
    if vals:
        print("  scene %2d  %s" % (i, vals))

print()
print("=== CHECK 4: values with NO count-up (static text) ===")
for i, b in enumerate(body):
    if 'class="row__val"' in b:
        vals = re.findall(r'<span class="row__val"><span data-num>([^<]*)</span>', b)
        if vals:
            print("  scene %2d  %s" % (i, vals))

print()
print("=== CHECK 5: document title vs payload title ===")
t = re.search(r"<title>(.*?)</title>", src, re.S)
doc = t.group(1).strip() if t else ""
m = re.search(r'window\.FUSION = \{"title":"([^"]*)"', src)
pay = m.group(1) if m else "?"
print("  <title>      :", doc)
print("  payload title:", pay)
# the document title may add a series suffix; what matters is that the
# on-screen headline is inside it and that it is not a leftover literal
if pay and pay.replace("&middot;", "·") in doc.replace("&middot;", "·"):
    print("  OK - the on-screen title is inside the document title")
else:
    print("  **MISMATCH** - the document title does not carry the episode title")

print()
print("=== CHECK 6: duplicate narration between windows ===")
F = None
try:
    import json
    F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", src, re.S).group(1))
except Exception as e:
    print("  payload parse failed:", e)
if F:
    words = F["words"]
    # rebuild per-scene word text
    per = {}
    for t2, w in words:
        per.setdefault(0, []).append(w)
    # scene word ranges
    seen = {}
    for i, sc in enumerate(F["scenes"]):
        txt = " ".join(w for t2, w in words if sc["s"] <= t2 <= sc["e"]).lower()
        seen[i] = txt
    for i in range(len(seen)):
        for j in range(i + 1, len(seen)):
            a, b = seen[i], seen[j]
            if len(a) < 80 or len(b) < 80:
                continue
            # longest common substring, word level
            aw, bw = a.split(), b.split()
            best = ""
            for x in range(len(aw)):
                for y in range(len(bw)):
                    k = 0
                    while x + k < len(aw) and y + k < len(bw) and aw[x + k] == bw[y + k]:
                        k += 1
                    if k > len(best.split()):
                        best = " ".join(aw[x:x + k])
            if len(best.split()) >= 8:
                print("  scene %2d and %2d share %d words: %r" % (i, j, len(best.split()), best[:110]))
