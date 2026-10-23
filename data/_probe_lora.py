# -*- coding: utf-8 -*-
"""Deep structural probe of a built FUSION deliverable.

    python data/_probe_lora.py BYTE-LORA

Prints the scene table, the beat rhythm law, and the density checks that
matter for the next build. Read-only: it never touches the deliverable.
"""
import io
import json
import os
import re
import statistics
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-LORA"

src = io.open(os.path.join(ROOT, NAME + ".html"), encoding="utf-8").read()
F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", src, re.S).group(1))

print("=" * 78)
print("FILE      :", NAME + ".html")
print("TITLE     :", F["title"])
print("KICKER    :", F["kicker"])
print("SUBTITLE  :", F["subtitle"])
print("TOTAL     : %.1fs  (= %d:%02d)" % (F["total"], F["total"] // 60, F["total"] % 60))
print("watermark :", F.get("watermark"), "| global_progress:", F.get("progress"))
print("scenes %d | beats %d | words %d"
      % (len(F["scenes"]), len(F["beats"]), len(F["words"])))

print()
print("=" * 78)
print("SCENE TABLE")
print("=" * 78)
per = defaultdict(list)
for b in F["beats"]:
    per[b["group"]].append(b)

for i, sc in enumerate(F["scenes"]):
    bs = sorted(per[i], key=lambda b: b["s"])
    dur = sc["e"] - sc["s"]
    print("%3d  %7.2f -> %7.2f  %6.2fs  %-16s beats=%2d"
          % (i, sc["s"], sc["e"], dur, sc["label"], len(bs)))
    for b in bs:
        extra = ""
        if b.get("anchor"):
            extra = "  <- %r" % b["anchor"][:44]
        print("        %7.2f  %-8s %-8s dur=%-5s%s"
              % (b["s"], b["kind"], b.get("ease"), b.get("dur"), extra))

print()
print("=" * 78)
print("RHYTHM / DENSITY")
print("=" * 78)
print("kind histogram:", Counter(b["kind"] for b in F["beats"]).most_common())
print("ease histogram:", Counter(b.get("ease") for b in F["beats"]).most_common())

gaps = []
for i in range(len(F["scenes"])):
    bs = sorted(per[i], key=lambda b: b["s"])
    for k in range(1, len(bs)):
        gaps.append(round(bs[k]["s"] - bs[k - 1]["s"], 3))
if gaps:
    gs = sorted(gaps)
    print("intra-scene beat gaps: n=%d min=%.3f med=%.3f mean=%.3f max=%.3f"
          % (len(gaps), gs[0], statistics.median(gaps), statistics.mean(gaps), gs[-1]))
    print("  gaps > 4.2s (warn):", sum(1 for g in gaps if g > 4.2),
          "  gaps > 6.0s (fail):", sum(1 for g in gaps if g > 6.0))

# dead air: longest silent stretch inside each scene
print()
print("DEAD AIR PER SCENE (scene start -> first beat, and beat -> scene end)")
worst = []
for i, sc in enumerate(F["scenes"]):
    bs = sorted(per[i], key=lambda b: b["s"])
    head = (bs[0]["s"] - sc["s"]) if bs else (sc["e"] - sc["s"])
    tail = (sc["e"] - bs[-1]["s"]) if bs else 0.0
    worst.append((max(head, tail), i, round(head, 2), round(tail, 2)))
    print("  scene %3d  head=%5.2fs  tail=%5.2fs  beats=%2d" % (i, head, tail, len(bs)))
worst.sort(reverse=True)
print("  worst dead spot:", worst[0])

durs = [round(sc["e"] - sc["s"], 2) for sc in F["scenes"]]
print()
print("scene durations: min %.2f  med %.2f  max %.2f" % (min(durs), statistics.median(durs), max(durs)))
print(durs)

# element census: how many animated elements per scene
print()
print("ELEMENT CENSUS (animated elements per scene)")
cnt = []
for i, sc in enumerate(F["scenes"]):
    n = len(per[i])
    cnt.append(n)
    if n < 4:
        print("  ** scene %d has only %d beats" % (i, n))
print("  min %d  med %.1f  max %d" % (min(cnt), statistics.median(cnt), max(cnt)))

# nudge / late audit
late = [b for b in F["beats"] if b.get("nudge", 0) > 1.0]
early = [b for b in F["beats"] if b.get("nudge", 0) < -2.0]
print()
print("nudge audit: LATE(>1.0s)=%d  TOO EARLY(<-2.0s)=%d" % (len(late), len(early)))

# assets used
assets = sorted(set(re.findall(r'id="w\d+_\d+"[^>]*class="artpanel"', src)))
print()
print("fonts embedded:", len(re.findall(r"@font-face", src)))
print("audio embedded:", "data:audio/mpeg;base64," in src,
      "%.2f MB" % (len(re.search(r"data:audio/mpeg;base64,([^\"]+)", src).group(1)) / 1048576.0))
print("file size: %.2f MB" % (os.path.getsize(os.path.join(ROOT, NAME + ".html")) / 1048576.0))

# ---------------------------------------------------------------- rule checks
print()
print("=" * 78)
print("EPISODE-RULES.md COMPLIANCE")
print("=" * 78)

labels = [sc["label"].split(" ", 1)[1] if " " in sc["label"] else sc["label"] for sc in F["scenes"]]
print("layout sequence:", " ".join(labels))
from collections import Counter
print("layout histogram:", Counter(labels).most_common())

runs = []
cur = labels[0]
n = 1
for x in labels[1:]:
    if x == cur:
        n += 1
    else:
        runs.append((cur, n))
        cur, n = x, 1
runs.append((cur, n))
bad = [r for r in runs if r[1] > 1]
print()
print("consecutive identical-layout runs:", bad if bad else "none")
print("  -> longest run:", max((r[1] for r in runs), default=0))

over = [(i, d) for i, d in enumerate(durs) if d > 20.0]
print()
print("windows LONGER than the 20 s rule: %d of %d" % (len(over), len(durs)))
for i, d in over:
    print("   scene %2d  %-8s %6.2fs" % (i, labels[i], d))
print("median window %.2fs (rule ~13s)" % statistics.median(durs))

# every window must carry a drawing
noart = []
for m in re.finditer(r'<section class="scene" data-scene="(\d+)">(.*?)</section>', src, re.S):
    if "<svg" not in m.group(2):
        noart.append(int(m.group(1)))
print()
print("windows with NO svg:", noart if noart else "none (all carry a drawing)")

# scene head/tail dead air, ranked
print()
print("worst 8 scenes by post-last-beat dead air (screen goes static):")
wt = sorted(((round(sc["e"] - max(b["s"] for b in per[i]), 2), i, labels[i]) for i, sc in enumerate(F["scenes"])), reverse=True)
for dead, i, lab in wt[:8]:
    print("   scene %2d  %-6s  %6.2fs static after the last reveal" % (i, lab, dead))
tot_dead = sum(d for d, _, _ in wt)
print("   total post-reveal static time across the episode: %.1fs of %.1fs (%.0f%%)"
      % (tot_dead, F["total"], 100.0 * tot_dead / F["total"]))

# what each window actually shows (layout -> component census in the HTML)
print()
print("=" * 78)
print("VISUAL VOCABULARY USED PER WINDOW (class census)")
print("=" * 78)
comps = ["row", "bar", "railrow", "chain__node", "note", "compare__col", "chip", "tape",
         "sticker", "gal__", "strip__", "nodes__", "crossout", "baseline", "cursor"]
for m in re.finditer(r'<section class="scene" data-scene="(\d+)">(.*?)</section>', src, re.S):
    i = int(m.group(1))
    body = m.group(2)
    hits = []
    for c in comps:
        n = len(re.findall(r'class="[^"]*\b%s' % re.escape(c), body))
        if n:
            hits.append("%s=%d" % (c.rstrip("_"), n))
    print("  scene %2d  %-6s  %s" % (i, labels[i], " ".join(hits)))
