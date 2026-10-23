# -*- coding: utf-8 -*-
"""Prove a NEW library asset drops into a scene and builds + gates clean."""
import io
import os
import subprocess
import sys

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
sys.path.insert(0, os.path.join(ROOT, "data"))

# a scratch spec that uses assets the approved episode never touches
spec = '''# -*- coding: utf-8 -*-
"""Scratch spec: proves the library is usable by the builder."""
NAME = "LIBTEST"
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


win("bars",
    vo="Here is a die, a fan, and a memory stick. The library has to supply the "
       "drawings and the engine has to place them.",
    kicker="LIBRARY TEST",
    title="NEW ASSETS, SAME ENGINE",
    sub="drawn from data/fusion_art.py",
    art="chip",
    art_caption="SILICON DIE",
    header_at="Here is a die",
    art_at="a fan",
    bars=[
        dict(lab="A", val="1", pct=100.0, cls="", at="a fan"),
        dict(lab="B", val="2", pct=60.0, cls="red", at="and a memory stick"),
    ],
    closing=dict(t="IT JUST WORKS", c="cyan", at="The library has to supply"),
    source="library smoke test")

win("rows",
    vo="And a second window using a different drawing, a memory bank.",
    kicker="LIBRARY TEST",
    title="SECOND WINDOW",
    sub="a different asset",
    art="ram_stick",
    art_caption="DDR5 DIMM",
    header_at="And a second window",
    art_at="a different drawing",
    rows=[
        dict(rank="01", name="A", val="100", sub="x", cls="gold", at="a different drawing"),
        dict(rank="02", name="B", val="50", sub="x", cls="red", at="a memory bank"),
    ],
    closing=dict(t="DONE", c="red", at="a memory bank"),
    source="library smoke test")
'''
p = os.path.join(ROOT, "data", "spec_libtest.py")
open(p, "w", encoding="utf-8").write(spec)

# run the builder against it
src = open(os.path.join(ROOT, "data", "fusion_build.py"), encoding="utf-8").read()
src2 = src.replace('NAME = "BYTE-07-FUSION"', 'NAME = "LIBTEST"')
src2 = src2.replace("import spec_07_fusion as spec", "import spec_libtest as spec")
open(os.path.join(ROOT, "data", "_build_libtest.py"), "w", encoding="utf-8").write(src2)
r = subprocess.run([sys.executable, os.path.join(ROOT, "data", "_build_libtest.py")],
                   capture_output=True, text=True, cwd=os.path.join(ROOT, "data"))
print(r.stdout[-1500:])
if r.returncode != 0:
    print("STDERR:", r.stderr[-2000:])

out = os.path.join(ROOT, "LIBTEST.html")
if os.path.exists(out):
    print("\nBUILT:", out, "%.2f MB" % (os.path.getsize(out) / 1048576.0))
    # render one frame of each scene to prove the new drawings landed
    from playwright.sync_api import sync_playwright
    import io as _io
    from PIL import Image
    url = "file:///" + out.replace("\\", "/")
    shots = []
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": 1920, "height": 1080})
        pg.goto(url + "?t=0", wait_until="load")
        pg.wait_for_timeout(400)
        pg.evaluate("() => document.fonts.ready")
        for t in (6.0, 14.0):
            pg.evaluate("(t) => window.renderAt(t)", t)
            pg.evaluate("() => new Promise(r => requestAnimationFrame("
                        "() => requestAnimationFrame(() => r(1))))")
            shots.append(Image.open(_io.BytesIO(pg.screenshot())).convert("RGB"))
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        br.close()
    sh = Image.new("RGB", (2 * 960 + 12, 540 + 12), (8, 10, 10))
    for k, im in enumerate(shots):
        sh.paste(im.resize((960, 540)), (6 + k * 966, 6))
    sh.save(os.path.join(ROOT, "proof", "_libtest.jpg"), quality=93)
    print("wrote proof/_libtest.jpg")
else:
    print("BUILD FAILED")
