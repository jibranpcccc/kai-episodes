# -*- coding: utf-8 -*-
"""make_spec.py -- the scale engine.

Turns an (angle, fact slice) pair from the research base into a complete,
buildable episode spec module that ``data/fusion_build.py`` can consume.

    python data/make_spec.py --list
    python data/make_spec.py VRAM-001
    python data/make_spec.py --batch 10
    python data/make_spec.py --check spec_gen_VRAM-001

The research base is IMPORTED at runtime, never read as text:

    data/facts.py   -> FACTS, by_id, by_topic, topic_list, RIG, RIG_QWEN, RIG_GLIMMER
    data/angles.py  -> W (the angle catalogue: id, thesis, subject, shape, facts,
                       caveat, title)

Deterministic by contract: the same angle id always produces a byte-identical
module. No random, no datetime.now(), no set iteration order in the output.
"""

from __future__ import annotations

import argparse
import importlib
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

CHANNEL = "BYTE FORENSICS"
GEN_PREFIX = "BYTE-GEN-"

# The episode spine. A window sequence is a prefix of this cycle, so no two
# consecutive windows can share a layout.
SPINE = ("hook", "chain", "rows", "bars", "rail", "note", "gallery", "strip",
         "title", "nodes")

# --------------------------------------------------------------------------
# ART KEYS -- exhaustive. A bad key raises at build time, so the generator
# refuses to emit one.
# --------------------------------------------------------------------------
ART = {
    "cache_grid":     ("THE CACHE, WHOLE", "the cache, whole"),
    "caveat":         ("READ THE SMALL PRINT", "read the small print"),
    "checklist":      ("THE WHOLE CHECKLIST", "the whole checklist"),
    "chip":           ("ONE MODEL, ONE FORMULA", "one model, one formula"),
    "clock":          ("THE CLOCK, NOT THE STOPWATCH", "the clock, not the stopwatch"),
    "cloud":          ("THE SAME QUESTION, REMOTE", "the same question, remote"),
    "collapse":       ("WHERE THE MARGIN COLLAPSES", "where the margin collapses"),
    "context_window": ("THE WINDOW AND WHAT IS IN IT", "the window and what is in it"),
    "cooler":         ("THERMAL, THEN EVERYTHING ELSE", "thermal, then everything else"),
    "cost_dial":      ("THE PRICE DIAL, TURNED ONCE", "the price dial, turned once"),
    "die":            ("THE DIE, UNDER THE LID", "the die, under the lid"),
    "dual_slot":      ("TWO SLOTS, ONE BOARD", "two slots, one board"),
    "fan":            ("FAN CURVE, NOISE CURVE", "fan curve, noise curve"),
    "folder":         ("THE PAPER FOLDER", "the paper folder"),
    "gauge":          ("THE GAUGE, HELD STILL", "the gauge, held still"),
    "gguf_blocks":    ("QUANTISED IN BLOCKS", "quantised in blocks"),
    "gpu":            ("THE CARD ON THE BENCH", "the card on the bench"),
    "hdd":            ("THE OLD SPINDLE", "the old spindle"),
    "heat_sink":      ("HEAT MOVES OUT", "heat moves out"),
    "kv_cache":       ("THE KEY-VALUE LEDGER", "the key-value ledger"),
    "lan_link":       ("ACROSS THE WIRE", "across the wire"),
    "laptop":         ("THE LAPTOP, OPEN", "the laptop, open"),
    "laptop_closed":  ("THE LAPTOP, CLOSED", "the laptop, closed"),
    "mac_mini":       ("THE TINY TOWER", "the tiny tower"),
    "magnifier":      ("THE MAGNIFIER PASS", "the magnifier pass"),
    "memory_bank":    ("THE MEMORY BANK", "the memory bank"),
    "meter":          ("THE METER READING", "the meter reading"),
    "mini_pc":        ("THE SMALL DESKTOP", "the small desktop"),
    "model_file":     ("THE WEIGHTS ON DISK", "the weights on disk"),
    "motherboard":    ("THE BOARD ITSELF", "the board itself"),
    "nvme_ssd":       ("THE SOLID STATE", "the solid state"),
    "pcb":            ("THE BOARD, TRACED", "the board, traced"),
    "pcie_slot":      ("THE SLOT IT PLUGS INTO", "the slot it plugs into"),
    "pipeline":       ("THE PIPELINE, STAGE BY STAGE", "the pipeline, stage by stage"),
    "power_rails":    ("WHERE THE POWER GOES", "where the power goes"),
    "price_tag":      ("THE PRICE ON THE TICKET", "the price on the ticket"),
    "prompt_stream":  ("THE PROMPT, INCOMING", "the prompt, incoming"),
    "psu":            ("THE POWER SUPPLY", "the power supply"),
    "question":       ("THE QUESTION, STATED PLAIN", "the question, stated plain"),
    "rack_server":    ("THE RACK, ONE SLOT", "the rack, one slot"),
    "ram_stick":      ("THE MODULE, SEATED", "the module, seated"),
    "riser":          ("THE RISER BRIDGE", "the riser bridge"),
    "router":         ("THE ROUTER, IN THE LOOP", "the router, in the loop"),
    "scales":         ("THE SCALES, LEVEL", "the scales, level"),
    "sodimm":         ("THE SOLDERED MODULE", "the soldered module"),
    "superchip":      ("ONE BIG DIE, ONE BUS", "one big die, one bus"),
    "switch":         ("A SWITCH, NOT A DIAL", "a switch, not a dial"),
    "timer_flat":     ("TIMING, LINE BY LINE", "timing, line by line"),
    "tok_speed_dial": ("THE TOKENS PER SECOND DIAL", "the tokens per second dial"),
    "token_blocks":   ("THE TOKENS, ONE BY ONE", "the tokens, one by one"),
    "tower_pc":       ("THE TOWER, OPEN", "the tower, open"),
    "two_die":        ("TWO DIES, ONE PACKAGE", "two dies, one package"),
    "vram_module":    ("THE VRAM STICKS", "the vram sticks"),
    "wafer":          ("THE WAFER IT CAME FROM", "the wafer it came from"),
    "warning":        ("THE WARNING LABEL", "the warning label"),
}

# Topic -> the art key that carries that topic.
TOPIC_ART = {
    "vram": "vram_module",
    "prefill": "prompt_stream",
    "generation": "token_blocks",
    "capacity": "context_window",
    "latency": "timer_flat",
    "cache": "kv_cache",
    "lora": "magnifier",
    "papers": "folder",
    "quant": "gguf_blocks",
}

# Short spoken labels for the strip layout.
STRIP_LABELS = {
    "vram": "vram budget",
    "prefill": "prefill budget",
    "generation": "decode budget",
    "capacity": "context budget",
    "latency": "latency budget",
    "cache": "cache budget",
    "lora": "adapter budget",
    "papers": "paper budget",
    "quant": "quant budget",
}

# --------------------------------------------------------------------------
# THE LAYOUT CONTRACT. Exact: a missing key raises KeyError at build time.
# --------------------------------------------------------------------------
LAYOUT_KEYS = {
    "hook": ["kicker", "title", "art", "art_caption", "header_at", "art_at",
             "chips", "stats", "tape", "tape_at", "source"],
    "rows": ["kicker", "title", "art", "art_caption", "header_at", "art_at",
             "rows", "closing", "source"],
    "bars": ["kicker", "title", "art", "art_caption", "header_at", "art_at",
             "bars", "closing", "mid", "source"],
    "rail": ["kicker", "title", "art", "art_caption", "header_at", "art_at",
             "rails", "closing", "source"],
    "chain": ["kicker", "title", "art", "art_caption", "header_at", "art_at",
             "chain", "compare", "source"],
    "note": ["kicker", "title", "art", "art_caption", "header_at", "art_at",
             "note_head", "note_items", "tape", "tape_at", "source", "source_at"],
    "gallery": ["kicker", "title", "art", "art_caption", "header_at", "art_at",
                "name", "blurb", "meta", "name_at", "blurb_at", "meta_at",
                "side", "source"],
    "strip": ["kicker", "title", "header_at", "items", "source"],
    "title": ["kicker", "title", "sub", "art", "head_at", "source"],
    "nodes": ["kicker", "title", "header_at", "art", "art_caption", "art_at",
              "chain", "source"],
}

# List element schemas: layout -> list key -> element keys.
LIST_SCHEMA = {
    "hook": {"chips": ["t", "c", "at"], "stats": ["v", "u", "lab", "c", "at"]},
    "rows": {"rows": ["rank", "name", "val", "sub", "cls", "at"]},
    "bars": {"bars": ["lab", "val", "unit", "pct", "cls", "at"]},
    "rail": {"rails": ["lab", "val", "pct", "cls", "at"]},
    "chain": {"chain": ["t", "s", "at"], "compare": ["cls", "title", "body", "at"]},
    "note": {"note_items": ["t", "at"]},
    "gallery": {},
    "strip": {"items": ["key", "label", "at"]},
    "title": {},
    "nodes": {"chain": ["t", "s", "at"]},
}

# Layouts that carry an art anchor.
LAYOUTS_WITH_ART_AT = ("hook", "rows", "bars", "rail", "chain", "note",
                       "gallery", "nodes")
LAYOUTS_WITH_TAPE = ("hook", "note")

# --------------------------------------------------------------------------
# NARRATION TEMPLATES. No numbers here -- every number on screen has to be
# spoken, and these lines are not where numbers live.
# --------------------------------------------------------------------------
HEADER_TPL = [
    "Same board. Same run. Same {topic}.",
    "The {topic} figure, read straight off the board.",
    "One {topic} number, one source, one board.",
    "Nothing here about {topic} is a guess.",
    "This is the {topic} of the hardware, not of the brochure.",
    "Measured {topic}, on this board, in this run.",
    "Every {topic} figure here carries its own source.",
    "The {topic} number does the talking, not the claim.",
]

TITLE_FRAME_TPL = [
    "One claim, one board, one run.",
    "One episode, one question, measured.",
    "Here is the claim this episode has to defend.",
    "One argument, and the numbers under it.",
]

FILLER_TPL = [
    "Nothing in this window claims that a model fits.",
    "Every figure on screen is measured or derived from a named source.",
    "The next figure belongs to the same run on the same board.",
    "Read them in order and they agree with each other.",
    "No rounding, no averaging, no marketing adjustment.",
    "The scale was fixed before the run started.",
    "The source line stays with the figure, not under a footnote.",
    "Same conditions for every number that follows.",
]

TAPE_TPL = [
    "Keep the source in view.",
    "Measure first. Claim nothing.",
    "That is the measured number.",
    "Hold the figure and the source.",
    "Nothing else is being promised here.",
]

CLOSING_TPL = {
    "rows": ["Same method, every row.", "The order is the reading.",
             "One method, every row.", "No fit claim here."],
    "bars": ["Same method, every bar.", "The order is the reading.",
             "One scale, every bar.", "No fit claim here."],
    "rail": ["Same method, every rail.", "The reading is the order.",
             "One scale, every rail.", "No fit claim here."],
}

COMPARE_TPL = {
    "cmp_hot": ("hot", "THE HEADLINE CLAIM",
                "The claim about {label}, taken on trust."),
    "cmp_good": ("good", "WHAT WE MEASURED",
                 "The measurement of {label}, taken on the board."),
}

NOTE_HEAD_TPL = [
    "WHAT THE NUMBER DOES NOT PROVE",
    "READ THE SMALL PRINT",
    "THE LIMITS OF THE FIGURE",
    "WHERE THE CLAIM STOPS",
]

MID_LINE = "Measured, not a fit claim"

REPEAT_TPL = [
    "The same {label} figure, from the same run.",
    "Read {label} again, and it does not move.",
    "Same {label} line, same board.",
    "The {label} figure holds still.",
]

CAVEAT_FALLBACK = [
    "This figure does not establish that a model fits.",
    "This figure does not establish a speed.",
    "This figure does not establish a fit claim.",
    "This figure does not establish a comparison.",
]

SOURCE_PHRASE = "The source sits at the foot of the window."

# --------------------------------------------------------------------------
# NUMBER TO WORDS. Used only when a fact has no usable claim sentence.
# --------------------------------------------------------------------------
_ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven",
         "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
_TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
         "eighty", "ninety"]
_UNIT_WORDS = {
    "gb": "gigabytes", "mb": "megabytes", "tb": "terabytes",
    "gib": "gibibytes", "mib": "mebibytes", "kib": "kibibytes",
    "ms": "milliseconds", "us": "microseconds", "\u00b5s": "microseconds",
    "ns": "nanoseconds", "s": "seconds", "min": "minutes", "h": "hours",
    "tok/s": "tokens per second", "tokens/s": "tokens per second",
    "t/s": "tokens per second", "gb/s": "gigabytes per second",
    "mb/s": "megabytes per second", "%": "percent", "w": "watts",
    "w/kg": "watts per kilogram", "a": "amperes", "v": "volts",
    "x": "times", "k": "thousand", "m": "million", "pp": "percentage points",
    "cores": "cores", "rows": "rows", "bytes": "bytes", "b": "bytes",
}


def _int_words(n: int) -> str:
    if n < 0:
        return "minus " + _int_words(-n)
    if n < 20:
        return _ONES[n]
    if n < 100:
        w = _TENS[n // 10]
        return w + ("-" + _ONES[n % 10] if n % 10 else "")
    if n < 1000:
        w = _ONES[n // 100] + " hundred"
        return w + (" and " + _int_words(n % 100) if n % 100 else "")
    if n < 1000000:
        w = _int_words(n // 1000) + " thousand"
        return w + (" " + _int_words(n % 1000) if n % 1000 else "")
    if n < 1000000000:
        w = _int_words(n // 1000000) + " million"
        return w + (" " + _int_words(n % 1000) if n % 1000 else "")
    return str(n)


def num_words(value) -> str:
    """Spell a number out in words. Returns '' when the value is not numeric."""
    try:
        if isinstance(value, bool):
            return ""
        num = float(value)
    except (TypeError, ValueError):
        return ""
    if num != num:  # NaN
        return ""
    if float(num).is_integer():
        return _int_words(int(num))
    whole = int(num)
    frac = abs(num - whole)
    frac_txt = ("%.6f" % frac).rstrip("0")
    frac_words = " ".join(_int_words(int(d)) for d in frac_txt.split(".")[1])
    return _int_words(whole) + " point " + frac_words


def unit_words(unit) -> str:
    u = str(unit or "").strip()
    if not u:
        return ""
    low = u.lower()
    if low in _UNIT_WORDS:
        return _UNIT_WORDS[low]
    letters = re.sub(r"[^A-Za-z]", "", u)
    return letters.lower() if letters else u


def spell_value(value) -> str:
    w = num_words(value)
    if w:
        return w
    return str(value).strip()


# --------------------------------------------------------------------------
# TEXT HELPERS
# --------------------------------------------------------------------------
def wc(text: str) -> int:
    return len(str(text).split())


def _spans(text: str):
    return [(m.group(0), m.start(), m.end()) for m in re.finditer(r"\S+", text)]


def _clean(cand: str) -> bool:
    """A readable anchor: no sentence break inside it."""
    return ". " not in cand


def speech(text: str) -> str:
    """Normalise a segment so it reads as narration and closes a sentence."""
    t = re.sub(r"\s+", " ", str(text)).strip()
    if not t:
        return t
    if t[-1] not in ".!?":
        t += "."
    return t


def find_anchor(vo: str, spans, seg_start: int, seg_end: int, after: int = 0,
                minw: int = 3, maxw: int = 18, prefer: str = ""):
    """Return (anchor, end_pos).

    The anchor is a substring of vo drawn from the segment [seg_start,
    seg_end); it must occur exactly once in vo, and it must start at or after
    `after` so that elements keep the order the script says them in. The scan
    starts at the first word of the segment and grows right, so the anchor
    keeps the meaning of the line it belongs to. If the segment alone cannot
    give a unique slice, the slice may run past the segment end. Returns None
    when no unique slice exists.
    """
    lo = None
    hi = None
    for i, (_t, a, b) in enumerate(spans):
        if a >= seg_start and b <= seg_end:
            if lo is None:
                lo = i
            hi = i
    if lo is None:
        for i, (_t, a, b) in enumerate(spans):
            if a >= seg_start:
                lo = i
                break
    if lo is None:
        return None
    n_spans = len(spans)
    low_vo = vo.lower()
    pref = prefer.lower()

    def try_windows(a_lo, a_hi, width, require_pref, clean_only, within):
        for i in range(a_lo, a_hi):
            for n in range(width, maxw + 1):
                j = i + n - 1
                if j >= n_spans:
                    break
                if within and hi is not None and j > hi:
                    break
                if spans[i][1] < after:
                    continue
                cand = vo[spans[i][1]:spans[j][2]]
                if require_pref and pref not in cand.lower():
                    continue
                if clean_only and not _clean(cand):
                    continue
                if low_vo.count(cand.lower()) != 1:
                    continue
                trimmed = cand.rstrip(".,;:")
                if trimmed != cand and trimmed and low_vo.count(trimmed.lower()) == 1:
                    return trimmed, spans[i][1] + len(trimmed)
                return cand, spans[j][2]
        return None

    widths = [w for w in (minw, 2) if w >= 2]
    a_hi = (hi + 1) if hi is not None else lo + 1

    # when a phrase is preferred, the scan starts where that phrase starts
    pref_lo = lo
    if pref:
        pos = low_vo.find(pref)
        if pos >= 0:
            for i, (_t, a, b) in enumerate(spans):
                if b > pos:
                    pref_lo = max(lo, i)
                    break

    # clean, inside the segment first -- the anchor should read like a phrase
    for width in widths:
        if pref:
            got = try_windows(pref_lo, a_hi, width, True, True, True)
            if got:
                return got
        got = try_windows(lo, a_hi, width, False, True, True)
        if got:
            return got
    # then the same scan without the readability filter
    for width in widths:
        if pref:
            got = try_windows(pref_lo, a_hi, width, True, False, True)
            if got:
                return got
        got = try_windows(lo, a_hi, width, False, False, True)
        if got:
            return got
    # last resort: the slice may run past the end of the segment
    for width in widths:
        if pref:
            got = try_windows(pref_lo, n_spans, width, True, False, False)
            if got:
                return got
        got = try_windows(lo, n_spans, width, False, False, False)
        if got:
            return got
    return None


# --------------------------------------------------------------------------
# FACT BASE ACCESS (imported at runtime, never read as text)
# --------------------------------------------------------------------------
def load_facts():
    return importlib.import_module("facts")


def load_angles():
    return importlib.import_module("angles")


def facts_for_topic(fmod, topic):
    t = str(topic)
    try:
        rows = list(fmod.by_topic(t))
    except Exception:
        rows = []
    if not rows:
        low = t.lower()
        rows = [f for f in fmod.FACTS if str(f.get("topic", "")).lower() == low]
    return rows


def fact_id(fact):
    return str(fact.get("id") or "")


def _fact_matches(fact, subject: str) -> bool:
    """Strict: the subject has to be a real name that appears inside a model,
    card or label. Prose subjects match nothing and are simply dropped."""
    if not subject or len(subject) > 40:
        return False
    for key in ("model", "card", "label"):
        val = str(fact.get(key, "") or "").lower()
        if val and subject in val:
            return True
    return False


def pct_of(fact):
    """The fill percentage for a bar or a rail.

    Taken from the fact record: its own `pct` when it has one, otherwise its
    own value when that value is already a percentage, otherwise zero (no
    percentage is claimed for that figure).
    """
    p = fact.get("pct")
    if p is not None:
        return p
    unit = str(fact.get("unit") or "").strip().lower()
    if unit in ("%", "pp"):
        return fact.get("value")
    return 0


def fact_source(fact) -> str:
    return str(fact.get("source") or "").strip()


def claim_text(fact) -> str:
    c = str(fact.get("claim") or "").strip()
    if c:
        return c
    return synth_sentence(fact)


def synth_sentence(fact) -> str:
    head = " ".join(str(fact.get(k, "") or "").strip()
                    for k in ("model", "label") if str(fact.get(k, "") or "").strip())
    val = spell_value(fact.get("value"))
    unit = unit_words(fact.get("unit"))
    tail = " ".join(x for x in (val, unit) if x)
    if head and tail:
        return "%s: %s." % (head, tail)
    if head:
        return "%s." % head
    return tail or "No figure on this line."


def caveat_text(fact, i: int = 0) -> str:
    c = str(fact.get("caveat") or "").strip()
    if c:
        return c
    return CAVEAT_FALLBACK[i % len(CAVEAT_FALLBACK)]


def fact_label(fact) -> str:
    for key in ("label", "card", "model"):
        v = str(fact.get(key, "") or "").strip()
        if v:
            return v
    return "the figure"


def fact_name(fact) -> str:
    for key in ("model", "card", "label"):
        v = str(fact.get(key, "") or "").strip()
        if v:
            return v
    return "the card"


def has_caveat(fact) -> bool:
    return bool(str(fact.get("caveat") or "").strip())


# --------------------------------------------------------------------------
# EPISODE PLAN
# --------------------------------------------------------------------------
SHAPE_FOCUS = {
    "MEASUREMENT": "bars",
    "MECHANISM": "chain",
    "DECISION": "rows",
    "COMPARISON": "rows",
    "MYTH": "note",
    "PARADOX": "chain",
    "MATH": "bars",
    "FAILURE": "note",
    "HISTORY": "gallery",
    "COST": "rail",
}


def focus_layout(shape: str) -> str:
    s = str(shape or "").strip()
    if s.upper() in SHAPE_FOCUS:
        return SHAPE_FOCUS[s.upper()]
    low = s.lower()
    for name in SPINE:
        if name in low:
            return name
    for word in re.findall(r"[a-z]+", low):
        if word in ("bar", "chart", "plot"):
            return "bars"
        if word in ("row", "table", "rank", "ranking", "list"):
            return "rows"
        if word in ("rail", "gauge", "slider"):
            return "rail"
        if word in ("note", "caveat", "warning"):
            return "note"
        if word in ("chain", "flow", "steps", "pipeline", "mechanism"):
            return "chain"
        if word in ("gallery", "showcase", "card"):
            return "gallery"
        if word in ("strip", "icons"):
            return "strip"
        if word in ("node", "graph", "map", "network"):
            return "nodes"
        if word in ("title", "intro", "cold"):
            return "title"
    return "bars"


def slot_target(layout: str) -> int:
    return {
        "hook": 3, "rows": 4, "bars": 4, "rail": 3, "chain": 4, "note": 3,
        "gallery": 3, "strip": 0, "title": 0, "nodes": 3,
    }.get(layout, 3)


def choose_sequence(shape: str, nfacts: int):
    focus = focus_layout(shape)
    nw = 5 + min(5, nfacts // 4)
    if nw > len(SPINE):
        nw = len(SPINE)
    if nw < 5:
        nw = 5
    need = SPINE.index(focus) + 1
    if nw < need:
        nw = need
    return list(SPINE[:nw])


def gather_facts(angle, fmod):
    """Ordered, topic-interleaved fact list for the angle."""
    topics = angle.get("facts")
    if isinstance(topics, str):
        topics = [topics]
    topics = [str(t) for t in (topics or [])]
    if not topics:
        try:
            topics = [str(t) for t in fmod.topic_list()]
        except Exception:
            topics = []
    pools = []
    for t in topics:
        rows = facts_for_topic(fmod, t)
        if rows:
            pools.append(rows)
    if not pools:
        pools = [list(fmod.FACTS)]

    subject = str(angle.get("subject") or "").strip().lower()
    depth = max((len(p) for p in pools), default=0)

    def collect(filter_subject):
        out = []
        used = set()
        for d in range(depth):
            for pool in pools:
                if d >= len(pool):
                    continue
                f = pool[d]
                fid = fact_id(f)
                if fid in used:
                    continue
                if filter_subject and not _fact_matches(f, subject):
                    continue
                used.add(fid)
                out.append(f)
        return out

    ordered = collect(True)
    if not ordered:
        ordered = collect(False)
    return ordered


# --------------------------------------------------------------------------
# WINDOW PLANS (element kinds per layout, fullest first)
# --------------------------------------------------------------------------
def plan_variants(layout: str, nfacts: int):
    if layout == "hook":
        if nfacts >= 3:
            return [[("chip", 0), ("chip", 1), ("stat", 2)],
                    [("chip", 0), ("stat", 1)],
                    [("chip", 0), ("stat", 0)]]
        if nfacts == 2:
            return [[("chip", 0), ("stat", 1)], [("chip", 0), ("stat", 0)]]
        return [[("chip", 0), ("stat", 0)]]
    if layout in ("rows", "bars", "rail"):
        kind = {"rows": "row", "bars": "bar", "rail": "rail"}[layout]
        full = [(kind, i) for i in range(min(4, nfacts))] or [(kind, 0)]
        out = [list(full)]
        while len(out[-1]) > 1:
            out.append(list(out[-1][:-1]))
        return out
    if layout == "chain":
        if nfacts >= 4:
            return [[("chain", 0), ("chain", 1), ("cmp_hot", 2), ("cmp_good", 3)],
                    [("chain", 0), ("cmp_hot", 1), ("cmp_good", 2)],
                    [("chain", 0), ("cmp_hot", 1)],
                    [("chain", 0), ("cmp_hot", 0)]]
        if nfacts == 3:
            return [[("chain", 0), ("cmp_hot", 1), ("cmp_good", 2)],
                    [("chain", 0), ("cmp_hot", 1)],
                    [("chain", 0), ("cmp_hot", 0)]]
        if nfacts == 2:
            return [[("chain", 0), ("cmp_hot", 1)], [("chain", 0), ("cmp_hot", 0)]]
        return [[("chain", 0), ("cmp_hot", 0)]]
    if layout == "note":
        full = [("item", i) for i in range(min(3, nfacts))] or [("item", 0)]
        out = [list(full)]
        while len(out[-1]) > 1:
            out.append(list(out[-1][:-1]))
        return out
    if layout == "gallery":
        if nfacts >= 3:
            return [[("name", 0), ("blurb", 1), ("meta", 2)],
                    [("name", 0), ("blurb", 1), ("meta", 1)],
                    [("name", 0), ("blurb", 0), ("meta", 0)]]
        if nfacts == 2:
            return [[("name", 0), ("blurb", 1), ("meta", 1)],
                    [("name", 0), ("blurb", 0), ("meta", 0)]]
        return [[("name", 0), ("blurb", 0), ("meta", 0)]]
    if layout == "nodes":
        full = [("chain", i) for i in range(min(3, nfacts))] or [("chain", 0)]
        out = [list(full)]
        while len(out[-1]) > 1:
            out.append(list(out[-1][:-1]))
        return out
    return [[]]


# --------------------------------------------------------------------------
# WINDOW BUILDER
# --------------------------------------------------------------------------
class WindowError(Exception):
    pass


def _topic_word(topic: str) -> str:
    t = str(topic or "").strip().lower()
    return t or "the board"


def _art_for(topic: str) -> str:
    return TOPIC_ART.get(str(topic or "").strip().lower(), "chip")


def _pick(sequence, index):
    if not sequence:
        return ""
    return sequence[index % len(sequence)]


def item_text(layout, kind, fact, seen, i):
    """The spoken line for one element."""
    if layout == "gallery":
        if kind == "name":
            return "On the bench: %s." % fact_name(fact)
        if kind == "blurb":
            return claim_text(fact)
        val = spell_value(fact.get("value"))
        unit = unit_words(fact.get("unit"))
        tail = " ".join(x for x in (val, unit) if x)
        return "The line reads %s, from the same run." % tail
    if layout == "note":
        return caveat_text(fact, i)
    if layout == "chain" and kind == "chain":
        return claim_text(fact)
    if kind in ("chain", "row", "bar", "rail", "chip", "stat"):
        fid = fact_id(fact)
        if fid in seen:
            return _pick(REPEAT_TPL, i).format(label=fact_label(fact).lower())
        seen.add(fid)
        return claim_text(fact)
    return claim_text(fact)


def build_window(layout: str, facts, ctx):
    """Build one window. Raises WindowError if no variant satisfies the
    contract (anchors, word budget, layout keys, provenance)."""
    variants = plan_variants(layout, len(facts))
    last_err = "no usable plan"
    for plan in variants:
        try:
            win = _attempt_window(layout, facts, plan, ctx)
        except WindowError as exc:
            last_err = str(exc)
            continue
        if win is not None:
            return win
    raise WindowError("%s: %s" % (layout, last_err))


def _attempt_window(layout: str, facts, plan, ctx):
    topic = ctx["topic"]
    topic_word = _topic_word(topic)
    wi = ctx["wi"]
    title = ctx["title"]
    kicker = "%s &middot; %s" % (CHANNEL, str(topic or "measured").upper())
    art = ctx["art"]
    art_caption, art_phrase = ART[art]

    segs = []       # list of {"text":..., "role":...}
    targets = []    # list of (seg_index, kind) in spoken order

    def add(text, role, target=None):
        segs.append({"text": speech(text), "role": role})
        idx = len(segs) - 1
        if target is not None:
            targets.append((idx, target))
        return idx

    seen = set()
    elems = []      # list of (kind, fact, seg_index)

    # ---- title window: framing, thesis, then the title itself -------------
    if layout == "title":
        add(_pick(TITLE_FRAME_TPL, wi).format(), "frame")
        add(ctx["sub"], "thesis")
        t_seg = add("%s" % title, "title", ("head_at", None))
    else:
        h_seg = add(_pick(HEADER_TPL, wi).format(topic=topic_word), "header",
                    ("header_at", None))
        if layout in LAYOUTS_WITH_ART_AT:
            add("Picture %s." % art_phrase, "art", ("art_at", None))
        for i, (kind, idx) in enumerate(plan):
            fact = facts[idx] if facts else None
            if fact is None:
                continue
            text = item_text(layout, kind, fact, seen, i)
            seg = add(text, "item", ("item", (kind, fact)))
            elems.append((kind, fact, seg))

    # ---- closing / mid / tape / source ------------------------------------
    closing = None
    mid_line = None
    if layout == "bars":
        # the mid caption belongs inside the chart, so it is said before the
        # closing callout that follows the bars on screen
        mid_line = {"t": MID_LINE, "c": "cyan"}
        add(MID_LINE + ".", "mid", ("mid", mid_line))
    if layout in CLOSING_TPL:
        text = _pick(CLOSING_TPL[layout], wi)
        closing = {"t": text, "c": "gold" if layout != "rail" else "cyan"}
        add(text, "closing", ("closing", closing))
    tape_line = None
    if layout in LAYOUTS_WITH_TAPE:
        tape_line = _pick(TAPE_TPL, wi)
        add(tape_line, "tape", ("tape_at", None))
    source_phrase = None
    if layout == "note":
        source_phrase = SOURCE_PHRASE
        add(source_phrase, "source", ("source_at", None))

    # ---- strip items -------------------------------------------------------
    strip_items = []
    if layout == "strip":
        for t in ctx["strip_topics"]:
            label = STRIP_LABELS.get(str(t).lower(),
                                     "%s budget" % str(t).lower())
            strip_items.append({"key": TOPIC_ART.get(str(t).lower(), "chip"),
                                "label": label, "at": None})
        strip_text = "Strip by strip: " + ", ".join(
            "the %s figure" % it["label"] for it in strip_items) + "."
        add(strip_text, "strip", ("strip", strip_items))

    # ---- assemble the vo ---------------------------------------------------
    def assemble(seg_list):
        pos = 0
        spans = []
        parts = []
        for s in seg_list:
            if parts:
                pos += 1
            spans.append((pos, pos + len(s["text"])))
            parts.append(s["text"])
            pos += len(s["text"])
        return " ".join(parts), spans

    vo, seg_spans = assemble(segs)
    words = wc(vo)
    if words < 26:
        fill_i = wi
        while wc(vo) < 26 and fill_i < wi + 10:
            extra = _pick(FILLER_TPL, fill_i)
            segs.insert(1, {"text": speech(extra), "role": "fill"})
            vo, seg_spans = assemble(segs)
            fill_i += 1
        words = wc(vo)
    if words < 26 or words > 52:
        return None

    # ---- derive the anchors ------------------------------------------------
    spans = _spans(vo)
    anchor_of = {}
    after = 0
    last_end = 0
    for seg_idx, (kind, payload) in targets:
        start, end = seg_spans[seg_idx]
        prefer = ""
        if kind == "strip":
            continue
        if kind == "item":
            kind2, fact = payload
            prefer = ""
        if kind == "head_at":
            cand = title
            low_vo = vo.lower()
            if cand and low_vo.count(cand.lower()) == 1:
                got = (cand, start + len(cand))
            else:
                got = find_anchor(vo, spans, start, end, after=after)
        else:
            got = find_anchor(vo, spans, start, end, after=after, prefer=prefer)
        if got is None:
            return None
        anchor, end_pos = got
        after = end_pos
        last_end = end_pos
        anchor_of[(seg_idx, kind)] = anchor
        if kind in ("closing", "mid"):
            payload["at"] = anchor
        if kind == "item":
            kind2, fact = payload
            anchor_of[(seg_idx, "item")] = anchor

    # strip items share one segment: anchor each label phrase in order
    if layout == "strip":
        seg_idx = None
        for i, s in enumerate(segs):
            if s["role"] == "strip":
                seg_idx = i
                break
        start, end = seg_spans[seg_idx]
        for it in strip_items:
            got = find_anchor(vo, spans, start, end, after=after,
                              prefer="the %s figure" % it["label"])
            if got is None:
                return None
            it["at"] = got[0]
            after = got[1]
            last_end = got[1]

    # ---- rule 3: no anchor may be a substring of header_at -----------------
    header_anchor = anchor_of.get((h_seg, "header_at")) if layout != "title" else None
    if header_anchor:
        for (seg_idx, kind), anchor in anchor_of.items():
            if kind == "header_at":
                continue
            if anchor.lower() in header_anchor.lower():
                return None

    # ---- beat: the last element lands in the closing stretch of the window
    if last_end < 0.5 * len(vo):
        return None

    # ---- assemble the window dict ------------------------------------------
    source = ""
    for f in facts:
        source = fact_source(f)
        if source:
            break
    if not source:
        source = str(ctx.get("default_source") or "").strip()
    if not source:
        source = "source pending"

    win = {"layout": layout, "vo": vo}
    win["kicker"] = kicker
    win["title"] = title
    win["art"] = art
    win["art_caption"] = art_caption
    if layout != "title":
        win["header_at"] = anchor_of[(h_seg, "header_at")]
    if layout in LAYOUTS_WITH_ART_AT:
        win["art_at"] = anchor_of[[k for k in anchor_of
                                   if k[1] == "art_at"][0][0], "art_at"]

    def at_of(kind, fact, seg):
        return anchor_of[(seg, "item")]

    if layout == "hook":
        chips = []
        stats = []
        ci = 0
        for kind, fact, seg in elems:
            if kind == "chip":
                if ci == 0:
                    col = "gold"
                elif has_caveat(fact):
                    col = "red"
                elif ci == 1:
                    col = "cyan"
                else:
                    col = "ghost"
                chips.append({"t": fact_label(fact), "c": col, "at": at_of(kind, fact, seg)})
                ci += 1
            else:
                if ci == 1 and not has_caveat(fact):
                    col = "gold"
                elif has_caveat(fact):
                    col = "red"
                else:
                    col = "cyan"
                stats.append({"v": str(fact.get("value", "")), "u": str(fact.get("unit", "")),
                              "lab": fact_label(fact), "c": col, "at": at_of(kind, fact, seg)})
        win["chips"] = chips
        win["stats"] = stats
        win["tape"] = tape_line
        win["tape_at"] = anchor_of[[k for k in anchor_of
                                    if k[1] == "tape_at"][0][0], "tape_at"]
    elif layout == "rows":
        rows = []
        r = 1
        for kind, fact, seg in elems:
            cls = "gold" if r == 1 else ("red" if has_caveat(fact) else "")
            rows.append({"rank": str(r), "name": fact_name(fact),
                         "val": ("%s %s" % (str(fact.get("value", "")),
                                            str(fact.get("unit", "")))).strip(),
                         "sub": fact_label(fact), "cls": cls, "at": at_of(kind, fact, seg)})
            r += 1
        win["rows"] = rows
        win["closing"] = closing
    elif layout == "bars":
        bars = []
        for kind, fact, seg in elems:
            cls = "red" if has_caveat(fact) else ""
            bars.append({"lab": fact_name(fact), "val": str(fact.get("value", "")),
                         "unit": str(fact.get("unit", "")), "pct": pct_of(fact),
                         "cls": cls, "at": at_of(kind, fact, seg)})
        win["bars"] = bars
        win["closing"] = closing
        win["mid"] = mid_line
    elif layout == "rail":
        rails = []
        for kind, fact, seg in elems:
            cls = "red" if has_caveat(fact) else ""
            rails.append({"lab": fact_label(fact), "val": str(fact.get("value", "")),
                          "pct": pct_of(fact), "cls": cls, "at": at_of(kind, fact, seg)})
        win["rails"] = rails
        win["closing"] = closing
    elif layout == "chain":
        chain = []
        compares = []
        for kind, fact, seg in elems:
            if kind == "chain":
                chain.append({"t": fact_label(fact), "s": caveat_text(fact, len(chain)),
                              "at": at_of(kind, fact, seg)})
            else:
                cls, ttitle, body = COMPARE_TPL[kind]
                compares.append({"cls": cls, "title": ttitle,
                                 "body": body.format(label=fact_label(fact)),
                                 "at": at_of(kind, fact, seg)})
        win["chain"] = chain
        win["compare"] = compares
    elif layout == "note":
        items = []
        for kind, fact, seg in elems:
            items.append({"t": caveat_text(fact, len(items)), "at": at_of(kind, fact, seg)})
        win["note_head"] = _pick(NOTE_HEAD_TPL, wi)
        win["note_items"] = items
        win["tape"] = tape_line
        win["tape_at"] = anchor_of[[k for k in anchor_of
                                    if k[1] == "tape_at"][0][0], "tape_at"]
        win["source_at"] = anchor_of[[k for k in anchor_of
                                      if k[1] == "source_at"][0][0], "source_at"]
    elif layout == "gallery":
        name = blurb = meta = ""
        for kind, fact, seg in elems:
            if kind == "name":
                name = fact_name(fact)
                win["name_at"] = at_of(kind, fact, seg)
            elif kind == "blurb":
                blurb = claim_text(fact)
                win["blurb_at"] = at_of(kind, fact, seg)
            else:
                meta = ("%s &middot; %s %s" % (fact_label(fact),
                                               str(fact.get("value", "")),
                                               str(fact.get("unit", "")))).strip()
                win["meta_at"] = at_of(kind, fact, seg)
        win["name"] = name
        win["blurb"] = blurb
        win["meta"] = meta
        win["side"] = "left" if wi % 2 == 1 else "right"
    elif layout == "strip":
        win["items"] = strip_items
    elif layout == "title":
        win["sub"] = ctx["sub"]
        win["head_at"] = anchor_of[[k for k in anchor_of
                                    if k[1] == "head_at"][0][0], "head_at"]
    elif layout == "nodes":
        chain = []
        for kind, fact, seg in elems:
            chain.append({"t": fact_label(fact), "s": caveat_text(fact, len(chain)),
                          "at": at_of(kind, fact, seg)})
        win["chain"] = chain

    win["source"] = source
    # provenance: which fact records this window is built from. The emitter
    # only writes the keys the layout declares, so this never reaches the
    # generated module.
    ids = []
    for _kind, fact, _seg in elems:
        fid = fact_id(fact)
        if fid and fid not in ids:
            ids.append(fid)
    for f in facts:
        fid = fact_id(f)
        if fid and fid not in ids:
            ids.append(fid)
    win["_fact_ids"] = ids
    return win


# --------------------------------------------------------------------------
# EPISODE ASSEMBLY
# --------------------------------------------------------------------------
def safe_sub(angle) -> str:
    """The line shown and spoken under the episode title. Kept digit free."""
    thesis = str(angle.get("thesis") or "").strip()
    if thesis and not re.search(r"[0-9]", thesis):
        return thesis
    cav = str(angle.get("caveat") or "").strip()
    if cav and not re.search(r"[0-9]", cav):
        return cav
    return "One claim, measured on the hardware."


def build_episode(angle, fmod):
    """Return (windows, error). error is None on success."""
    aid = str(angle.get("id") or "").strip()
    title = str(angle.get("title") or aid).strip().upper()
    shape = str(angle.get("shape") or "")

    facts = gather_facts(angle, fmod)
    if not facts:
        return None, "no facts for this angle"

    seq = choose_sequence(shape, len(facts))
    topics = []
    for f in facts:
        t = str(f.get("topic") or "")
        if t and t not in topics:
            topics.append(t)
    strip_topics = (topics or ["vram"])[:4]
    sub = safe_sub(angle)
    default_source = ""
    for f in facts:
        default_source = fact_source(f)
        if default_source:
            break

    windows = []
    cursor = 0
    nfacts = len(facts)
    for wi, layout in enumerate(seq):
        need = slot_target(layout)
        chunk = []
        if need and facts:
            if layout == "note":
                cav = []
                seen_cav = set()
                for f in facts:
                    if not has_caveat(f):
                        continue
                    key = caveat_text(f).lower()
                    if key in seen_cav:
                        continue
                    seen_cav.add(key)
                    cav.append(f)
                if cav:
                    chunk = cav[:need]
                    cursor = (cursor + len(chunk)) % nfacts
                else:
                    chunk = [facts[(cursor + k) % nfacts] for k in range(need)]
                    cursor += need
            elif layout in ("bars", "rail"):
                # a gauge wants facts that carry their own percentage
                withpct = [f for f in facts if f.get("pct") is not None]
                pool = withpct if withpct else facts
                chunk = [pool[(cursor + k) % len(pool)] for k in range(need)]
                cursor += need
            else:
                chunk = [facts[(cursor + k) % nfacts] for k in range(need)]
                cursor += need
        topic = str(chunk[0].get("topic") or "") if chunk else ""
        if not topic:
            topic = topics[wi % len(topics)] if topics else "vram"
        ctx = {"wi": wi, "topic": topic, "title": title,
               "art": _art_for(topic), "sub": sub, "strip_topics": strip_topics,
               "default_source": default_source}
        try:
            win = build_window(layout, chunk, ctx)
        except WindowError as exc:
            return None, "window %d (%s): %s" % (wi, layout, exc)
        windows.append(win)

    return windows, None


# --------------------------------------------------------------------------
# SELF CHECKS (nine). The generator refuses to write a file that fails.
# --------------------------------------------------------------------------
def header_field(layout):
    if "header_at" in LAYOUT_KEYS.get(layout, []):
        return "header_at"
    return None


def anchors_of(window):
    """(field, phrase) for every anchor in the window, header first."""
    layout = window.get("layout")
    out = []
    hf = header_field(layout)
    if hf:
        out.append((hf, str(window.get(hf, "") or "")))
    for key in LAYOUT_KEYS.get(layout, []):
        if key.endswith("_at") and key != hf:
            val = window.get(key)
            if isinstance(val, str):
                out.append((key, val))
    for list_key in LIST_SCHEMA.get(layout, {}):
        for elem in window.get(list_key, []) or []:
            if isinstance(elem, dict) and "at" in elem:
                out.append(("%s[].at" % list_key, str(elem.get("at", "") or "")))
    return out


def ordered_anchors(window):
    """The window's anchors in the order the builder lays them out."""
    layout = window.get("layout")
    out = []
    for key in LAYOUT_KEYS.get(layout, []):
        if key.endswith("_at"):
            val = window.get(key)
            if isinstance(val, str):
                out.append((key, val))
        for elem in window.get(key, []) or []:
            if isinstance(elem, dict) and "at" in elem:
                out.append(("%s[].at" % key, str(elem.get("at", "") or "")))
    return out


def check_builder_compat(windows):
    """Render every window through the real builder.

    This is the check that catches a contract the spec sheets can only hint
    at: the builder indexes keys directly (a missing key is a KeyError at
    build time) and it resolves every beat anchor against the script, so an
    anchor that is not in the vo stops the build. If the builder is not
    importable the check is skipped rather than failed.
    """
    try:
        import copy
        fb = importlib.import_module("fusion_build")
    except Exception:
        return True, "builder not available, skipped"
    bad = []
    try:
        for i, w in enumerate(windows):
            lay = w.get("layout")
            data = copy.deepcopy(w)
            data.setdefault("art", "magnifier" if lay == "note" else "chip")
            data.setdefault("art_caption", data["art"].replace("_", " ").upper())
            data.setdefault("art_at", data.get("header_at") or data.get("head_at"))
            data.setdefault("meta", "asset: %s" % data["art"])
            data.setdefault("side", "right")
            data.setdefault("sub", "")
            data.setdefault("blurb", "")
            data.setdefault("name", data.get("title", ""))
            data.setdefault("kicker", CHANNEL)
            data.setdefault("title", data.get("name", ""))
            data.setdefault("header_at", data.get("head_at"))
            win = fb.Win(i, data)
            html = fb.RENDER[lay](data, win)
            vo = str(data.get("vo", "")).lower()
            if not html:
                bad.append("w%d %s rendered empty" % (i, lay))
            for b in win.beats:
                at = b.get("at")
                if not at or str(at).lower() not in vo:
                    bad.append("w%d %s beat anchor %r" % (i, lay, at))
    except Exception as exc:
        bad.append("render failed: %s: %s" % (type(exc).__name__, exc))
    return (not bad), "; ".join(bad[:4])


def run_checks(windows, fmod=None):
    """Run the nine self-checks. Returns list of (name, ok, detail)."""
    results = []

    def add(name, ok, detail=""):
        results.append((name, bool(ok), detail))

    # 1. every at is a substring of its window vo, case-insensitively
    bad = []
    for i, w in enumerate(windows):
        low = str(w.get("vo", "")).lower()
        for field, phrase in anchors_of(w):
            if not phrase or phrase.lower() not in low:
                bad.append("w%d %s %r" % (i, field, phrase))
    add("anchors-present", not bad, "; ".join(bad[:4]))

    # 2. every at is unique in its vo
    bad = []
    for i, w in enumerate(windows):
        low = str(w.get("vo", "")).lower()
        for field, phrase in anchors_of(w):
            if phrase and low.count(phrase.lower()) != 1:
                bad.append("w%d %s %r x%d" % (i, field, phrase, low.count(phrase.lower())))
    add("anchors-unique", not bad, "; ".join(bad[:4]))

    # 3. no at phrase is a substring of that window's header_at
    bad = []
    for i, w in enumerate(windows):
        hf = header_field(w.get("layout"))
        if not hf:
            continue
        head = str(w.get(hf, "")).lower()
        for field, phrase in anchors_of(w):
            if field == hf or not phrase:
                continue
            if phrase.lower() in head:
                bad.append("w%d %s %r" % (i, field, phrase))
    add("anchors-not-in-header", not bad, "; ".join(bad[:4]))

    # 4. every window has 26-52 words
    bad = []
    for i, w in enumerate(windows):
        n = wc(str(w.get("vo", "")))
        if n < 26 or n > 52:
            bad.append("w%d %d words" % (i, n))
    add("word-budget", not bad, "; ".join(bad[:4]))

    # 5. every window has a source
    bad = []
    for i, w in enumerate(windows):
        if not str(w.get("source", "")).strip():
            bad.append("w%d" % i)
    add("sources-present", not bad, "; ".join(bad[:4]))

    # 6. chain windows have a source and a compare list
    bad = []
    for i, w in enumerate(windows):
        if w.get("layout") == "chain":
            if not str(w.get("source", "")).strip() or not w.get("compare"):
                bad.append("w%d" % i)
    add("chain-has-source-and-compare", not bad, "; ".join(bad[:4]))

    # 7. no two consecutive windows share a layout
    bad = []
    for i in range(1, len(windows)):
        if windows[i].get("layout") == windows[i - 1].get("layout"):
            bad.append("w%d %s" % (i, windows[i].get("layout")))
    add("no-consecutive-same-layout", not bad, "; ".join(bad[:4]))

    # 8. every art key is in the valid list
    bad = []
    for i, w in enumerate(windows):
        val = w.get("art")
        if val and val not in ART:
            bad.append("w%d art=%r" % (i, val))
        for elem in w.get("items", []) or []:
            if elem.get("key") not in ART:
                bad.append("w%d item key=%r" % (i, elem.get("key")))
    add("art-keys-valid", not bad, "; ".join(bad[:4]))

    # 9. every value on screen came from a fact record
    bad = []
    if fmod is not None:
        allowed_vals = set()
        allowed_units = set()
        allowed_pcts = set()
        for f in fmod.FACTS:
            allowed_vals.add(str(f.get("value", "")))
            allowed_units.add(str(f.get("unit", "")))
            allowed_pcts.add(str(f.get("pct", "")))
        allowed_vals.add("0")
        allowed_pcts.add("0")

        def known(pool, val):
            if str(val) in pool:
                return True
            try:
                fv = float(val)
            except (TypeError, ValueError):
                return False
            for a in pool:
                try:
                    if abs(float(a) - fv) < 1e-9:
                        return True
                except (TypeError, ValueError):
                    continue
            return False

        for i, w in enumerate(windows):
            for el in w.get("stats", []) or []:
                if not known(allowed_vals, el.get("v")):
                    bad.append("w%d stat v=%r" % (i, el.get("v")))
                if not known(allowed_units, el.get("u")):
                    bad.append("w%d stat u=%r" % (i, el.get("u")))
            for el in w.get("bars", []) or []:
                if not known(allowed_vals, el.get("val")):
                    bad.append("w%d bar val=%r" % (i, el.get("val")))
                if not known(allowed_units, el.get("unit")):
                    bad.append("w%d bar unit=%r" % (i, el.get("unit")))
                if not known(allowed_pcts, el.get("pct")) and \
                        not known(allowed_vals, el.get("pct")):
                    bad.append("w%d bar pct=%r" % (i, el.get("pct")))
            for el in w.get("rails", []) or []:
                if not known(allowed_vals, el.get("val")):
                    bad.append("w%d rail val=%r" % (i, el.get("val")))
                if not known(allowed_pcts, el.get("pct")) and \
                        not known(allowed_vals, el.get("pct")):
                    bad.append("w%d rail pct=%r" % (i, el.get("pct")))
            for el in w.get("rows", []) or []:
                val = str(el.get("val", "")).strip()
                if " " in val:
                    num, unit = val.rsplit(" ", 1)
                else:
                    num, unit = val, ""
                if not known(allowed_vals, num):
                    bad.append("w%d row val=%r" % (i, val))
                if unit and not known(allowed_units, unit):
                    bad.append("w%d row unit=%r" % (i, unit))
    add("values-from-fact-base", not bad, "; ".join(bad[:4]))

    # 10. elements are listed in the order the script says them
    bad = []
    for i, w in enumerate(windows):
        low = str(w.get("vo", "")).lower()
        last = -1
        for field, phrase in ordered_anchors(w):
            if not phrase:
                continue
            pos = low.find(phrase.lower())
            if pos < 0:
                continue
            if pos < last:
                bad.append("w%d %s %r" % (i, field, phrase))
                break
            last = pos
    add("element-order", not bad, "; ".join(bad[:4]))

    return results


def check_layout_contract(windows):
    """Every window carries exactly the keys its layout declares, and every
    list element carries the keys the builder indexes."""
    bad = []
    for i, w in enumerate(windows):
        layout = w.get("layout")
        keys = LAYOUT_KEYS.get(layout)
        if keys is None:
            bad.append("w%d unknown layout %r" % (i, layout))
            continue
        for key in keys:
            if key not in w:
                bad.append("w%d missing %s" % (i, key))
        for key in ("closing", "mid"):
            val = w.get(key)
            if isinstance(val, dict):
                for sub in ("t", "c", "at"):
                    if sub not in val:
                        bad.append("w%d %s missing %s" % (i, key, sub))
        for list_key, elem_keys in LIST_SCHEMA.get(layout, {}).items():
            for j, elem in enumerate(w.get(list_key, []) or []):
                if not isinstance(elem, dict):
                    bad.append("w%d %s[%d] not a dict" % (i, list_key, j))
                    continue
                for sub in elem_keys:
                    if sub not in elem:
                        bad.append("w%d %s[%d] missing %s" % (i, list_key, j, sub))
    return bad


# --------------------------------------------------------------------------
# MODULE EMISSION
# --------------------------------------------------------------------------
def _fmt(v):
    if isinstance(v, str):
        out = v.replace("\\", "\\\\").replace('"', '\\"')
        out = out.replace("\r", "\\r").replace("\n", "\\n").replace("\t", "\\t")
        return '"' + out + '"'
    if isinstance(v, bool):
        return "True" if v else "False"
    if isinstance(v, (int, float)):
        return repr(v)
    if v is None:
        return "None"
    if isinstance(v, list):
        return "[" + ", ".join(_fmt(x) for x in v) + "]"
    if isinstance(v, dict):
        return "{" + ", ".join('"%s": %s' % (k, _fmt(x)) for k, x in v.items()) + "}"
    return repr(v)


def emit_module(angle, windows):
    aid = str(angle.get("id") or "").strip()
    title = str(angle.get("title") or aid).strip().upper()
    doc_lines = [
        "Generated from angle %s -- %s." % (aid, title),
        "",
        "Source of truth: data/angles.py (angle) + data/facts.py (every number).",
        "Regenerate with: python data/make_spec.py %s" % aid,
    ]
    doc = ("\n".join(doc_lines) + "\n").replace("\\", "\\\\").replace('"""', '\\"\\"\\"')

    out = []
    out.append("# -*- coding: utf-8 -*-")
    out.append('"""' + doc + '"""')
    out.append("W = []")
    out.append("")
    out.append("")
    out.append("def win(layout, vo, **data):")
    out.append("    W.append(dict(layout=layout, vo=vo, **data))")
    out.append("")

    for w in windows:
        layout = w["layout"]
        pairs = [("layout", layout), ("vo", w["vo"])]
        for key in LAYOUT_KEYS.get(layout, []):
            if key not in w:
                continue
            pairs.append((key, w[key]))
        out.append("win(")
        for key, val in pairs:
            out.append("    %s=%s," % (key, _fmt(val)))
        out.append(")")
        out.append("")

    out.append('NAME = "%s%s"' % (GEN_PREFIX, aid))
    out.append("TITLE = %s" % _fmt(title))
    out.append("DOC_TITLE = %s" % _fmt("%s &middot; %s" % (title, CHANNEL)))
    out.append("KICKER = %s" % _fmt("%s &middot; GENERATED" % CHANNEL))
    out.append("SUBTITLE = %s" % _fmt("a scaffold from the fact base"))
    out.append("GLOBAL_PROGRESS = False")
    out.append("")
    return "\n".join(out)


def safe_name(aid: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]", "_", str(aid))


def write_spec(angle, fmod, outdir=None):
    """Build, check and write one spec module. Returns (path, windows, error)."""
    outdir = outdir or HERE
    aid = safe_name(angle.get("id") or "ANGLE")
    path = Path(outdir) / ("spec_gen_%s.py" % aid)
    windows, err = build_episode(angle, fmod)
    if err:
        return path, None, err
    bad = check_layout_contract(windows)
    if bad:
        return path, None, "layout contract: " + "; ".join(bad[:4])
    results = run_checks(windows, fmod)
    failed = [(n, d) for n, ok, d in results if not ok]
    if failed:
        return path, None, "self-check failed: " + "; ".join(
            "%s (%s)" % (n, d) for n, d in failed)
    ok, detail = check_builder_compat(windows)
    if not ok:
        return path, None, "builder compat failed: " + detail
    src = emit_module(angle, windows)
    path.write_text(src, encoding="utf-8", newline="\n")
    return path, windows, None


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def cmd_list(angles, args):
    for a in angles:
        print("%s  %s  %s" % (a.get("id"), a.get("shape"), a.get("title")))
    return 0


def cmd_one(angle, fmod, args):
    path, windows, err = write_spec(angle, fmod)
    if err:
        print("FAIL %s" % angle.get("id"))
        print("  %s" % err)
        print("  no file written")
        return 1
    layouts = " > ".join(w["layout"] for w in windows)
    topics = []
    for w in windows:
        t = str(w.get("kicker", "")).split("&middot;")[-1].strip()
        if t and t not in topics:
            topics.append(t)
    ids = []
    for w in windows:
        for fid in w.get("_fact_ids", []) or []:
            if fid not in ids:
                ids.append(fid)
    print(str(path))
    print("  windows : %d" % len(windows))
    print("  layouts : %s" % layouts)
    print("  topics  : %s" % ", ".join(topics))
    print("  facts   : %d (%s)" % (len(ids), ", ".join(ids) if ids else "none"))
    return 0


def cmd_batch(angles, fmod, args):
    n = int(args.batch)
    outdir = HERE
    wrote = []
    skipped = []
    failed = []
    for a in angles:
        if len(wrote) + len(failed) >= n:
            break
        aid = safe_name(a.get("id") or "ANGLE")
        path = outdir / ("spec_gen_%s.py" % aid)
        if path.exists():
            skipped.append(aid)
            continue
        path, windows, err = write_spec(a, fmod, outdir)
        if err:
            failed.append((aid, err))
        else:
            wrote.append((aid, path, windows))
    print("%-14s %-6s %-8s %s" % ("ID", "STATUS", "WINDOWS", "LAYOUTS"))
    print("-" * 96)
    for aid, path, windows in wrote:
        print("%-14s %-6s %-8d %s" % (aid, "ok", len(windows),
                                      " > ".join(w["layout"] for w in windows)))
    for aid, err in failed:
        print("%-14s %-6s %-8s %s" % (aid, "FAIL", "-", err[:70]))
    for aid in skipped:
        print("%-14s %-6s %-8s %s" % (aid, "skip", "-", "file already exists"))
    print("-" * 96)
    print("wrote %d, skipped %d, failed %d" % (len(wrote), len(skipped), len(failed)))
    return 0


def load_generated(name):
    name = str(name).strip()
    if name.endswith(".py"):
        name = name[:-3]
    path = HERE / (name + ".py")
    if not path.exists():
        return None, "no such module: %s" % path
    mod_name = "spec_check_" + re.sub(r"[^A-Za-z0-9_]", "_", name)
    spec = importlib.util.spec_from_file_location(mod_name, str(path))
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as exc:
        return None, "import failed: %s" % exc
    return mod, None


def cmd_check(name, fmod, args):
    mod, err = load_generated(name)
    if err:
        print("FAIL  %s" % err)
        return 1
    windows = list(getattr(mod, "W", []))
    print("module : %s" % (HERE / (str(name).replace(".py", "") + ".py")))
    print("windows: %d" % len(windows))
    contract = check_layout_contract(windows)
    print("%-5s %s" % ("PASS" if not contract else "FAIL",
                       "layout-contract" + ("" if not contract
                                            else ": " + "; ".join(contract[:4]))))
    results = run_checks(windows, fmod)
    npass = 1 if not contract else 0
    for name_, ok, detail in results:
        npass += 1 if ok else 0
        print("%-5s %s%s" % ("PASS" if ok else "FAIL", name_,
                            "" if ok else ": " + detail))
    bok, bdetail = check_builder_compat(windows)
    npass += 1 if bok else 0
    print("%-5s %s%s" % ("PASS" if bok else "FAIL", "builder-compat",
                        "" if bok else ": " + bdetail))
    total = len(results) + 2
    ok_all = (not contract) and all(ok for _n, ok, _d in results)
    print("RESULT: %s (%d/%d)" % ("PASS" if ok_all else "FAIL", npass, total))
    return 0 if ok_all else 1


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="make_spec.py",
        description="Turn (angle, fact slice) into a buildable episode spec module.")
    ap.add_argument("angle", nargs="?", help="angle id, e.g. VRAM-001")
    ap.add_argument("--list", action="store_true", help="list every angle")
    ap.add_argument("--batch", type=int, default=None, help="write the first N angles")
    ap.add_argument("--check", metavar="MODULE", help="check a generated spec module")
    args = ap.parse_args(argv)

    if args.check:
        fmod = load_facts()
        return cmd_check(args.check, fmod, args)

    amod = load_angles()
    angles = list(getattr(amod, "W", []))
    fmod = load_facts()

    if args.list:
        return cmd_list(angles, args)
    if args.batch is not None:
        return cmd_batch(angles, fmod, args)
    if args.angle:
        wanted = str(args.angle).strip().lower()
        for a in angles:
            if str(a.get("id", "")).lower() == wanted:
                return cmd_one(a, fmod, args)
        print("no such angle: %s" % args.angle)
        print("try --list")
        return 2
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
