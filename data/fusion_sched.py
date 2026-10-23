# -*- coding: utf-8 -*-
"""Read a built FUSION html and print the beat schedule with gaps."""
import io
import json
import re
import sys

p = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\jibra\Desktop\1\KAI\BYTE-07-FUSION.html"
s = io.open(p, encoding="utf-8").read()
m = re.search(r"window\.FUSION = (\{.*?\});</script>", s, re.S)
F = json.loads(m.group(1))

scenes = F["scenes"]
beats = F["beats"]
words = F["words"]
print("runtime %.2fs   words %d   beats %d" % (F["total"], len(words), len(beats)))
print()

for sc in scenes:
    bs = [b for b in beats if b["group"] == sc["id"]]
    print("=== scene %d  %.2f - %.2f  (%5.2fs)  beats=%d"
          % (sc["id"] + 1, sc["s"], sc["e"], sc["e"] - sc["s"], len(bs)))
    prev = sc["s"]
    for b in bs:
        gap = b["s"] - prev
        flag = ""
        if gap > 5.0:
            flag = "   <<< DEAD SPOT"
        elif gap > 3.0:
            flag = "   <-- long"
        print("   %7.2f  gap %5.2f  %-8s %-34s %-22s nudge %+.2f%s"
              % (b["s"], gap, b["kind"], (b.get("anchor") or "")[:34],
                 b["el"], b.get("nudge", 0), flag))
        prev = b["s"]
    print()
