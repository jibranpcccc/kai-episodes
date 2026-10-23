# -*- coding: utf-8 -*-
"""
EPISODE 09 -- THE FULL EPISODE
===============================
  "WHY A LONGER CONTEXT COSTS YOU MORE MEMORY"
  the cache is a second bill

This module is the index. It stitches the episode together from its parts:

  spec_ep09_kv   windows  1- 7   the paradox            (act 1)
  ep09_s2        windows  8-16   what the cache is      (act 2)
  ep09_s3        windows 17-25   what was measured      (act 3)
  ep09_s4        windows 26-33   what changes the bill  (act 4)
  ep09_s5        windows 34-38   the measurement        (act 5)

The window map, the voice rules, the number bank and the code contract live
in data/ep09_plan.py. Read that before changing anything here.

    FUSION_SPEC=spec_ep09_full python data/fusion_build.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import spec_ep09_kv
import ep09_s2
import ep09_s3
import ep09_s4
import ep09_s5

NAME = "BYTE-EP09"
TITLE = "WHY A LONGER CONTEXT COSTS YOU MORE MEMORY"
DOC_TITLE = "WHY A LONGER CONTEXT COSTS YOU MORE MEMORY &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; EPISODE 09"
SUBTITLE = "the cache is a second bill"
GLOBAL_PROGRESS = False

# The chapter list a viewer navigates on YouTube. The first chapter starts
# at 00:00, there are at least three, and every one of them runs for at
# least ten seconds, so these are grouped by idea and not by scene.
CHAPTERS = [
    (1, "THE SECOND BILL"),
    (2, "HOW THE CACHE FILLS"),
    (3, "THE ARITHMETIC, THEN THE MEASURED CURVE"),
    (5, "THE WAIT, THE BOUNDARY, THE ORDER"),
    (8, "THREE THINGS CALLED MEMORY"),
    (10, "WHAT IS INSIDE THE CACHE"),
    (14, "THE CACHE SCALES WITH CONTEXT"),
    (17, "WHAT WAS MEASURED"),
    (26, "WHAT THE HARDWARE ACTUALLY DOES"),
    (30, "HOLDING THE CACHE COARSER"),
    (34, "MEASURING BEFORE YOU BUY"),
    (43, "WHAT FITS, AND THE VERDICT"),
]

W = (list(spec_ep09_kv.W)
     + list(ep09_s2.W)
     + list(ep09_s3.W)
     + list(ep09_s4.W)
     + list(ep09_s5.W))

if __name__ == "__main__":
    print("EPISODE 09 -- %d windows" % len(W))
    for i, w in enumerate(W):
        print("  %2d  %-8s %-14s %3d words" % (i + 1, w["layout"],
                                                w.get("art", "-"),
                                                len(w["vo"].split())))
