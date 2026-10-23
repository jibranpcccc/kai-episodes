# -*- coding: utf-8 -*-
"""Render the WHOLE asset library to one contact sheet."""
import os
import sys

sys.path.insert(0, r"C:\Users\jibra\Desktop\1\KAI\data")
import fusion_art as A

from playwright.sync_api import sync_playwright

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
names = sorted(A.ART)

cells = "".join('<div class="c"><div class="lab">%s</div>%s</div>' % (n, A.ART[n]())
                for n in names)
html = ('<!doctype html><html><head><meta charset="utf-8"><style>'
        '@font-face{font-family:"FuseMono";src:url("file:///C:/Users/jibra/Desktop/1/KAI/core/fonts/JetBrainsMono-Bold.ttf");font-weight:700}'
        'html,body{margin:0;background:#0D1110;font-family:FuseMono,monospace}'
        '.wrap{display:flex;flex-wrap:wrap}'
        '.c{width:620px;height:420px;position:relative;display:flex;align-items:center;'
        'justify-content:center;border:1px solid #1b2321;box-sizing:border-box}'
        '.c svg{width:590px;height:390px;overflow:visible}'
        '.lab{position:absolute;left:9px;top:7px;color:#F5C531;font-size:12px;'
        'letter-spacing:.18em;text-transform:uppercase;z-index:9}'
        '</style></head><body><div class="wrap">' + cells + '</div></body></html>')

tmp = os.path.join(ROOT, "proof", "_library.html")
open(tmp, "w", encoding="utf-8").write(html)

COLS = 4
rows = (len(names) + COLS - 1) // COLS
with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={"width": 620 * COLS, "height": 420 * rows})
    pg.goto("file:///" + tmp.replace("\\", "/"), wait_until="load")
    pg.wait_for_timeout(1400)
    out = os.path.join(ROOT, "proof", "_library.png")
    pg.screenshot(path=out, full_page=True)
    br.close()
print("wrote", out, "with", len(names), "assets")
