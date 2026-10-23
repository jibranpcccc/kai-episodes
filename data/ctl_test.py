from playwright.sync_api import sync_playwright
from pathlib import Path
url=Path("BYTE-02.html").resolve().as_uri()
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"])
    pg=b.new_page(viewport={"width":1440,"height":810})
    pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.goto(url); pg.wait_for_timeout(700)

    btns=pg.evaluate("[...document.querySelectorAll('#ctl button')].map(b=>b.textContent.trim())")
    print("buttons:", btns)

    for r in ["2","4","1.5","1"]:
        pg.click(f'#ctl .rate[data-r="{r}"]')
        rate=pg.evaluate("document.getElementById('vo').playbackRate")
        on=pg.evaluate("document.querySelector('#ctl .rate.on') && document.querySelector('#ctl .rate.on').textContent.trim()")
        print(f"  clicked {r}x -> playbackRate={rate}  highlighted={on}")

    pg.click("#ctlPlay"); pg.wait_for_timeout(1200)
    st=pg.evaluate("({t:document.getElementById('vo').currentTime, paused:document.getElementById('vo').paused})")
    print("after PLAY  :", st)

    pg.click("#ctlPlay"); pg.wait_for_timeout(300)
    st2=pg.evaluate("({t:document.getElementById('vo').currentTime, paused:document.getElementById('vo').paused})")
    print("after PAUSE :", st2)

    pg.click("#ctlStop"); pg.wait_for_timeout(300)
    st3=pg.evaluate("({t:document.getElementById('vo').currentTime, paused:document.getElementById('vo').paused, start:!document.getElementById('start').classList.contains('hide')})")
    print("after STOP  :", st3)

    pg.screenshot(path="proof/controls.png", clip={"x":1000,"y":640,"width":440,"height":170})
    print("errors:", errs[:3] if errs else "none")
    b.close()
