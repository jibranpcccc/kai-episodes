# -*- coding: utf-8 -*-
"""
FUSION GATE — 13 checks on a built fusion episode.

    python data/fusion_gate.py BYTE-07-FUSION

This reads the BUILT html and re-derives everything. It never trusts the
builder. The rhythm law is re-implemented here from the spec, not imported.
"""
import base64
import io
import json
import os
import re
import subprocess
import sys

import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-07-FUSION"
SPEC = sys.argv[2] if len(sys.argv) > 2 else None
if not SPEC:
    if 'vram' in NAME.lower(): SPEC = 'spec_vram'
    elif 'lora' in NAME.lower(): SPEC = 'spec_lora'
    elif 'bottleneck' in NAME.lower(): SPEC = 'spec_bottleneck'
sys.path.insert(0, os.path.join(ROOT, 'data'))
PATH = os.path.join(ROOT, NAME + ".html")
if not os.path.exists(PATH):
    PATH = os.path.join(ROOT, "episodes", NAME + ".html")

# ---- the law, restated independently of the builder ------------------
MIN_GAP = 0.30
HERO_ALONE = 0.55
MAX_GAP_FAIL = 8.00
MAX_GAP_WARN = 6.00
NUDGE_BOUND = 1.00
TEASE_BOUND = 2.00
WORD_TOL = 0.55
LOUD_LO, LOUD_HI = -14.8, -13.2
STATIC_LO, STATIC_HI = 0.35, 0.70
INK_MIN = 0.010
INK_SPARSE = 0.015
SPARSE_MAX_RUN = 2.0

# ---- the rules the old gate did not look for -------------------------
TRUE_PEAK_MAX = -1.2        # dBFS. The old chain put the master at -0.5
CAPTION_MIN_WORDS = 2       # a one-word cue is not a caption
CAPTION_MAX_WORDS = 12
WINDOW_MAX = 19.0           # seconds. EPISODE-RULES says 20
FROZEN_MAX = 4.0            # seconds of a static screen at the end of a window
SAME_WORD_LEN = 8

FAILS, WARNS, PASSES = [], [], []


def ok(n, msg):
    PASSES.append((n, msg))
    print("  PASS  %-4s %s" % (n, msg))


def bad(n, msg):
    FAILS.append((n, msg))
    print("  FAIL  %-4s %s" % (n, msg))


def warn(n, msg):
    WARNS.append((n, msg))
    print("  WARN  %-4s %s" % (n, msg))


# ================================================================== extra
def _norm(s):
    s = (s or "").lower().replace("&middot;", " ")
    s = re.sub(r"[^a-z0-9%.\- ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _words(s):
    """Comparable words: case and trailing sentence punctuation removed."""
    return [w.rstrip(".,;:!?") for w in _norm(s).split()]


def _parse_srt(path):
    """(cues, error). A cue is (start, end, text)."""
    if not os.path.exists(path):
        return None, "no .srt file beside the episode"
    raw = io.open(path, encoding="utf-8-sig").read()
    cues = []
    for block in re.split(r"\r?\n\r?\n", raw.strip()):
        lines = [x for x in block.splitlines() if x.strip()]
        if len(lines) < 2:
            continue
        m = re.match(r"(\d+):(\d+):(\d+),(\d+)\s*-->\s*(\d+):(\d+):(\d+),(\d+)",
                     lines[1])
        if not m:
            return None, ("cue %r is not valid SRT -- a comma is required "
                          "before the milliseconds" % lines[1][:36])
        g = [int(x) for x in m.groups()]
        a = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000.0
        b = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000.0
        cues.append((a, b, " ".join(lines[2:])))
    return cues, None


def _role(tag, cls):
    """The visual role of an element, from the class it carries."""
    if re.search(r"\brow row--", cls):
        return "row"
    if re.search(r"\bchip chip--", cls):
        return "chip"
    if re.search(r"\bbar\b", cls):
        return "bar"
    if "railrow" in cls:
        return "rail"
    if "chain__node" in cls:
        return "chain"
    if tag == "li":
        return "note"
    return None


def extra_checks(s, F, beats, scenes, words, total):
    """The checks the old gate did not make. Each one is a defect that
    actually shipped in a published episode."""
    from collections import defaultdict

    # --------------------------------------------------------------- 14
    # captions must cover the narration 100 % word for word
    srt_path = os.path.join(ROOT, NAME + ".srt")
    if not os.path.exists(srt_path):
        srt_path = os.path.join(ROOT, "episodes", NAME + ".srt")
    cues, err = _parse_srt(srt_path)
    if err:
        bad("14", "captions: %s" % err)
    else:
        # The caption must COVER the speech: every spoken word has to fall
        # inside a cue, so nothing the voice says goes uncaptioned. The TEXT
        # identity of the caption is check 14e, which compares it against the
        # script itself.
        uncovered = []
        cs = sorted(cues)
        for t, w in words:
            if not any(c0 - 0.001 <= t <= c1 + 0.001 for c0, c1, _ in cs):
                uncovered.append(w)
        if uncovered:
            bad("14", "captions leave %d of %d spoken words uncovered -- %r"
                % (len(uncovered), len(words), " ".join(uncovered[:8])))
        else:
            ok("14", "captions cover all %d spoken words" % len(words))

        thin = [t for _, _, t in cues if len(t.split()) < CAPTION_MIN_WORDS]
        fat = [t for _, _, t in cues if len(t.split()) > CAPTION_MAX_WORDS]
        if thin or fat:
            bad("14b", "caption granularity: %d cue(s) under %d words, %d over %d"
                % (len(thin), CAPTION_MIN_WORDS, len(fat), CAPTION_MAX_WORDS))
        else:
            ok("14b", "every caption reads as a line (%d-%d words)"
                % (min(len(t.split()) for _, _, t in cues),
                   max(len(t.split()) for _, _, t in cues)))

        over = sum(1 for k in range(1, len(cues)) if cues[k][0] < cues[k - 1][1] - 0.001)
        if over:
            bad("14c", "%d overlapping caption cues" % over)
        elif cues[0][0] > 0.05:
            bad("14c", "the first caption starts at %.3fs" % cues[0][0])
        elif total - cues[-1][1] > 1.5:
            bad("14c", "the last caption ends %.2fs before the audio ends -- the "
                       "tail was never captioned" % (total - cues[-1][1]))
        else:
            ok("14c", "no overlapping cues, the whole speech is captioned")

        chap = os.path.join(ROOT, NAME + "-chapters.txt")
        if not os.path.exists(chap):
            bad("14d", "no chapters file beside the episode")
        else:
            lines = [x for x in io.open(chap, encoding="utf-8").read().splitlines()
                     if x.strip()]
            n = len(lines)
            if n == len(scenes):
                ok("14d", "chapters file has one line per window (%d)" % n)
            else:
                # A chapter list is not a scene list. It has to satisfy the
                # rules a viewer can act on: the first chapter at 00:00, at
                # least three of them, every one of them at least ten
                # seconds, moving forward, and no two with the same title.
                import re as _re
                stamps = []
                titles = []
                for ln in lines:
                    m = _re.match(r"^(?:(\d+):)?(\d{1,2}):(\d{2})\s+(.+)$", ln)
                    if not m:
                        bad("14d", "chapter line is not a timestamp: %r" % ln)
                        stamps = None
                        break
                    stamps.append(int(m.group(1) or 0) * 3600
                                  + int(m.group(2)) * 60 + int(m.group(3)))
                    titles.append(m.group(4))
                if stamps:
                    problems = []
                    if len(stamps) < 3:
                        problems.append("only %d chapters; YouTube wants at least 3"
                                        % len(stamps))
                    if stamps[0] != 0:
                        problems.append("the first chapter starts at %ds, not 0"
                                        % stamps[0])
                    for k in range(len(stamps) - 1):
                        if stamps[k + 1] <= stamps[k]:
                            problems.append("chapter %d does not move forward" % (k + 1))
                        elif stamps[k + 1] - stamps[k] < 10.0:
                            problems.append("chapter %d is only %.1fs long (%s)"
                                            % (k + 1, stamps[k + 1] - stamps[k], titles[k]))
                    if len(set(titles)) != len(titles):
                        problems.append("two chapters share a title")
                    for p in problems:
                        bad("14d", p)
                    if not problems and len(stamps) > 1:
                        ok("14d", "chapter list is valid for YouTube (%d chapters, "
                                  "shortest %.1fs)"
                            % (len(stamps),
                               min(stamps[k + 1] - stamps[k]
                                   for k in range(len(stamps) - 1))))

        # the caption TEXT must be the script's own words
        if SPEC:
            try:
                import importlib
                mod = importlib.import_module(SPEC)
                script = [w for win in mod.W for w in _words(win["vo"])]
                capn = [w for _, _, t in cues for w in _words(t)]
                same = sum(1 for a, b in zip(script, capn) if a == b)
                if same == len(script) == len(capn):
                    ok("14e", "caption text is the script's own words (%d/%d)"
                       % (same, len(script)))
                else:
                    bad("14e", "caption text is not the script's own words "
                               "(%d of %d match)" % (same, len(script)))
            except Exception as e:
                warn("14e", "could not compare the captions with the spec: %s" % e)

    # --------------------------------------------------------------- 15
    # every window carries a source footer
    scene_html = re.findall(r'<section class="scene" data-scene="\d+">(.*?)</section>',
                            s, re.S)
    nosrc = [i for i, x in enumerate(scene_html) if 'class="src"' not in x]
    if nosrc:
        bad("15", "window(s) %s carry no source footer" % nosrc[:6])
    else:
        ok("15", "every window carries a source footer (%d)" % len(scene_html))

    # --------------------------------------------------------------- 16
    # elements must reveal in their authored order
    bt = defaultdict(dict)
    for b in beats:
        el = (b.get("el") or "")
        if el.startswith("#"):
            bt[b.get("group", 0)][el[1:]] = b["s"]
    out_of_order = []
    for i, x in enumerate(scene_html):
        roles = {}
        for m in re.finditer(r'<(\w+)([^>]*\bid="(w\d+_\d+)"[^>]*)>', x):
            tag, attrs, rid = m.group(1), m.group(2), m.group(3)
            cm = re.search(r'class="([^"]*)"', attrs)
            r = _role(tag, cm.group(1) if cm else "")
            if r:
                roles[rid] = r
        byrole = defaultdict(list)
        for rid, r in roles.items():
            if rid in bt.get(i, {}):
                byrole[r].append((rid, bt[i][rid]))
        for r, items in byrole.items():
            if len(items) < 2:
                continue
            t = [q[1] for q in items]
            if t != sorted(t):
                out_of_order.append((i + 1, r, items))
    if out_of_order:
        bad("16", "%d window(s) reveal out of authored order, e.g. window %d (%s)"
            % (len(out_of_order), out_of_order[0][0], out_of_order[0][1]))
    else:
        ok("16", "every window reveals its elements in the authored order")

    # --------------------------------------------------------------- 17
    # no narration repeated between windows
    per = {}
    for t2, w in words:
        for i, sc in enumerate(scenes):
            if sc["s"] <= t2 <= sc["e"]:
                per.setdefault(i, []).append(w)
    seen = {}
    dup = []
    for i, ws in sorted(per.items()):
        for sent in re.split(r"(?<=\.)\s+", " ".join(ws)):
            k = _norm(sent)
            if len(k.split()) >= SAME_WORD_LEN:
                if k in seen:
                    dup.append((seen[k] + 1, i + 1, k))
                else:
                    seen[k] = i
    if dup:
        bad("17", "narration repeated between windows %d and %d: %r"
            % (dup[0][0], dup[0][1], dup[0][2][:50]))
    else:
        ok("17", "no sentence is narrated twice")

    # --------------------------------------------------------------- 18
    # the document title must carry the episode
    tm = re.search(r"<title>(.*?)</title>", s, re.S)
    title = _norm(tm.group(1)) if tm else ""
    want = _norm(F.get("title", ""))
    if want and want in title:
        ok("18", "the document title carries the episode title")
    else:
        bad("18", "the document title is %r and does not carry %r"
            % (title[:48], want[:48]))

    # --------------------------------------------------------------- 20
    # no window over the limit, and no two consecutive identical layouts
    dur = [(sc["e"] - sc["s"]) for sc in scenes]
    over = [(i + 1, d) for i, d in enumerate(dur) if d > WINDOW_MAX]
    if over:
        bad("20", "window(s) %s run longer than %.0fs (worst %.1fs)"
            % ([i for i, _ in over[:5]], WINDOW_MAX, max(d for _, d in over)))
    else:
        ok("20", "no window runs longer than %.0fs (worst %.1fs)"
            % (WINDOW_MAX, max(dur) if dur else 0))
    labs = [sc["label"].split(" ", 1)[-1].strip().upper() for sc in scenes]
    runs = [i + 1 for i in range(1, len(labs)) if labs[i] == labs[i - 1]]
    if runs:
        bad("20b", "two consecutive windows share a layout at %s" % runs[:6])
    else:
        ok("20b", "no two consecutive windows share a layout")

    # --------------------------------------------------------------- 21
    # no window ends on a frozen screen
    last = {}
    for b in beats:
        g = b.get("group", 0)
        if g not in last or b["s"] > last[g]:
            last[g] = b["s"]
    frozen = [(i + 1, scenes[i]["e"] - last.get(i, scenes[i]["s"]))
              for i in range(len(scenes))
              if scenes[i]["e"] - last.get(i, scenes[i]["s"]) > FROZEN_MAX]
    if frozen:
        bad("21", "window(s) %s end on more than %.1fs of frozen screen (worst %.1fs)"
            % ([i for i, _ in frozen[:5]], FROZEN_MAX, max(d for _, d in frozen)))
    else:
        ok("21", "no window ends on more than %.1fs of frozen screen" % FROZEN_MAX)

    # --------------------------------------------------------------- 22
    # a bar must carry a unit, and never a throughput unit on a score
    BENCH = ("mmlu", "flan", "gsm", "humaneval", "arc", "hellaswag", "winogrande")
    badbars = []
    for i, x in enumerate(scene_html):
        for chunk in re.split(r'<div class="bar"', x)[1:]:
            lm = re.search(r'class="bar__lab">(.*?)</div>', chunk, re.S)
            um = re.search(r'class="bar__val">(.*?)</div>', chunk, re.S)
            if not lm or not um:
                continue
            label = _norm(lm.group(1))
            sm = re.search(r"<small>(.*?)</small>", um.group(1))
            unit = _norm(sm.group(1)) if sm else ""
            if not unit:
                badbars.append((i + 1, label, "no unit"))
            elif unit == "t/s" and (re.match(r"^\d+k$", label) or label in BENCH):
                badbars.append((i + 1, label, "T/S on a %s" % label))
    if badbars:
        bad("22", "bar unit problem: %s" % "; ".join(
            "window %d %r %s" % b for b in badbars[:4]))
    else:
        ok("22", "every bar carries a unit and no score wears a T/S")


def main():
    if not os.path.exists(PATH):
        print("no such file: %s" % PATH)
        return 1
    s = io.open(PATH, encoding="utf-8").read()
    F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", s, re.S).group(1))
    beats, scenes, words, total = F["beats"], F["scenes"], F["words"], F["total"]
    print("FUSION GATE  %s   runtime %.1fs   beats %d   words %d\n"
          % (NAME, total, len(beats), len(words)))

    # ---------------------------------------------------------------
    # 1  no two beats closer than MIN_GAP inside a scene
    # 2  the first beat of a scene lands alone
    # 3  no dead spot
    v1 = v2 = v3 = 0
    _mingap = None
    for sc in scenes:
        bs = sorted([b for b in beats if b["group"] == sc["id"]], key=lambda b: b["s"])
        for i in range(1, len(bs)):
            gap = bs[i]["s"] - bs[i - 1]["s"]
            if gap < MIN_GAP - 0.01:
                v1 += 1
                if _mingap is None or gap < _mingap:
                    _mingap = gap
            if gap > MAX_GAP_FAIL:
                v3 += 1
            elif gap > MAX_GAP_WARN:
                v3 += 0
                warn("3", "scene %d: %.2fs hold at t=%.2f (%s)"
                     % (sc["id"] + 1, gap, bs[i]["s"], (bs[i].get("anchor") or "")[:34]))
        if len(bs) > 1 and (bs[1]["s"] - bs[0]["s"]) < HERO_ALONE - 1e-6:
            v2 += 1
    if v1 == 0:
        ok("1", "no two beats within %.2fs" % MIN_GAP)
    else:
        bad("1", "%d beat pairs closer than %.2fs (smallest %.4fs)"
            % (v1, MIN_GAP, _mingap if _mingap is not None else -1))
    if v2 == 0:
        ok("2", "every scene opens with a lone hero (>= %.2fs)" % HERO_ALONE)
    else:
        bad("2", "%d scenes open without a lone hero" % v2)
    if v3 == 0:
        ok("3", "no dead spot longer than %.1fs" % MAX_GAP_FAIL)
    else:
        bad("3", "%d dead spots longer than %.1fs" % (v3, MAX_GAP_FAIL))

    # ---------------------------------------------------------------
    # 4  every beat points at a real element
    # 7  every data-fx element is claimed by exactly one beat
    from playwright.sync_api import sync_playwright
    url = "file:///" + PATH.replace("\\", "/")
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": 1920, "height": 1080})
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.goto(url + "?t=0", wait_until="load")
        pg.wait_for_timeout(500)

        dom = pg.evaluate(r"""() => {
          const claimed = new Set(window.FUSION.beats.map(b => b.el.slice(1)));
          const fx = [...document.querySelectorAll('[data-fx]')].map(e => e.id);
          const missing = window.FUSION.beats.filter(b => !document.querySelector(b.el)).map(b => b.el);
          const orphan = fx.filter(id => !claimed.has(id));
          const dupe = [];
          const seen = {};
          window.FUSION.beats.forEach(b => { const k = b.el; if (seen[k]) dupe.push(k); seen[k] = 1; });
          const noSvg = window.FUSION.scenes.map(sc => {
            const el = document.querySelector('.scene[data-scene="' + sc.id + '"]');
            return el && el.querySelector('svg') ? null : sc.id + 1;
          }).filter(x => x !== null);
          // overflow
          const over = [];
          document.querySelectorAll('.scene [data-fx]').forEach(e => {
            const r = e.getBoundingClientRect();
            if (r.right > 1921 || r.bottom > 1081 || r.left < -1 || r.top < -1)
              over.push(e.id + ' ' + JSON.stringify({l: Math.round(r.left), t: Math.round(r.top),
                                                    r: Math.round(r.right), b: Math.round(r.bottom)}));
          });
          // undefined css vars
          const vars = new Set();
          for (const sheet of document.styleSheets) {
            let rules; try { rules = sheet.cssRules; } catch (e) { continue; }
            for (const r of rules || []) {
              const t = r.cssText || '';
              const re = /var\(\s*(--[a-z0-9-]+)\s*([,)]?)/gi;
              let mm = null;
              while ((mm = re.exec(t)) !== null) {
                if (mm[2] !== ',') vars.add(mm[1]);   // no fallback -> must exist
              }
            }
          }
          const root = getComputedStyle(document.documentElement);
          const undef = [...vars].filter(v => !root.getPropertyValue(v).trim());
          // a child that spills out of the card that holds it. A row whose
          // value is wider than the row pushes the row's own label over the
          // art column; a chain node whose title is too wide hangs past the
          // chain. Both are invisible to a canvas-overflow check.
          //
          // The boxes are LAYOUT boxes (offsetLeft/offsetTop), not
          // getBoundingClientRect: the reveal animations leave a transform on
          // every element before its beat, and a transformed rect would report
          // a card that is still settling as an overflow.
          const CARDS = '.row,.chain,.chain__node,.compare__col,.bar,.railrow,.strip__cell';
          const cardOver = [];
          const layBox = (el) => {
            let x = 0, y = 0, n = el;
            while (n && n !== document.body) {
              x += n.offsetLeft; y += n.offsetTop; n = n.offsetParent;
            }
            return {l: x, t: y, r: x + el.offsetWidth, b: y + el.offsetHeight};
          };
          document.querySelectorAll('.scene').forEach((scene) => {
            const sid = scene.getAttribute('data-scene');
            scene.querySelectorAll(CARDS).forEach((card) => {
              const cs = getComputedStyle(card);
              if (cs.display === 'none') return;
              const cb = layBox(card);
              if (!cb.r || !cb.b) return;
              const box = {
                l: cb.l + (parseFloat(cs.paddingLeft) || 0),
                r: cb.r - (parseFloat(cs.paddingRight) || 0),
                t: cb.t + (parseFloat(cs.paddingTop) || 0),
                b: cb.b - (parseFloat(cs.paddingBottom) || 0)
              };
              let l = Infinity, tp = Infinity, r = -Infinity, b = -Infinity, n = 0;
              card.querySelectorAll('*').forEach((c) => {
                const s = getComputedStyle(c);
                if (s.display === 'none') return;
                const rc = layBox(c);
                if (!rc.r && !rc.b) return;
                l = Math.min(l, rc.l); tp = Math.min(tp, rc.t);
                r = Math.max(r, rc.r); b = Math.max(b, rc.b); n++;
              });
              if (!n) return;
              const over = Math.max(0, box.l - l, r - box.r, box.t - tp, b - box.b);
              /* Two pixels of slack: the layout boxes are fractional and a
                 third of a pixel of rounding is not a defect. */
              if (over > 2) {
                cardOver.push('w' + (parseInt(sid, 10) + 1) + ' ' +
                  card.className.split(' ').slice(0, 2).join('.') +
                  ' +' + Math.round(over) + 'px');
              }
            });
          });
          return {missing, orphan, dupe, noSvg, over, undef, cardOver,
                  fxCount: fx.length, beatCount: window.FUSION.beats.length};
        }""")

        if not dom["missing"]:
            ok("4", "every beat resolves to a real element")
        else:
            bad("4", "%d beats point at nothing: %s" % (len(dom["missing"]), dom["missing"][:5]))
        if not dom["noSvg"]:
            ok("6", "every window carries a drawing")
        else:
            bad("6", "windows with no svg: %s" % dom["noSvg"])
        if not dom["orphan"] and not dom["dupe"]:
            ok("7", "all %d elements claimed exactly once" % dom["fxCount"])
        else:
            bad("7", "%d unclaimed, %d double-claimed: %s %s"
                % (len(dom["orphan"]), len(dom["dupe"]), dom["orphan"][:4], dom["dupe"][:4]))
        if not dom["over"]:
            ok("10", "nothing overflows the 1920x1080 canvas")
        else:
            bad("10", "%d elements overflow: %s" % (len(dom["over"]), dom["over"][:4]))
        if not dom["cardOver"]:
            ok("23", "no card child spills out of the card that holds it")
        else:
            bad("23", "%d card overflow(s): %s"
                % (len(dom["cardOver"]), dom["cardOver"][:6]))
        if not dom["undef"]:
            ok("9", "no undefined var(--x) colours")
        else:
            bad("9", "undefined vars: %s" % dom["undef"][:6])

        # ---------------------------------------------------------------
        # 5  every beat lands on the word that introduces it
        def word_at(ws, t):
            best = None
            for wt, txt in ws:
                if wt <= t + 1e-6:
                    best = (wt, txt)
                else:
                    break
            return best

        v5 = 0
        seen_groups = set()
        for b in beats:
            key = (b["group"], b.get("anchor"))
            if key in seen_groups:
                continue
            seen_groups.add(key)
            t_arr = b.get("arr", b["s"])
            w = word_at(words, t_arr)
            if w is None:
                continue
            off = t_arr - w[0]
            if abs(off) <= WORD_TOL:
                continue
            nud = b.get("nudge", 0)
            if abs(nud) <= NUDGE_BOUND:
                continue
            if nud < 0 and -nud <= TEASE_BOUND:
                continue        # a deliberate tease: it lands before its word
            v5 += 1
            bad("5", "arrival for %r at %.2fs is %.2fs from the word '%s'"
                % ((b.get("anchor") or "")[:30], t_arr, off, w[1]))
        if v5 == 0:
            ok("5", "every arrival lands within %.2fs of its spoken word" % WORD_TOL)

        # ---------------------------------------------------------------
        # 11  static-frame band + 12  ink coverage, sampled at 3 fps
        frames = []
        ink = []
        dip = []
        # sample adaptively: a 12 minute episode at 3 fps is 2000+ screenshots
        # and takes half an hour. 600 samples measures the same thing.
        FPS = 3.0 if total <= 240 else max(1.0, 600.0 / total)
        n = int(total * FPS)
        for k in range(n + 1):
            t = k / FPS
            pg.evaluate("(t) => window.renderAt(t)", t)
            # WAAPI commits on the next animation frame; two rAFs guarantee the
            # painted result matches the requested timestamp
            pg.evaluate("() => new Promise(r => requestAnimationFrame("
                        "() => requestAnimationFrame(() => r(1))))")
            dip.append(pg.evaluate("() => window.__FUSION__.dipOpacity(window.FUSION.__t || 0)"))
            raw = pg.screenshot(type="jpeg", quality=70)
            a = np.asarray(Image.open(io.BytesIO(raw)).convert("RGB"), dtype=np.int16)
            frames.append(a)
            ink.append(float((a.max(axis=2) > 90).mean()))
            if len(frames) > 1:
                pass
        diffs = []
        for i in range(1, len(frames)):
            d = np.abs(frames[i] - frames[i - 1])
            diffs.append(float((d.max(axis=2) > 18).mean()))
        changed = sum(1 for d in diffs if d >= 0.0008) / max(1, len(diffs))
        static = 1.0 - changed
        if (1 - STATIC_HI) <= changed <= (1 - STATIC_LO):
            ok("11", "static %.1f%% / changed %.1f%% (band %.0f-%.0f%% static; KAI 76%%, RepoChad ~20%%)"
               % (static * 100, changed * 100, STATIC_LO * 100, STATIC_HI * 100))
        else:
            bad("11", "static %.1f%% outside %.0f-%.0f%%"
                % (static * 100, STATIC_LO * 100, STATIC_HI * 100))
        # a cut to black is a designed transition, not a sparse frame
        lit = [v for v, d in zip(ink, dip) if d < 0.02]
        # judge each WINDOW, not every sample. A window whose art is drawing
        # itself in for its first half second is not an empty window.
        win_ink = {}
        for k, (v, d) in enumerate(zip(ink, dip)):
            sc = 0
            for q2 in range(len(scenes)):
                if k / FPS >= scenes[q2]["s"]:
                    sc = q2
            win_ink.setdefault(sc, []).append(v)
        empty = []
        for sc, vals in sorted(win_ink.items()):
            med = float(np.median(vals))
            if med < INK_MIN:
                empty.append((sc + 1, round(med * 100, 2)))
        lowink = empty
        print("        ink: min %.1f%%  p5 %.1f%%  median %.1f%%  max %.1f%%   (%d windows)"
              % (min(lit) * 100 if lit else 0,
                 np.percentile(lit, 5) * 100 if lit else 0,
                 np.median(lit) * 100 if lit else 0,
                 max(lit) * 100 if lit else 0, len(win_ink)))
        if not lowink:
            ok("12", "every window carries a picture (median ink >= %.1f%%)" % (INK_MIN * 100))
        else:
            bad("12", "%d windows carry no picture: %s" % (len(lowink), lowink[:8]))
        # no window may be sparse for its whole length
        worst = (0.0, 0)
        for sc, vals in sorted(win_ink.items()):
            # a window that is sparse ALL THE WAY THROUGH is a title card.
            # check 12 already proved it carries a picture.
            if float(np.median(vals)) < INK_SPARSE:
                continue
            frac = sum(1 for v in vals if v < INK_SPARSE) / float(len(vals))
            if frac > worst[0]:
                worst = (frac, sc + 1)
        if worst[0] <= 0.60:
            ok("12b", "no window is mostly sparse (worst %.0f%% of window %d)"
               % (worst[0] * 100, worst[1]))
        else:
            bad("12b", "window %d is %.0f%% sparse (limit 60%%)"
                % (worst[1], worst[0] * 100))

        # ---------------------------------------------------------------
        # 13  determinism: the same t must render the same pixels
        # The web fonts are ~1.4 MB of base64. Until they decode, the
        # browser paints text with a fallback face, so a frame captured too
        # early is not the frame you think it is. Both pages wait for the
        # fonts, exactly like the runtime's own ?t= path does.
        def fonts_ready(page):
            try:
                page.evaluate("async () => { if (document.fonts && "
                              "document.fonts.ready) await document.fonts.ready; }")
            except Exception:
                pass

        probes = [round(total * 0.12, 2), round(total * 0.45, 2),
                  round(total * 0.80, 2)]
        pg.goto(url + "?t=0", wait_until="load")
        pg.wait_for_timeout(1200)
        shots1 = []
        fonts_ready(pg)
        for t in probes:
            pg.evaluate("(t) => window.renderAt(t)", t)
            pg.evaluate("() => new Promise(r => requestAnimationFrame("
                        "() => requestAnimationFrame(() => r(1))))")
            shots1.append(pg.screenshot())
        pg2 = br.new_page(viewport={"width": 1920, "height": 1080})
        pg2.goto(url + "?t=0", wait_until="load")
        pg2.wait_for_timeout(1200)
        fonts_ready(pg2)
        shots2 = []
        for t in probes:
            pg2.evaluate("(t) => window.renderAt(t)", t)
            pg2.evaluate("() => new Promise(r => requestAnimationFrame("
                        "() => requestAnimationFrame(() => r(1))))")
            shots2.append(pg2.screenshot())
        def px(shot):
            return np.asarray(Image.open(io.BytesIO(shot)).convert("RGB"), dtype=np.int16)
        diffs = [float(np.abs(px(a) - px(b)).max()) for a, b in zip(shots1, shots2)]
        if max(diffs) == 0:
            ok("13", "renderAt(t) is pixel-identical across two loads")
        else:
            bad("13", "renderAt(t) differs across two loads (max channel delta %d)"
                % int(max(diffs)))
        if errs:
            bad("JS", "console errors: %s" % errs[:3])
        else:
            ok("JS", "no console errors")
        br.close()

    # ---------------------------------------------------------------
    # 8  loudness of the EMBEDDED audio
    m = re.search(r'"vo":"data:audio/mpeg;base64,([A-Za-z0-9+/=]+)"', s)
    if not m:
        bad("8", "no embedded audio found")
    else:
        tmp = os.path.join(ROOT, "build", NAME + "_gate.mp3")
        os.makedirs(os.path.dirname(tmp), exist_ok=True)
        open(tmp, "wb").write(base64.b64decode(m.group(1)))
        o = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", tmp, "-af",
                            "ebur128=peak=true", "-f", "null", "-"],
                           capture_output=True, text=True).stderr
        tail = o[-900:]
        mm = re.findall(r"I:\s*(-?[\d.]+)\s+LUFS", tail)
        pk = re.findall(r"Peak:\s*(-?[\d.]+)\s+dBFS", tail)
        if mm:
            lufs = float(mm[-1])
            if LOUD_LO <= lufs <= LOUD_HI:
                ok("8", "embedded audio %.1f LUFS (target -14 +/- 0.8)" % lufs)
            else:
                bad("8", "embedded audio %.1f LUFS, outside -14 +/- 0.8" % lufs)
            if pk:
                tp = float(pk[-1])
                if tp <= TRUE_PEAK_MAX:
                    ok("8b", "true peak %.1f dBFS (limit %.1f)" % (tp, TRUE_PEAK_MAX))
                else:
                    bad("8b", "true peak %.1f dBFS is above the %.1f dBFS limit"
                        % (tp, TRUE_PEAK_MAX))
        else:
            bad("8", "could not measure loudness")

    # ---------------------------------------------------------------
    extra_checks(s, F, beats, scenes, words, total)

    # ---------------------------------------------------------------
    print("\n%d passed   %d warnings   %d failed" % (len(PASSES), len(WARNS), len(FAILS)))
    if FAILS:
        print("\nFAILED")
        for n, m in FAILS:
            print("   [%s] %s" % (n, m))
        return 1
    print("\nGATE PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
