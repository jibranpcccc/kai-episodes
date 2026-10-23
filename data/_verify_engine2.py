# -*- coding: utf-8 -*-
import io
import re
import difflib

root = r"C:\Users\jibra\Desktop\1\KAI"
src = io.open(root + r"\BYTE-07-FUSION.html", encoding="utf-8").read()
css = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
js = re.search(r"<script>(.*?)</script>", src, re.S).group(1)
core_css = io.open(root + r"\core\fusion.css", encoding="utf-8").read()
core_js = io.open(root + r"\core\fusion.js", encoding="utf-8").read()


def strip_fonts(t):
    t = re.sub(r"@font-face\s*\{.*?\}", "", t, flags=re.S)
    t = re.sub(r"data:[^)\"']+", "DATA", t)
    return re.sub(r"\s+", " ", t).strip()


a, b = strip_fonts(css), strip_fonts(core_css)
print("CSS  identical after removing @font-face/data URIs:", a == b)
if a != b:
    r = list(difflib.unified_diff(a.split("}"), b.split("}"), lineterm="", n=1))
    print("   css diff hunks:", len([x for x in r if x.startswith(("+", "-")) and not x.startswith(("+++", "---"))]))

a, b = strip_fonts(js), strip_fonts(core_js)
print("JS   identical after removing @font-face/data URIs:", a == b)
if a != b:
    r = list(difflib.unified_diff(a.split("\n"), b.split("\n"), lineterm="", n=0))
    for x in r[:20]:
        print("   ", x[:150])