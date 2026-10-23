# -*- coding: utf-8 -*-
"""Reveal-order check by VISUAL ROLE.

The DOM interleaves a row with its nested value span, so id order alone is
not visual order. This groups elements by the class that decides where they
draw, then checks the beat times inside each group are monotonic.

    python data/_probe_seq2.py BYTE-LORA
"""
import io
import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-LORA"
src = io.open(os.path.join(ROOT, NAME + ".html"), encoding="utf-8").read()
F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", src, re.S).group(1))

secs = re.findall(r'<section class="scene" data-scene="(\d+)">(.*?)</section>', src, re.S)
body = [b for _, b in secs]

per = defaultdict(list)
for beat in F["beats"]:
    per[beat["group"]].append(beat)

# role -> class fragment that decides where the element draws
ROLES = [
    ("row", "row row--"),
    ("chip", "chip chip--"),
    ("note_item", None),   # resolved by tag
    ("chain_node", "chain__node"),
    ("compare_col", "compare__col"),
    ("bar", "bar bar--"),
    ("rail", "rail__row"),
    ("stack", "stack stack--"),
    ("tape", "tape"),
]


def classify(seg):
    cls = re.search(r'class="([^"]*)"', seg)
    cls = cls.group(1) if cls else ""
    if "row row--" in cls:
        return "row"
    if "chip chip--" in cls:
        return "chip"
    if "chain__node" in cls:
        return "chain_node"
    if "compare__col" in cls:
        return "compare_col"
    if "bar bar--" in cls or "bar--" in cls:
        return "bar"
    if "rail__row" in cls or "railrow" in cls:
        return "rail"
    if cls.startswith("stack"):
        return "stack"
    if cls.startswith("tape"):
        return "tape"
    if cls.startswith("note"):
        return "note"
    if "<li" in seg or "note__item" in cls or cls == "":
        return "note_item"
    return None


bad_windows = []
for i, sec in enumerate(body):
    beats = {b.get("el"): b["s"] for b in per[i] if b.get("el")}
    groups = defaultdict(list)
    for m in re.finditer(r'<(\w+)[^>]*id="(w\d+_\d+)"[^>]*>', sec):
        tag, rid = m.group(1), m.group(2)
        if "#" + rid not in beats:
            continue
        start = m.start()
        seg = sec[start:start + 260]
        role = classify(seg)
        if role is None:
            continue
        groups[role].append((rid, beats["#" + rid]))
    for role, items in groups.items():
        if len(items) < 3:
            continue
        times = [t for _, t in items]
        if times != sorted(times):
            bad_windows.append((i, role, items))

if not bad_windows:
    print("ALL WINDOWS: elements reveal in their authored visual order.")
else:
    print("windows with out-of-order reveals:")
    for i, role, items in bad_windows:
        print("\n  scene %2d  role=%s" % (i, role))
        sec = body[i]
        for rid, t in items:
            k = sec.index('id="%s"' % rid)
            txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", sec[k:k + 220])).strip()
            print("      %-9s %6.2fs  %s" % (rid, t, txt[:72]))

# also report simultaneous arrivals (no stagger)
print()
print("=== simultaneous arrivals within a visual group (no stagger) ===")
for i, sec in enumerate(body):
    beats = {b.get("el"): b["s"] for b in per[i] if b.get("el")}
    groups = defaultdict(list)
    for m in re.finditer(r'<(\w+)[^>]*id="(w\d+_\d+)"[^>]*>', sec):
        tag, rid = m.group(1), m.group(2)
        if "#" + rid not in beats:
            continue
        role = classify(sec[m.start():m.start() + 260])
        if role:
            groups[role].append((rid, beats["#" + rid]))
    for role, items in groups.items():
        if len(items) < 3:
            continue
        by_t = defaultdict(list)
        for rid, t in items:
            by_t[round(t, 3)].append(rid)
        for t, ids in by_t.items():
            if len(ids) > 1:
                print("  scene %2d  role=%-11s at %6.2fs -> %s" % (i, role, t, ", ".join(ids)))
