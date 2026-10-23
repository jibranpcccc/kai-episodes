# -*- coding: utf-8 -*-
import io
import re

root = r"C:\Users\jibra\Desktop\1\KAI"
src = io.open(root + r"\BYTE-07-FUSION.html", encoding="utf-8").read()
runtime = [x for x in re.findall(r"<script>(.*?)</script>", src, re.S)
           if "FUSION \u2014 Byte Forensics runtime" in x or "Byte Forensics runtime" in x]
print("runtime blocks found:", len(runtime))
runtime = runtime[0]
core_js = io.open(root + r"\core\fusion.js", encoding="utf-8").read()


def norm(t):
    t = re.sub(r"data:[^)\"']+", "DATA", t)
    return t.replace("\r\n", "\n").strip()


print("RUNTIME IDENTICAL to core/fusion.js:", norm(runtime) == norm(core_js))
print("  approved runtime bytes:", len(runtime))
print("  core/fusion.js bytes  :", len(core_js))