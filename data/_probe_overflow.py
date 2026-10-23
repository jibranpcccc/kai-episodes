# -*- coding: utf-8 -*-
"""Measure whether any child element spills out of the card that holds it.

The defect class: a row's value is wider than the row, so the row's own label
is pushed past the card and over the art column. A chain node's title is wider
than the chain, so the last node hangs past the chain box.

This walks every window of the episode, and for each card (a .row, a .chain, a
.chain__node, a .compare__col, a .bar, a .railrow, a .note, a .strip__cell)
compares the children's union box against the card's own content box.

Usage: python data/_probe_overflow.py EPISODE
"""
import os
import sys

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EP = sys.argv[1]
PATH = os.path.join(ROOT, EP + ".html")

JS = """
() => {
  const CARDS = '.row,.chain,.chain__node,.compare__col,.bar,.railrow,.note,.strip__cell,.gal__art,.chain__top';
  const layBox = (el) => {
    // LAYOUT boxes, not painted rects: the reveal animations leave a
    // transform on every element before its beat, and a transformed rect
    // reports a card that is still settling as an overflow. This is the same
    // measurement the gate's check 23 makes.
    let x = 0, y = 0, n = el;
    while (n && n !== document.body) { x += n.offsetLeft; y += n.offsetTop; n = n.offsetParent; }
    return {l: x, t: y, r: x + el.offsetWidth, b: y + el.offsetHeight};
  };
  const out = [];
  const scene = document.querySelector('.scene.on');
  if (!scene) return out;
  scene.querySelectorAll(CARDS).forEach((card) => {
    const cs = getComputedStyle(card);
    const pad = {
      l: parseFloat(cs.paddingLeft) || 0, r: parseFloat(cs.paddingRight) || 0,
      t: parseFloat(cs.paddingTop) || 0, b: parseFloat(cs.paddingBottom) || 0
    };
    const cb = layBox(card);
    if (!cb.r && !cb.b) return;
    const box = {l: cb.l + pad.l, r: cb.r - pad.r, t: cb.t + pad.t, b: cb.b - pad.b};
    let l = Infinity, t = Infinity, r = -Infinity, b = -Infinity, n = 0;
    card.querySelectorAll('*').forEach((c) => {
      const s = getComputedStyle(c);
      if (s.display === 'none') return;
      const rc = layBox(c);
      if (!rc.r && !rc.b) return;
      l = Math.min(l, rc.l); t = Math.min(t, rc.t);
      r = Math.max(r, rc.r); b = Math.max(b, rc.b); n++;
    });
    if (!n) return;
    const over = Math.max(0, box.l - l, r - box.r, box.t - t, b - box.b);
    if (over > 0.5) {
      out.push({
        card: card.className.split(' ').slice(0, 2).join('.'),
        over: Math.round(over * 10) / 10,
        side: (box.l - l > 0.5 ? 'L' : '') + (r - box.r > 0.5 ? 'R' : '') +
              (box.t - t > 0.5 ? 'T' : '') + (b - box.b > 0.5 ? 'B' : ''),
        w: Math.round(r - l), boxw: Math.round(box.r - box.l),
        h: Math.round(b - t), boxh: Math.round(box.b - box.t)
      });
    }
  });
  return out;
}
"""

worst = []
with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={"width": 1920, "height": 1080})
    for t in range(0, 627, 12):
        pg.goto("file:///" + PATH.replace("\\", "/") + "?t=" + str(t), wait_until="load")
        pg.wait_for_timeout(700)
        for e in pg.evaluate(JS):
            e["t"] = t
            worst.append(e)
    br.close()

# The same tolerance the gate's check 23 uses: a sub-2px overhang is an
# integer-rounding artefact of the layout boxes, not a visible overflow.
TOL = 2.0
hard = [e for e in worst if e["over"] > TOL]
notes = [e for e in worst if 0.5 < e["over"] <= TOL]

print("EPISODE: %s   samples every 12s" % EP)
if not worst:
    print("PASS  no card had a child spilling out of it at any sample")
elif not hard:
    print("NOTE  %d card overhang(s) measured, all within the %.1fpx tolerance"
          % (len(worst), TOL))
    for e in sorted(worst, key=lambda x: -x["over"]):
        print("   %-22s over %7.1f px  side=%s  children %dx%d in box %dx%d  (t=%.0f)"
              % (e["card"], e["over"], e["side"], e["w"], e["h"],
                 e["boxw"], e["boxh"], e["t"]))
else:
    print("FAIL  %d card overflow(s) measured" % len(hard))
    seen = set()
    for e in sorted(hard, key=lambda x: -x["over"]):
        key = (e["card"], e["side"])
        if key in seen:
            continue
        seen.add(key)
        print("   %-22s over %7.1f px  side=%s  children %dx%d in box %dx%d  (t=%.0f)"
              % (e["card"], e["over"], e["side"], e["w"], e["h"],
                 e["boxw"], e["boxh"], e["t"]))
    print()
    print("distinct card/side pairs: %d" % len(seen))
    raise SystemExit("OVERFLOW PROBE FAILED")
