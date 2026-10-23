"""Export stills from an episode as thumbnails (default 1280x720).

    python data/thumb.py BYTE-02.html --t 17 --out thumbnails/ep02.png
    python data/thumb.py BYTE-02.html --t 17 --t 48 --dir thumbnails
"""
import argparse, os, sys
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HARNESS = """() => {
  var vo = document.getElementById('vo');
  try { vo.play = function(){ return Promise.resolve(); }; } catch(e){}
  try { Object.defineProperty(vo, 'currentTime',
        { get: function(){ return window.__T; }, set: function(v){} }); } catch(e){}
}"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--t", type=float, action="append", required=True)
    ap.add_argument("--out")
    ap.add_argument("--dir", default="thumbnails")
    ap.add_argument("--w", type=int, default=1280)
    ap.add_argument("--h", type=int, default=720)
    a = ap.parse_args()

    html = a.html if os.path.isabs(a.html) else os.path.join(ROOT, a.html)
    if not os.path.exists(html):
        sys.exit(f"not found: {html}")
    stem = os.path.splitext(os.path.basename(html))[0]

    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        pg.goto("file:///" + html.replace("\\", "/"))
        pg.wait_for_timeout(700)
        pg.evaluate(HARNESS)
        pg.evaluate("document.body.classList.add('render')")

        for t in a.t:
            if a.out and len(a.t) == 1:
                out = a.out if os.path.isabs(a.out) else os.path.join(ROOT, a.out)
            else:
                out = os.path.join(ROOT, a.dir, f"{stem}-t{int(t):03d}.png")
            os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
            pg.evaluate(f"window.__T = {t}")
            pg.evaluate(f"window.renderAt({t})")
            pg.wait_for_timeout(450)          # let draw-on finish
            raw = out + ".raw.png"
            pg.screenshot(path=raw)
            im = Image.open(raw).convert("RGB")
            if (im.width, im.height) != (a.w, a.h):
                im = im.resize((a.w, a.h), Image.LANCZOS)
            im.save(out, optimize=True)
            os.remove(raw)
            print("ok   " + os.path.abspath(out))
        b.close()


if __name__ == "__main__":
    main()
