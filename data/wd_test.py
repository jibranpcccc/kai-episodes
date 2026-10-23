from playwright.sync_api import sync_playwright
from pathlib import Path
url=Path("BYTE-02.html").resolve().as_uri()
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1920,"height":1080})
    pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.goto(url); pg.wait_for_timeout(600)
    pg.evaluate("""()=>{
        window.__T=0;
        const vo=document.getElementById('vo');
        vo.play=()=>Promise.resolve();
        Object.defineProperty(vo,'currentTime',{get:()=>window.__T,set:v=>{window.__T=v;}});
    }""")
    pg.click("#start")
    pg.evaluate("window.__T=30"); pg.wait_for_timeout(300)
    a=pg.evaluate("document.querySelectorAll('[data-in].on').length")
    tc_a=pg.evaluate("document.getElementById('tc').textContent")

    # simulate a background tab: rAF stops firing entirely
    pg.evaluate("window.requestAnimationFrame = function(){ return 0; };")
    pg.evaluate("window.__T=70"); pg.wait_for_timeout(900)
    b_on=pg.evaluate("document.querySelectorAll('[data-in].on').length")
    tc_b=pg.evaluate("document.getElementById('tc').textContent")
    act=pg.evaluate("[...document.querySelectorAll('.scene')].findIndex(s=>s.classList.contains('active'))")

    print(f"before throttle: on={a}  tc={tc_a}")
    print(f"after  throttle: on={b_on}  tc={tc_b}  active_scene={act}")
    print("verdict:", "WATCHDOG WORKS" if tc_b!=tc_a and b_on!=a else "STILL FROZEN")
    print("errors:", errs[:3] if errs else "none")
    b.close()
