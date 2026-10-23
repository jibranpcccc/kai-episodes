# -*- coding: utf-8 -*-
"""
Restore the APPROVED engine.

BYTE-07-FUSION.html is the video the owner approved 100%. It has the styling
frozen inside it. Extract the CSS and the JS back out of that file, put the
font data URIs back to file references, and write them to core/.

This is the reference everything else must match.
"""
import io
import os
import re

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
SRC = os.path.join(ROOT, "BYTE-07-FUSION.html")

s = io.open(SRC, encoding="utf-8").read()

# ---- the CSS is the only <style> block --------------------------------
m = re.search(r"<style>(.*?)</style>", s, re.S)
css = m.group(1).strip()

# ---- the JS is the second <script> block -----------------------------
scripts = re.findall(r"<script>(.*?)</script>", s, re.S)
print("script blocks:", len(scripts))
js = None
for blk in scripts:
    if "window.FUSION" in blk:
        continue
    if "FUSION" in blk or "renderAt" in blk:
        js = blk
        break
if js is None:
    js = scripts[-1]
js = js.strip()

# ---- put the fonts back as file references ---------------------------
FONTS = {
    ("FuseMono", "400"): "JetBrainsMono-Regular.ttf",
    ("FuseMono", "500"): "JetBrainsMono-Medium.ttf",
    ("FuseMono", "700"): "JetBrainsMono-Bold.ttf",
    ("FuseMono", "800"): "JetBrainsMono-ExtraBold.ttf",
    ("FuseDisplay", "400"): "Anton-Regular.ttf",
    ("FuseBlack", "400"): "ArchivoBlack-Regular.ttf",
}
used = []


def fix_face(m):
    block = m.group(0)
    fam = re.search(r'font-family:"([^"]+)"', block)
    wgt = re.search(r"font-weight:(\d+)", block)
    key = (fam.group(1) if fam else "", wgt.group(1) if wgt else "400")
    fn = FONTS.get(key)
    if not fn:
        return block
    used.append(fn)
    return re.sub(r"url\(data:font/ttf;base64,[^)]+\)", 'url("fonts/%s")' % fn, block)


css = re.sub(r"@font-face\{.*?\}", fix_face, css, flags=re.S)

# ---- write them -------------------------------------------------------
for path, content, label in [
    (os.path.join(ROOT, "core", "fusion.css"), css, "core/fusion.css"),
    (os.path.join(ROOT, "core", "fusion.js"), js, "core/fusion.js"),
]:
    bak = path + ".new"
    if os.path.exists(path):
        os.replace(path, bak)
    open(path, "w", encoding="utf-8").write(content)
    print("restored %-20s %6d bytes" % (label, len(content)))

print("fonts referenced:", sorted(set(used)))
missing = [f for f in set(used) if not os.path.exists(os.path.join(ROOT, "core", "fonts", f))]
print("missing font files:", missing or "none")
