# -*- coding: utf-8 -*-
"""Find why a spoken word falls outside every caption cue in one window."""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

from fusion_build import _align_tokens, _groups

EP = sys.argv[1] if len(sys.argv) > 1 else "BYTE-LORA"
WIN = int(sys.argv[2]) if len(sys.argv) > 2 else 21
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

s = io.open(os.path.join(ROOT, EP + ".html"), encoding="utf-8").read()
F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", s, re.S).group(1))
scenes = F["scenes"]
words = F["words"]

sc = scenes[WIN - 1]
lo, hi = sc["s"], sc["e"]
ws = [(t, w) for t, w in words if lo <= t <= hi]
print("window %d  %s -> %s   (%d tokens)" % (WIN, lo, hi, len(ws)))
print("first 12 tokens:", [w for _, w in ws[:12]])

import importlib
mod = importlib.import_module(sys.argv[3] if len(sys.argv) > 3 else "spec_lora_full")
vw = mod.W[WIN - 1]["vo"].split()
print()
print("vo (%d words):" % len(vw))
print("  ", " ".join(vw[:14]))
print()
tok = _align_tokens(vw, ws)
print("first 12 token indices:", tok[:12])
print()
print("token index -> word:", [(i, ws[i][1]) for i in range(min(8, len(ws)))])
print()
cues = F.get("cues")
