# -*- coding: utf-8 -*-
"""Check a spec's layout rotation, source coverage and closing coverage."""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mods = sys.argv[1:] or ["spec_ep09_full"]
W = []
for m in mods:
    mod = importlib.import_module(m)
    W.extend(mod.W)

print("=== %s : %d windows ===" % ("+".join(mods), len(W)))
prev = None
runs = 0
for i, w in enumerate(W):
    lay = w["layout"]
    n = len(w["vo"].split())
    flag = []
    if not w.get("source"):
        flag.append("NO-SOURCE")
    if w.get("art") is None and lay not in ("strip", "title"):
        flag.append("NO-ART")
    if lay == prev:
        flag.append("SAME-LAYOUT")
        runs += 1
    if lay in ("bars", "rows", "rail", "chain", "note", "nodes", "strip") \
            and not (w.get("closing") or w.get("tape")):
        flag.append("NO-CLOSING")
    if n < 26 or n > 52:
        flag.append("WORDS-%d" % n)
    prev = lay
    print("  %2d  %-8s %-16s %3dw  %s"
          % (i + 1, lay, w.get("art", "-"), n, " ".join(flag)))

print()
print("layout sequence:")
print("  " + ", ".join(w["layout"] for w in W))
print()
print("consecutive same-layout runs:", runs)
print("windows without a source:",
      [i + 1 for i, w in enumerate(W) if not w.get("source")])
print("windows without a closing chip or tape:",
      [i + 1 for i, w in enumerate(W)
       if w["layout"] in ("bars", "rows", "rail", "chain", "note", "nodes", "strip")
       and not (w.get("closing") or w.get("tape"))])
print("total words:", sum(len(w["vo"].split()) for w in W))
