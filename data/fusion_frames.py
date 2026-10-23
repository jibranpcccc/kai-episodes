# -*- coding: utf-8 -*-
"""
FUSION FRAMES — render the built episode at chosen timestamps and build a
contact sheet.  THIS IS THE LOOK REVIEW.  If you do not look at the sheet,
you have not checked anything.
"""
import io
import json
import os
import re
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-07-FUSION"
OUT = os.path.join(ROOT, "proof", NAME + "_frames")
SHEET = os.path.join(ROOT, "proof", NAME + "_sheet.jpg")

s = io.open(os.path.join(ROOT, NAME + ".html"), encoding="utf-8").read()
F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", s, re.S).group(1))
beats = F["beats"]
scenes = F["scenes"]

# --- pick the timestamps: every beat, then thin them out ------------
times = [b["s"] for b in beats]
times += [sc["e"] - 0.6 for sc in scenes]
times = sorted(set(round(t, 2) for t in times))
# thin to at most MAX frames
MAX = int(os.environ.get("FUSION_MAX_FRAMES", "40"))
if len(times) > MAX:
    step = len(times) / float(MAX)
    times = [times[int(i * step)] for i in range(MAX)]

os.makedirs(OUT, exist_ok=True)
url = "file:///" + os.path.join(ROOT, NAME + ".html").replace("\\", "/")

from playwright.sync_api import sync_playwright

shots = []
with sync_playwright() as pw:
    br = pw.chromium.launch(args=["--force-color-profile=srgb", "--font-render-hinting=none"])
    pg = br.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
    errs = []
    pg.on("console", lambda m: errs.append(m.type + ": " + m.text) if m.type == "error" else None)
    pg.on("pageerror", lambda e: errs.append("pageerror: " + str(e)))
    for t in times:
        pg.goto(url + "?t=%.2f" % t, wait_until="load")
        pg.wait_for_timeout(420)
        p = os.path.join(OUT, "t%07.2f.png" % t)
        pg.screenshot(path=p)
        shots.append((t, p))
    br.close()

if errs:
    print("CONSOLE ERRORS:")
    for e in errs[:20]:
        print("   ", e)
else:
    print("no console errors")

# --- contact sheet -------------------------------------------------
COLS, TW = 5, 384
TH = int(TW * 1080 / 1920)
rows = (len(shots) + COLS - 1) // COLS
PAD, LBL = 6, 22
sheet = Image.new("RGB", (COLS * (TW + PAD) + PAD, rows * (TH + PAD + LBL) + PAD), (8, 10, 10))
d = ImageDraw.Draw(sheet)
try:
    f = ImageFont.truetype("seguisb.ttf", 15)
except Exception:
    f = ImageFont.load_default()
for k, (t, p) in enumerate(shots):
    im = Image.open(p).convert("RGB").resize((TW, TH), Image.LANCZOS)
    x = PAD + (k % COLS) * (TW + PAD)
    y = PAD + (k // COLS) * (TH + PAD + LBL)
    sheet.paste(im, (x, y + LBL))
    d.text((x + 3, y + 3), "t=%.2f" % t, font=f, fill=(150, 255, 190))
sheet.save(SHEET, quality=92)
print("wrote %s  (%d frames, %dx%d)" % (SHEET, len(shots), sheet.width, sheet.height))
print("frames in %s" % OUT)
