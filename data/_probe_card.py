# -*- coding: utf-8 -*-
"""Print the children of one card class and how each sits against the card.

Usage: python data/_probe_card.py EPISODE CARD_SELECTOR [t ...]
"""
import os
import sys

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EP = sys.argv[1]
SEL = sys.argv[2]
TIMES = [float(x) for x in sys.argv[3:]] or [0.0]
PATH = os.path.join(ROOT, EP + ".html")

JS = """
(sel) => {
  const out = [];
  const scene = document.querySelector('.scene.on');
  if (!scene) return out;
  scene.querySelectorAll(sel).forEach((card) => {
    const cs = getComputedStyle(card);
    const cb = card.getBoundingClientRect();
    const box = {
      l: cb.left + (parseFloat(cs.paddingLeft) || 0),
      r: cb.right - (parseFloat(cs.paddingRight) || 0),
      t: cb.top + (parseFloat(cs.paddingTop) || 0),
      b: cb.bottom - (parseFloat(cs.paddingBottom) || 0)
    };
    out.push({who: 'CARD ' + card.className, box, pad: cs.padding, m: cs.margin});
    card.querySelectorAll('*').forEach((c) => {
      const s = getComputedStyle(c);
      const rc = c.getBoundingClientRect();
      const over = Math.max(0, box.l - rc.left, rc.right - box.r, box.t - rc.top, rc.bottom - box.b);
      if (over > 0.5) {
        out.push({
          who: (c.tagName + '.' + (c.getAttribute('class') || '')).slice(0, 60),
          over: Math.round(over * 10) / 10,
          rect: {l: Math.round(rc.left), t: Math.round(rc.top),
                 r: Math.round(rc.right), b: Math.round(rc.bottom)},
          box: {l: Math.round(box.l), t: Math.round(box.t),
                r: Math.round(box.r), b: Math.round(box.b)},
          pos: s.position, mt: s.marginTop, fs: s.fontSize, lh: s.lineHeight
        });
      }
    });
  });
  return out;
}
"""

with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={"width": 1920, "height": 1080})
    for t in TIMES:
        pg.goto("file:///" + PATH.replace("\\", "/") + "?t=" + str(t), wait_until="load")
        pg.wait_for_timeout(800)
        print("--- t=%.1f ---" % t)
        for e in pg.evaluate(JS, SEL):
            print("  ", e)
    br.close()
