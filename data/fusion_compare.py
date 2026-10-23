# -*- coding: utf-8 -*-
"""Prove a rebuild matches a shipped file, frame for frame."""
import os
import sys

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
A = sys.argv[1]
B = sys.argv[2]
PROBES = [3.2, 11.0, 19.4, 27.6, 36.1, 44.8, 52.0, 61.3, 70.0, 79.5, 88.0, 97.5, 106.0, 115.0]


def shots(path):
    url = "file:///" + os.path.join(ROOT, path).replace("\\", "/")
    out = []
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": 1920, "height": 1080})
        pg.goto(url + "?t=0", wait_until="load")
        pg.wait_for_timeout(400)
        pg.evaluate("() => document.fonts.ready")
        for t in PROBES:
            pg.evaluate("(t) => window.renderAt(t)", t)
            pg.evaluate("() => new Promise(r => requestAnimationFrame("
                        "() => requestAnimationFrame(() => r(1))))")
            out.append(np.asarray(Image.open(
                __import__("io").BytesIO(pg.screenshot())).convert("RGB"), dtype=np.int16))
        br.close()
    return out


sa = shots(A)
sb = shots(B)
worst = 0
for t, a, b in zip(PROBES, sa, sb):
    d = int(np.abs(a - b).max())
    n = int((np.abs(a - b).max(axis=2) > 8).sum())
    worst = max(worst, d)
    print("  t=%6.1f  max delta %-4d  pixels differ %d" % (t, d, n))
print("\n%s vs %s -> %s" % (A, B, "IDENTICAL" if worst == 0 else "DIFFERENT (worst %d)" % worst))
