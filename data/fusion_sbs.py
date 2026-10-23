# -*- coding: utf-8 -*-
"""Sample frames next to the APPROVED video's frames, same scale."""
import io
import os

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = r"C:\Users\jibra\Desktop\1\KAI"


def grab(path, times):
    url = "file:///" + os.path.join(ROOT, path).replace("\\", "/")
    out = []
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": 1920, "height": 1080})
        pg.goto(url + "?t=0", wait_until="load")
        pg.wait_for_timeout(400)
        pg.evaluate("() => document.fonts.ready")
        for t in times:
            pg.evaluate("(t) => window.renderAt(t)", t)
            pg.evaluate("() => new Promise(r => requestAnimationFrame("
                        "() => requestAnimationFrame(() => r(1))))")
            out.append(Image.open(io.BytesIO(pg.screenshot())).convert("RGB"))
        br.close()
    return out


approved = grab("BYTE-07-FUSION.html", [3.4, 12.0, 20.5, 29.0, 37.5])
sample = grab("BYTE-LORA-SAMPLE.html", [5.0, 17.0, 31.0, 45.0, 60.0])

TW, TH = 620, 349
sheet = Image.new("RGB", (2 * (TW + 8) + 8, 5 * (TH + 8) + 8), (8, 10, 10))
for r in range(5):
    for c, im in enumerate((approved[r], sample[r])):
        sheet.paste(im.resize((TW, TH), Image.LANCZOS), (8 + c * (TW + 8), 8 + r * (TH + 8)))
sheet.save(os.path.join(ROOT, "proof", "_side_by_side.jpg"), quality=94)
print("wrote proof/_side_by_side.jpg  (left: APPROVED BYTE-07-FUSION   right: NEW SAMPLE)")
