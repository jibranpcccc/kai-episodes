# -*- coding: utf-8 -*-
"""Time the gate's frame-sampling loop, to find what it actually costs.

Usage: python data/_time_gate.py EPISODE [n_samples]
"""
import io
import os
import sys
import time

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EP = sys.argv[1]
N = int(sys.argv[2]) if len(sys.argv) > 2 else 20
PATH = os.path.join(ROOT, EP + ".html")

t_shot = 0.0
t_dec = 0.0
t_eval = 0.0
frames = []

with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={"width": 1920, "height": 1080})
    pg.goto("file:///" + PATH.replace("\\", "/") + "?t=0", wait_until="load")
    pg.wait_for_timeout(600)
    for k in range(N):
        t0 = time.time()
        pg.evaluate("(t) => window.renderAt(t)", k * 2.0)
        pg.evaluate("() => new Promise(r => requestAnimationFrame("
                    "() => requestAnimationFrame(() => r(1))))")
        t_eval += time.time() - t0
        t0 = time.time()
        raw = pg.screenshot(type="jpeg", quality=70)
        t_shot += time.time() - t0
        t0 = time.time()
        a = np.asarray(Image.open(io.BytesIO(raw)).convert("RGB"), dtype=np.int16)
        frames.append(a)
        t_dec += time.time() - t0
    br.close()

t0 = time.time()
for i in range(1, len(frames)):
    d = np.abs(frames[i] - frames[i - 1])
    _ = float((d.max(axis=2) > 18).mean())
t_diff = time.time() - t0

n = float(N)
print("EPISODE: %s   samples: %d" % (EP, N))
print("  evaluate + rAF   : %6.3f s/sample   -> %6.1f s for 600" % (t_eval / n, t_eval / n * 600))
print("  screenshot jpeg  : %6.3f s/sample   -> %6.1f s for 600" % (t_shot / n, t_shot / n * 600))
print("  jpeg decode+numpy: %6.3f s/sample   -> %6.1f s for 600" % (t_dec / n, t_dec / n * 600))
print("  frame diff loop  : %6.3f s/sample   -> %6.1f s for 600" % (t_diff / n, t_diff / n * 600))
tot = (t_eval + t_shot + t_dec) / n + t_diff / n
print("  TOTAL            : %6.3f s/sample   -> %6.1f s for 600" % (tot, tot * 600))
