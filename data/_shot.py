# -*- coding: utf-8 -*-
"""One-shot screenshot of a built episode at a given timestamp."""
import os
import sys

from playwright.sync_api import sync_playwright

EP = sys.argv[1]
T = sys.argv[2] if len(sys.argv) > 2 else "0"
OUT = sys.argv[3] if len(sys.argv) > 3 else os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "proof", EP + "_t.png")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, EP + ".html")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={"width": 1920, "height": 1080})
    pg.goto("file:///" + PATH.replace("\\", "/") + "?t=" + str(T), wait_until="load")
    pg.wait_for_timeout(1400)
    pg.screenshot(path=OUT)
    br.close()

print("wrote", OUT)
