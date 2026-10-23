# -*- coding: utf-8 -*-
"""
EP09 LAYOUT AUDIT -- how much of the 1920x1080 canvas does each window use?

READ-ONLY with respect to the episode. Measures the built artefact
  C:\\Users\\jibra\\Desktop\\1\\KAI\\BYTE-EP09.html
and writes
  C:\\Users\\jibra\\Desktop\\1\\KAI\\data\\_audit_layout.json

No file outside data\\ (this script + the json) and docs\\EP09-LAYOUT-AUDIT.md
is created or modified.

--------------------------------------------------------------------------
THREE TIMESTAMPS ARE MEASURED PER SCENE
--------------------------------------------------------------------------
  t_early   = scene.s + min(1.2, 0.60 * len)   <- the task's prescription
  t_60      = scene.s + 0.60 * len             <- the task's other option
  t_full    = just after the last beat of the scene has landed
               (clamped to stay inside the scene)

t_full is the one the findings are based on: it is the only one that shows
the window at its fullest, and the only one that answers "how much canvas
does this window actually use". t_early is 1.2 s into a 8-18 s window, so
beats have not landed yet and the screen is mostly still black -- measuring
only there would flag reveal timing, not layout.

--------------------------------------------------------------------------
THREE UNIONS / SETS ARE COMPUTED
--------------------------------------------------------------------------
  NAIVE  the task recipe: every visible descendant of the active .scene
         (display:none / visibility:hidden / effective opacity 0 / zero size
         skipped), .scene__inner excluded because it is
         position:absolute;inset:0 and so covers the whole stage by
         construction. This turns out to be the padded content box
         (1580 x 856) for essentially every window, i.e. degenerate.

  INK    the subset of NAIVE that actually PAINTS pixels:
           - a non-whitespace direct text node
           - an <svg> / <img> / <canvas> / <video>
           - a paintable SVG shape (fill or stroke not none)
           - a non-transparent background / background-image
           - a visible border / outline / box-shadow
         Pure flex scaffolding (.rows__body{flex:1} etc.) has no paint and
         is excluded.

  DRAW   INK, but an <svg> contributes the bounding box of its drawn
         graphic children rather than its CSS viewport, so an art panel
         whose drawing occupies 60% of the svg box is not credited with
         100% of it. This is the headline set.

--------------------------------------------------------------------------
MEASUREMENTS
--------------------------------------------------------------------------
  union W x H      bounding box of the set, in stage coordinates (0,0-1920,1080)
  band (spec)      largest empty horizontal band = max(gap above the union
                   box, gap below it); vertical = max(left gap, right gap)
  band (interior)  longest contiguous run of canvas rows/columns that NO
                   painted element touches, counted inside the union box
                   only (so it is the dead zone in the middle of a window)
  coverage %       union box area / (1920*1080) * 100
  spill            visible elements whose box leaves the stage
"""
import json
import os
import re
import sys

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EP = os.path.join(ROOT, "BYTE-EP09.html")
SRT = os.path.join(ROOT, "BYTE-EP09.srt")
OUT = os.path.join(ROOT, "data", "_audit_layout.json")

STAGE_W = 1920
STAGE_H = 1080
SETTLE_MS = 1400
EPS = 0.5


# --------------------------------------------------------------------------
MEASURE_JS = r"""
(cfg) => {
  const STAGE_W = cfg.w, STAGE_H = cfg.h, EPS = cfg.eps;
  const stage = document.getElementById('stage');
  if (!stage) return { error: 'no #stage' };
  const sr = stage.getBoundingClientRect();
  const scenes = Array.prototype.slice.call(document.querySelectorAll('.scene'));
  const active = document.querySelector('.scene.on');
  if (!active) return { error: 'no .scene.on', sceneCount: scenes.length };
  const activeIdx = scenes.indexOf(active);

  function effOpacity(el) {
    let o = 1, n = el;
    while (n && n !== document.body) {
      const v = parseFloat(getComputedStyle(n).opacity);
      if (!isNaN(v)) o *= v;
      n = n.parentElement;
    }
    return o;
  }

  const GRAPH = 'path,rect,circle,line,polyline,polygon,ellipse,text,tspan,use';

  function paints(el, cs) {
    const tag = (el.tagName || '').toLowerCase();
    if (tag === 'svg' || tag === 'img' || tag === 'canvas' || tag === 'video' ||
        tag === 'picture' || tag === 'iframe') return true;
    if (tag === 'g' || tag === 'defs' || tag === 'title' || tag === 'desc') return false;
    if (tag === 'path' || tag === 'circle' || tag === 'rect' || tag === 'line' ||
        tag === 'polyline' || tag === 'polygon' || tag === 'ellipse' ||
        tag === 'text' || tag === 'tspan' || tag === 'use') {
      const f = cs.fill, s = cs.stroke;
      if (f && f !== 'none' && f !== 'transparent') return true;
      if (s && s !== 'none' && s !== 'transparent') return true;
      return false;
    }
    for (const n of el.childNodes) {
      if (n.nodeType === 3 && n.textContent.trim().length > 0) return true;
    }
    const bg = cs.backgroundColor;
    if (bg && bg !== 'transparent' && bg !== 'rgba(0, 0, 0, 0)') return true;
    if (cs.backgroundImage && cs.backgroundImage !== 'none') return true;
    for (const k of ['Top', 'Right', 'Bottom', 'Left']) {
      const w = parseFloat(cs['border' + k + 'Width']) || 0;
      const st = cs['border' + k + 'Style'];
      if (w > 0 && st && st !== 'none') return true;
    }
    if (cs.boxShadow && cs.boxShadow !== 'none') return true;
    if (cs.outlineStyle && cs.outlineStyle !== 'none' &&
        (parseFloat(cs.outlineWidth) || 0) > 0) return true;
    return false;
  }

  // the drawn extent of an <svg>: union of its graphic children
  function svgExtent(svg) {
    let kids;
    try { kids = svg.querySelectorAll(GRAPH); } catch (e) { return null; }
    let l = Infinity, t = Infinity, r = -Infinity, b = -Infinity, any = false;
    for (const k of kids) {
      const kr = k.getBoundingClientRect();
      if (kr.width <= 0 && kr.height <= 0) continue;
      any = true;
      if (kr.left < l) l = kr.left;
      if (kr.top < t) t = kr.top;
      if (kr.right > r) r = kr.right;
      if (kr.bottom > b) b = kr.bottom;
    }
    if (!any) return null;
    return { l: l - sr.left, t: t - sr.top, r: r - sr.left, b: b - sr.top };
  }

  const naive = [];
  let textCount = 0;
  const all = active.querySelectorAll('*');
  for (const el of all) {
    if (el.classList && el.classList.contains('scene__inner')) continue;
    const cs = getComputedStyle(el);
    if (cs.display === 'none') continue;
    if (cs.visibility === 'hidden' || cs.visibility === 'collapse') continue;
    if (effOpacity(el) <= 0.001) continue;
    const r = el.getBoundingClientRect();
    if (r.width <= 0 || r.height <= 0) continue;
    const hasText = Array.prototype.some.call(el.childNodes,
        n => n.nodeType === 3 && n.textContent.trim().length > 0);
    if (hasText) textCount++;
    const box = { l: r.left - sr.left, t: r.top - sr.top,
                  r: r.right - sr.left, b: r.bottom - sr.top,
                  text: hasText, id: el.id || '',
                  tag: (el.tagName || '').toLowerCase(),
                  cls: (el.getAttribute('class') || '').slice(0, 48) };
    naive.push(box);
    if (paints(el, cs)) {
      const isSvg = box.tag === 'svg';
      const ext = isSvg ? svgExtent(el) : null;
      naive[naive.length - 1].ink = true;
      naive[naive.length - 1].drawn = ext || box;
    }
  }

  function union(list) {
    if (!list.length) return null;
    let l = Infinity, t = Infinity, r = -Infinity, b = -Infinity;
    for (const x of list) {
      if (x.l < l) l = x.l; if (x.t < t) t = x.t;
      if (x.r > r) r = x.r; if (x.b > b) b = x.b;
    }
    return { l: l, t: t, r: r, b: b, w: r - l, h: b - t };
  }

  function bands(u) {
    if (!u) return null;
    const topGap = Math.max(0, u.t), botGap = Math.max(0, STAGE_H - u.b);
    const leftGap = Math.max(0, u.l), rightGap = Math.max(0, STAGE_W - u.r);
    return { top: topGap, bottom: botGap, left: leftGap, right: rightGap,
             h: Math.max(topGap, botGap), v: Math.max(leftGap, rightGap),
             hSide: topGap >= botGap ? 'top' : 'bottom',
             vSide: leftGap >= rightGap ? 'left' : 'right' };
  }

  // interior dead zone: longest run of rows/cols no painted element touches
  function interior(list, u) {
    if (!list.length || !u) return { h: 0, v: 0 };
    const row = new Uint8Array(STAGE_H), col = new Uint8Array(STAGE_W);
    for (const x of list) {
      const y0 = Math.max(0, Math.floor(x.t)), y1 = Math.min(STAGE_H, Math.ceil(x.b));
      for (let y = y0; y < y1; y++) row[y] = 1;
      const x0 = Math.max(0, Math.floor(x.l)), x1 = Math.min(STAGE_W, Math.ceil(x.r));
      for (let i = x0; i < x1; i++) col[i] = 1;
    }
    function longest(arr, lo, hi) {
      let best = 0, run = 0, bestAt = lo;
      for (let i = lo; i < hi; i++) {
        if (arr[i]) { run = 0; }
        else { run++; if (run > best) { best = run; bestAt = i - run + 1; } }
      }
      return { len: best, at: bestAt };
    }
    const ry = longest(row, Math.max(0, Math.floor(u.t)), Math.min(STAGE_H, Math.ceil(u.b)));
    const rx = longest(col, Math.max(0, Math.floor(u.l)), Math.min(STAGE_W, Math.ceil(u.r)));
    return { h: ry.len, hAt: ry.at, v: rx.len, vAt: rx.at };
  }

  function spillOf(list) {
    const out = [];
    for (const x of list) {
      const over = [];
      if (x.l < -EPS) over.push('left ' + x.l.toFixed(1));
      if (x.t < -EPS) over.push('top ' + x.t.toFixed(1));
      if (x.r > STAGE_W + EPS) over.push('right ' + (x.r - STAGE_W).toFixed(1));
      if (x.b > STAGE_H + EPS) over.push('bottom ' + (x.b - STAGE_H).toFixed(1));
      if (over.length) out.push({ tag: x.tag, id: x.id, cls: x.cls,
                                  over: over.join(', ') });
    }
    return out;
  }

  const inkList = naive.filter(x => x.ink);
  const drawList = inkList.map(x => x.drawn);
  const uNaive = union(naive);
  const uInk = union(inkList);
  const uDraw = union(drawList);

  const spillNaive = spillOf(naive);
  const spillDraw = spillOf(drawList);

  return {
    activeIdx: activeIdx,
    sceneCount: scenes.length,
    ids: Array.prototype.map.call(active.querySelectorAll('*'), e => e.id)
            .filter(Boolean),
    visibleCount: naive.length,
    inkCount: inkList.length,
    drawCount: drawList.length,
    textCount: textCount,
    naive: uNaive, naiveBands: bands(uNaive),
    ink: uInk, inkBands: bands(uInk),
    inkInterior: interior(inkList, uInk),
    draw: uDraw, drawBands: bands(uDraw),
    drawInterior: interior(drawList, uDraw),
    spill: spillDraw.slice(0, 10), spillCount: spillDraw.length,
    spillNaiveCount: spillNaive.length,
    spillNaive: spillNaive.slice(0, 6)
  };
}
"""


# --------------------------------------------------------------------------
def parse_srt(path):
    with open(path, "r", encoding="utf-8-sig") as fh:
        raw = fh.read()
    raw = raw.replace("\r\n", "\n").replace("\r", "\n")
    cues = []
    for block in re.split(r"\n\s*\n", raw.strip()):
        lines = [l for l in block.split("\n") if l.strip()]
        if len(lines) < 2:
            continue
        m = re.match(
            r"(\d+):(\d+):(\d+)[,.](\d+)\s*-->\s*(\d+):(\d+):(\d+)[,.](\d+)",
            lines[1])
        if not m:
            continue
        g = [int(x) for x in m.groups()]
        start = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000.0
        end = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000.0
        cues.append((start, end, " ".join(lines[2:]).strip()))
    return cues


def srt_word_timeline(cues):
    out = []
    for cs, ce, text in cues:
        words = text.split()
        if not words:
            continue
        dur = max(ce - cs, 1e-6)
        for i, w in enumerate(words):
            out.append((cs + dur * (i + 0.5) / len(words), w))
    out.sort(key=lambda x: x[0])
    return out


# --------------------------------------------------------------------------
def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    only = sys.argv[2] if len(sys.argv) > 2 else None

    cues = parse_srt(SRT)
    words = srt_word_timeline(cues)
    print("srt cues=%d words=%d" % (len(cues), len(words)), flush=True)

    url = "file:///" + EP.replace("\\", "/")
    cfg = {"w": STAGE_W, "h": STAGE_H, "eps": EPS}

    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": 1920, "height": 1080})
        pg.goto(url + "?t=0", wait_until="load")
        pg.wait_for_timeout(1500)
        fusion = pg.evaluate("() => window.FUSION")
        scenes = fusion["scenes"]
        beats = fusion.get("beats") or []
        print("scenes=%d beats=%d total=%s" % (len(scenes), len(beats),
                                               fusion.get("total")), flush=True)

        results = []
        for i, sc in enumerate(scenes):
            if only is not None and str(i) != only:
                continue
            s = float(sc["s"])
            e = float(sc["e"])
            ln = e - s

            t_early = round(min(s + 1.2, s + 0.6 * ln), 3)
            t_60 = round(s + 0.6 * ln, 3)

            scene_beats = [b for b in beats if s <= float(b.get("s", -1)) < e]
            last_beat_end = max([float(b.get("e", 0)) for b in scene_beats] or [s])
            t_full = round(min(e - 0.05, max(last_beat_end + 0.40, s + 1.2)), 3)
            if t_full <= s:
                t_full = round(min(e - 0.02, s + 0.5), 3)

            def at(t):
                pg.goto(url + "?t=" + str(t), wait_until="load")
                pg.wait_for_timeout(SETTLE_MS)
                return pg.evaluate(MEASURE_JS, cfg)

            def at_render(t):
                """same code path the ?t= param uses (window.renderAt), for the
                page already loaded -- fonts are resolved by now."""
                pg.evaluate("(t) => window.renderAt(t)", t)
                pg.wait_for_timeout(450)
                return pg.evaluate(MEASURE_JS, cfg)

            # primary: a fresh load at the settled timestamp
            m_full = at(t_full)
            # secondaries: same page, scrubbed with renderAt (pure function of t)
            m_early = at_render(t_early)
            m_60 = at_render(t_60)

            ids = set(m_full.get("ids") or [])
            nb_time = len(scene_beats)
            nb_el = sum(1 for b in scene_beats if b.get("el") in ids)

            wc = sum(1 for (wt, _w) in words if s <= wt < e)

            results.append({
                "idx": i, "id": sc.get("id"), "label": sc.get("label"),
                "s": s, "e": e, "dur": round(ln, 3),
                "t_early": t_early, "t_60": t_60, "t_full": t_full,
                "words": wc,
                "beats_time": nb_time, "beats_el": nb_el,
                "early": m_early, "p60": m_60, "full": m_full,
            })
            mf = m_full
            print("  [%2d] t_early=%-8s t_60=%-8s t_full=%-8s vis=%-4s ink=%-4s draw=%-4s txt=%-4s beats=%-3s %s"
                  % (i, t_early, t_60, t_full, mf.get("visibleCount"),
                     mf.get("inkCount"), mf.get("drawCount"),
                     mf.get("textCount"), nb_time,
                     (sc.get("label") or "")[:30]), flush=True)
            if limit and len(results) >= limit:
                break

        br.close()

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"scenes": results}, fh, indent=1)
    print("wrote", OUT, flush=True)


if __name__ == "__main__":
    main()
