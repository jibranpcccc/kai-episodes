from playwright.sync_api import sync_playwright
from pathlib import Path
url=Path("BYTE-02.html").resolve().as_uri()
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1920,"height":1080})
    pg.on("pageerror", lambda e: errs.append(str(e)[:300]))
    pg.on("console", lambda m: errs.append("console:"+m.text[:200]) if m.type=="error" else None)
    pg.goto(url); pg.wait_for_timeout(600)
    pg.evaluate("""()=>{
        window.__T=0;
        const vo=document.getElementById('vo');
        vo.play=function(){return Promise.resolve();};
        Object.defineProperty(vo,'currentTime',{get:()=>window.__T,set:v=>{window.__T=v;}});
    }""")
    pg.click("#start")
    # advance the clock in 0.5s steps and watch the state
    rows=[]
    for i in range(0, 460, 5):
        pg.evaluate(f"window.__T={i}")
        pg.wait_for_timeout(60)
        st=pg.evaluate("""()=>{
            const act=[...document.querySelectorAll('.scene')].findIndex(s=>s.classList.contains('active'));
            const sc=document.querySelectorAll('.scene')[act];
            const on=sc?sc.querySelectorAll('[data-in].on').length:-1;
            return {act, on, tc:document.getElementById('tc').textContent,
                    bar:document.getElementById('bar').style.width};
        }""")
        rows.append((i,st))
    for t,st in rows:
        if t%20==0 or st["on"]==0:
            print(f"  t={t:3}s active={st['act']:2} on={st['on']:3} tc='{st['tc']}' bar={st['bar']}")
    print("\nJS errors:", errs[:6] if errs else "none")
    b.close()
