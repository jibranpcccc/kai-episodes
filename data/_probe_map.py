# -*- coding: utf-8 -*-
"""Map the built scenes against the spec windows, window by window."""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

EP = sys.argv[1] if len(sys.argv) > 1 else "BYTE-LORA"
SPEC = sys.argv[2] if len(sys.argv) > 2 else "spec_lora_full"
LO = int(sys.argv[3]) if len(sys.argv) > 3 else 1
HI = int(sys.argv[4]) if len(sys.argv) > 4 else 6
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

s = io.open(os.path.join(ROOT, EP + ".html"), encoding="utf-8").read()
F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", s, re.S).group(1))
scenes = F["scenes"]
words = F["words"]

import importlib
mod = importlib.import_module(SPEC)

print("html scenes: %d   spec windows: %d   html words: %d"
      % (len(scenes), len(mod.W), len(words)))
for i in range(LO - 1, min(HI, len(scenes))):
    sc = scenes[i]
    ws = [(t, w) for t, w in words if sc["s"] <= t <= sc["e"]]
    spoken = " ".join(w for _, w in ws[:8])
    written = " ".join(mod.W[i]["vo"].split()[:8])
    print()
    print("scene %2d  %8.2f -> %8.2f  (%d tokens)"
          % (i + 1, sc["s"], sc["e"], len(ws)))
    print("   spoken : %s" % spoken)
    print("   script : %s" % written)
