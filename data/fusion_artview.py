# -*- coding: utf-8 -*-
"""Render every art drawing large so the flaws are actually visible."""
import io
import os
import sys

from playwright.sync_api import sync_playwright

sys.path.insert(0, r"C:\Users\jibra\Desktop\1\KAI\data")
from fusion_art import ART

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
one = sys.argv[1] if len(sys.argv) > 1 else None

names = [one] if one else list(ART.keys())
cells = []
for n in names:
    cells.append('<div class="c"><div class="lab">%s</div>%s</div>' % (n, ART[n]()))

html = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:"FuseMono";src:url("file:///C:/Users/jibra/Desktop/1/KAI/core/fonts/JetBrainsMono-Bold.ttf");font-weight:700}
html,body{margin:0;background:#0D1110;font-family:FuseMono,monospace}
.wrap{display:flex;flex-wrap:wrap;gap:0}
.c{width:960px;height:660px;position:relative;display:flex;align-items:center;
   justify-content:center;border:1px solid #1b2321;box-sizing:border-box}
.c svg{width:880px;height:600px;overflow:visible}
.lab{position:absolute;left:10px;top:8px;color:#F5C531;font-size:13px;letter-spacing:.2em;
     text-transform:uppercase;z-index:9}
</style></head><body><div class="wrap">%s</div></body></html>""" % "".join(cells)

tmp = os.path.join(ROOT, "proof", "_art.html")
open(tmp, "w", encoding="utf-8").write(html)

with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={"width": 960 * (1 if one else 2), "height": 660 * ((len(names) + 1) // 2)})
    pg.goto("file:///" + tmp.replace("\\", "/"), wait_until="load")
    pg.wait_for_timeout(900)
    out = os.path.join(ROOT, "proof", "_art.png" if not one else "_art_%s.png" % one)
    pg.screenshot(path=out, full_page=True)
    br.close()
print("wrote", out)
