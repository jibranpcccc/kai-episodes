# -*- coding: utf-8 -*-
"""Every number the episode puts on screen, per window.

This is the inventory the source-of-truth fact sheet has to cover. A number
that appears on screen and is not in the fact sheet is a number nobody
checked, which is exactly how the EP09 errors got in.

    python data/_numbers_on_screen.py [spec_module]
"""
import importlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# A multi-dot version ("595.58.03") is one token. A number glued to letters
# ("153d324bc") is an identifier, not a number, and is not counted.
NUM = re.compile(r"\d[\d,]*(?:\.\d+)+|\b\d[\d,]*(?:\.\d+)?\b")

FIELDS = ("kicker", "title", "sub", "art_caption", "note_head", "tape",
          "blurb", "meta", "name", "source")


def strings(w):
    """Every visible string in this window."""
    out = [(k, w[k]) for k in FIELDS if w.get(k)]
    for k in ("closing", "mid"):
        if isinstance(w.get(k), dict) and w[k].get("t"):
            out.append(("chip", w[k]["t"]))
    for r in (w.get("rows") or []):
        out.append(("row.name", r.get("name", "")))
        out.append(("row.val", r.get("val", "")))
        out.append(("row.sub", r.get("sub", "")))
    for b in (w.get("bars") or []):
        out.append(("bar.lab", b.get("lab", "")))
        out.append(("bar.val", b.get("val", "")))
        out.append(("bar.unit", b.get("unit", "")))
    for r in (w.get("rails") or []):
        out.append(("rail.lab", r.get("lab", "")))
        out.append(("rail.val", r.get("val", "")))
    for c in (w.get("chain") or []):
        out.append(("chain.t", c.get("t", "")))
        out.append(("chain.s", c.get("s", "")))
    for c in (w.get("compare") or []):
        out.append(("compare.title", c.get("title", "")))
        out.append(("compare.body", c.get("body", "")))
    for i in (w.get("items") or []):
        out.append(("strip.label", i.get("label", "")))
    for n in (w.get("note_items") or []):
        out.append(("note.item", n.get("t", "")))
    for c in (w.get("chips") or []):
        out.append(("hook.chip", c.get("t", "")))
    for s in (w.get("stats") or []):
        out.append(("hook.stat", "%s %s %s" % (s.get("v", ""), s.get("u", ""),
                                                s.get("lab", ""))))
    mk = w.get("mark")
    if mk:
        out.append(("axis.mark", mk.get("lab", "")))
    return out


def main(spec_name="spec_ep09_full"):
    spec = importlib.import_module(spec_name)
    allnums = {}
    for i, w in enumerate(spec.W):
        seen = []
        for label, text in strings(w):
            for m in NUM.findall(str(text)):
                if m not in seen:
                    seen.append(m)
        if seen:
            print("W%02d  %s" % (i + 1, "  ".join(seen)))
        for m in seen:
            allnums.setdefault(m, []).append(i + 1)
    print("\n--- distinct numbers ---")
    for m in sorted(allnums, key=lambda x: (len(x), x)):
        print("%-12s %s" % (m, allnums[m]))
    print("\n%d distinct numbers" % len(allnums))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "spec_ep09_full")
