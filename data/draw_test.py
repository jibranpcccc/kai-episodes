from playwright.sync_api import sync_playwright
from pathlib import Path
url=Path("BYTE-02.html").resolve().as_uri()
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1920,"height":1080})
    pg.goto(url); pg.wait_for_timeout(600)
    pg.evaluate("()=>{document.body.classList.add('render'); window.renderAt(17);}")
    pg.wait_for_timeout(120)
    mid=pg.evaluate("""()=>{
        const el=document.querySelector('.scene.active .art path, .scene.active .art rect');
        if(!el) return 'no art';
        const cs=getComputedStyle(el);
        return {dash:cs.strokeDashoffset, anim:cs.animationName, dur:cs.animationDuration, len:el.getAttribute('pathLength')};
    }""")
    pg.wait_for_timeout(1100)
    done=pg.evaluate("""()=>{
        const el=document.querySelector('.scene.active .art path, .scene.active .art rect');
        return el?getComputedStyle(el).strokeDashoffset:'none';
    }""")
    print("mid-animation :", mid)
    print("after 1.2s    :", done)
    b.close()
