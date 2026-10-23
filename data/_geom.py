# -*- coding: utf-8 -*-
"""DOM geometry audit of the built episode: every visible text box vs the stage,
text-vs-text collisions, tiny type, clipped type, and banned tokens."""
import io
import json
import re
import sys

from playwright.sync_api import sync_playwright

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-LORA"
PATH = ROOT + "\\" + NAME + ".html"
url = "file:///" + PATH.replace("\\", "/")

BANNED = ["EPISODE", "ACT ONE", "ACT TWO", "ACT 1", "ACT 2", "TEXT_ANCHOR",
          "PLACEHOLDER", "HEADLINE", "BRANDING", "TODO", "LOREM", "XXX"]

PROBE = r"""() => {
  const shell = document.querySelector('.stage') || document.body;
  const SR = shell.getBoundingClientRect();
  const stage = document.querySelector('.scene.on')
             || document.querySelector('.scene')
             || shell;
  const R = stage.getBoundingClientRect();
  const out = { stage: [SR.x, SR.y, SR.width, SR.height],
                scene: [R.x, R.y, R.width, R.height],
                hidden: false, texts: [], art: [], clipped: [] };
  if (!document.querySelector('.scene')) return out;

  const all = [...stage.querySelectorAll('*')];
  for (const e of all) {
    if (e.closest('.scene') !== stage) continue;
    const cs = getComputedStyle(e);
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) < 0.05) continue;
    for (let p = e; p && p !== document.body; p = p.parentElement) {
      const pcs = getComputedStyle(p);
      if (pcs.display === 'none' || pcs.visibility === 'hidden') { e.__skip = 1; break; }
    }
    if (e.__skip) { delete e.__skip; continue; }
    if (e.tagName === 'svg' || e.closest('svg')) {
      if (e.tagName === 'svg') {
        const r = e.getBoundingClientRect();
        out.art.push({ cls: e.getAttribute('class') || '', r: [r.x, r.y, r.width, r.height] });
      }
      continue;
    }
    const r = e.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) continue;

    let t = '';
    for (const n of e.childNodes) if (n.nodeType === 3) t += n.textContent;
    t = t.replace(/\s+/g, ' ').trim();

    if (t) {
      out.texts.push({
        cls: (typeof e.className === 'string' ? e.className : e.tagName) || e.tagName,
        t: t.slice(0, 70),
        r: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)],
        fs: Math.round(parseFloat(cs.fontSize) * 10) / 10
      });
    }
    if (e.scrollWidth > e.clientWidth + 2 && cs.overflow !== 'visible' && t) {
      out.clipped.push({ cls: e.className, t: t.slice(0, 40),
                         sw: e.scrollWidth, cw: e.clientWidth });
    }
  }
  return out;
}"""


def overlap(a, b, tol=2):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    ix = min(ax + aw, bx + bw) - max(ax, bx)
    iy = min(ay + ah, by + bh) - max(ay, by)
    if ix <= tol or iy <= tol:
        return 0
    return ix * iy


with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={"width": 1920, "height": 1080})
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(url + "?t=0", wait_until="load")
    pg.wait_for_timeout(400)

    meta = pg.evaluate(r"""() => ({
      keys: Object.keys(window.FUSION.scenes[0]),
      scenes: window.FUSION.scenes.map(s => [s.id, s.s, s.e])
    })""")
    print("scene keys:", meta["keys"])

    problems = []
    seen_tokens = set()
    minsize = 99
    for sid, ss, se in meta["scenes"]:
        for frac in (0.55, 0.92):
            t = ss + (se - ss) * frac
            pg.evaluate("t => window.renderAt(t)", t)
            pg.wait_for_timeout(30)
            d = pg.evaluate(PROBE)
            sx, sy, sw, sh = d["stage"]
            win = sid + 1
            tag = "w%02d@%.0f%%" % (win, frac * 100)

            for o in d["texts"]:
                x, y, w, h = o["r"]
                if x < sx - 1 or y < sy - 1 or x + w > sx + sw + 1 or y + h > sy + sh + 1:
                    problems.append("%s OUT OF STAGE  [%s] %r  rect=%s stage=%s"
                                    % (tag, o["cls"], o["t"][:44], o["r"], d["stage"]))
                minsize = min(minsize, o["fs"])
                up = o["t"].upper()
                for b in BANNED:
                    if b in up:
                        seen_tokens.add((tag, b, o["t"][:44], o["cls"]))

            for o in d["art"]:
                x, y, w, h = o["r"]
                if x < sx - 1 or y < sy - 1 or x + w > sx + sw + 1 or y + h > sy + sh + 1:
                    problems.append("%s ART OUT OF STAGE [%s] rect=%s" % (tag, o["cls"], o["r"]))

            ts = d["texts"]
            for i in range(len(ts)):
                for j in range(i + 1, len(ts)):
                    a, b = ts[i]["r"], ts[j]["r"]
                    ov = overlap(a, b)
                    if ov > 0:
                        amin = min(a[2] * a[3], b[2] * b[3])
                        frac = ov / max(1, amin)
                        if frac > 0.18:
                            problems.append("%s TEXT COLLISION %.0f%%  %r %s  <>  %r %s"
                                            % (tag, frac * 100, ts[i]["t"][:30], a,
                                               ts[j]["t"][:30], b))
            for c in d["clipped"]:
                problems.append("%s CLIPPED TEXT [%s] %r sw=%s cw=%s"
                                % (tag, c["cls"], c["t"], c["sw"], c["cw"]))

    print("console errors:", errs[:5])
    print("smallest visible font: %.1f px" % minsize)
    print("banned tokens:", sorted(seen_tokens) if seen_tokens else "NONE")
    print("--- problems (%d) ---" % len(problems))
    per = {}
    for p in problems:
        per.setdefault(p.split()[0], []).append(p)
    for k in sorted(per):
        print("  " + k)
        for p in per[k][:4]:
            print("      " + p[len(k):].strip()[:150])
        if len(per[k]) > 4:
            print("      ... +%d more" % (len(per[k]) - 4))
    br.close()