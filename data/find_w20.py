# -*- coding: utf-8 -*-
with open(r"C:\Users\jibra\Desktop\1\KAI\BYTE-STRUCTURED-OUTPUTS.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
m = re.search(r'<section class="scene" data-scene="20">(.*?)</section>', text, re.S)
if m:
    print(m.group(1))
