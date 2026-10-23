from playwright.sync_api import sync_playwright
from pathlib import Path
url=Path("BYTE-01.html").resolve().as_uri()
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1920,"height":1080})
    pg.goto(url); pg.wait_for_timeout(700)
    out=pg.evaluate("""()=>{
        window.renderAt(16.6);
        const sc=document.querySelectorAll('.scene')[1];
        const track=sc.querySelector('.bf-bar__track');
        const fill=sc.querySelector('.bf-bar__fill');
        const tr=track.getBoundingClientRect(), fr=fill.getBoundingClientRect();
        const cs=getComputedStyle(fill);
        return {
          track:{w:Math.round(tr.width),h:Math.round(tr.height),flex:getComputedStyle(track).flex},
          fill:{w:Math.round(fr.width),h:Math.round(fr.height)},
          cssWidth:cs.width, cssVarW:cs.getPropertyValue('--w'),
          inlineStyle: fill.getAttribute('style'),
          rules:[...document.styleSheets].flatMap(s=>{try{return [...s.cssRules]}catch(e){return []}})
                .filter(r=>r.selectorText && r.selectorText.includes('grow'))
                .map(r=>r.selectorText+' {'+r.style.cssText+'}')
        };
    }""")
    import json; print(json.dumps(out, indent=1))
    b.close()
