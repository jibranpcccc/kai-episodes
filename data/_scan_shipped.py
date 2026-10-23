# -*- coding: utf-8 -*-
"""Report which shipped episodes still carry the pre-fix engine defects.

  * an unbounded pivot  -- data-amb="spin" with data-amb-box (a needle on a
    bounded dial that rotates a full 360 degrees and leaves the drawing)
  * a bare connector   -- class="chain__arrow" with no id and no beat, so the
    arrow is painted from the first frame of its window
  * a late opening     -- a window whose first element arrives more than
    0.35s after the window opens

Usage: python data/_scan_shipped.py [NAME ...]
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAMES = sys.argv[1:] or [
    "BYTE-EP09", "BYTE-EP09-KV", "BYTE-LORA", "BYTE-LORA-SAMPLE",
    "BYTE-LORA-30S", "BYTE-07-FUSION", "BYTE-STACK", "BYTE-LIB",
]

print("%-18s %10s %9s %9s %8s %9s" %
      ("episode", "size(MB)", "unbound", "bareArrow", "lateOpen", "worstGap"))
for name in NAMES:
    path = os.path.join(ROOT, name + ".html")
    if not os.path.exists(path):
        print("%-18s   (no file)" % name)
        continue
    html = open(path, "r", encoding="utf-8", errors="replace").read()
    mb = os.path.getsize(path) / 1048576.0

    unbound = len(re.findall(r'data-amb="spin"[^>]*data-amb-box', html))
    tags = re.findall(r'<[^>]*class="chain__arrow"[^>]*>', html)
    bare = sum(1 for t in tags if 'id="' not in t)

    late = 0
    worst = 0.0
    m = re.search(r"window\.FUSION\s*=\s*(\{.*?\});\s*</script>", html, re.S)
    if m:
        F = json.loads(m.group(1))
        beats = F.get("beats", [])
        for i, sc in enumerate(F.get("scenes", [])):
            bs = [b["s"] for b in beats if b.get("group") == i]
            if not bs:
                late += 1
                worst = max(worst, 99.0)
                continue
            g = min(bs) - sc["s"]
            if g > 0.35:
                late += 1
                worst = max(worst, g)
    print("%-18s %10.2f %9d %9d %8d %9.2f" %
          (name, mb, unbound, bare, late, worst))
