# -*- coding: utf-8 -*-
"""Scratch: realistic proofs against a COPY of a real episode.

1. strip data-amb-amp from a real bounded sway  -> check 3 must FAIL
2. inject the original bug (bare <div class="chain__arrow">&rarr;</div>)
   into a real scene                             -> check 2b must FAIL
The real episode files are never touched.
"""
import os
import re
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import _check_open as co  # noqa: E402

SRC = os.path.join(co.ROOT, "BYTE-EP09.html")
html = open(SRC, encoding="utf-8").read()

# --- 1. a bounded sway that lost its amplitude ---------------------------
m = re.search(r'<[^>]*data-amb="sway"[^>]*data-amb-box="view-box"[^>]*>', html)
print("real sway tag:", m.group(0)[:160])
broken = html[:m.start()] + m.group(0).replace(' data-amb-amp="', ' data-amb-ampX="') + html[m.end():]

# --- 2. the original defect, injected into a real scene ------------------
chain = re.search(r'<div id="w\d+_\d+" data-fx="1" class="chain__arrow">&rarr;</div>', html)
print("real arrow tag:", chain.group(0)[:120])
inject = html[:chain.start()] + '<div class="chain__arrow">&rarr;</div>' + html[chain.end():]

tmp = tempfile.mkdtemp(prefix="checkopen_real_")
for label, body in (("MUTANT-SWAY", broken), ("MUTANT-ARROW", inject)):
    with open(os.path.join(tmp, "BYTE-EP09.html"), "w", encoding="utf-8") as fh:
        fh.write(body)
    co.ROOT = tmp
    print("=" * 70)
    print("CASE:", label)
    co.main(["_check_open.py", "BYTE-EP09"])
print("tmp:", tmp)
