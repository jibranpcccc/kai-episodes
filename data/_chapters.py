# -*- coding: utf-8 -*-
"""YouTube chapter file for a built episode.

The builder writes one chapter per window, which is a scene index and not a
chapter list: on YouTube a chapter has to run for at least ten seconds, the
first one has to start at 00:00, and a list of 45 micro-chapters is noise.
This groups the windows into chapters a viewer can actually navigate, and
checks the result against the rules before it writes anything.

    python data/_chapters.py BYTE-EP09-FINAL
"""
import importlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "data"))
MIN_SECONDS = 10.0


def groups_for(name):
    """The chapter grouping the spec declares. The spec is the only place
    the chapter list is written down."""
    for mod in ("spec_ep09_full", "spec_ep09_kv"):
        try:
            spec = importlib.import_module(mod)
        except ImportError:
            continue
        if getattr(spec, "NAME", None) == name and getattr(spec, "CHAPTERS", None):
            return spec.CHAPTERS
    raise SystemExit("no spec declares chapters for %s" % name)


def read_scenes(html_path):
    """The scene table the builder wrote into the page."""
    with open(html_path, encoding="utf-8") as fh:
        text = fh.read()
    m = re.search(r"window\.FUSION\s*=\s*(\{.*?\});", text, re.S)
    if not m:
        raise SystemExit("could not find window.FUSION in %s" % html_path)
    return json.loads(m.group(1))["scenes"]


def stamp(seconds):
    seconds = int(round(seconds))
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    if h:
        return "%d:%02d:%02d" % (h, m, s)
    return "%d:%02d" % (m, s)


def main(name):
    html_path = os.path.join(ROOT, name + ".html")
    if not os.path.exists(html_path):
        raise SystemExit("%s does not exist" % html_path)
    scenes = read_scenes(html_path)
    starts = {s["id"] + 1: s["s"] for s in scenes}
    total = max(s["e"] for s in scenes)

    rows = []
    for w, title in groups_for(name):
        rows.append((starts[w], title))
    rows.sort()

    problems = []
    if len(rows) < 3:
        problems.append("only %d chapters" % len(rows))
    if rows[0][0] != 0:
        problems.append("the first chapter starts at %.3fs" % rows[0][0])
    for i in range(len(rows) - 1):
        d = rows[i + 1][0] - rows[i][0]
        if d < MIN_SECONDS:
            problems.append("chapter %r is only %.1fs long"
                            % (rows[i][1], d))
    titles = [r[1] for r in rows]
    if len(set(titles)) != len(titles):
        problems.append("two chapters share a title")
    if problems:
        for p in problems:
            print("  CHAPTER PROBLEM: %s" % p)
        raise SystemExit("CHAPTER CHECK FAILED")

    out = os.path.join(ROOT, name + "-CHAPTERS.txt")
    with open(out, "w", encoding="utf-8") as fh:
        for t, title in rows:
            fh.write("%s %s\n" % (stamp(t), title))
    print("wrote %s  (%d chapters, %s total)"
          % (out, len(rows), stamp(total)))
    for i, (t, title) in enumerate(rows):
        end = rows[i + 1][0] if i + 1 < len(rows) else total
        print("   %-8s %-42s %.1fs" % (stamp(t), title, end - t))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "BYTE-EP09")
