# -*- coding: utf-8 -*-
"""Does every window actually FILL its frame?

This is the check that was missing. Every other quality gate in the project
looked for overflows, collisions, missing beats and wrong captions -- and all
of them passed on an episode whose worst frames painted 1.8% of the canvas.
A window can be perfectly legal and still look empty: a small block of
content centred in a 630 px body band, with hundreds of dead pixels above
and below it.

So this measures the two things that decide whether a frame reads as full:

  INK    the fraction of the 1920x1080 canvas that differs from the
         background at the window's settled timestamp. A frame with a
         headline and a small diagram in the middle is around 2%.

  DEAD   the longest run of canvas rows, inside the window's own content
         band, that nothing paints at all.

Both are measured on the SETTLED frame (the window's last moment), because
that is the state the layout is judged on. The mid-window value is reported
too, since a window that is still nearly empty halfway through is a pacing
problem rather than a layout one.

    python data/_check_fill.py BYTE-EP09
"""
import io
import json
import os
import re
import sys

import numpy as np
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-EP09"

# A window below this much ink reads as an empty screen with a caption.
MIN_INK = 0.030
# A dead band wider than this is a hole in the middle of the composition.
MAX_DEAD = 300

results = []


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print("%s  %-46s %s" % ("PASS" if ok else "FAIL", name, detail))


def ink_and_dead(arr, bg):
    """ink fraction and the longest run of empty canvas rows"""
    mask = np.abs(arr.astype(np.int16) - bg) > 12
    ink = float(mask.mean())
    rows = mask.any(axis=1)
    best = cur = 0
    for r in rows:
        cur = 0 if r else cur + 1
        best = max(best, cur)
    return ink, best


def main():
    path = os.path.join(ROOT, NAME + ".html")
    text = io.open(path, encoding="utf-8").read()
    F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", text, re.S).group(1))
    scenes = F["scenes"]
    total = F["total"]
    url = "file:///" + path.replace("\\", "/")

    samples = []
    with sync_playwright() as pw:
        br = pw.chromium.launch(args=["--force-color-profile=srgb",
                                      "--font-render-hinting=none"])
        pg = br.new_page(viewport={"width": 1920, "height": 1080},
                          device_scale_factor=1)
        pg.goto(url + "?t=0", wait_until="load")
        pg.wait_for_timeout(2200)
        for s in scenes:
            settled = min(s["e"] - 0.35, total - 0.05)
            mid = s["s"] + (s["e"] - s["s"]) * 0.55
            row = {"label": s["label"], "s": s["s"], "e": s["e"]}
            for tag, t in (("set", settled), ("mid", mid)):
                pg.evaluate("(t) => window.renderAt(t)", t)
                shot = pg.screenshot(type="png")
                import tempfile
                with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as fh:
                    fh.write(shot)
                    tmp = fh.name
                from PIL import Image
                a = np.asarray(Image.open(tmp).convert("L"), dtype=np.uint8)
                os.unlink(tmp)
                bg = int(np.bincount(a.ravel(), minlength=256).argmax())
                ink, dead = ink_and_dead(a, bg)
                row["ink_" + tag] = ink
                row["dead_" + tag] = dead
            samples.append(row)
        br.close()

    print("FILL CHECK -- %s   %d windows" % (NAME, len(samples)))
    print()
    print("  window            settled ink   dead band   mid ink")
    for r in sorted(samples, key=lambda x: x["ink_set"]):
        print("  %-14s   %7.2f%%   %6d px   %6.2f%%"
              % (r["label"], r["ink_set"] * 100, r["dead_set"], r["ink_mid"] * 100))
    print()

    worst_ink = min(r["ink_set"] for r in samples)
    worst_dead = max(r["dead_set"] for r in samples)
    thin = [r["label"] for r in samples if r["ink_set"] < MIN_INK]
    holed = [r["label"] for r in samples if r["dead_set"] > MAX_DEAD]
    mid_thin = [r["label"] for r in samples if r["ink_mid"] < 0.015]

    check("every window paints enough of the frame", not thin,
          "thinnest %.2f%% (floor %.1f%%)%s"
          % (worst_ink * 100, MIN_INK * 100,
             "; thin: " + ", ".join(thin) if thin else ""))
    check("no window has a hole in the middle of it", not holed,
          "widest dead band %d px (limit %d)%s"
          % (worst_dead, MAX_DEAD,
             "; holed: " + ", ".join(holed) if holed else ""))

    print()
    if mid_thin:
        print("NOTE  %d window(s) are under 1.5%% ink at their midpoint -- that is"
              % len(mid_thin))
        print("      the progressive reveal, not a layout fault: %s"
              % ", ".join(mid_thin))
    print("median settled ink %.2f%%   mean %.2f%%"
          % (float(np.median([r["ink_set"] for r in samples])) * 100,
             float(np.mean([r["ink_set"] for r in samples])) * 100))

    bad = [r for r in results if not r[1]]
    print("\n%d passed, %d failed" % (len(results) - len(bad), len(bad)))
    if bad:
        raise SystemExit("FILL CHECK FAILED: " + "; ".join(r[0] for r in bad))
    print("FILL CHECK PASSED")


if __name__ == "__main__":
    main()
