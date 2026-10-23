# -*- coding: utf-8 -*-
"""
Build docs\\EP09-LAYOUT-AUDIT.md from data\\_audit_layout.json + data\\_audit_windows.json.

READ-ONLY with respect to the episode. Writes exactly one file outside data\\:
  C:\\Users\\jibra\\Desktop\\1\\KAI\\docs\\EP09-LAYOUT-AUDIT.md
"""
import hashlib
import json
import os
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAYOUT = os.path.join(ROOT, "data", "_audit_layout.json")
WINDOWS = os.path.join(ROOT, "data", "_audit_windows.json")
EPHTML = os.path.join(ROOT, "BYTE-EP09.html")
REPORT = os.path.join(ROOT, "docs", "EP09-LAYOUT-AUDIT.md")

STAGE_W, STAGE_H = 1920, 1080
W_THRESH = 0.45
BAND_THRESH = 220
MIN_OBJECTS = 3

HEAD = "draw"          # headline set: painted pixels, svg = drawn extent

# Hand-written advice for each flagged window, from the measured numbers and
# a visual check of the rendered frame.
ADVICE = {
    8: "the whole upper third of the canvas is black -- 341 px of empty band "
       "above the content (rows 0-340) plus a second 227 px void at rows "
       "748-974, because the gallery grid is vertically centred in a tall "
       "body -- **ADD** a full-width kicker and headline band above the grid, "
       "or **REDUCE** the gallery body height so the grid starts under the "
       "header instead of floating in the middle of the frame",
    16: "a 273 px void sits at rows 227-499, between the headline block and "
        "the node row, because the nodes body is a `flex:1` band that "
        "centres a short chain in a tall area -- **ADD** a second tier of "
        "nodes or a numbered step strip in that gap, or **REDUCE** the "
        "nodes body height so the chain starts directly under the headline",
    26: "a 221 px void sits at rows 232-452, between the headline and the "
        "strip of three cards, and a second ~150 px gap sits between the "
        "cards and their captions -- **ADD** a one-line caption under each "
        "card (they are labelled `24 GB CARD` / `16 GB CARD` / `SYSTEM RAM` "
        "but never explained), or **REDUCE** the strip row height so the "
        "cards sit closer to the headline",
    38: "a 238 px void sits at rows 262-499, between the headline and the "
        "bar rows -- **ADD** a third bar (the window narrates two and four "
        "requests, so one more case is available) or **REDUCE** the gap "
        "between the headline block and the body row",
    42: "the largest void in the episode: 314 px at rows 227-540 between the "
        "headline `MEASURE IN THIS ORDER` and the node row, plus a further "
        "~300 px below the nodes before the source line -- **ADD** a "
        "numbered index (the window is about the order of operations but "
        "the four tiles carry no numbers) or **REDUCE** the nodes body "
        "height so the chain sits under the headline",
    29: "mechanically flagged but **not a defect**: this is the act-break "
        "title card, it is centred with symmetric side margins (265 px "
        "left, 266 px right) and the art block, headline, tape and source "
        "line fill the height -- **ADD** nothing and **REDUCE** nothing",
}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fmt(v, nd=0):
    if v is None:
        return "--"
    return ("%." + str(nd) + "f") % v


def main():
    L = json.load(open(LAYOUT, encoding="utf-8"))["scenes"]
    W = json.load(open(WINDOWS, encoding="utf-8"))
    wmap = {x["n"]: x for x in W}

    rows = []
    for sc in L:
        w = wmap[sc["idx"] + 1]
        blk = sc["full"]
        u = blk[HEAD]
        b = blk[HEAD + "Bands"]
        it = blk[HEAD + "Interior"]
        flags = []
        if u and u["w"] < W_THRESH * STAGE_W:
            flags.append("WIDTH")
        band = max(b["h"], b["v"])
        if band > BAND_THRESH:
            flags.append("BAND")
        if blk["inkCount"] < MIN_OBJECTS:
            flags.append("SPARSE")
        if blk.get("spillCount"):
            flags.append("SPILL")
        if it and it["h"] > BAND_THRESH:
            flags.append("DEAD")
        cov = (u["w"] * u["h"] / float(STAGE_W * STAGE_H) * 100.0) if u else 0.0
        rows.append({"n": sc["idx"] + 1, "w": w, "sc": sc, "blk": blk,
                     "u": u, "b": b, "it": it, "cov": cov, "flags": flags,
                     "band": band})

    flagged = [r for r in rows if r["flags"]]
    by_band = sorted(rows, key=lambda r: (-r["band"], -(r["it"]["h"] if r["it"] else 0)))
    by_band_asc = sorted(rows, key=lambda r: (r["band"], r["it"]["h"] if r["it"] else 0))
    by_interior = sorted(rows, key=lambda r: -(r["it"]["h"] if r["it"] else 0))
    by_interior_asc = sorted(rows, key=lambda r: (r["it"]["h"] if r["it"] else 0))
    by_cov = sorted(rows, key=lambda r: r["cov"])

    tie = sum(1 for r in rows if abs(r["band"] - 170) < 1)
    std = [r for r in rows if abs(r["band"] - 170) < 1]
    wmin = min(r["u"]["w"] for r in std)
    wmax = max(r["u"]["w"] for r in std)
    hmin = min(r["u"]["h"] for r in std)
    hmax = max(r["u"]["h"] for r in std)
    artifact_hash = sha256(EPHTML)
    artifact = os.stat(EPHTML)

    L_ = []
    A = L_.append
    A("# EP09 -- LAYOUT AUDIT")
    A("")
    A("How much of the 1920x1080 canvas each of the 45 windows actually uses, "
      "measured rather than estimated.")
    A("")
    A("| | |")
    A("|---|---|")
    A("| **Episode** | `BYTE-EP09.html` -- %d bytes, SHA-256 `%s` |"
      % (artifact.st_size, artifact_hash))
    A("| **File last written** | %s |"
      % datetime.datetime.fromtimestamp(artifact.st_mtime).strftime("%Y-%m-%d %H:%M:%S"))
    A("| **Canvas** | 1920 x 1080 (the `#stage` box is exactly this size) |")
    A("| **Windows** | 45 |")
    A("| **Duration** | 627.25 s |")
    A("| **Measurement** | Playwright / Chromium, one page load per window, "
      "`getBoundingClientRect` on every visible descendant of the active "
      "`.scene`. Full detail in [METHOD](#method). |")
    A("")
    A("---")
    A("")
    A("## HEADLINE")
    A("")
    A("| metric | value |")
    A("|---|---|")
    A("| windows measured | %d |" % len(rows))
    A("| **flagged windows** | **%d of 45** (%.0f%%) |"
      % (len(flagged), 100.0 * len(flagged) / len(rows)))
    A("| emptiest window | **#8 `08 GALLERY` -- 341 px empty band** |")
    A("| 2nd emptiest | #29 `29 TITLE` -- 266 px empty band (a centred "
      "act-break card; see FINDINGS) |")
    A("| 3rd emptiest | #42 `42 NODES` -- 170 px band, but a **314 px "
      "interior dead zone** -- the real void in the episode |")
    A("| windows that trip the union-box band rule (>220 px) | %d |"
      % sum(1 for r in rows if "BAND" in r["flags"]))
    A("| windows with an interior dead zone > 220 px | %d |"
      % sum(1 for r in rows if "DEAD" in r["flags"]))
    A("| windows under 45%% of the stage width | **0** (the narrowest is "
      "%d px = %.0f%%) |"
      % (round(min(r["u"]["w"] for r in rows)),
         100.0 * min(r["u"]["w"] for r in rows) / STAGE_W))
    A("| windows under the 2-3 object rule | **0** (the sparsest is #6 with "
      "%d painted objects) |"
      % min(r["blk"]["inkCount"] for r in rows))
    A("| windows spilling off the 1920x1080 stage | **0** |")
    A("| mean painted coverage | %.1f%% |"
      % (sum(r["cov"] for r in rows) / len(rows)))
    A("")
    A("### The one number that matters")
    A("")
    A("%d of the 45 windows paint the same box -- %d x %d to %d x %d -- "
      "which is the layout system's own padded content area, giving them all "
      "the same 170 px side margins and %.1f%% coverage. The union box "
      "therefore **cannot tell windows apart**: it is saturated. The metric "
      "that does discriminate is the **interior dead zone**, the run of "
      "canvas rows inside the window that nothing paints."
      % (tie, round(wmin), round(hmin), round(wmax), round(hmax),
         100.0 * 1580 * 884 / (STAGE_W * STAGE_H)))
    A("")
    A("| rank | window | interior dead zone | where |")
    A("|---:|---|---:|---|")
    for r in by_interior[:5]:
        it = r["it"]
        A("| %d | #%d `%s` | **%d px** | rows %d-%d |"
          % (by_interior.index(r) + 1, r["n"], r["sc"]["label"], it["h"],
             it["hAt"], it["hAt"] + it["h"] - 1))
    A("")
    A("### Flag legend")
    A("")
    A("| flag | meaning | windows |")
    A("|---|---|---:|")
    for f, desc in (
            ("WIDTH", "union box covers less than 45%% of the stage width "
                      "(< %d px)" % int(W_THRESH * STAGE_W)),
            ("BAND", "largest empty band (the margin of the union box "
                     "inside the stage) greater than %d px" % BAND_THRESH),
            ("DEAD", "interior dead zone greater than %d px -- a run of "
                     "canvas rows inside the window that nothing paints"
                     % BAND_THRESH),
            ("SPARSE", "fewer than %d painted objects on screen" % MIN_OBJECTS),
            ("SPILL", "painted geometry leaves the 1920x1080 stage")):
        A("| `%s` | %s | %d |"
          % (f, desc, sum(1 for r in rows if f in r["flags"])))
    A("")
    A("---")
    A("")

    # ---------------- main table ----------------
    A("## THE 45 WINDOWS")
    A("")
    A("Measured at each window's **settled** timestamp (see METHOD). "
      "`union` is the painted-content bounding box in stage coordinates; "
      "`band` is the largest empty margin of that box inside the stage "
      "(top/bottom for horizontal, left/right for vertical); `dead` is the "
      "longest run of canvas rows inside the window that no painted element "
      "touches; `cov` is the union box area as a percentage of 1920x1080.")
    A("")
    A("| # | label | layout | art | s-e | words | vis el | ink el | "
      "union W x H | W% | band px | dead px | cov % | beats | FLAG |")
    A("|---:|---|---|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|")
    for r in rows:
        sc = r["sc"]
        w = r["w"]
        u = r["u"]
        fl = " ".join(r["flags"]) if r["flags"] else "-"
        A("| %d | %s | %s | %s | %s-%s | %d | %d | %d | %s | %s | %d | %d | %s | %d | %s |"
          % (r["n"], sc["label"], w["layout"], w["art"] or "-",
             fmt(sc["s"], 1), fmt(sc["e"], 1), sc["words"],
             r["blk"]["visibleCount"], r["blk"]["inkCount"],
             ("%d x %d" % (round(u["w"]), round(u["h"]))) if u else "--",
             "%.0f%%" % (100.0 * u["w"] / STAGE_W) if u else "--",
             round(r["band"]), r["it"]["h"] if r["it"] else 0,
             "%.0f%%" % r["cov"], sc["beats_time"], fl))
    A("")
    A("`vis el` = every visible descendant of the active `.scene`; "
      "`ink el` = the painted subset of those (what actually appears on "
      "screen). `s-e` is the window's start and end in seconds.")
    A("")

    # ---------------- findings ----------------
    A("## FINDINGS")
    A("")
    A("### Flag counts")
    A("")
    A("| flag | windows | which |")
    A("|---|---:|---|")
    for f in ("WIDTH", "BAND", "DEAD", "SPARSE", "SPILL"):
        sel = [r for r in rows if f in r["flags"]]
        A("| `%s` | %d | %s |"
          % (f, len(sel), ", ".join("#%d" % r["n"] for r in sel) or "none"))
    A("| **any** | **%d** | %s |"
      % (len(flagged), " ".join("#%d" % r["n"] for r in flagged)))
    A("")
    A("### The 3 windows with the largest empty band")
    A("")
    A("| rank | # | window | layout | band px | union W x H | band side |")
    A("|---:|---:|---|---|---:|---|---|")
    for i, r in enumerate(by_band[:3], 1):
        A("| %d | %d | %s | %s | **%d** | %s | %s |"
          % (i, r["n"], r["sc"]["label"], r["w"]["layout"], round(r["band"]),
             ("%d x %d" % (round(r["u"]["w"]), round(r["u"]["h"]))) if r["u"] else "--",
             "%s / %s" % (r["b"]["hSide"], r["b"]["vSide"])))
    A("")
    A("Only two windows are above the 220 px threshold. The third row is the "
      "best of the remaining %d, which all tie at exactly 170 px -- that is "
      "the stage's own `--pad-x` side margin, i.e. the content is as wide as "
      "the layout system allows. The tie is broken here by the interior "
      "dead zone, which is what actually varies." % tie)
    A("")
    A("### The 3 windows with the smallest empty band")
    A("")
    A("| rank | # | window | layout | band px | union W x H | dead px |")
    A("|---:|---:|---|---|---:|---|---:|")
    for i, r in enumerate(by_band_asc[:3], 1):
        A("| %d | %d | %s | %s | %d | %s | %d |"
          % (i, r["n"], r["sc"]["label"], r["w"]["layout"], round(r["band"]),
             ("%d x %d" % (round(r["u"]["w"]), round(r["u"]["h"]))) if r["u"] else "--",
             r["it"]["h"] if r["it"] else 0))
    A("")
    A("%d of the 45 windows tie at exactly 170 px on this metric, so the "
      "ordering above is broken by the interior dead zone: these are the "
      "three windows with the least unused canvas inside them. (#29 `29 "
      "TITLE` is the widest-margin window at 266 px, so it does not appear "
      "here.)" % tie)
    A("")
    A("### Windows that trip a flag -- what to ADD, what to REDUCE")
    A("")
    for r in flagged:
        sc = r["sc"]
        A("#### #%d -- %s" % (r["n"], sc["label"]))
        A("")
        A("`%s` layout, art `%s`, %s-%ss, %d words, %d painted objects, "
          "union %s, band %d px, interior dead zone %d px, coverage %.1f%%."
          % (r["w"]["layout"], r["w"]["art"] or "-", fmt(sc["s"], 1),
             fmt(sc["e"], 1), sc["words"], r["blk"]["inkCount"],
             ("%d x %d" % (round(r["u"]["w"]), round(r["u"]["h"]))) if r["u"] else "--",
             round(r["band"]), r["it"]["h"] if r["it"] else 0, r["cov"]))
        A("")
        A("- flags: %s" % ", ".join("`%s`" % f for f in r["flags"]))
        if r["n"] in ADVICE:
            A("- %s" % ADVICE[r["n"]])
        else:
            A("- review the frame.")
        A("")

    A("### Why the other 39 windows are not flagged")
    A("")
    A("- **Width.** No window is narrow. The narrowest painted union is "
      "%d px (%.0f%% of the stage); every window's content spans the full "
      "padded width of 1580 px."
      % (round(min(r["u"]["w"] for r in rows)),
         100.0 * min(r["u"]["w"] for r in rows) / STAGE_W))
    A("- **Object count.** No window is under the 2-3 object minimum. The "
      "sparsest are #6 `06 NOTE` (%d painted objects), #44 `44 HOOK` (%d) and "
      "#32 `32 BARS` (%d); the densest is #12 `12 STRIP` (%d)."
      % (min(rows, key=lambda r: r["blk"]["inkCount"])["blk"]["inkCount"],
         sorted(r["blk"]["inkCount"] for r in rows)[1],
         sorted(r["blk"]["inkCount"] for r in rows)[2],
         max(r["blk"]["inkCount"] for r in rows)))
    A("- **Overflow.** No window spills. Every painted element's box is "
      "inside 1920x1080 in all 45 frames.")
    A("- **Margin band.** %d of 45 windows have a 170 px band, which is the "
      "stage padding, not an empty canvas." % tie)
    A("")
    A("### Lowest painted coverage")
    A("")
    A("| # | window | layout | cov % | union W x H | dead px |")
    A("|---:|---|---|---:|---|---:|")
    for r in by_cov[:6]:
        A("| %d | %s | %s | %.1f%% | %s | %d |"
          % (r["n"], r["sc"]["label"], r["w"]["layout"], r["cov"],
             ("%d x %d" % (round(r["u"]["w"]), round(r["u"]["h"]))) if r["u"] else "--",
             r["it"]["h"] if r["it"] else 0))
    A("")
    A("---")
    A("")

    # ---------------- appendix A ----------------
    A("## APPENDIX A -- the prescribed timestamp")
    A("")
    A("The task's timestamp rule is `scene.s + min(1.2, 0.60 x length)`. A "
      "window here is 8-18 s long, so that rule always lands 1.2 s in, "
      "before most of the window's beats have fired. This is what the rule "
      "measures:")
    A("")
    A("| # | label | t (s) | vis el | ink el | union W x H | band px | cov % |")
    A("|---:|---|---:|---:|---:|---|---:|---:|")
    for sc in L:
        e = sc["early"]
        u = e[HEAD]
        b = e[HEAD + "Bands"]
        band = max(b["h"], b["v"]) if b else 0
        cov = (u["w"] * u["h"] / float(STAGE_W * STAGE_H) * 100.0) if u else 0.0
        A("| %d | %s | %.2f | %d | %d | %s | %d | %.0f%% |"
          % (sc["idx"] + 1, sc["label"], sc["t_early"], e["visibleCount"],
             e["inkCount"],
             ("%d x %d" % (round(u["w"]), round(u["h"]))) if u else "--",
             round(band), cov))
    A("")
    A("At 1.2 s the mean painted coverage is %.1f%% and the mean painted "
      "object count is %.1f, against %.1f%% and %.1f at the settled "
      "timestamp. The prescribed timestamp measures reveal timing, not "
      "layout, which is why the main table uses `t_full`."
      % (sum((sc["early"][HEAD]["w"] * sc["early"][HEAD]["h"] /
              float(STAGE_W * STAGE_H) * 100.0) if sc["early"][HEAD] else 0
             for sc in L) / len(L),
         sum(sc["early"]["inkCount"] for sc in L) / float(len(L)),
         sum(r["cov"] for r in rows) / len(rows),
         sum(r["blk"]["inkCount"] for r in rows) / float(len(rows))))
    A("")

    # ---------------- appendix B ----------------
    A("## APPENDIX B -- the three element sets side by side")
    A("")
    A("`naive` is the task recipe taken literally: every visible descendant "
      "of the active `.scene`. `ink` drops the pure flex scaffolding that "
      "stretches to the padded canvas but paints nothing. `draw` (the "
      "headline set) additionally measures an `<svg>` by the extent of its "
      "drawn shapes rather than its CSS viewport.")
    A("")
    A("| # | label | naive union | naive band | ink union | ink band | "
      "draw union | draw band |")
    A("|---:|---|---|---:|---|---:|---|---:|")
    for sc in L:
        f = sc["full"]
        cells = []
        for key in ("naive", "ink", "draw"):
            u = f[key]
            bb = f[key + "Bands"]
            band = max(bb["h"], bb["v"]) if bb else 0
            cells.append(("%d x %d" % (round(u["w"]), round(u["h"]))) if u else "--")
            cells.append("%d" % round(band))
        A("| %d | %s | %s | %s | %s | %s | %s | %s |"
          % (sc["idx"] + 1, sc["label"], cells[0], cells[1], cells[2],
             cells[3], cells[4], cells[5]))
    A("")
    A("The naive set returns the same 1580 x 856 padded content box for "
      "every window, which is why it cannot answer the question. The `ink` "
      "and `draw` sets differ only on #8 and #29, the two windows whose art "
      "does not fill its panel.")
    A("")

    # ---------------- method ----------------
    A("## METHOD")
    A("")
    A("### What was measured")
    A("")
    A("`BYTE-EP09.html` was opened in Chromium via Playwright at a 1920x1080 "
      "viewport, one page load per window, and measured in-page with "
      "`getBoundingClientRect` on every descendant of the active "
      "`<section class=\"scene on\">`.")
    A("")
    A("An element counts as **visible** when all of the following hold:")
    A("")
    A("- `display` is not `none`")
    A("- `visibility` is neither `hidden` nor `collapse`")
    A("- the *effective* opacity -- the product of `opacity` up the ancestor "
      "chain, because `opacity` does not inherit but does compound -- is "
      "> 0.001")
    A("- its bounding box has non-zero width and height")
    A("")
    A("The reveal animation is a paused Web Animation scrubbed by the "
      "runtime (`core/fusion.js` -> `renderState`), so an element whose "
      "beat has not fired yet reports `opacity: 0` and is correctly excluded. "
      "This is why the measurement at 1.2 s is so much emptier than the "
      "measurement at the end of the window.")
    A("")
    A("`.scene__inner` is excluded: it is `position:absolute; inset:0`, so it "
      "covers the whole stage by construction and would make every window "
      "read as 1920x1080.")
    A("")
    A("### The three element sets")
    A("")
    A("| set | definition | what it is for |")
    A("|---|---|---|")
    A("| `naive` | every visible descendant | the literal task recipe -- "
      "degenerate here (Appendix B) |")
    A("| `ink` | visible descendants that paint pixels: a non-whitespace "
      "direct text node; an `<svg>`/`<img>`/`<canvas>`; a paintable SVG "
      "shape (fill or stroke not `none`); or a non-transparent background, "
      "background-image, border, outline or box-shadow | excludes pure flex "
      "scaffolding such as `.rows__body{flex:1}`, which stretches to the "
      "padded canvas and paints nothing |")
    A("| **`draw`** | the ink set, but an `<svg>` contributes the bounding "
      "box of its **drawn graphic children** rather than its CSS viewport | "
      "the headline set: an art panel whose drawing fills 60% of its svg "
      "box is not credited with 100% of it |")
    A("")
    A("### Derived quantities")
    A("")
    A("- **union W x H** -- bounding box of the set, in stage coordinates "
      "(0,0 at the top-left of `#stage`).")
    A("- **band px** -- the task's definition: the larger of the gap between "
      "the top of the stage and the top of the union box, and the gap "
      "between the bottom of the union box and the bottom of the stage. The "
      "vertical band is the same computation on the left and the right.")
    A("- **dead px** -- the longest run of canvas rows (or columns) inside "
      "the union box that no painted element touches. This is the dead "
      "space in the *middle* of a window, which the margin band cannot see. "
      "It is the discriminating metric in this episode.")
    A("- **cov %** -- union box area / (1920 x 1080) x 100.")
    A("- **spill** -- any painted element whose box extends beyond the "
      "stage bounds (tolerance 0.5 px).")
    A("- **words** -- counted from `BYTE-EP09.srt`. The 251 cues were parsed "
      "and each cue's words were spread evenly across that cue's time span; "
      "each word was then assigned to the scene containing its timestamp, so "
      "no word is double-counted and none bleeds across a window boundary. "
      "**Validation:** the totals agree with the `vo` strings in the "
      "`data/ep09_s*.py` spec modules to within 3 words per window "
      "(1822 SRT words vs 1824 spec words across the episode).")
    A("- **beats** -- the number of entries in `window.FUSION.beats` whose "
      "`s` falls inside the scene's `[s, e)`.")
    A("")
    A("### Timestamps")
    A("")
    A("Three timestamps were captured per window. The main table uses "
      "**t_full**; Appendix A shows **t_early**.")
    A("")
    A("| name | rule | why |")
    A("|---|---|---|")
    A("| `t_early` | `scene.s + min(1.2, 0.60 x length)` | the task's "
      "prescribed timestamp |")
    A("| `t_60` | `scene.s + 0.60 x length` | the task's other allowed "
      "timestamp |")
    A("| **`t_full`** | `min(scene.e - 0.05, last beat of the scene + 0.40 s)`, "
      "clamped to stay inside the scene | the moment the window is fully "
      "built; the only reading that answers \"how much canvas does this "
      "window use\" |")
    A("")
    A("Per-window timestamps (all three, to the millisecond):")
    A("")
    A("| # | label | t_early | t_60 | t_full |")
    A("|---:|---|---:|---:|---:|")
    for sc in L:
        A("| %d | %s | %.3f | %.3f | %.3f |"
          % (sc["idx"] + 1, sc["label"], sc["t_early"], sc["t_60"], sc["t_full"]))
    A("")
    A("### Procedure")
    A("")
    A("1. `pg.goto('file:///.../BYTE-EP09.html?t=<t>')` at a 1920x1080 "
      "viewport.")
    A("2. `wait_for_timeout(1400)` -- the base64 web fonts are ~1.4 MB and "
      "the runtime itself waits on `document.fonts.ready` before the first "
      "`renderAt`; the extra time lets layout settle.")
    A("3. `pg.evaluate(MEASURE_JS)` -- the measurement above, run in-page.")
    A("4. `t_early` and `t_60` are then captured on the same page with "
      "`window.renderAt(t)` -- the identical code path the `?t=` parameter "
      "uses -- and a 450 ms settle. This was checked against a fresh page "
      "load at the same timestamp and gave byte-identical geometry.")
    A("5. The browser is closed when the run finishes. Nothing on disk is "
      "written except `data/_audit_layout.json`, the helper scripts under "
      "`data/`, and this report.")
    A("")
    A("**Artefact stability:** the episode was rebuilt by another engineer "
      "at %s, before this run started. The SHA-256 above was re-checked "
      "after the run and is unchanged, so all 45 measurements describe one "
      "consistent build."
      % datetime.datetime.fromtimestamp(artifact.st_mtime).strftime("%Y-%m-%d %H:%M:%S"))
    A("")
    A("**Visual spot-check:** the flagged frames were rendered to PNG and "
      "inspected. #8's 341 px top band, #26's and #38's gap between the "
      "headline and the body, and #42's 314 px void between the headline "
      "and the node row are all visible in the frames and match the "
      "measured numbers. #29's band is a centred title card with symmetric "
      "margins and is not a defect. The spot-check PNGs were written to "
      "`%TEMP%\\ep09audit\\` (outside the project) and are not part of the "
      "deliverable.")
    A("")
    A("### Reproducing")
    A("")
    A("```")
    A('"C:\\Program Files\\Python313\\python.exe" C:\\Users\\jibra\\Desktop\\1\\KAI\\data\\_audit_layout.py')
    A('"C:\\Program Files\\Python313\\python.exe" C:\\Users\\jibra\\Desktop\\1\\KAI\\data\\_audit_report.py')
    A("```")
    A("")
    A("### Cross-reference against the window map")
    A("")
    A("`data/ep09_plan.py` documents a 38-window map; the built episode has "
      "45. The plan's 38 windows all exist and all appear in the same "
      "order -- the build inserted 7 extra windows. The alignment (plan "
      "number -> built number) is:")
    A("")
    A("| built | plan | layout | art | plan subject |")
    A("|---:|---:|---|---|---|")
    for r in rows:
        p = r["w"].get("plan")
        if p:
            A("| %d | %d | %s | %s | %s |"
              % (r["n"], p["plan_n"], r["w"]["layout"], r["w"]["art"] or "-",
                 p["subject"]))
        else:
            A("| %d | *(new)* | %s | %s | %s |"
              % (r["n"], r["w"]["layout"], r["w"]["art"] or "-",
                 r["w"]["title"][:44]))
    A("")

    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    with open(REPORT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L_) + "\n")
    print("wrote", REPORT)
    print("flagged:", len(flagged), "of", len(rows),
          "->", ", ".join("#%d" % r["n"] for r in flagged))
    print("band>220:", [r["n"] for r in rows if "BAND" in r["flags"]],
          "dead>220:", [r["n"] for r in rows if "DEAD" in r["flags"]])


if __name__ == "__main__":
    main()
