import os
from playwright.sync_api import sync_playwright
from PIL import Image
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
url="file:///"+os.path.join(ROOT,"BYTE-02-SHORT.html").replace("\\","/")
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920}, device_scale_factor=1)
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
    pg.goto(url); pg.wait_for_timeout(800)
    pg.evaluate("""() => {
        document.body.classList.add('render');
        const vo = document.getElementById('vo');
        window.__T = 0;
        Object.defineProperty(vo, 'currentTime', {get: () => window.__T, set: v => {}});
    }""")
    for T,tag in [(4,"a"),(22,"b"),(36,"c")]:
        pg.evaluate("t => { window.__T = t; window.renderAt(t); }", T)
        pg.wait_for_timeout(500)
        pg.screenshot(path=os.path.join(ROOT,"proof",f"short_{tag}.png"))
        im=Image.open(os.path.join(ROOT,"proof",f"short_{tag}.png"))
        print(f"  t={T}s  {im.size}")
    st=pg.evaluate("({total:window.EPISODE.total, scenes:window.EPISODE.scenes.length, boxes:document.querySelectorAll('.scene').length, w:document.getElementById('stage').getBoundingClientRect().width})")
    print("state:", st, " errors:", errs[:2] if errs else "none")
    b.close()
