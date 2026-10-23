import os
from playwright.sync_api import sync_playwright
from PIL import Image
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
url="file:///"+os.path.join(ROOT,"BYTE-02.html").replace("\\","/")
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1920,"height":1080})
    pg.goto(url); pg.wait_for_timeout(800)
    pg.evaluate("""()=>{document.body.classList.add('render');
      const vo=document.getElementById('vo'); window.__T=0;
      Object.defineProperty(vo,'currentTime',{get:()=>window.__T,set:v=>{}});}""")
    for t in (199,200,201,202,240,300):
        pg.evaluate("t=>{window.__T=t;window.renderAt(t);}", t)
        pg.wait_for_timeout(350)
        f=os.path.join(ROOT,"proof",f"slate_{t}.png"); pg.screenshot(path=f)
        im=Image.open(f).convert("RGB"); w,h=im.size; px=im.load()
        br=sum(1 for y in range(0,h,4) for x in range(0,w,4) if sum(px[x,y])>330)
        print(f"  t={t}s bright={br:5d} {'<-- still sparse' if br<300 else 'ok'}")
    b.close()
