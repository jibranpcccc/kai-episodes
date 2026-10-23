# -*- coding: utf-8 -*-
import io
import re

root = r"C:\Users\jibra\Desktop\1\KAI"
src = io.open(root + r"\BYTE-07-FUSION.html", encoding="utf-8").read()
scripts = re.findall(r"<script>(.*?)</script>", src, re.S)
print("script blocks in approved file:", [len(x) for x in scripts])
runtime = max(scripts, key=len)
print("runtime block starts:", runtime.strip()[:60].replace("\n", " "))
core_js = io.open(root + r"\core\fusion.js", encoding="utf-8").read()
print("core/fusion.js starts:", core_js.strip()[:60].replace("\n", " "))


def norm(t):
    t = re.sub(r"data:[^)\"']+", "DATA", t)
    return t.strip()


print("RUNTIME IDENTICAL:", norm(runtime) == norm(core_js))
if norm(runtime) != norm(core_js):
    import difflib
    r = list(difflib.unified_diff(norm(runtime).split("\n"), norm(core_js).split("\n"), lineterm="", n=0))
    print("hunks:", len(r))
    for x in r[:12]:
        print("  ", x[:160])