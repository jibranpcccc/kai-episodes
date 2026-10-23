from playwright.sync_api import sync_playwright
from pathlib import Path
url=Path("BYTE-01.html").resolve().as_uri()
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1920,"height":1080})
    pg.goto(url); pg.wait_for_timeout(800)
    print("SCENES:", pg.evaluate("JSON.stringify(window.EPISODE.scenes)"))
    for T in (16.6, 47.5):
        info=pg.evaluate("""(T)=>{
            window.renderAt(T);
            const act=[...document.querySelectorAll('.scene')].findIndex(s=>s.classList.contains('active'));
            const sc=document.querySelectorAll('.scene')[act];
            const on=sc? sc.querySelectorAll('[data-in].on').length : -1;
            const tot=sc? sc.querySelectorAll('[data-in]').length : -1;
            const fill=sc? sc.querySelector('.bf-bar__fill') : null;
            const rect=fill? fill.getBoundingClientRect() : null;
            return {T, act, on, tot,
                    fill: rect? {w:Math.round(rect.width), h:Math.round(rect.height), cls:fill.className}:null,
                    html: sc? sc.innerHTML.slice(0,120):null};
        }""", T)
        print(info)
    b.close()
