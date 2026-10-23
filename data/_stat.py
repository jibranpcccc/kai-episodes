# -*- coding: utf-8 -*-
import io
import json
import re

s = io.open(r"C:\Users\jibra\Desktop\1\KAI\BYTE-LORA.html", encoding="utf-8").read()
F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", s, re.S).group(1))
print("runtime %.1fs = %d:%02d" % (F["total"], F["total"] // 60, F["total"] % 60))
print("windows %d   beats %d   spoken words %d" % (len(F["scenes"]), len(F["beats"]), len(F["words"])))
arts = sorted(set(re.findall(r'data-art="([a-z0-9_]+)"', s)))
print("assets used (%d): %s" % (len(arts), ", ".join(arts)))