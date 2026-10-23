# -*- coding: utf-8 -*-
"""Every beat anchor must exist in the window's own narration.

The builder resolves an anchor by searching the narration text for it. A
missing anchor used to raise "anchor not in script" at build time, but that
error arrives after the audio has already been generated, so the run is
wasted. This check runs first and says exactly which anchor is missing and
which window it belongs to.

    python data/_check_anchors.py [spec_module]
"""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

LIST_KEYS = ("bars", "rows", "rails", "chain", "items", "note_items", "chips",
             "stats", "compare")


def anchors(w):
    """Every phrase the builder will look up in this window's narration."""
    out = []
    for k in ("header_at", "head_at", "art_at", "tape_at", "source_at"):
        if w.get(k):
            out.append((k, w[k]))
    for k in LIST_KEYS:
        for i, it in enumerate(w.get(k) or []):
            if isinstance(it, dict) and it.get("at"):
                out.append(("%s[%d].at" % (k, i), it["at"]))
    for k in ("closing", "mid"):
        if isinstance(w.get(k), dict) and w[k].get("at"):
            out.append(("%s.at" % k, w[k]["at"]))
    return out


def main(spec_name="spec_ep09_full"):
    spec = importlib.import_module(spec_name)
    W = spec.W
    bad = 0
    for i, w in enumerate(W):
        vo = (w.get("vo") or "").lower()
        for label, phrase in anchors(w):
            p = phrase.lower()
            if p not in vo:
                print("  win %2d  %-18s %r  NOT IN SCRIPT" % (i + 1, label, phrase))
                bad += 1
    print("\n%d windows, %d anchors, %d missing"
          % (len(W), sum(len(anchors(w)) for w in W), bad))
    if bad:
        raise SystemExit("ANCHOR CHECK FAILED")
    print("ANCHOR CHECK PASSED")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "spec_ep09_full")
