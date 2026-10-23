import os
from playwright.sync_api import sync_playwright
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
url="file:///"+os.path.join(ROOT,"BYTE-02-SHORT.html").replace("\\","/")
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.goto(url); pg.wait_for_timeout(700)
    pg.evaluate("""()=>{document.body.classList.add('render');
      const vo=document.getElementById('vo'); window.__T=0;
      Object.defineProperty(vo,'currentTime',{get:()=>window.__T,set:v=>{}});}""")
    for T,tag in [(4,"a"),(22,"b")]:
        pg.evaluate("t=>{window.__T=t;window.renderAt(t);}", T)
        pg.wait_for_timeout(500)
        pg.screenshot(path=os.path.join(ROOT,"proof",f"short2_{tag}.png"))
    b.close()
print("shots ok")
