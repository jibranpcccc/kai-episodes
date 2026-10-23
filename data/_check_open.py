# -*- coding: utf-8 -*-
"""Static checker for the deterministic HTML video engine.

Usage:  python data/_check_open.py <EPISODE_BASE_NAME>

Reads "<BASE>.html" next to the project root, extracts the timing model from
the embedded `window.FUSION = {...};` object and runs five structural checks:

    1.   NO EMPTY OPENING STAGE     - every window opens with content within 0.35s
    2.   NO ORPHAN ANIMATED ELEMENTS - every data-fx="1" element has a beat
    2b.  ALWAYS-VISIBLE LEAVES      - nothing that paints ink stays unanimated
    3.   NO UNBOUNDED PIVOT         - every bounded spin/sway has an amplitude
    4.   NO ORPHAN BEATS             - every beat targets an existing element id

Exit code 0 when all checks pass, 1 otherwise.
"""
import json
import os
import re
import sys
from html import unescape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_OPENING_GAP = 0.35

# A tag may contain ">" inside a quoted attribute value, so match quoted
# runs explicitly instead of stopping at the first ">".
TAG_RE = re.compile(r"<(?:[^>\"']|\"[^\"]*\"|'[^']*')+>")
# A start tag, an end tag or a run of text.  A "<" that cannot start a tag is
# text (as HTMLParser keeps it, e.g. "<30M").
TOKEN_RE = re.compile(r"<(/?)([a-zA-Z][\w:-]*)((?:[^>\"']|\"[^\"]*\"|'[^']*')*)>"
                      r"|([^<]+|<(?![a-zA-Z/!]))")
ATTR_RE = re.compile(r"([\w:-]+)\s*=\s*\"([^\"]*)\"")
DECL_RE = re.compile(r"([-a-zA-Z]+)\s*:\s*((?:[^;(]|\([^)]*\))*)")
WIDTH_RE = re.compile(r"^(?:\d*\.?\d+)(?:px|em|rem|%)?$")

VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input",
             "link", "meta", "param", "source", "track", "wbr"}
INK_TAGS = {"img", "svg", "canvas", "video"}
BORDER_STYLES = {"solid", "dashed", "dotted", "double", "groove", "ridge",
                 "inset", "outset"}


def fail(msg):
    print(msg)
    sys.exit(1)


def load_episode(name):
    """Read the episode HTML and return (html_text, fusion_dict)."""
    path = os.path.join(ROOT, name + ".html")
    if not os.path.isfile(path):
        fail("ERROR: episode file not found: " + path)
    try:
        with open(path, "r", encoding="utf-8") as fh:
            html = fh.read()
    except Exception as exc:  # noqa: BLE001 - report and exit cleanly
        fail("ERROR: cannot read " + path + ": " + str(exc))
    m = re.search(r"window\.FUSION\s*=\s*(\{.*?\});\s*</script>", html, re.S)
    if not m:
        fail("ERROR: no window.FUSION object found in " + path)
    try:
        fusion = json.loads(m.group(1))
    except Exception as exc:  # noqa: BLE001
        fail("ERROR: window.FUSION is not valid JSON: " + str(exc))
    if not isinstance(fusion, dict) or "scenes" not in fusion or "beats" not in fusion:
        fail("ERROR: window.FUSION missing .scenes/.beats")
    return html, fusion


def collect_ids(html):
    """Every id attribute value in the document."""
    return set(re.findall(r'\bid="([^"]+)"', html))


def scan_elements(html, beats):
    """One pass over the markup: fx maps id -> tag for the data-fx="1"
       elements, vis lists the wN_MM ids with neither data-fx nor a beat -
       they can never be animated, so they sit on screen from frame one."""
    beat_targets = set(b.get("el")[1:] for b in beats if b.get("el"))
    fx, vis = {}, set()
    for tag in TAG_RE.findall(html):
        idm = re.search(r'\bid="(w\d+_\d+)"', tag)
        if not idm:
            continue
        oid = idm.group(1)
        if 'data-fx="1"' in tag:
            fx[oid] = " ".join(tag.split())
        elif oid not in beat_targets:
            vis.add(oid)
    return fx, sorted(vis)


def check_opening(scenes, beats):
    """Check 1 - no window may sit empty for more than MAX_OPENING_GAP seconds."""
    per_group = {}
    for beat in beats:
        grp = beat.get("group")
        if grp is not None:
            per_group.setdefault(grp, []).append(beat.get("s", 0))
    rows = []
    for i, scene in enumerate(scenes):
        start = scene.get("s", 0)
        starts = per_group.get(i)
        rows.append((min(starts) - start if starts else None, i, start, scene.get("label", "")))
    offenders = [r for r in rows if r[0] is None or r[0] > MAX_OPENING_GAP]
    # worst first: a window with no beats at all counts as an infinite gap
    offenders.sort(key=lambda r: (-(r[0] if r[0] is not None else 1e9), r[1]))
    return offenders, rows


def check_orphan_fx(fx_map, beats):
    """Check 2 - every data-fx="1" element must be the target of some beat."""
    beat_targets = set(b.get("el") for b in beats if b.get("el"))
    return sorted(i for i in fx_map if ("#" + i) not in beat_targets)


def check_pivot(html):
    """Check 3 - a bounded pivot (data-amb-box) needs an amplitude.

    WHY: the runtime treats a bounded "spin" AND a bounded "sway" alike.  A
    spin without data-amb-amp spins forever (a legitimate rotating fan), but
    a sway without data-amb-amp silently falls back to a +/-8 degree default
    (core/fusion.js), which is NOT the position the drawing shows.  So both
    kinds must carry an amplitude whenever they are pinned to a box.
    """
    offenders = []
    for tag in TAG_RE.findall(html):
        if 'data-amb="spin"' not in tag and 'data-amb="sway"' not in tag:
            continue
        if 'data-amb-box=' not in tag:
            continue  # unbounded rotating fan / free sway: legitimate
        if 'data-amb-amp=' in tag:
            continue
        offenders.append(" ".join(tag.split()))
    return offenders


def check_orphan_beats(html, beats):
    """Check 4 - every beat target must exist as an element id."""
    ids = collect_ids(html)
    missing = []
    for beat in beats:
        el = beat.get("el")
        if not el:
            continue
        key = el[1:] if el.startswith("#") else el
        if key not in ids:
            missing.append(el)
    return sorted(set(missing))


# ---------------------------------------------------------------------------
# Check 2b - ALWAYS-VISIBLE LEAVES
#
# WHY: check 2 only sees elements whose id has the shape wN_MM, so a
# decoration with no id at all was invisible to it.  The original defect was
# exactly that shape - <div class="chain__arrow">&rarr;</div>: no id, no
# data-fx, no beat - so the arrow was painted from the first frame of its
# window and could never be animated.  This check walks every
# <section class="scene"> and fails any element that paints ink while
# neither it nor any ancestor inside that section carries data-fx="1".  The
# footer, caption bar, stage, HUD and player chrome sit outside the
# sections, so they are never considered.
# ---------------------------------------------------------------------------

def _paints(text):
    """Does this declaration text paint a background or draw a border?"""
    decls = {m.group(1).lower(): m.group(2).strip() for m in DECL_RE.finditer(text)}
    for prop, value in decls.items():
        val = value.strip().lower()
        if prop in ("background", "background-color"):
            if val not in ("", "none", "transparent") and \
                    not re.search(r",\s*0(?:\.0+)?\s*\)", val):
                return True
        elif prop == "background-image":
            return True
        elif prop.startswith("border") and "radius" not in prop:
            bits = val.split()
            if any(b in BORDER_STYLES for b in bits) and \
                    any(WIDTH_RE.match(b) or b.startswith("var(") for b in bits):
                return True
    return False

def _ink_map(css):
    """(classes, tags, ids) whose stylesheet rules paint ink."""
    classes, tags, ids = set(), set(INK_TAGS), set()
    css = re.sub(r"/\*.*?\*/", " ", css, flags=re.S)
    css = re.sub(r"@font-face\s*\{[^{}]*\}", " ", css)
    for sel, body in re.findall(r"([^{}]*)\{([^{}]*)\}", css):
        if not _paints(body):
            continue
        for one in sel.split(","):
            # the subject of the selector: its last compound, no pseudo-element
            subject = re.sub(r"::[A-Za-z-]+.*$", "", re.split(r"[>\s]+", one.strip())[-1])
            m = re.fullmatch(r"([a-zA-Z][\w-]*)?((?:[.#][\w-]+)*)", subject)
            if not m:
                continue
            if m.group(1):
                tags.add(m.group(1).lower())
            classes.update(re.findall(r"\.([\w-]+)", m.group(2)))
            ids.update(re.findall(r"#([\w-]+)", m.group(2)))
    return classes, tags, ids

def _ink(tag, attrs, text, pmap):
    """Does this element put visible ink on the canvas?"""
    classes, tags, ids = pmap
    if text.strip() or tag in tags:
        return True                       # a real text node / an image
    if attrs.get("id", "") in ids:
        return True
    if set(attrs.get("class", "").split()) & classes:
        return True                       # a class the stylesheet paints
    return _paints(attrs.get("style", ""))

def _scene_elements(html):
    """(scene index, tag, attrs, own text, animated) for every element that
    sits inside a <section class="scene">.  "animated" is True when the
    element or one of its ancestors carries data-fx="1", so it can never be
    an always-visible leaf."""
    skip = [(m.start(), m.end()) for m in re.finditer(
        r"<(?:script|style)\b[^>]*>.*?</(?:script|style)>", html, re.S)]
    index = 0
    for m in re.finditer(r"<section\b", html):
        if any(a <= m.start() < b for a, b in skip):
            continue
        open_tag = TAG_RE.match(html, m.start())
        if not open_tag or not re.search(r'class="[^"]*\bscene\b[^"]*"', open_tag.group(0)):
            continue
        close = html.find("</section>", open_tag.end())
        if close < 0:
            continue
        index += 1
        stack = [[None, {}, "", False]]
        for t in TOKEN_RE.finditer(html[open_tag.end():close]):
            close_tag, tag, attrs, text = t.group(1), t.group(2), t.group(3), t.group(4)
            if text is not None:
                stack[-1][2] += unescape(text)
                continue
            if close_tag:
                if len(stack) > 1:
                    el = stack.pop()
                    yield index, el[0], el[1], el[2], el[3]
                continue
            raw = attrs.rstrip()
            d = {k.lower(): v for k, v in ATTR_RE.findall(raw)}
            animated = stack[-1][3] or d.get("data-fx") == "1"
            tag = tag.lower()
            if tag in VOID_TAGS or raw.endswith("/"):
                yield index, tag, d, "", animated
            else:
                stack.append([tag, d, "", animated])

def check_always_visible(html, pmap):
    """Check 2b - no ink-painting element may sit outside the animated tree."""
    offenders = []
    for index, tag, attrs, text, animated in _scene_elements(html):
        if not animated and _ink(tag, attrs, text, pmap):
            offenders.append((index, tag, attrs, text))
    return offenders


def report(num, title, offenders, summary_ok, summary_fail, detail=None):
    """Print one check line plus a DETAIL block when it fails."""
    if offenders:
        print("FAIL  %s %s   (%s)" % (num, title, summary_fail(len(offenders))))
        print("DETAIL %s %s" % (num, title))
        for off in offenders:
            print("  " + (detail(off) if detail else str(off)))
    else:
        print("PASS  %s %s   (%s)" % (num, title, summary_ok()))
    print("")


def main(argv):
    if len(argv) != 2:
        print("usage: python _check_open.py <EPISODE_BASE_NAME>")
        return 1
    name = argv[1]
    html, fusion = load_episode(name)
    scenes = fusion.get("scenes") or []
    beats = fusion.get("beats") or []
    print("EPISODE: %s  (%d scenes, %d beats)" % (name, len(scenes), len(beats)))
    print("")

    # --- Check 1 -----------------------------------------------------------
    off1, rows1 = check_opening(scenes, beats)
    worst = sorted([r for r in rows1 if r[0] is not None], key=lambda r: -r[0])[:5]
    report(1, "NO EMPTY OPENING STAGE", off1,
           lambda: "worst gap %.2fs over %d windows" % (worst[0][0] if worst else 0.0, len(scenes)),
           lambda n: "%d offenders over %d windows" % (n, len(scenes)),
           lambda r: ("window %d  start %.2fs  label=%r  -> NO BEATS AT ALL"
                      % (r[1], r[2], r[3])) if r[0] is None else
                     ("window %d  start %.2fs  label=%r  -> gap %.2fs (max %.2fs)"
                      % (r[1], r[2], r[3], r[0], MAX_OPENING_GAP)))
    # The margin matters even on a pass, so always show the tightest windows.
    print("  worst opening gaps: " + ", ".join(
        "w%d=%.2fs" % (idx, gap) for gap, idx, _, _ in worst))
    print("")

    # --- Check 2 -----------------------------------------------------------
    fx_map, vis = scan_elements(html, beats)
    orphans = check_orphan_fx(fx_map, beats)
    report(2, "NO ORPHAN ANIMATED ELEMENTS", orphans,
           lambda: "0 orphans",
           lambda n: "%d orphans: %s" % (n, ", ".join(orphans)),
           lambda oid: "%s  -> no beat targets #%s%s" % (
               oid, oid, ("\n      markup: " + fx_map[oid]) if oid in fx_map else ""))
    # Informational only: ids that are neither marked nor beat-targeted.
    # Whether they actually show up on screen is decided by check 2b.
    if vis:
        print("  INFO  ids with no data-fx and no beat (2b decides if they paint ink): %d -> %s"
              % (len(vis), ", ".join(vis[:20]) + (" ..." if len(vis) > 20 else "")))
    print("")

    # --- Check 2b ----------------------------------------------------------
    style_m = re.search(r"<style>(.*?)</style>", html, re.S)
    pmap = _ink_map(style_m.group(1) if style_m else "")
    leaves = check_always_visible(html, pmap)
    report("2b", "ALWAYS-VISIBLE LEAVES", leaves,
           lambda: "0 always-visible leaves",
           lambda n: "%d always-visible leaves over %d scenes" % (n, len(scenes)),
           lambda o: "<%s class=%s id=%s>  scene %d  text=%r  -> paints ink, no data-fx on it or any ancestor"
           % (o[1], o[2].get("class", "") or "-", o[2].get("id", "") or "-", o[0],
              " ".join(o[3].split())[:40]))

    # --- Check 3 -----------------------------------------------------------
    pivots = check_pivot(html)
    report(3, "NO UNBOUNDED PIVOT", pivots,
           lambda: "0 unbounded pivots",
           lambda n: "%d unbounded pivots" % n)

    # --- Check 4 -----------------------------------------------------------
    missing = check_orphan_beats(html, beats)
    report(4, "NO ORPHAN BEATS", missing,
           lambda: "0 missing targets",
           lambda n: "%d missing targets" % n,
           lambda el: "%s  -> %d beat(s) point at a missing id"
                      % (el, sum(1 for b in beats if b.get("el") == el)))

    checks = (off1, orphans, leaves, pivots, missing)
    failed = sum(1 for off in checks if off)
    if failed:
        print("FAILED  (%d checks, %d failed)" % (len(checks), failed))
        return 1
    print("ALL CHECKS PASS  (%d checks, 0 failed)" % len(checks))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
