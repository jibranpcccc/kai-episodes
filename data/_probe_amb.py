# -*- coding: utf-8 -*-
"""Prove that no ambient motion pushes an element outside its drawing.

The engine's ambient modes move elements analytically every frame. A needle
that rotates a full 360 degrees sweeps out of its dial and off the drawing,
which is exactly what the owner reported. This probe loads the built episode
at a set of timestamps, and for every element carrying data-amb it compares
the element's live screen rect against the screen rect of its SVG's viewBox.

Usage: python data/_probe_amb.py EPISODE [t1 t2 ...]
"""
import os
import sys

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EP = sys.argv[1]
TIMES = [float(x) for x in sys.argv[2:]] or [0.0]
PATH = os.path.join(ROOT, EP + ".html")

JS = """
() => {
  const out = [];
  document.querySelectorAll('[data-amb]').forEach((el) => {
    const svg = el.closest('svg');
    if (!svg) return;
    const vb = svg.viewBox && svg.viewBox.baseVal;
    if (!vb || !vb.width || !vb.height) return;
    const ctm = svg.getScreenCTM();
    if (!ctm) return;
    const pt = svg.createSVGPoint();
    const corners = [[vb.x, vb.y], [vb.x + vb.width, vb.y],
                     [vb.x + vb.width, vb.y + vb.height], [vb.x, vb.y + vb.height]]
      .map((p) => { pt.x = p[0]; pt.y = p[1]; return pt.matrixTransform(ctm); });
    const minX = Math.min(...corners.map((p) => p.x));
    const maxX = Math.max(...corners.map((p) => p.x));
    const minY = Math.min(...corners.map((p) => p.y));
    const maxY = Math.max(...corners.map((p) => p.y));
    const r = el.getBoundingClientRect();
    if (!r.width && !r.height) return;
    const over = Math.max(0, minX - r.left, r.right - maxX, minY - r.top, r.bottom - maxY);
    out.push({
      mode: el.getAttribute('data-amb'),
      amp: el.getAttribute('data-amb-amp'),
      origin: el.getAttribute('data-amb-origin'),
      art: svg.getAttribute('data-art') || '(none)',
      over: Math.round(over * 100) / 100,
      w: Math.round(r.width), h: Math.round(r.height)
    });
  });
  return out;
}
"""

worst = {}
fails = []
with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={"width": 1920, "height": 1080})
    for t in TIMES:
        pg.goto("file:///" + PATH.replace("\\", "/") + "?t=" + str(t), wait_until="load")
        pg.wait_for_timeout(900)
        for e in pg.evaluate(JS):
            key = (e["mode"], e["origin"], e["art"])
            if e["over"] > worst.get(key, (-1, None, 0))[0]:
                worst[key] = (e["over"], t, e["amp"])
            if e["over"] > 1.0:
                fails.append((t, e))
    br.close()

print("EPISODE: %s   samples: %s" % (EP, ", ".join("%.1f" % t for t in TIMES)))
print()
print("%-6s %-22s %-10s %-8s %10s %8s" % ("mode", "origin", "art", "amp", "over(px)", "at t"))
for (mode, origin, art), (over, t, amp) in sorted(worst.items(), key=lambda kv: -kv[1][0]):
    print("%-6s %-22s %-10s %-8s %10.1f %8.1f" %
          (mode, origin or "-", art, amp if amp is not None else "-", over, t))
print()
if fails:
    print("FAIL  %d ambient element(s) left their drawing by more than 1px" % len(fails))
    for t, e in fails[:20]:
        print("   t=%.1f  %s %s origin=%s art=%s over=%.1fpx"
              % (t, e["mode"], e["amp"] or "-", e["origin"], e["art"], e["over"]))
else:
    print("PASS  every ambient element stayed inside its drawing at every sample")
