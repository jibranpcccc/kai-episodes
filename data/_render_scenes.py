# -*- coding: utf-8 -*-
"""Render the corrected scenes and check the page in a real browser.

The plan is driven by WINDOW INDEX, not by hard-coded seconds, so the frames
always cover the content the repair touched no matter how the timeline drifts.
The brief's own named time ranges are kept as the first column of labels.

It renders a frame from each planned range, plus one frame from every one of
the 45 windows, saves the PNGs, and reports any console error the page
produced while it was open. It also measures the canvas, so an element that
has left the 1920x1080 stage is caught here and not by eye.

    python data/_render_scenes.py BYTE-EP09
"""
import io
import json
import os
import re
import sys

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-EP09"
OUT = os.path.join(ROOT, "proof", NAME + "_scenes")

# (label, first window, last window) -- 1-based window numbers.
# The first column reproduces the time range the brief named; the window
# numbers are what actually guarantee the corrected content is captured.
RANGES = [
    ("OPENING 0:00-0:10", 1, 2),
    ("KV PERSISTENCE 1:57-2:13", 9, 9),
    ("HARDWARE DATA 4:30-4:52", 18, 21),
    ("MEMORY SCALING 4:52-5:27", 22, 23),
    ("CACHE SHARING 8:22-8:44", 37, 38),
    ("SPEED COMPARISON 8:44-9:03", 39, 39),
    ("CLOSING last 30s", 44, 45),
]


def main():
    path = os.path.join(ROOT, NAME + ".html")
    text = io.open(path, encoding="utf-8").read()
    F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", text, re.S).group(1))
    scenes = F["scenes"]
    total = F["total"]
    os.makedirs(OUT, exist_ok=True)

    def win_span(a, b):
        """the seconds covered by windows a..b (1-based), clipped to the runtime"""
        lo = scenes[a - 1]["s"]
        hi = scenes[min(b, len(scenes)) - 1]["e"]
        return lo, min(hi, total)

    plan = []
    for label, a, b in RANGES:
        lo, hi = win_span(a, b)
        # three frames per range: its start, its middle and its end
        for frac, tag in ((0.15, "a"), (0.5, "b"), (0.85, "c")):
            t = lo + (hi - lo) * frac
            if t > total:
                continue
            w = None
            for s in scenes:
                if s["s"] <= t < s["e"]:
                    w = s
                    break
            plan.append((label, tag, round(t, 2),
                         w["label"] if w else "?"))

    # one frame from every window, so nothing in the episode is unsampled
    for s in scenes:
        t = s["s"] + (s["e"] - s["s"]) * 0.55
        if t > total:
            t = s["e"] - 0.05
        plan.append(("EVERY WINDOW", "w%02d" % (s["id"] + 1), round(t, 2), s["label"]))

    url = "file:///" + path.replace("\\", "/")

    shots = []
    errs = []
    with sync_playwright() as pw:
        br = pw.chromium.launch(args=["--force-color-profile=srgb",
                                      "--font-render-hinting=none"])
        pg = br.new_page(viewport={"width": 1920, "height": 1080},
                          device_scale_factor=1)
        pg.on("console", lambda m: errs.append(m.type + ": " + m.text)
              if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append("pageerror: " + str(e)))
        for label, tag, t, wlabel in plan:
            pg.goto(url + "?t=%.2f" % t, wait_until="load")
            pg.wait_for_timeout(420)
            # the stage has to be exactly 1920x1080 and fully painted
            box = pg.evaluate("""() => {
                const s = document.getElementById('stage');
                const r = s.getBoundingClientRect();
                let bad = [];
                document.querySelectorAll('#stage *').forEach(el => {
                  const b = el.getBoundingClientRect();
                  if (b.width === 0 && b.height === 0) return;
                  if (b.left < -2 || b.top < -2 || b.right > 1922 || b.bottom > 1082) {
                    bad.push((el.id || el.className || el.tagName) + ' ' +
                             [b.left,b.top,b.right,b.bottom].map(v=>Math.round(v)).join(','));
                  }
                });
                return {w: r.width, h: r.height, spill: bad.slice(0,6),
                        n: bad.length};
            }""")
            name = "%s_%s_%07.2f.png" % (re.sub(r"[^A-Za-z0-9]+", "_", label),
                                         tag, t)
            p = os.path.join(OUT, name)
            pg.screenshot(path=p)
            shots.append((label, tag, t, wlabel, p, box))
        br.close()

    print("RENDER -- %s" % NAME)
    for label, tag, t, wlabel, p, box in shots:
        flag = ""
        if box["n"]:
            flag = "  <-- %d element(s) outside the canvas" % box["n"]
        print("   %-28s %-6s t=%7.2f  %-12s %s%s"
              % (label, tag, t, wlabel, os.path.basename(p), flag))
        for s in box["spill"]:
            print("        spill: %s" % s)
    if errs:
        print("\nCONSOLE ERRORS")
        for e in errs[:20]:
            print("   %s" % e)
    else:
        print("\nno console errors in %d page loads" % len(shots))
    print("\n%d frames in %s" % (len(shots), OUT))
    if errs:
        raise SystemExit("RENDER FAILED: console errors")


if __name__ == "__main__":
    main()
