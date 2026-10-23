# -*- coding: utf-8 -*-
"""One frame per window, captured at the END of the window so the art is
fully drawn.  This is the real look review."""
import io
import json
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-LIB"

s = io.open(os.path.join(ROOT, NAME + ".html"), encoding="utf-8").read()
F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", s, re.S).group(1))
scenes = F["scenes"]

out = os.path.join(ROOT, "proof", NAME + "_windows")
os.makedirs(out, exist_ok=True)
url = "file:///" + os.path.join(ROOT, NAME + ".html").replace("\\", "/")

shots = []
with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={"width": 1920, "height": 1080})
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    pg.goto(url + "?t=0", wait_until="load")
    pg.wait_for_timeout(300)
    pg.evaluate("() => document.fonts.ready")
    for sc in scenes:
        t = max(0.0, sc["e"] - 0.45)
        pg.evaluate("(t) => window.renderAt(t)", t)
        pg.evaluate("() => new Promise(r => requestAnimationFrame("
                    "() => requestAnimationFrame(() => r(1))))")
        p = os.path.join(out, "w%02d.png" % (sc["id"] + 1))
        pg.screenshot(path=p)
        shots.append((sc, p))
    br.close()

print("console errors:", errs[:3] if errs else "none")

COLS = 3
TW = 620
TH = int(TW * 1080 / 1920)
rows = (len(shots) + COLS - 1) // COLS
PAD, LBL = 6, 20
sheet = Image.new("RGB", (COLS * (TW + PAD) + PAD, rows * (TH + PAD + LBL) + PAD), (8, 10, 10))
d = ImageDraw.Draw(sheet)
try:
    f = ImageFont.truetype("seguisb.ttf", 14)
except Exception:
    f = ImageFont.load_default()
for k, (sc, p) in enumerate(shots):
    im = Image.open(p).convert("RGB").resize((TW, TH), Image.LANCZOS)
    x = PAD + (k % COLS) * (TW + PAD)
    y = PAD + (k // COLS) * (TH + PAD + LBL)
    sheet.paste(im, (x, y + LBL))
    d.text((x + 3, y + 2), "window %02d  t=%.1f" % (sc["id"] + 1, sc["e"] - 0.45),
           font=f, fill=(150, 255, 190))
sheet.save(os.path.join(ROOT, "proof", NAME + "_windows.jpg"), quality=92)
print("wrote proof/%s_windows.jpg  (%d windows)" % (NAME, len(shots)))
h = sheet.height
for i in range(4):
    sheet.crop((0, h * i // 4, sheet.width, h * (i + 1) // 4)).save(
        os.path.join(ROOT, "proof", "_%s_w%d.png" % (NAME, i + 1)))
print("split into 4")
