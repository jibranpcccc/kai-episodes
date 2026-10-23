# -*- coding: utf-8 -*-
"""Dump the raw bars markup of a scene so the unit suffix is visible.

    python data/_probe_bars.py BYTE-LORA 14
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-LORA"
SCENE = int(sys.argv[2]) if len(sys.argv) > 2 else 14

src = io.open(os.path.join(ROOT, NAME + ".html"), encoding="utf-8").read()
secs = re.findall(r'<section class="scene" data-scene="(\d+)">(.*?)</section>', src, re.S)
body = secs[SCENE][1]

k = body.find("bars__body")
if k < 0:
    k = body.find("bar__")
print(body[max(0, k - 200):k + 2600])
