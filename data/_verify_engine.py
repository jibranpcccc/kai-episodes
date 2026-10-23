# -*- coding: utf-8 -*-
import hashlib
import io
import re

root = r"C:\Users\jibra\Desktop\1\KAI"


def h(b):
    return hashlib.sha256(b).hexdigest()[:16]


src = io.open(root + r"\BYTE-07-FUSION.html", encoding="utf-8").read()
css = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
js = re.search(r"<script>(.*?)</script>", src, re.S).group(1)

core_css = io.open(root + r"\core\fusion.css", encoding="utf-8").read()
core_js = io.open(root + r"\core\fusion.js", encoding="utf-8").read()

print("approved css  %s   core/fusion.css %s   %s" % (h(css.encode()), h(core_css.encode()),
      "MATCH" if css == core_css else "**DIFFERS**"))
print("approved js   %s   core/fusion.js  %s   %s" % (h(js.encode()), h(core_js.encode()),
      "MATCH" if js == core_js else "**DIFFERS**"))

out = io.open(root + r"\BYTE-LORA.html", encoding="utf-8").read()
print("deliverable links core engine:",
      ('href="core/fusion.css"' in out or "fusion.css" in out),
      ('src="core/fusion.js"' in out or "fusion.js" in out))
print("deliverable inlines engine    :", "<style>" in out and "fusion.css" not in out)