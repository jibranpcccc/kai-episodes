# -*- coding: utf-8 -*-
import os, json
from playwright.sync_api import sync_playwright
ROOT = r"C:\Users\jibra\Desktop\1\KAI"
NAME = "BYTE-07-FUSION"
url = "file:///" + os.path.join(ROOT, NAME + ".html").replace("\\","/")
with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={"width":1920,"height":1080})
    pg.goto(url+"?t=0", wait_until="load"); pg.wait_for_timeout(400)
    pg.evaluate("(t)=>window.renderAt(t)", 12.34)
    pg.evaluate("()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(()=>r(1))))")
    out = pg.evaluate("""() => {
      const R=[1277,795,1522,807];
      const res=[];
      document.querySelectorAll('*').forEach(el=>{
        const b=el.getBoundingClientRect();
        if(b.width<2||b.height<2) return;
        if(b.right<R[0]||b.left>R[2]||b.bottom<R[1]||b.top>R[3]) return;
        res.push({tag:el.tagName, cls:el.getAttribute('class')||'', id:el.id||'',
                  x:Math.round(b.x), y:Math.round(b.y), w:Math.round(b.width), h:Math.round(b.height),
                  txt:(el.textContent||'').trim().slice(0,40),
                  anim:getComputedStyle(el).animationName+' '+getComputedStyle(el).animationPlayState,
                  op:getComputedStyle(el).opacity, tf:getComputedStyle(el).transform});
      });
      return res.slice(0,25);
    }""")
    for r in out: print(r)
    br.close()
