# -*- coding: utf-8 -*-
"""Measure the leading gap of every window in a built episode.

For each window: scene start, first beat, last beat, scene end, and the gap
between the window opening and its first visible element.

Usage: python data/_probe_gap.py BYTE-EP09
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EP = sys.argv[1]
html = open(os.path.join(ROOT, EP + ".html"), "r", encoding="utf-8").read()
m = re.search(r"window\.FUSION\s*=\s*(\{.*?\});\s*</script>", html, re.S)
F = json.loads(m.group(1))

scenes = F["scenes"]
beats = F["beats"]

print("%-6s %-14s %8s %8s %8s %8s %9s %6s" %
      ("win", "label", "start", "first", "last", "end", "leadGap", "beats"))
bad = []
for i, s in enumerate(scenes):
    ws = [b for b in beats if b.get("group") == i]
    if not ws:
        print("%-6d %-14s %8.2f %8s %8s %8.2f %9s %6d" %
              (i, s.get("label"), s["s"], "-", "-", s.get("e", -1), "NO BEATS", 0))
        bad.append((i, s.get("label"), "NO BEATS", 0))
        continue
    first = min(b["s"] for b in ws)
    last = max(b["e"] for b in ws)
    lead = first - s["s"]
    flag = ""
    if lead > 0.35:
        flag = "  <== LATE OPEN"
        bad.append((i, s.get("label"), "lead %.2f" % lead, len(ws)))
    print("%-6d %-14s %8.2f %8.2f %8.2f %8.2f %9.2f %6d%s" %
          (i, s.get("label"), s["s"], first, last, s.get("e", -1), lead, len(ws), flag))

print()
print("windows opening late (>0.35s):", len(bad))
for i, lab, why, n in bad:
    print("   scene %-3d %-14s %s (%d beats)" % (i, lab, why, n))
