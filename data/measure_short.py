import os
from playwright.sync_api import sync_playwright
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
url="file:///"+os.path.join(ROOT,"BYTE-02-SHORT.html").replace("\\","/")
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.goto(url); pg.wait_for_timeout(600)
    pg.evaluate("document.body.classList.add('render')")
    m=pg.evaluate("""() => {
      const g=id=>{const e=document.getElementById(id),r=e.getBoundingClientRect(),c=getComputedStyle(e);
        return {w:Math.round(r.width),h:Math.round(r.height),css_h:c.height,transform:c.transform};};
      const sc=document.querySelector('.scene').getBoundingClientRect();
      return {wrap:g('wrap'), stage:g('stage'), scene:{w:Math.round(sc.width),h:Math.round(sc.height)},
              inner:[innerWidth,innerHeight]};
    }""")
    print(m)
    b.close()
