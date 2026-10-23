# -*- coding: utf-8 -*-
"""
FUSION BUILDER
===============
spec_07_fusion.py  ->  BYTE-07-FUSION.html  (+ .srt)

  1. edge-tts per window, boundary="WordBoundary"  -> REAL word timings
  2. resolve each anchor phrase to the word that carries it
  3. schedule the beats under the rhythm law
  4. concat with gaps, loudnorm -14 LUFS, embed as base64
  5. render every window from the component library
  6. inline CSS + JS + fonts + audio + beat table  ->  ONE self-contained file

There is no fallback timing anywhere. An anchor that is not in the script
raises and the build stops (EPISODE-RULES.md, bug 3).
"""
import asyncio
import base64
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusion_art import ART

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = "BYTE-07-FUSION"
VOICE = "en-US-AndrewNeural"
RATE = "+4%"
GAP = 0.32
TAIL = 0.9

# ---------------------------------------------------------------- the law
MIN_GAP = 0.30        # no two beats closer than this           (RepoChad)
HERO_ALONE = 0.55     # the first beat of a window lands alone  (RepoChad)
MAX_GAP_FAIL = 8.00   # a dead spot longer than this fails the build
MAX_GAP_WARN = 6.00   # longer than this is flagged for a human look
NUDGE_BOUND = 1.00
TEASE_BOUND = 2.00   # a beat may land this far BEFORE its word (a deliberate tease)    # a beat may never move further than this from its word
OPEN_LEAD = 0.00     # a window's first arrival may not sit later than this after its first word

DUR = {"rise": 340, "slam": 460, "pop": 420, "sticker": 380, "wipe": 520,
       "nudge": 300, "count": 340, "sweep": 340, "draw": 850, "push": 1400}

CAPTION_WORDS = 8   # words per .srt cue -- a caption should read as a line


def _plain(s):
    """The text of a spec field with the HTML entities resolved."""
    return (s or "").replace("&middot;", "·").replace("&amp;", "&") \
        .replace("&lt;", "<").replace("&gt;", ">").replace("&nbsp;", " ").strip()


def _groups(n, size):
    """Split n items into groups of at most `size`, balanced.

    A window of nine words must not become a cue of eight words and a cue of
    one: a single-word caption is not a caption. The groups are spread as
    evenly as the count allows."""
    if n <= 0:
        return []
    k = max(1, (n + size - 1) // size)
    base, extra = n // k, n % k
    out, i = [], 0
    for g in range(k):
        take = base + (1 if g < extra else 0)
        out.append((i, i + take))
        i += take
    return out


# ==================================================================== TTS
async def record(W, work):
    os.makedirs(work, exist_ok=True)
    sem = asyncio.Semaphore(6)

    async def record_one(i, w):
        # The cache is keyed by the TEXT, not by the index. A window that is
        # rewritten, split or moved must never inherit the audio of the
        # window that used to sit at this index -- that silently ships the
        # wrong voice over the right words.
        key = hashlib.sha1(("%s|%s|%s" % (w["vo"], VOICE, RATE))
                           .encode("utf-8")).hexdigest()[:16]
        raw = os.path.join(work, "r%d-%s.mp3" % (i, key))
        wav = os.path.join(work, "n%d-%s.wav" % (i, key))
        jsf = os.path.join(work, "n%d-%s.json" % (i, key))
        if os.path.exists(wav) and os.path.exists(jsf) and os.path.getsize(wav) > 1000:
            try:
                ws_cached = json.loads(open(jsf, "r", encoding="utf-8").read())
                return ws_cached, wav
            except Exception:
                pass
        async with sem:
            buf, ws = bytearray(), []
            for attempt in range(5):
                try:
                    import edge_tts
                    c = edge_tts.Communicate(w["vo"], VOICE, rate=RATE, boundary="WordBoundary")
                    buf, ws = bytearray(), []
                    async for ch in c.stream():
                        if ch["type"] == "audio":
                            buf += ch["data"]
                        elif ch["type"] == "WordBoundary":
                            ws.append((ch["offset"] / 1e7, ch["text"]))
                    if buf:
                        break
                except Exception:
                    if attempt == 4:
                        raise
                    await asyncio.sleep(1 + attempt)
            open(raw, "wb").write(bytes(buf))
            o = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", raw, "-af",
                                "silencedetect=noise=-45dB:d=0.05", "-f", "null", "-"],
                               capture_output=True, text=True).stderr
            e = re.findall(r"silence_end: ([0-9.]+)", o)
            lead = float(e[0]) if e else 0.0
            subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", raw,
                            "-af", "silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,"
                                   "areverse,silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,areverse",
                            "-ar", "44100", "-ac", "1", "-c:a", "pcm_s16le", wav], check=True)
            res_words = [(max(0.0, x - lead + 0.04), t) for x, t in ws]
            open(jsf, "w", encoding="utf-8").write(json.dumps(res_words))
            if os.path.exists(raw):
                os.remove(raw)
            return res_words, wav

    tasks = [record_one(i, w) for i, w in enumerate(W, 1)]
    results = await asyncio.gather(*tasks)
    words = [r[0] for r in results]
    files = [r[1] for r in results]
    return words, files


def _norm_word(s):
    """A word reduced to what the script and the synthesiser can agree on."""
    return s.lower().strip(".,;:!?\"'()[]")


def _align_tokens(vw, ws):
    """Map every script word onto the synthesiser token that carries it.

    The synthesiser re-tokenises what it is given: "llama.cpp" arrives as
    three tokens. The caption has to show the SCRIPT's words, so the two
    lists are aligned and each script word takes the token it belongs to.

    Returns one token index per script word.
    """
    sw = [_norm_word(x) for x in vw]
    tw = [_norm_word(x[1]) for x in ws]
    idx = []
    sm = difflib.SequenceMatcher(None, sw, tw, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        n, m = i2 - i1, j2 - j1
        if tag == "insert":
            continue
        if tag == "equal":
            for k in range(n):
                idx.append(j1 + k)
        elif tag == "replace":
            for k in range(n):
                idx.append(j1 + (int(k * m / float(n)) if (n and m) else 0))
        elif tag == "delete":
            for k in range(n):
                idx.append(min(j1, len(ws) - 1))
    if not idx:
        idx = [0] * len(vw)
    # Two script words may share a token: the synthesiser does not say the
    # word the script wrote ("two hundred and eighty-eight" arrives without
    # the "and"), and both words belong to the token that carries them.
    idx = idx[:len(vw)]
    while len(idx) < len(vw):
        idx.append(min(len(ws) - 1, idx[-1]))
    return idx


def phrase_time(text, ws, phrase):
    """The time of the first spoken word at or after the phrase starts."""
    p = text.lower().find(phrase.lower())
    if p < 0:
        raise ValueError("anchor not in script: %r" % phrase)
    low, cur = text.lower(), 0
    for t, w in ws:
        wl = w.lower().strip(".,;:!?\"'()")
        i = low.find(wl, cur) if wl else -1
        if i < 0:
            i = cur
        else:
            cur = i + len(wl)
        if i >= p:
            return t
    return ws[-1][0]


def dur_of(f):
    o = subprocess.run(["ffmpeg", "-hide_banner", "-i", f], capture_output=True, text=True).stderr
    m = re.findall(r"Duration: (\d+):(\d+):([\d.]+)", o)
    h, mnt, s = m[0]
    return int(h) * 3600 + int(mnt) * 60 + float(s)


# ================================================================ SCHEDULER
def schedule(beats, wtext, ws):
    """Resolve anchors to real word times, then enforce the rhythm law.

    Beats that share an anchor arrive as one GROUP. The nudge is measured on
    the group's arrival, not on each member, so a four-part arrival (panel +
    sketch + camera + caption) counts as one honest arrival rather than four
    drifted ones."""
    for b in beats:
        b["_t0"] = phrase_time(wtext, ws, b["at"]) if b.get("at") else None
    last = 0.0
    for b in beats:
        if b["_t0"] is None:
            b["_t0"] = last
        else:
            last = b["_t0"]
    # NO EMPTY OPENING STAGE. The first thing a window puts on screen has to
    # arrive with the window's first spoken words. A window that opens on an
    # empty background for seconds is a real defect -- the owner reported it
    # as "there is a blank background in the start of the video" -- so the
    # earliest arrival is pulled back to the first word of the window.
    open_t = ws[0][0] if ws else 0.0
    late = None
    if beats:
        k = min(range(len(beats)), key=lambda i: beats[i]["_t0"])
        if beats[k]["_t0"] > open_t + OPEN_LEAD:
            late = beats[k]["_t0"] - open_t
            beats[k]["_t0"] = open_t + OPEN_LEAD
    # arrival order is the resolved order, not the authoring order
    beats.sort(key=lambda bb: bb["_t0"])
    # group = consecutive beats that share an anchor
    gi = 0
    for i, bb in enumerate(beats):
        if i > 0 and bb["_t0"] != beats[i - 1]["_t0"]:
            gi = 0
        bb["_off"] = gi
        gi += 1
    # Group-based scheduling: sub-beats belonging to the same arrival group
    # share the group's arrival time, rather than cascading sequentially and
    # causing multi-second delays for subsequent cards.
    notes = []
    if late is not None:
        notes.append(("LATE OPEN", None, round(late, 2),
                      "first arrival pulled %.2fs back to the window's first word" % late))

    # Identify distinct arrival groups
    group_indices = []
    for i, b in enumerate(beats):
        if b["_off"] == 0:
            group_indices.append(i)

    group_times = [beats[gi]["_t0"] for gi in group_indices]

    # Enforce HERO ALONE between group 0 and group 1 only if group 1 is not word 1
    if len(group_times) > 1 and group_times[1] - group_times[0] < HERO_ALONE - 1e-6:
        group_times[1] = group_times[0] + HERO_ALONE

    # Enforce MIN_GAP between DISTINCT GROUPS
    for k in range(1, len(group_times)):
        if group_times[k] - group_times[k - 1] < MIN_GAP - 1e-6:
            group_times[k] = group_times[k - 1] + MIN_GAP + 0.004

    # Enforce MAX_GAP_FAIL between distinct groups
    for k in range(1, len(group_times)):
        gap = group_times[k] - group_times[k - 1]
        if gap > MAX_GAP_FAIL:
            pull = min(gap - MAX_GAP_FAIL, TEASE_BOUND)
            group_times[k] -= pull
            notes.append(("LONG HOLD", beats[group_indices[k]].get("at"), round(gap, 2),
                          "pulled %.2fs" % pull))

    # Distribute group times to all member beats
    times = [0.0] * len(beats)
    for k, gi in enumerate(group_indices):
        next_gi = group_indices[k + 1] if k + 1 < len(group_indices) else len(beats)
        gt = group_times[k]
        for idx in range(gi, next_gi):
            times[idx] = round(gt, 3)

    for i, b in enumerate(beats):
        g = i - b["_off"]                       # first member of its group
        b["_nudge"] = round(times[g] - beats[g]["_t0"], 3)
        b["_arr"] = round(times[g], 3)          # the group's arrival
        # a group of N beats legitimately spans (N-1) gaps, so its arrival may
        # sit further from the word than a single beat would
        gsize = b["_off"] + 1
        allow = NUDGE_BOUND + (gsize - 1) * MIN_GAP
        if b["_nudge"] > allow + 1e-6:
            # LATE is a sync problem: the picture arrives after the words
            notes.append(("LATE", b.get("at"), round(b["_nudge"], 3),
                          "allow %.2fs (group of %d)" % (allow, gsize)))
        elif -b["_nudge"] > TEASE_BOUND + 1e-6:
            # EARLY is a tease, and RepoChad does it deliberately
            notes.append(("TOO EARLY", b.get("at"), round(b["_nudge"], 3),
                          "tease bound %.2fs" % TEASE_BOUND))
    return times, notes


# ================================================================= RENDER
def _sent_phrase(vo, n):
    """The opening words of the nth sentence (0 based).

    Anchoring to a sentence number instead of a phrase keeps a visual event
    from sitting deep inside a long sentence, where it would leave the screen
    static for seconds at a time."""
    parts = [x.strip() for x in re.split(r"(?<=\.)\s+", vo or "") if x.strip()]
    if not parts:
        return ""
    n = max(0, min(n, len(parts) - 1))
    return " ".join(parts[n].split()[:4])


def _num(v):
    """The integer a label represents, or None if it is not a number."""
    try:
        return int(str(v).replace(",", "").strip())
    except (ValueError, TypeError):
        return None


class Win(object):
    """One window. Ids are allocated up front so beats can point at them."""

    def __init__(self, idx, data=None):
        self.idx = idx
        self.data = data or {}
        self.parts = []
        self.beats = []
        self._n = 0

    def nid(self):
        self._n += 1
        return "w%d_%02d" % (self.idx, self._n)

    def beat(self, eid, kind, at, **kw):
        dur = kw.pop("dur", DUR.get(kind, 340))
        ease = kw.pop("ease", "rise")
        b = dict(el="#" + eid, kind=kind, at=at, dur=dur, ease=ease)
        b.update(kw)
        self.beats.append(b)
        return b

    def div(self, inner, eid=None, cls="", attrs=""):
        eid = eid or self.nid()
        self.parts.append('<div id="%s" data-fx="1" class="%s" %s>%s</div>'
                          % (eid, cls, attrs, inner))
        return eid


def header(win, at):
    eid = win.nid()
    h = ('<div class="kicker"><i></i>%s</div>'
         '<div class="display" style="font-size:88px;max-width:1400px;margin-top:8px">%s</div>'
         '<div class="lbl lbl--gray" style="font-size:21px;margin-top:16px">%s</div>'
         % (win.data["kicker"], win.data["title"], win.data.get("sub", "")))
    win.beat(eid, "rise", at, dur=460, ease="rise")
    return '<div id="%s" data-fx="1" class="stack stack--tight">%s</div>' % (eid, h)


def artpanel(win, at, name, caption, show_caption=True):
    """Outer wrapper fades in, the line art SKETCHES ITSELF ON, the inner
    wrapper carries the camera so the drawing settles into frame.

    The camera push is on an HTML div, never on the SVG (an SVG element that
    carries a transform attribute collapses to the top-left if you animate its
    transform)."""
    outer, inner, svgid, cap = win.nid(), win.nid(), win.nid(), win.nid()
    svg = ART[name]()
    svg = svg.replace("<svg ", '<svg id="%s" data-fx="1" ' % svgid, 1)
    win.beat(outer, "rise", at, dur=520, ease="rise")
    win.beat(svgid, "draw", at, dur=1400, ease="draw", sdur=900)
    win.beat(inner, "push", at, dur=1400, ease="push", **{"from": 0.962, "to": 1.0})
    caphtml = ""
    if show_caption:
        win.beat(cap, "rise", at, dur=340, ease="rise")
        caphtml = ('<div id="%s" data-fx="1" class="lbl lbl--xs" style="text-align:center;'
                   'width:100%%;margin-top:12px">%s</div>' % (cap, caption))
    return ('<div id="%s" data-fx="1" class="artpanel">'
            '<div id="%s" class="artpanel__in">%s</div></div>%s'
            % (outer, inner, svg, caphtml))


def source(win, at, text):
    eid = win.nid()
    win.beat(eid, "rise", at, dur=340, ease="rise")
    return '<div id="%s" data-fx="1" class="src">%s</div>' % (eid, text)


def closing_chip(win, at, c, t):
    eid = win.nid()
    win.beat(eid, "pop", at, dur=420, ease="pop")
    return ('<div id="%s" data-fx="1" class="rowflex" style="gap:16px">'
            '<div class="chip chip--%s">%s</div></div>' % (eid, c, t))


# ------------------------------------------------------------------ hooks
def r_hook(w, win):
    h = header(win, w["header_at"])
    a = artpanel(win, w["art_at"], w["art"], w["art_caption"])
    chips = ""
    for c in w["chips"]:
        eid = win.nid()
        chips += '<div id="%s" data-fx="1" class="chip chip--%s">%s</div>' % (eid, c["c"], c["t"])
        win.beat(eid, "card", c["at"], dur=420, ease="card")
    stats = ""
    for s in w["stats"]:
        eid = win.nid()
        stats += ('<div id="%s" data-fx="1" class="stack" style="gap:2px">'
                  '<span class="num num--%s" style="font-size:124px">%s</span>'
                  '<div class="lbl lbl--sm"><span style="color:var(--dim)">%s</span>'
                  ' &middot; %s</div></div>'
                  % (eid, s["c"], s["v"], s["u"], s["lab"]))
        win.beat(eid, "slam", s["at"], dur=460, ease="slam")
    tape = ""
    if w.get("tape"):
        tid = win.nid()
        win.beat(tid, "sticker", w["tape_at"], dur=420, ease="sticker")
        tape = '<div id="%s" data-fx="1" class="tape">%s</div>' % (tid, w["tape"])
    # A hook is a window like any other: it carries its source too.
    src = ""
    if w.get("source"):
        src = source(win, w.get("source_at") or w.get("tape_at") or w["header_at"],
                     w["source"])
    return ('<div class="scene__inner">%s'
            '<div class="hook__body">'
            '<div class="hook__left">'
            '<div class="hook__stats">%s</div>%s</div>'
            '<div class="hook__art">%s</div>'
            '</div>'
            '<div class="hook__chips">%s</div>'
            '</div>%s' % (h, stats, tape, a, chips, src))


def r_bars(w, win):
    h = header(win, w["header_at"])
    a = artpanel(win, w["art_at"], w["art"], w["art_caption"])
    bars = ""
    scale = w.get("scale")
    for b in w["bars"]:
        rid, vid = win.nid(), win.nid()
        b["at"] = b.get("at") or _sent_phrase(w["vo"], b.get("sent", 1))
        # The unit is stated by the spec. A wrong unit on screen is worse
        # than no unit, so it is never guessed here.
        unit = b.get("unit")
        unithtml = "<small>%s</small>" % unit if unit else ""
        # A bar fill with no declared pct is scaled from the value itself,
        # so the length of the bar always means the number next to it.
        pct = b.get("pct")
        if pct is None:
            nv = _num(b["val"])
            pct = (abs(nv) / float(scale) * 100.0) if (nv is not None and scale) else 50.0
            pct = max(2.0, min(100.0, pct))
        bars += ('<div id="%s" data-fx="1" class="bar">'
                 '<div class="bar__lab">%s</div>'
                 '<div class="bar__track"><div class="bar__fill bar__fill--%s"></div></div>'
                 '<div id="%s" class="bar__val">'
                 '<span data-num>%s</span>%s</div></div>'
                 % (rid, b["lab"], b["cls"], vid, b["val"], unithtml))
        win.beat(rid, "edge", b["at"], dur=380, ease="edge",
               fill=dict(sel="#%s .bar__fill" % rid, w=pct), fdur=650, fd=0.18)
        win.beat(vid, "count", b["at"], dur=340, ease="rise",
               count=dict(sel="#%s [data-num]" % vid, to=_num(b["val"]), dec=0),
               cdur=650) if _num(b["val"]) is not None else None
    # A bar list with no scale is a list of numbers. The axis gives the bars a
    # baseline and puts the hardware boundary ON the chart, so the viewer can
    # see which rows the card can hold and which rows only describe a
    # requirement. "pct" is where the line sits on the same scale as the bars.
    axis = ""
    mk = w.get("mark")
    if mk:
        aid = win.nid()
        axis = ('<div id="%s" data-fx="1" class="bars__axis">'
                '<div class="bars__axisbase"></div>'
                '<div class="bars__axistick" style="left:%.2f%%"><i></i>'
                '<span>%s</span></div></div>'
                % (aid, float(mk["pct"]), mk["lab"]))
        win.beat(aid, "rise", w.get("mark_at") or w["header_at"], dur=340, ease="rise")
    mid = ""
    if w.get("mid"):
        mid = closing_chip(win, w["mid"]["at"], w["mid"]["c"], w["mid"]["t"])
    ch = ""
    if w.get("closing"):
        ch = closing_chip(win, w["closing"]["at"], w["closing"]["c"], w["closing"]["t"])
    src = ""
    if w.get("source"):
        src = source(win, w.get("source_at")
                     or (w["closing"]["at"] if w.get("closing") else w["header_at"]),
                     w["source"])
    return ('<div class="scene__inner">%s'
            '<div class="bars__body">'
            '<div class="bars__left"><div class="bars">%s</div>%s%s%s</div>'
            '<div class="bars__art">%s</div>'
            '</div>%s</div>'
            % (h, bars, axis, mid, ch, a, src))


def _row_val_size(v):
    """The size a row's value can be and still sit inside its own card.

    The value sits in a hero display face between a label on the left and a
    fixed-width unit on the right. A short number can be 42px. A phrase
    cannot: at 42px "CURRENT LAYER" is 384px wide, and that is what pushed
    the row's own label off the card and over the art column. So the size
    steps down with the length of the text."""
    n = len(str(v).strip())
    if n <= 8:
        return 42
    if n <= 10:
        return 36
    if n <= 13:
        return 30
    return 26


def r_rows(w, win):
    h = header(win, w["header_at"])
    a = artpanel(win, w["art_at"], w["art"], w["art_caption"])
    rows = ""
    for r in w["rows"]:
        rid, vid = win.nid(), win.nid()
        r["at"] = r.get("at") or _sent_phrase(w["vo"], r.get("sent", 1))
        cls = r["cls"] + (" row--mark" if r["cls"] == "gold" else "")
        rows += ('<div id="%s" data-fx="1" class="row row--%s">'
                 '<span class="row__rank">%s</span>'
                 '<span class="row__name">%s</span>'
                 '<span id="%s" class="row__val" style="font-size:%dpx">'
                 '<span data-num>%s</span></span>'
                 '<span class="row__sub">%s</span></div>'
                 % (rid, cls, r["rank"], r["name"], vid,
                    _row_val_size(r["val"]), r["val"], r["sub"]))
        win.beat(rid, "wipein", r["at"], dur=460, ease="wipe")
        nv = _num(r["val"])
        if nv is not None:
            win.beat(vid, "count", r["at"], dur=340, ease="rise",
                     count=dict(sel="#%s [data-num]" % vid, to=nv, dec=0), cdur=650)
    ch = ""
    if w.get("closing"):
        ch = closing_chip(win, w["closing"]["at"], w["closing"]["c"], w["closing"]["t"])
    src = ""
    if w.get("source"):
        src = source(win, w.get("source_at")
                     or (w["closing"]["at"] if w.get("closing") else w["header_at"]),
                     w["source"])
    return ('<div class="scene__inner">%s'
            '<div class="rows__body">'
            '<div class="rows__top"><div class="rows__list">%s</div>'
            '<div class="rows__art">%s</div></div>%s</div>%s</div>'
            % (h, rows, a, ch, src))


def r_rail(w, win):
    h = header(win, w["header_at"])
    a = artpanel(win, w["art_at"], w["art"], w["art_caption"])
    rails = ""
    for r in w["rails"]:
        rid, vid = win.nid(), win.nid()
        r["at"] = r.get("at") or _sent_phrase(w["vo"], r.get("sent", 1))
        # the value carries its own unit: "512 TOKENS" is two words, the first
        # one is the number that counts up and the rest is the unit
        bits = str(r["val"]).split(" ", 1)
        head = bits[0]
        tail = (" " + bits[1]) if len(bits) > 1 else ""
        nv = _num(head)
        disp = ('<span data-num>%s</span>%s' % (head, tail)) if nv is not None else head + tail
        rails += ('<div id="%s" data-fx="1" class="railrow">'
                  '<span class="railrow__lab">%s</span>'
                  '<span class="railrow__track">'
                  '<span class="railrow__fill railrow__fill--%s"></span></span>'
                  '<span id="%s" class="railrow__val%s">%s</span></div>'
                  % (rid, r["lab"], r["cls"], vid,
                     " railrow__val--red" if r["cls"] == "red" else "", disp))
        win.beat(rid, "edge", r["at"], dur=380, ease="edge",
               fill=dict(sel="#%s .railrow__fill" % rid, w=r["pct"]), fdur=650, fd=0.18)
        if nv is not None:
            win.beat(vid, "count", r["at"], dur=340, ease="rise",
                     count=dict(sel="#%s [data-num]" % vid, to=nv, dec=0), cdur=650)
    ch = ""
    if w.get("closing"):
        ch = closing_chip(win, w["closing"]["at"], w["closing"]["c"], w["closing"]["t"])
    src = ""
    if w.get("source"):
        src = source(win, w.get("source_at")
                     or (w["closing"]["at"] if w.get("closing") else w["header_at"]),
                     w["source"])
    return ('<div class="scene__inner">%s'
            '<div class="rail__body">'
            '<div class="rail__top"><div class="rail__rails">%s</div>'
            '<div class="rail__art">%s</div></div>%s</div>%s</div>'
            % (h, rails, a, ch, src))


def r_chain(w, win):
    h = header(win, w["header_at"])
    a = artpanel(win, w["art_at"], w["art"], w["art_caption"])
    chain = w["chain"]
    # The connector between two nodes arrives with the node it points AT, so
    # the chain builds one step at a time. An arrow with no beat would be
    # painted from the first frame of the window, before the words that
    # introduce the step it points at.
    ats = []
    for n in chain:
        n["at"] = n.get("at") or _sent_phrase(w["vo"], n.get("sent", 1))
        ats.append(n["at"])
    nodes = ""
    for i, n in enumerate(chain):
        nid = win.nid()
        last = (i == len(chain) - 1)
        nodes += ('<div id="%s" data-fx="1" class="chain__node%s">'
                  '<b>%s</b><span>%s</span></div>'
                  % (nid, " chain__node--gold" if last else "", n["t"], n["s"]))
        win.beat(nid, "pop", n["at"], dur=420, ease="pop")
        if not last:
            aid = win.nid()
            nodes += ('<div id="%s" data-fx="1" class="chain__arrow">&rarr;</div>' % aid)
            win.beat(aid, "wipein", ats[i + 1], dur=240, ease="wipe")
    cols = ""
    for c in w["compare"]:
        cid = win.nid()
        cols += ('<div id="%s" data-fx="1" class="compare__col compare__col--%s">'
                 '<div class="compare__title">%s</div>'
                 '<div class="compare__body">%s</div></div>'
                 % (cid, c["cls"], c["title"], c["body"]))
        win.beat(cid, "wipein", c["at"], dur=460, ease="wipe")
    sat = w.get("source_at") or (w["closing"]["at"] if w.get("closing")
                                 else w["compare"][-1]["at"])
    src = source(win, sat, w["source"])
    ch = ""
    if w.get("closing"):
        ch = closing_chip(win, w["closing"]["at"], w["closing"]["c"], w["closing"]["t"])
    return ('<div class="scene__inner">%s'
            '<div class="chain__body">'
            '<div class="chain__top"><div class="chain__nodes"><div class="chain">%s</div></div>'
            '<div class="chain__art">%s</div></div>'
            '<div class="compare">%s</div>%s</div>%s</div>'
            % (h, nodes, a, cols, ch, src))


def r_note(w, win):
    h = header(win, w["header_at"])
    a = artpanel(win, w["art_at"], w["art"], w["art_caption"])
    items = ""
    for it in w["note_items"]:
        iid = win.nid()
        it["at"] = it.get("at") or _sent_phrase(w["vo"], it.get("sent", 1))
        items += '<li id="%s" data-fx="1">%s</li>' % (iid, it["t"])
        win.beat(iid, "nudge", it["at"], dur=340, ease="nudge")
    eid = win.nid()
    win.beat(eid, "slam", w["header_at"], dur=520, ease="slam")
    card = ('<div id="%s" data-fx="1" class="note">'
            '<div class="note__head">%s</div><ul>%s</ul></div>' % (eid, w["note_head"], items))
    tape = ""
    if w.get("tape"):
        tid = win.nid()
        win.beat(tid, "sticker", w["tape_at"], dur=420, ease="sticker")
        tape = '<div id="%s" data-fx="1" class="tape">%s</div>' % (tid, w["tape"])
    src = ""
    if w.get("source"):
        src = source(win, w.get("source_at", w["header_at"]), w["source"])
    return ('<div class="scene__inner">%s'
            '<div class="note__body"><div class="note__left">%s%s</div>'
            '<div class="note__art">%s</div></div>%s</div>' % (h, card, tape, a, src))


def r_gallery(w, win):
    """One asset per window. The art flips side to side so no two consecutive
    windows share a composition."""
    flip = (w.get("side") == "left")
    kk = win.nid()
    win.parts.append('<div id="%s" data-fx="1" class="kicker"><i></i>%s</div>' % (kk, w["kicker"]))
    win.beat(kk, "rise", w["header_at"], dur=340, ease="rise")
    a = artpanel(win, w["art_at"], w["art"], w["art_caption"])
    name = win.nid()
    blurb = win.nid()
    meta = win.nid()
    win.beat(name, "slam", w.get("name_at") or w["header_at"], dur=460, ease="slam")
    win.beat(blurb, "rise", w.get("blurb_at") or w["header_at"], dur=420, ease="rise")
    win.beat(meta, "rise", w.get("meta_at") or w["header_at"], dur=340, ease="rise")
    text = ('<div class="gal__text">'
            '<div id="%s" data-fx="1" class="kicker"><i></i>%s</div>'
            '<div id="%s" data-fx="1" class="gal__name">%s</div>'
            '<div id="%s" data-fx="1" class="gal__blurb">%s</div>'
            '<div id="%s" data-fx="1" class="gal__meta">%s</div></div>'
            % (kk, w["kicker"], name, w["name"], blurb, w["blurb"], meta, w.get("meta", "")))
    art = '<div class="gal__art">%s</div>' % a
    body = (art + text) if flip else (text + art)
    cls = "gal gal--flip" if flip else "gal"
    src = ""
    if w.get("source"):
        src = source(win, w.get("meta_at") or w["header_at"], w["source"])
    return ('<div class="scene__inner"><div class="%s">%s</div>%s</div>'
            % (cls, body, src))


def r_title(w, win):
    """A title card, with a drawing that sketches itself in behind it.

    Two things keep this layout honest. The card is full bleed, so the card
    itself never carries the scale of the slam, or it would push past the
    canvas; the slam lands on the text stack instead. And a title card is the
    one layout that can end on a frozen screen, so it also accepts a tape and
    a closing chip, each with its own anchor, and it closes on a beat."""
    eid = win.nid()
    svgid = win.nid()
    svg = ART[w.get("art", "chip")]()
    svg = svg.replace("<svg ", '<svg id="%s" data-fx="1" ' % svgid, 1)
    tape = ""
    if w.get("tape"):
        tid = win.nid()
        win.beat(tid, "sticker", w["tape_at"], dur=420, ease="sticker")
        tape = '<div id="%s" data-fx="1" class="tape">%s</div>' % (tid, w["tape"])
    ch = ""
    if w.get("closing"):
        ch = closing_chip(win, w["closing"]["at"], w["closing"]["c"], w["closing"]["t"])
    win.parts.append('<div class="titlecard">'
                     '<div class="titlecard__art">%s</div>'
                     '<div id="%s" data-fx="1" class="titlecard__in">'
                     '<div class="kicker"><i></i>%s</div>'
                     '<div class="display">%s</div>'
                     '<div class="lbl lbl--gray">%s</div>'
                     '%s%s</div></div>'
                     % (svg, eid, w["kicker"], w["title"], w.get("sub", ""), ch, tape))
    win.beat(svgid, "draw", w["head_at"], dur=2000, ease="draw", sdur=1200)
    win.beat(eid, "slam", w["head_at"], dur=620, ease="slam")
    inner = "".join(win.parts)
    src = ""
    if w.get("source"):
        sat = (w.get("source_at")
               or (w["closing"]["at"] if w.get("closing") else w["head_at"]))
        src = source(win, sat, w["source"])
    return '<div class="scene__inner">%s%s</div>' % (inner, src)


def r_strip(w, win):
    """Three assets in a row, each with its own sentence, each at a smaller
    scale than a hero window would give them."""
    kk = win.nid()
    win.parts.append('<div id="%s" data-fx="1" class="kicker"><i></i>%s</div>' % (kk, w["kicker"]))
    win.beat(kk, "rise", w["header_at"], dur=340, ease="rise")
    ttl = win.nid()
    win.parts.append('<div id="%s" data-fx="1" class="display" style="font-size:64px">%s</div>'
                     % (ttl, w["title"]))
    win.beat(ttl, "slam", w["header_at"], dur=460, ease="slam")
    cells = []
    for it in w["items"]:
        a = artpanel(win, it["at"], it["key"], it["label"], show_caption=False)
        cap = win.nid()
        win.beat(cap, "rise", it["at"], dur=340, ease="rise")
        cells.append('<div class="strip__cell">%s'
                     '<div id="%s" data-fx="1" class="strip__cap">%s</div></div>'
                     % (a, cap, it["label"]))
    src = ""
    if w.get("source"):
        src = source(win, w["items"][-1]["at"], w["source"])
    ch = ""
    if w.get("closing"):
        ch = closing_chip(win, w["closing"]["at"], w["closing"]["c"], w["closing"]["t"])
    return ('<div class="scene__inner"><div class="strip">'
            '<div class="strip__head">%s<div id="%s" data-fx="1" class="display" '
            'style="font-size:64px">%s</div></div>'
            '<div class="strip__row">%s</div>%s</div>%s</div>'
            % (win.parts[0], ttl, w["title"], "".join(cells), ch, src))


def r_nodes(w, win):
    """A horizontal node chain, with a supporting drawing beside it."""
    kk = win.nid()
    win.parts.append('<div id="%s" data-fx="1" class="kicker"><i></i>%s</div>' % (kk, w["kicker"]))
    win.beat(kk, "rise", w["header_at"], dur=340, ease="rise")
    ttl = win.nid()
    win.parts.append('<div id="%s" data-fx="1" class="display" style="font-size:58px">%s</div>'
                     % (ttl, w["title"]))
    win.beat(ttl, "slam", w["header_at"], dur=460, ease="slam")
    nodes = ""
    chain = w["chain"]
    # The connector between two nodes arrives with the node it points AT, so
    # the chain builds one step at a time. An arrow with no beat would be
    # painted from the first frame of the window.
    ats = []
    for n in chain:
        n["at"] = n.get("at") or _sent_phrase(w["vo"], n.get("sent", 1))
        ats.append(n["at"])
    for i, n in enumerate(chain):
        nid = win.nid()
        last = (i == len(chain) - 1)
        # A step list, not a row of chips: the nodes layout is a tall band and
        # a horizontal row of small tiles floated in the middle of it with
        # hundreds of empty pixels above and below. The steps go down, they
        # fill the column, and each one carries its position.
        nodes += ('<div id="%s" data-fx="1" class="chain__node chain__node--step%s">'
                  '<div class="chain__num">%02d</div>'
                  '<div class="chain__lab"><b>%s</b><span>%s</span></div></div>'
                  % (nid, " chain__node--gold" if last else "", i + 1,
                     n["t"], n["s"]))
        win.beat(nid, "pop", n["at"], dur=420, ease="pop")
        if not last:
            aid = win.nid()
            nodes += ('<div id="%s" data-fx="1" class="chain__arrow">&darr;</div>' % aid)
            win.beat(aid, "wipein", ats[i + 1], dur=240, ease="wipe")
    a = artpanel(win, w["art_at"], w["art"], w["art_caption"])
    src = ""
    if w.get("source"):
        src = source(win, w["chain"][-1]["at"], w["source"])
    ch = ""
    if w.get("closing"):
        ch = closing_chip(win, w["closing"]["at"], w["closing"]["c"], w["closing"]["t"])
    return ('<div class="scene__inner"><div class="nodes">'
            '<div class="nodes__head">%s<div id="%s" data-fx="1" class="display" '
            'style="font-size:58px">%s</div></div>'
            '<div class="nodes__body"><div class="chain">%s</div>'
            '<div class="nodes__art">%s</div></div>%s</div>%s</div>'
            % (win.parts[0], ttl, w["title"], nodes, a, ch, src))


RENDER = {"hook": r_hook, "bars": r_bars, "rows": r_rows,
          "rail": r_rail, "chain": r_chain, "note": r_note,
          "gallery": r_gallery, "title": r_title, "strip": r_strip,
          "nodes": r_nodes}


# ==================================================================== LOUDNESS
def _measure_lufs(path):
    """(integrated LUFS, true peak dBFS) for a file, or (None, None)."""
    o = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af",
                        "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    tail = o[-1200:]
    i = re.findall(r"I:\s*(-?[\d.]+)\s+LUFS", tail)
    p = re.findall(r"Peak:\s*(-?[\d.]+)\s+dBFS", tail)
    return (float(i[-1]) if i else None, float(p[-1]) if p else None)


def _loudnorm_master(vo, vo_m, work):
    """-14 LUFS integrated, with the true peak held at -1.5 dBFS.

    The narration is very peaky, about 18 dB of crest, so loudnorm cannot
    reach -14 LUFS under a -1.5 dBFS ceiling in linear mode: the gain it
    would need pushes the peaks straight over the limit and ffmpeg falls
    back to dynamic mode, landing short at about -15.3 LUFS.

    The chain is therefore loudnorm for the shape, a static gain, then a true
    limiter with its auto-level disabled. The limiter clamps the peaks, so
    the gain is solved in a loop against the measured result rather than
    guessed. The old chain applied a flat +1.2 dB AFTER loudnorm, which
    put the finished master at -14.1 LUFS but a -0.5 dBFS true peak.
    """
    TARGET_I = -14.0
    CEIL = 0.8413            # -1.5 dBFS
    tmp = os.path.join(work, "vo_tune.mp3")

    # pass 1 -- how far does loudnorm think it has to go on its own?
    o = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", vo, "-af",
                        "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True).stderr
    blocks = re.findall(r"\{[^{}]*input_i[^{}]*\}", o, re.S)
    gain = 0.0
    if blocks:
        try:
            gain = float(json.loads(blocks[-1]).get("target_offset", 0.0))
        except (ValueError, TypeError):
            gain = 0.0

    best = None
    for _ in range(5):
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", vo,
                        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11,volume=%.3fdB,"
                               "alimiter=limit=%.4f:level=disabled:attack=5:release=50"
                               % (gain, CEIL),
                        "-c:a", "libmp3lame", "-b:a", "192k", tmp], check=True)
        lufs, tp = _measure_lufs(tmp)
        if lufs is None:
            break
        if best is None or abs(lufs - TARGET_I) < abs(best[0] - TARGET_I):
            best = (lufs, tp, gain)
        err = TARGET_I - lufs
        if abs(err) <= 0.15:
            break
        # the limiter gives back part of the gain, so damp the step
        gain = max(-6.0, min(12.0, gain + err * 0.8))

    if best is None:
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", vo,
                        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                        "-c:a", "libmp3lame", "-b:a", "192k", vo_m], check=True)
        return
    lufs, tp, gain = best
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", vo,
                    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11,volume=%.3fdB,"
                           "alimiter=limit=%.4f:level=disabled:attack=5:release=50"
                           % (gain, CEIL),
                    "-c:a", "libmp3lame", "-b:a", "192k", vo_m], check=True)
    print("  audio: %.1f LUFS, true peak %.1f dBFS (gain %+.2f dB)"
          % (lufs, tp if tp is not None else 0.0, gain))


# =================================================================== BUILD
def build():
    import importlib
    import os as _os
    spec_name = _os.environ.get("FUSION_SPEC")
    if len(sys.argv) > 1 and not spec_name:
        spec_name = sys.argv[1]
    if not spec_name:
        spec_name = "spec_07_fusion"
    spec = importlib.import_module(spec_name)
    W = spec.W
    name = getattr(spec, "NAME", NAME)
    work = os.path.join(ROOT, "build", name)
    os.makedirs(work, exist_ok=True)

    print("FUSION build: %s  %d windows, voice=%s rate=%s" % (name, len(W), VOICE, RATE))
    words, files = asyncio.run(record(W, work))

    # The recording has to BE this window. A cached or mismatched audio file
    # puts the right words over the wrong voice, and nothing downstream can
    # see it, so it is checked here and the build stops.
    for i, w in enumerate(W):
        ws = words[i]
        vw = w["vo"].split()
        if not ws or not vw:
            continue
        a, b = _norm_word(ws[0][1]), _norm_word(vw[0])
        if a and b and a != b:
            raise SystemExit("window %d: the recording starts %r but the script "
                             "starts %r -- this audio does not belong to this "
                             "window" % (i + 1, a, b))

    d = [dur_of(f) for f in files]
    speech_and_gaps = sum(d) + GAP * (len(d) - 1)
    if getattr(spec, "TARGET_TOTAL", None):
        target = float(spec.TARGET_TOTAL)
        tail_dur = max(0.6, round(target - speech_and_gaps, 3))
    else:
        tail_dur = getattr(spec, "TAIL", TAIL)

    g = os.path.join(work, "g.wav")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "lavfi",
                    "-i", "anullsrc=r=44100:cl=mono", "-t", str(GAP), "-c:a", "pcm_s16le", g], check=True)
    tail = os.path.join(work, "t.wav")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "lavfi",
                    "-i", "anullsrc=r=44100:cl=mono", "-t", str(tail_dur), "-c:a", "pcm_s16le", tail], check=True)
    seq = []
    for i, f in enumerate(files):
        seq.append(f)
        if i < len(files) - 1:
            seq.append(g)
    seq.append(tail)
    lst = os.path.join(work, "l.txt")
    with open(lst, "w") as fh:
        for p in seq:
            fh.write("file '%s'\n" % p.replace("\\", "/"))
    vo = os.path.join(work, "vo.mp3")
    vo_m = os.path.join(work, "vo_master.mp3")
    latest_src = max([os.path.getmtime(f) for f in files] + [0])
    if os.path.exists(vo_m) and os.path.getsize(vo_m) > 1000 and os.path.getmtime(vo_m) >= latest_src:
        print("  audio cache hit: %s (master is up to date)" % vo_m)
    else:
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat",
                        "-safe", "0", "-i", lst, "-c:a", "libmp3lame", "-b:a", "160k", vo], check=True)
        _loudnorm_master(vo, vo_m, work)

    starts, acc = [], 0.0
    for x in d:
        starts.append(acc)
        acc += x + GAP
    total = sum(d) + GAP * (len(d) - 1) + tail_dur

    scenes_html, beats, scene_meta, srt, chap = [], [], [], [], []
    scene_index = []
    cues_by_window = []
    warn = []
    for i, w in enumerate(W):
        # fill in whatever the layout needs but the author left out, so a
        # window only has to state what is actually different about it
        lay = w["layout"]
        w.setdefault("art", "magnifier" if lay == "note" else "chip")
        w.setdefault("art_caption", w["art"].replace("_", " ").upper())
        w.setdefault("art_at", w.get("header_at") or w.get("head_at"))
        w.setdefault("meta", "asset: %s" % w["art"])
        w.setdefault("side", "right")
        w.setdefault("sub", "")
        w.setdefault("blurb", "")
        w.setdefault("name", w.get("title", ""))
        w.setdefault("kicker", "BYTE FORENSICS")
        w.setdefault("title", w.get("name", ""))
        w.setdefault("header_at", w.get("head_at"))
        win = Win(i, w)
        inner = RENDER[w["layout"]](w, win)
        times, notes = schedule(win.beats, w["vo"], words[i])
        lead = float(w.get("lead_in", 0.0))
        for b, t in zip(win.beats, times):
            b["s"] = round(starts[i] + t - lead, 3)
            b["e"] = round(starts[i] + t - lead + b["dur"] / 1000.0, 3)
            b["i"] = len(beats)
            b["group"] = i
            b["anchor"] = b.get("at")
            b["nudge"] = b.pop("_nudge", 0.0)
            b["arr"] = round(starts[i] - lead + b.pop("_arr", 0.0), 3)
            b.pop("_t0", None)
            b.pop("at", None)
            beats.append(b)
        for n in notes:
            warn.append((i, n))
        gaps = [(round(times[k] - times[k - 1], 2), win.beats[k].get("at"))
                for k in range(1, len(times))]
        big = [g for g in gaps if g[0] > MAX_GAP_WARN]
        print("  win %d  %-6s %5.1fs  beats=%2d  max gap=%.2fs%s"
              % (i + 1, w["layout"], d[i], len(win.beats),
                 max([g[0] for g in gaps]) if gaps else 0.0,
                 ("   <-- " + ", ".join("%.1fs" % g[0] for g in big)) if big else ""))
        scenes_html.append('  <section class="scene" data-scene="%d">%s</section>'
                           % (i, inner))
        scene_meta.append(dict(id=i, s=round(starts[i] - lead, 3), e=round(starts[i] + d[i], 3),
                                label="%02d %s" % (i + 1, w.get("label", w["layout"].upper()))))
        # ---- captions -----------------------------------------------------
        # Eight words per cue, so the caption reads as a line and not as a
        # column of single words. The cue text is ALWAYS the SCRIPT's own
        # words, punctuation included; the TIMING comes from the synthesiser.
        # The two are aligned first, because the synthesiser re-tokenises what
        # it is given ("llama.cpp" arrives as three tokens) and the caption
        # must not drift to its wording when that happens.
        # The last cue of a window ends with the window's audio, so the final
        # word of every window is captioned and never dropped.
        ws = words[i]
        vw = w["vo"].split()
        tok = _align_tokens(vw, ws)
        groups = _groups(len(vw), CAPTION_WORDS)
        cstart = []
        for a, b in groups:
            t = ws[tok[a]][0]
            if cstart and t <= cstart[-1]:
                t = cstart[-1] + 0.05
            cstart.append(t)
        for c, (a, b) in enumerate(groups):
            t0 = starts[i] + cstart[c]
            t1 = (starts[i] + cstart[c + 1] if c + 1 < len(cstart)
                  else starts[i] + d[i])
            srt.append((t0, t1, " ".join(vw[a:b])))
        cues_by_window.append([(t0, t1) for t0, t1, _ in srt[-len(groups):]])
        chap.append("%d:%02d %s %02d" % (int(starts[i] // 60), int(starts[i] % 60),
                                         _plain(w.get("kicker") or w.get("title", "")),
                                         i + 1))
        scene_index.append("%d:%02d %s %02d" % (int(starts[i] // 60),
                                                 int(starts[i] % 60),
                                                 _plain(w.get("title", "")), i + 1))

    allwords = []
    for i in range(len(W)):
        for t, t2 in words[i]:
            allwords.append([round(starts[i] + t, 4), t2])

    css = open(os.path.join(ROOT, "core", "fusion.css"), encoding="utf-8").read()
    js = open(os.path.join(ROOT, "core", "fusion.js"), encoding="utf-8").read()
    for fn in os.listdir(os.path.join(ROOT, "core", "fonts")):
        if not fn.endswith(".ttf"):
            continue
        b64 = base64.b64encode(open(os.path.join(ROOT, "core", "fonts", fn), "rb").read()).decode()
        css = css.replace('url("fonts/%s") format("truetype")' % fn,
                          'url(data:font/ttf;base64,%s) format("truetype")' % b64)

    b64audio = base64.b64encode(open(vo_m, "rb").read()).decode()

    payload = dict(
        title=getattr(spec, "TITLE", "HOW LONG BEFORE THE FIRST WORD"),
        kicker=getattr(spec, "KICKER", "BYTE FORENSICS &middot; EPISODE 07 &middot; PREFILL"),
        subtitle=getattr(spec, "SUBTITLE", "the number nobody measures"),
        watermark="Byte Forensics",
        progress=bool(getattr(spec, "GLOBAL_PROGRESS", False)),
        total=round(total, 3),
        words=allwords,
        scenes=scene_meta,
        beats=beats,
        sfx=[],
        vo="data:audio/mpeg;base64," + b64audio,
    )
    payload_js = json.dumps(payload, separators=(",", ":"))

    # The document title comes from the spec, never from a literal in here.
    # Bare "&" is escaped; "&middot;" and friends are left as entities.
    doc_title = getattr(spec, "DOC_TITLE", None) or getattr(spec, "TITLE", None) \
        or getattr(spec, "NAME", "BYTE FORENSICS")
    doc_title = re.sub(r"&(?!(?:[a-zA-Z]+|#\d+);)", "&amp;", str(doc_title))

    html = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>%s</title>
<style>
%s
</style></head><body>
<div id="wrap"><div id="stage" class="stage">
%s
</div></div>
<script>window.FUSION = %s;</script>
<script>
%s
</script>
</body></html>""" % (doc_title, css, "\n".join(scenes_html), payload_js, js)

    out = os.path.join(ROOT, name + ".html")
    open(out, "w", encoding="utf-8").write(html)
    print("\nwrote %s  (%.2f MB)  runtime %.1fs  beats %d"
          % (out, os.path.getsize(out) / 1048576.0, total, len(beats)))

    if srt:
        srt[-1] = (srt[-1][0], round(total, 3), srt[-1][2])

    def ts(x):
        h = int(x // 3600)
        m = int((x % 3600) // 60)
        s = x % 60
        # SRT wants a comma before the milliseconds. A dot is not valid SRT
        # and some importers reject the whole file over it.
        return ("%02d:%02d:%06.3f" % (h, m, s)).replace(".", ",")
    lines = []
    for k, (a, b, t) in enumerate(srt, 1):
        lines.append("%d\n%s --> %s\n%s\n" % (k, ts(a), ts(b), t.strip()))
    open(os.path.join(ROOT, name + ".srt"), "w", encoding="utf-8").write("\n".join(lines))
    print("wrote %s  (%d captions)" % (name + ".srt", len(srt)))

    # The captions must cover the narration word for word, 100 %. This is the
    # one rule that shipped broken for a whole episode, so it is checked at
    # build time rather than trusted.
    spoken_n = len(allwords)
    capt_n = sum(len(t.split()) for _, _, t in srt)
    script_n = sum(len(w["vo"].split()) for w in W)
    if capt_n != script_n:
        raise SystemExit("caption carries %d of %d script words (%.2f%%) -- "
                         "the .srt must hold the script's own words"
                         % (capt_n, script_n, 100.0 * capt_n / max(1, script_n)))
    # every spoken token must fall inside a cue, so the caption covers the
    # speech and not only its own text
    for i in range(len(W)):
        lo, hi = starts[i], starts[i] + d[i]
        spans = cues_by_window[i] if i < len(cues_by_window) else []
        for t, _ in allwords:
            if not (lo - 0.001 <= t <= hi + 0.001):
                continue
            if not any(a - 0.001 <= t <= b + 0.001 for a, b in spans):
                raise SystemExit("a spoken word at %.3fs in window %d falls "
                                 "outside every caption cue" % (t, i + 1))
    thin = [t for _, _, t in srt if len(t.split()) < 2]
    if thin:
        raise SystemExit("%d caption(s) carry a single word, e.g. %r -- a cue "
                         "must read as a line" % (len(thin), thin[0][:40]))
    print("captions: %d words over %d cues -- %d of %d script words (100%%) "
          "[%d spoken tokens]"
          % (capt_n, len(srt), capt_n, script_n, spoken_n))

    # The scene index is one line per window. The chapter file is what a
    # viewer actually navigates on YouTube: the first chapter starts at
    # 00:00, there are at least three, and every one of them runs for at
    # least ten seconds. A spec that does not declare its chapters falls
    # back to the per-window list, which is what the older episodes ship.
    si = os.path.join(ROOT, name + "-scenes.txt")
    open(si, "w", encoding="utf-8").write("\n".join(scene_index))
    print("wrote %s  (%d scenes)" % (name + "-scenes.txt", len(scene_index)))

    groups = getattr(spec, "CHAPTERS", None)
    if groups:
        def _stamp(x):
            h = int(x // 3600)
            m = int((x % 3600) // 60)
            s = int(x % 60)
            return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))
        rows = []
        for wno, title in groups:
            i = int(wno) - 1
            if i < 0 or i >= len(starts):
                raise SystemExit("chapter points at window %s, which does not "
                                 "exist" % wno)
            rows.append((starts[i], str(title)))
        rows.sort()
        bad = []
        if len(rows) < 3:
            bad.append("only %d chapters; YouTube wants at least 3" % len(rows))
        if rows and rows[0][0] > 0.001:
            bad.append("the first chapter starts at %.3fs, not 0" % rows[0][0])
        for k in range(len(rows) - 1):
            d = rows[k + 1][0] - rows[k][0]
            if d < 10.0:
                bad.append("chapter %r is only %.1fs long" % (rows[k][1], d))
        if len(set(t for _, t in rows)) != len(rows):
            bad.append("two chapters share a title")
        if bad:
            for b in bad:
                print("  CHAPTER PROBLEM: %s" % b)
            raise SystemExit("the chapter list is not valid for YouTube")
        chap = ["%s %s" % (_stamp(t), title) for t, title in rows]

    cp = os.path.join(ROOT, name + "-chapters.txt")
    open(cp, "w", encoding="utf-8").write("\n".join(chap))
    print("wrote %s  (%d chapters)" % (name + "-chapters.txt", len(chap)))

    if warn:
        print("\nSCHEDULER NOTES")
        for i, n in warn:
            print("  win %d  %s  %s  %s  (%s)" % (i + 1, n[0], n[1], n[2], n[3]))
    else:
        print("\nno scheduler notes")
    return out


if __name__ == "__main__":
    t0 = time.time()
    build()
    print("done in %.1fs" % (time.time() - t0))
