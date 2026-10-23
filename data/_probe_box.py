# -*- coding: utf-8 -*-
"""One-shot DOM probe: dump element boxes for one scene of a built episode."""
import json
import os
import sys

from playwright.sync_api import sync_playwright

EP = sys.argv[1] if len(sys.argv) > 1 else "BYTE-LAYOUT-PROBE"
SCENE = sys.argv[2] if len(sys.argv) > 2 else "0"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, EP + ".html")

with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={"width": 1920, "height": 1080})
    pg.goto("file:///" + PATH.replace("\\", "/") + "?t=0", wait_until="load")
    pg.wait_for_timeout(600)
    out = pg.evaluate(r"""(sc) => {
      const el = document.querySelector('.scene[data-scene="' + sc + '"]');
      if (!el) return {err: 'no scene'};
      const rows = [];
      el.querySelectorAll('[data-fx]').forEach(e => {
        const r = e.getBoundingClientRect();
        const cs = getComputedStyle(e);
        rows.push({id: e.id, tag: e.tagName, cls: e.className,
                   l: Math.round(r.left), t: Math.round(r.top),
                   w: Math.round(r.width), h: Math.round(r.height),
                   disp: cs.display, pos: cs.position,
                   tr: cs.transform.slice(0, 40), fs: cs.fontSize});
      });
      const sceneR = el.getBoundingClientRect();
      return {rows: rows, scene: {l: Math.round(sceneR.left), t: Math.round(sceneR.top),
               w: Math.round(sceneR.width), h: Math.round(sceneR.height)}};
    }""", SCENE)
    br.close()

print(json.dumps(out, indent=1)[:6000])
