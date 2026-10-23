# -*- coding: utf-8 -*-
"""Nudge / arrival-latency audit straight from the built payload.

    python data/_probe_nudge.py BYTE-LORA
"""
import io
import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-LORA"
src = io.open(os.path.join(ROOT, NAME + ".html"), encoding="utf-8").read()
F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", src, re.S).group(1))

late = [b for b in F["beats"] if b.get("nudge", 0) > 0.9]
early = [b for b in F["beats"] if b.get("nudge", 0) < -1.5]
print("beats total            :", len(F["beats"]))
print("LATE  (nudge >  0.9 s) :", len(late))
for b in late:
    print("   scene %2d  %-9s nudge %+5.2fs  %r" % (b["group"], b.get("el"), b["nudge"], (b.get("anchor") or "")[:52]))
print("EARLY (nudge < -1.5 s) :", len(early))
for b in early:
    print("   scene %2d  %-9s nudge %+5.2fs  %r" % (b["group"], b.get("el"), b["nudge"], (b.get("anchor") or "")[:52]))

ns = sorted(b.get("nudge", 0) for b in F["beats"])
print()
print("nudge distribution: min %.2f  p50 %.2f  p90 %.2f  max %.2f" % (ns[0], ns[len(ns) // 2], ns[int(len(ns) * .9)], ns[-1]))

# how many beats are pulled forward more than 1s (tease) - these land BEFORE their word
tease = [b for b in F["beats"] if b.get("nudge", 0) < -1.0]
print("teased forward >1.0s  :", len(tease))
for b in tease:
    print("   scene %2d  %-9s nudge %+5.2fs  %r" % (b["group"], b.get("el"), b["nudge"], (b.get("anchor") or "")[:52]))
