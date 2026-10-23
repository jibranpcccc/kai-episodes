# -*- coding: utf-8 -*-
"""Dump every visible string in an episode spec, so it can be read and checked.

Text that reaches the screen comes from a small number of places. This walks
the spec and prints each one with the window it belongs to, which is what the
spelling and terminology review reads.

    python data/_dump_text.py [spec_module]
"""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def visible(w):
    """(label, text) for everything the viewer can read in this window."""
    out = []
    for k in ("kicker", "title", "sub", "art_caption", "note_head", "tape",
              "blurb", "meta", "name", "source"):
        if w.get(k):
            out.append((k, w[k]))
    for it in (w.get("closing") or {}), (w.get("mid") or {}):
        if it.get("t"):
            out.append(("chip", it["t"]))
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
    for i, w in enumerate(spec.W):
        print("=" * 78)
        print("WINDOW %02d  %s   %s" % (i + 1, w["layout"].upper(),
                                        w.get("title", "")))
        for label, text in visible(w):
            if text:
                print("   %-14s %s" % (label, text))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "spec_ep09_full")
