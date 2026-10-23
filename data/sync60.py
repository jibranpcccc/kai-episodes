import json, math, pathlib
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
D=json.loads(pathlib.Path(ROOT+"/data/w60.json").read_text())
AUD=pathlib.Path(ROOT+"/data/w60.b64").read_text()
starts=D["starts"]; scenes=D["scenes"]; TOTAL=D["total"]

def wt(si, token):
    toks=[w[1].strip(".,").lower() for w in scenes[si]["words"]]
    for i,t in enumerate(toks):
        if token in t: return round(starts[si]+scenes[si]["words"][i][0],2)
    return round(starts[si]+0.5,2)

def fan(cx,cy,r):
    o=[f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="#232b33" stroke="#eef3f8" stroke-width="3"/>']
    for k in range(11):
        a0=k*360/11*math.pi/180;a1=(k*360/11+20)*math.pi/180
        o.append(f'<path d="M{cx+r*.30*math.cos(a0):.1f},{cy+r*.30*math.sin(a0):.1f} '
                 f'Q{cx+r*.72*math.cos(a0+.32):.1f},{cy+r*.72*math.sin(a0+.32):.1f} '
                 f'{cx+r*.93*math.cos(a1):.1f},{cy+r*.93*math.sin(a1):.1f}" fill="#39434d" stroke="#20272e" stroke-width="1.5"/>')
    o.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r*.31:.0f}" fill="#f2f6fa"/>')
    return "".join(o)
def gpu(w,x,y):
    h=w*.30
    g=[f'<g transform="translate({x},{y})">',
       f'<rect width="{w:.0f}" height="{h:.0f}" rx="{h*.13:.0f}" fill="#e9eef3" stroke="#fbfdff" stroke-width="3"/>',
       f'<rect x="{w*.025:.0f}" y="{h*.07:.0f}" width="{w*.95:.0f}" height="{h*.78:.0f}" rx="{h*.09:.0f}" fill="#c8d2dc" stroke="#9aa7b4" stroke-width="2"/>']
    R=h*.29; cy=h*.46
    for f in (0.21,0.50,0.79): g.append(fan(w*f,cy,R))
    for xx in (0.355,0.645): g.append(f'<rect x="{w*xx-4:.0f}" y="{cy-R*.85:.0f}" width="8" height="{R*1.7:.0f}" rx="4" fill="#9b8cff"/>')
    g.append('</g>'); return "".join(g)

BARS=[("4K","74.8",100,"seventy"),("16K","52.2",70,"fifty"),("32K","38.0",51,"thirty"),("64K","28.9",39,"sixty"),("128K","22.8",31,"twenty-two")]
bars="".join(
  f'<g data-cue-at="{wt(1,tok)}"><text x="120" y="{310+i*94+30}" font-family="Consolas,monospace" font-size="20" letter-spacing="2" fill="#8b98a5">{lab}</text>'
  f'<rect data-bar="{w*8.6}" x="220" y="{310+i*94}" width="0" height="42" rx="5" fill="{"#eef3f8" if i==0 else "#f5c531"}"/>'
  f'<text data-num="{v}" x="{240+w*8.6:.0f}" y="{310+i*94+30}" font-family="Inter,sans-serif" font-weight="700" font-size="26" fill="#f2f6fa">0.0</text></g>'
  for i,(lab,v,w,tok) in enumerate(BARS))

S=[]
S.append(f'<svg class="art" viewBox="0 0 1920 1080">{gpu(760,240,560)}'
 f'<g data-cue-at="{wt(0,"four")}"><g transform="translate(1420,340) rotate(-7)"><rect width="250" height="70" rx="22" fill="rgba(10,12,16,.94)" stroke="#f5c531" stroke-width="2.5"/>'
 '<text x="125" y="47" text-anchor="middle" font-family="Inter,sans-serif" font-weight="700" font-size="27" fill="#f5c531">4K ONLY</text></g></g>'
 f'<g data-cue-at="{wt(0,"third")}"><g transform="translate(1140,650)"><rect width="670" height="200" rx="16" fill="rgba(15,17,24,.92)" stroke="rgba(155,140,255,.3)" stroke-width="2"/>'
 '<text x="28" y="46" font-family="Consolas,monospace" font-size="16" letter-spacing="5" fill="#7b8794">AT 128K CONTEXT</text>'
 '<text data-num="22.8" x="28" y="158" font-family="Inter,sans-serif" font-weight="800" font-size="98" fill="#f5c531">0.0</text>'
 '<text x="310" y="158" font-family="Consolas,monospace" font-size="22" fill="#8b98a5">tokens / second</text></g></g></svg>')
S.append(f'<svg class="art" viewBox="0 0 1920 1080">{bars}</svg>')
chips="".join(f'<g data-cue-at="{wt(2,"key") if i<3 else wt(2,"value")}"><rect x="150" y="{330+i*84}" width="34" height="34" rx="7" fill="#9b8cff"/>'
              f'<text x="204" y="{358+i*84}" font-family="Consolas,monospace" font-size="24" fill="#c9d3dd">token {i+1} · key + value</text></g>' for i in range(6))
S.append(f'<svg class="art" viewBox="0 0 1920 1080">{chips}<g data-cue-at="{wt(2,"silicon")}">'
 '<g transform="translate(1180,380) rotate(-6)"><rect width="330" height="70" rx="22" fill="rgba(10,12,16,.94)" stroke="#f87171" stroke-width="2.5"/>'
 '<text x="165" y="47" text-anchor="middle" font-family="Inter,sans-serif" font-weight="700" font-size="27" fill="#f87171">NOT THE GPU</text></g></g></svg>')
S.append(f'<svg class="art" viewBox="0 0 1920 1080"><g data-cue-at="{wt(3,"twenty-six")}">'
 '<text x="150" y="330" font-family="Consolas,monospace" font-size="20" letter-spacing="4" fill="#8b98a5">NEEDED 26 GB</text>'
 '<rect data-grow="560" x="150" y="360" width="0" height="60" rx="8" fill="#f87171"/></g>'
 f'<g data-cue-at="{wt(3,"twenty-four")}"><text x="150" y="480" font-family="Consolas,monospace" font-size="20" letter-spacing="4" fill="#8b98a5">THE CARD 24 GB</text>'
 '<rect data-grow="500" x="150" y="510" width="0" height="60" rx="8" fill="#eef3f8"/></g>'
 f'<g data-cue-at="{wt(3,"makes") if False else wt(3,"card")}"><g transform="translate(1200,430) rotate(-6)"><rect width="310" height="80" rx="24" fill="rgba(10,12,16,.94)" stroke="#f87171" stroke-width="3"/>'
 '<text x="155" y="55" text-anchor="middle" font-family="Inter,sans-serif" font-weight="800" font-size="34" fill="#f87171">2 GB OVER</text></g></g></svg>')
S.append(f'<svg class="art" viewBox="0 0 1920 1080"><g data-cue-at="{wt(4,"sixty-four")}">'
 '<text data-num="64" x="150" y="500" font-family="Inter,sans-serif" font-weight="800" font-size="230" fill="#f5c531">0</text>'
 '<text x="150" y="590" font-family="Consolas,monospace" font-size="26" letter-spacing="4" fill="#8b98a5">THE PRACTICAL CEILING</text></g>'
 f'<g data-cue-at="{wt(4,"memory")}"><g transform="translate(1220,400) rotate(6)"><rect width="380" height="74" rx="22" fill="rgba(10,12,16,.94)" stroke="#43d17a" stroke-width="2.5"/>'
 '<text x="190" y="48" text-anchor="middle" font-family="Inter,sans-serif" font-weight="700" font-size="27" fill="#43d17a">PLAN AROUND IT</text></g></g></svg>')
S.append(f'<svg class="art" viewBox="0 0 1920 1080">'
 f'<g data-cue-at="{wt(5,"number")}"><rect x="150" y="320" width="640" height="240" rx="18" fill="rgba(15,17,24,.92)" stroke="rgba(255,255,255,.12)" stroke-width="2"/>'
 '<text x="180" y="380" font-family="Consolas,monospace" font-size="18" letter-spacing="5" fill="#7b8794">ON THE BOX</text>'
 '<text x="180" y="500" font-family="Inter,sans-serif" font-weight="800" font-size="110" fill="#6d7a86">24 GB</text></g>'
 f'<g data-cue-at="{wt(5,"fits")}"><rect x="900" y="320" width="760" height="240" rx="18" fill="rgba(15,17,24,.92)" stroke="rgba(245,197,49,.4)" stroke-width="2"/>'
 '<text x="930" y="380" font-family="Consolas,monospace" font-size="18" letter-spacing="5" fill="#7b8794">WHAT FITS</text>'
 '<text x="930" y="500" font-family="Inter,sans-serif" font-weight="800" font-size="110" fill="#f5c531">64K</text></g></svg>')
S.append('<svg class="art" viewBox="0 0 1920 1080">'
 + "".join(f'<g data-cue-at="{wt(6,t)}"><circle cx="200" cy="{330+i*130}" r="26" fill="#9b8cff"/>'
           f'<text x="200" y="{342+i*130}" text-anchor="middle" font-family="Inter,sans-serif" font-weight="800" font-size="26" fill="#0d1014">{i+1}</text>'
           f'<text x="252" y="{344+i*130}" font-family="Inter,sans-serif" font-size="36" fill="#e8ecf4">{lab}</text></g>'
           for i,(t,lab) in enumerate([("load","load the model"),("vram","read the VRAM"),("double","double the context")]))
 + '</svg>')
S.append(f'<svg class="art" viewBox="0 0 1920 1080"><g data-cue-at="{wt(7,"ceiling")}">'
 '<circle data-ring="1" cx="960" cy="470" r="150" fill="none" stroke="#43d17a" stroke-width="6"/>'
 '<text x="960" y="500" text-anchor="middle" font-family="Inter,sans-serif" font-weight="800" font-size="84" fill="#43d17a">FOUND</text></g></svg>')

html=f"""<!doctype html><html><head><meta charset="utf-8"><title>BYTE 60 · visual sync</title><style>
html,body{{margin:0;background:#06070a;font-family:Inter,'Segoe UI',sans-serif}}
#stage{{position:relative;width:1920px;height:1080px;overflow:hidden;background:radial-gradient(120% 90% at 26% 12%,#191537 0%,#0a0b10 55%,#06070a 100%)}}
.scene{{position:absolute;inset:0;opacity:0;visibility:hidden}}
.scene.on{{opacity:1;visibility:visible}}
.art{{width:100%;height:100%}}
[data-cue-at]{{opacity:0}}
#bar{{position:fixed;left:0;right:0;bottom:0;height:72px;display:flex;align-items:center;gap:16px;padding:0 24px;
 background:#0b0f14;border-top:1px solid #1d242c;z-index:20}}
button{{font:800 15px/1 Inter,sans-serif;letter-spacing:.14em;padding:15px 28px;border-radius:10px;border:1px solid #2f3a46;background:#141c24;color:#e6eff7;cursor:pointer}}
#play{{background:#f5c531;color:#12161b;border-color:#f5c531}}
#t{{flex:1;accent-color:#f5c531}}
#clock{{font:600 14px/1 Consolas,monospace;color:#8b98a5;min-width:118px;text-align:right}}
</style></head><body>
<div id="stage">{''.join(f'<div class="scene">{s}</div>' for s in S)}</div>
<div id="bar"><button id="play">PLAY</button><button id="rew">⟲</button>
<input id="t" type="range" min="0" step="0.02" value="0"><span id="clock">0.0 / {TOTAL:.1f}s</span></div>
<audio id="vo" preload="auto" src="data:audio/mpeg;base64,{AUD}"></audio>
<script>
const ST={json.dumps(starts)}; const TOTAL={TOTAL};
const scenes=[...document.querySelectorAll('.scene')];
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x)),seg=(t,a,b)=>clamp((t-a)/(b-a),0,1),out=t=>1-Math.pow(1-t,3);
window.renderAt=function(t){{
  let idx=0; for(let i=0;i<ST.length;i++){{ if(t>=ST[i]) idx=i; }}
  scenes.forEach((el,i)=>el.classList.toggle('on',i===idx));
  const sc=scenes[idx];
  sc.querySelectorAll('[data-cue-at]').forEach(el=>{{
    const at=parseFloat(el.dataset.cueAt); const q=seg(t,at,at+0.55);
    el.style.opacity=q>0?1:0; el.style.transform='translateY('+((1-out(q))*18).toFixed(1)+'px)';
  }});
  sc.querySelectorAll('[data-grow]').forEach(el=>{{
    const g=sc.querySelectorAll('[data-grow]'); const i=[...g].indexOf(el);
    const at=parseFloat(el.closest('[data-cue-at]').dataset.cueAt);
    el.setAttribute('width',(parseFloat(el.dataset.grow)*out(seg(t,at+0.15,at+1.2))).toFixed(1));
  }});
  sc.querySelectorAll('[data-bar]').forEach(el=>{{
    const at=parseFloat(el.closest('[data-cue-at]').dataset.cueAt);
    el.setAttribute('width',(parseFloat(el.dataset.bar)*out(seg(t,at+0.1,at+0.9))).toFixed(1));
  }});
  sc.querySelectorAll('[data-num]').forEach(el=>{{
    const at=parseFloat(el.closest('[data-cue-at]').dataset.cueAt);
    const to=parseFloat(el.dataset.num);
    el.textContent=(to*out(seg(t,at+0.15,at+1.2))).toFixed(to>=100?0:1);
  }});
  const ring=sc.querySelector('[data-ring]');
  if(ring){{ const at=parseFloat(ring.closest('[data-cue-at]').dataset.cueAt);
    const q=seg(t,at,at+0.9); ring.setAttribute('stroke-dasharray',String(2*Math.PI*150));
    ring.setAttribute('stroke-dashoffset',(2*Math.PI*150*(1-q)).toFixed(1)); }}
}};
const vo=document.getElementById('vo'),sl=document.getElementById('t'),cl=document.getElementById('clock'),pb=document.getElementById('play');
sl.max=String(TOTAL); let playing=false,raf=null;
function loop(){{ if(!playing)return; const t=Math.min(vo.currentTime,TOTAL);
 renderAt(t); sl.value=String(t); cl.textContent=t.toFixed(1)+' / '+TOTAL.toFixed(1)+'s';
 if(t>=TOTAL){{playing=false;pb.textContent='REPLAY';return;}} raf=requestAnimationFrame(loop); }}
pb.onclick=()=>{{ if(!playing){{ if(vo.currentTime>=TOTAL)vo.currentTime=0; vo.play(); playing=true; pb.textContent='PAUSE'; loop(); }}
 else {{ vo.pause(); playing=false; pb.textContent='PLAY'; cancelAnimationFrame(raf); }} }};
document.getElementById('rew').onclick=()=>{{ vo.pause(); playing=false; pb.textContent='PLAY'; cancelAnimationFrame(raf);
 vo.currentTime=0; renderAt(0); sl.value='0'; }};
sl.oninput=()=>{{ vo.currentTime=parseFloat(sl.value); renderAt(vo.currentTime); }};
renderAt(0);
</script></body></html>"""
pathlib.Path(ROOT+"/BYTE-SYNC60.html").write_text(html,encoding="utf-8")
cues=[]
for si in range(len(scenes)):
    pass
print("wrote BYTE-SYNC60.html  scenes:",len(S))
print("cue times s2:",[wt(1,t) for t in ("seventy","fifty","thirty","sixty","twenty-two")])
print("cue times s4:",[wt(3,t) for t in ("twenty-six","twenty-four","card")])

