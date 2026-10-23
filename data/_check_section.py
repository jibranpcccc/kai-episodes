# -*- coding: utf-8 -*-
r"""Check an episode section file: anchors, uniqueness, word budget, duplication.

    python data\_check_section.py ep09_s5 [ep09_s4 ...]

Every `at` anchor must be an exact substring of its own window's `vo`, must
resolve to a unique word, and no window may exceed the word budget. Also
reports narration duplicated between windows.
"""
import importlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MAX_WORDS = 52
MIN_WORDS = 26


def walk(w, path=""):
    """Every (anchor, label) pair in a window."""
    out = []
    for k, v in w.items():
        if k in ("vo", "layout"):
            continue
        if isinstance(v, str) and k in ("header_at", "art_at", "tape_at", "source_at",
                                        "head_at", "name_at", "blurb_at", "meta_at"):
            out.append((v, k))
        elif isinstance(v, dict):
            for kk, vv in v.items():
                if kk == "at" and isinstance(vv, str):
                    out.append((vv, "%s.%s" % (k, kk)))
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    for kk, vv in item.items():
                        if kk == "at" and isinstance(vv, str):
                            out.append((vv, "%s[%d].%s" % (k, i, kk)))
    return out


def main(names):
    bad = 0
    all_vo = []
    for name in names:
        m = importlib.import_module(name)
        print("=== %s -- %d windows ===" % (name, len(m.W)))
        for i, w in enumerate(m.W):
            vo = w["vo"]
            nw = len(vo.split())
            all_vo.append((name, i, vo))
            flag = ""
            if nw > MAX_WORDS or nw < MIN_WORDS:
                flag = "  ** WORD BUDGET **"
                bad += 1
            print("  win %-3d %-8s %3d words%s" % (i + 1, w["layout"], nw, flag))
            for anchor, label in walk(w):
                if anchor not in vo:
                    print("      ** MISSING ** %-22s %r" % (label, anchor[:60]))
                    bad += 1
                elif vo.count(anchor) > 1:
                    print("      ** AMBIGUOUS ** %-20s %r appears %dx"
                          % (label, anchor[:50], vo.count(anchor)))
                    bad += 1
            if w["layout"] == "chain" and "source" not in w:
                print("      ** chain layout requires a source **")
                bad += 1

    print()
    print("=== duplicated narration across sections ===")
    seen = {}
    dup = 0
    for name, i, vo in all_vo:
        sents = [x.strip().lower() for x in re.split(r"(?<=\.)\s+", vo) if x.strip()]
        for s in sents:
            if len(s.split()) >= 8:
                if s in seen:
                    print("  ** %r == %s win %d **" % (s[:70], seen[s][0], seen[s][1]))
                    dup += 1
                else:
                    seen[s] = (name, i)
    if not dup:
        print("  none (no sentence of 8+ words is repeated)")

    print()
    print("PROBLEMS: %d" % (bad + dup))
    return 0 if (bad + dup) == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["ep09_s5"]))
