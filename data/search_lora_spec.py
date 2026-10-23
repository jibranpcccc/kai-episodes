# -*- coding: utf-8 -*-
with open(r"C:\Users\jibra\Desktop\1\KAI\data\spec_lora_full.py", "r", encoding="utf-8") as f:
    text = f.read()

import re

keywords = ["25", "twenty-five", "382", "457", "wafer", "hardware-corner", "qwen3.8", "die"]
for kw in keywords:
    matches = [m.start() for m in re.finditer(re.escape(kw), text, re.I)]
    print(f"Keyword '{kw}': {len(matches)} occurrences")
    for pos in matches[:8]:
        line_no = text[:pos].count('\n') + 1
        line = text.splitlines()[line_no - 1]
        print(f"   L{line_no}: {line.strip()[:100]}")
