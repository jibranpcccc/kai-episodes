import json, math, pathlib
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
tm=json.loads(pathlib.Path(ROOT+"/data/rc_timing.json").read_text())
AUD=pathlib.Path(ROOT+"/data/rc_audio.b64").read_text()
ST,DU,TOT=tm["starts"],tm["durs"],tm["total"]

def fan(cx,cy,r):
    o=[f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="#232b33" stroke="#eef3f8" stroke-width="3"/>']
    for k in range(11):
        a0=k*360/11*math.pi/180;a1=(k*360/11+20)*math.pi/180
        x0=cx+r*.30*math.cos(a0);y0=cy+r*.30*math.sin(a0)
        x1=cx+r*.93*math.cos(a1);y1=cy+r*.93*math.sin(a1)
        mx=cx+r*.72*math.cos(a0+.32);my=cy+r*.72*math.sin(a0+.32)
        o.append(f'<path d="M{x0:.1f},{y0:.1f} Q{mx:.1f},{my:.1f} {x1:.1f},{y1:.1f}" fill="#39434d" stroke="#20272e" stroke-width="1.6"/>')
    o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r*.31:.1f}" fill="#f2f6fa"/>')
    o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r*.12:.1f}" fill="#1a2026"/>')
    return "".join(o)

def gpu(w):
    h=w*.30
    g=[f'<rect width="{w:.0f}" height="{h:.0f}" rx="{h*.13:.0f}" fill="#e9eef3" stroke="#fbfdff" stroke-width="3"/>',
       f'<rect x="{w*.025:.0f}" y="{h*.07:.0f}" width="{w*.95:.0f}" height="{h*.78:.0f}" rx="{h*.09:.0f}" fill="#c8d2dc" stroke="#9aa7b4" stroke-width="2"/>']
    R=h*.29;cy=h*.46
    for f in (0.21,0.50,0.79): g.append(fan(w*f,cy,R))
    for xx in (0.355,0.645): g.append(f'<rect x="{w*xx-4:.0f}" y="{cy-R*.85:.0f}" width="8" height="{R*1.7:.0f}" rx="4" fill="#9b8cff"/>')
    g.append(f'<rect x="{w*.09:.0f}" y="{h*.865:.0f}" width="{w*.52:.0f}" height="{h*.075:.0f}" rx="4" fill="#d6b234"/>')
    return "".join(g)

def stamp(txt,color,x,y,rot,fs):
    w=len(txt)*fs*.63+44
    return (f'<g transform="translate({x},{y}) rotate({rot})"><rect width="{w:.0f}" height="{fs*1.85:.0f}" rx="{fs*.34:.0f}" '
            f'fill="rgba(10,12,16,.94)" stroke="{color}" stroke-width="2.5"/>'
            f'<text x="{w/2:.0f}" y="{fs*1.26:.0f}" text-anchor="middle" font-family="Inter,sans-serif" font-weight="700" font-size="{fs}" fill="{color}">{txt}</text></g>')

def card(x,y,w,h,title):
    return (f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="16" fill="rgba(15,17,24,.9)" '
            f'stroke="rgba(155,140,255,.30)" stroke-width="2"/>'
            f'<text x="28" y="44" font-family="Consolas,monospace" font-size="16" letter-spacing="5" fill="#7b8794">{title}</text>')

def kick(h1,sub,step):
    return (f'<text x="96" y="112" font-family="Consolas,monospace" font-size="18" letter-spacing="9" fill="#9b8cff">{step}</text>'
            f'<text x="96" y="202" font-family="Inter,sans-serif" font-weight="800" font-size="80" fill="#f2f6fa" letter-spacing="-1.5">{h1}</text>'
            f'<text x="96" y="248" font-family="Consolas,monospace" font-size="20" letter-spacing="5" fill="#7b8794">{sub}</text>')

BARS=[("4K","74.8",100),("16K","52.2",70),("32K","38.0",51),("64K","28.9",39),("128K","22.8",31)]

S=[]
S.append(kick("The card is fast. Until it isn't.","RTX 5090 · QWEN 3.8 27B · 32 GB","01 · THE HOOK")
 +f'<g transform="translate(560,420)">{gpu(820)}</g>'
 +stamp("4K ONLY","#f5c531",1420,430,-8,30)
 +'<g transform="translate(1180,620)"><rect width="640" height="180" rx="16" fill="rgba(15,17,24,.9)" stroke="rgba(155,140,255,.3)" stroke-width="2"/>'
  '<text x="28" y="46" font-family="Consolas,monospace" font-size="16" letter-spacing="5" fill="#7b8794">AT 128K CONTEXT</text>'
  '<text id="n1" x="28" y="146" font-family="Inter,sans-serif" font-weight="800" font-size="88" fill="#f5c531">0</text>'
  '<text x="330" y="146" font-family="Consolas,monospace" font-size="24" fill="#8b98a5">tokens / second</text></g>')
S.append(kick("The curve falls off a cliff.","MEASURED · QWEN 3.8 27B · RTX 5090","02 · THE CURVE")
 +card(96,330,1728,560,"TOKENS / SECOND BY CONTEXT")
 +''.join(f'<g transform="translate(150,{410+i*88})">'
          f'<text x="0" y="28" font-family="Consolas,monospace" font-size="20" letter-spacing="3" fill="#8b98a5">{lab}</text>'
          f'<rect x="120" y="0" width="0" height="40" rx="5" fill="{ "#eef3f8" if i==0 else "#f5c531"}"/>'
          f'<text x="{140+w*10.5:.0f}" y="28" font-family="Inter,sans-serif" font-weight="700" font-size="24" fill="#f2f6fa">{v}</text></g>'
          for i,(lab,v,w) in enumerate(BARS))
 +f'<text x="150" y="852" font-family="Consolas,monospace" font-size="15" letter-spacing="3" fill="#6d7a86">1× = NO SPEEDUP BASELINE</text>')
S.append(kick("It is not the silicon.","EVERY TOKEN WRITES A KEY AND A VALUE","03 · THE CAUSE")
 +card(96,330,860,520,"WHAT CHANGES WITH CONTEXT")
 +''.join(f'<g transform="translate(140,{400+i*74})"><rect width="30" height="30" rx="6" fill="#9b8cff" opacity="{0.95-i*0.13:.2f}"/>'
          f'<text x="48" y="24" font-family="Consolas,monospace" font-size="21" fill="#c9d3dd">token {i+1} · key + value</text></g>' for i in range(6))
 +'<g transform="translate(1000,360)"><rect width="760" height="200" rx="16" fill="rgba(15,17,24,.9)" stroke="rgba(245,197,49,.35)" stroke-width="2"/>'
  '<text x="28" y="46" font-family="Consolas,monospace" font-size="16" letter-spacing="5" fill="#7b8794">CACHE AT 128K</text>'
  '<text x="28" y="150" font-family="Inter,sans-serif" font-weight="800" font-size="86" fill="#f5c531">+8 GB</text>'
  '<text x="330" y="150" font-family="Consolas,monospace" font-size="22" fill="#8b98a5">on top of weights</text></g>'
 +stamp("NOT THE GPU","#f87171",1060,600,-6,28))
S.append(kick("Two gigabytes over.","26 GB NEEDED · 24 GB CARD","04 · THE LIMIT")
 +card(96,330,860,520,"VRAM AT 128K")
 +'<g transform="translate(150,430)"><rect width="0" height="52" rx="6" fill="#f87171" id="need"/></g>'
 +'<text x="150" y="530" font-family="Consolas,monospace" font-size="20" letter-spacing="3" fill="#8b98a5">NEEDED 26 GB</text>'
 +'<g transform="translate(150,600)"><rect width="0" height="52" rx="6" fill="#eef3f8" id="have"/></g>'
 +'<text x="150" y="700" font-family="Consolas,monospace" font-size="20" letter-spacing="3" fill="#8b98a5">CARD 24 GB</text>'
 +stamp("2 GB OVER","#f87171",1120,520,-7,34))
S.append(kick("So 64K is the ceiling.","ABOVE IT YOU RUN THE MEMORY SYSTEM","05 · THE RULE")
 +card(96,330,1728,420,"THE PRACTICAL CEILING")
 +'<text x="150" y="470" font-family="Inter,sans-serif" font-weight="800" font-size="150" fill="#f5c531">64K</text>'
 +'<text x="150" y="560" font-family="Consolas,monospace" font-size="24" letter-spacing="4" fill="#8b98a5">fits with headroom · 128K does not</text>'
 +stamp("PLAN AROUND IT","#43d17a",1180,470,6,28))
S.append(kick("Measure your own window.","THAT IS THE WHOLE METHOD","06 · YOUR TURN")
 +card(96,330,1728,420,"THE TEST")
 +'<text x="150" y="470" font-family="Inter,sans-serif" font-size="46" fill="#e8ecf4">load · read VRAM · double the context</text>'
 +'<text x="150" y="560" font-family="Consolas,monospace" font-size="24" letter-spacing="4" fill="#8b98a5">repeat until the number stops climbing</text>'
 +'<circle cx="1600" cy="540" r="66" fill="none" stroke="#43d17a" stroke-width="4"/>'
 +'<text x="1600" y="558" text-anchor="middle" font-family="Inter,sans-serif" font-weight="800" font-size="44" fill="#43d17a">OK</text>')

scenes=[{"t0":ST[i],"dur":DU[i],"svg":f'<svg class="art" viewBox="0 0 1920 1080">{s}</svg>'} for i,s in enumerate(S)]

html=f"""<!doctype html><html><head><meta charset="utf-8"><title>BYTE · 60s · fusion</title><style>
html,body{{margin:0;background:#06070a;font-family:Inter,'Segoe UI',sans-serif}}
#stage{{position:relative;width:1920px;height:1080px;overflow:hidden;background:radial-gradient(120% 90% at 26% 14%,#191537 0%,#0a0b10 52%,#06070a 100%)}}
.scene{{position:absolute;inset:0;opacity:0;visibility:hidden;transition:opacity .30s ease}}
.scene.on{{opacity:1;visibility:visible}}
#bar{{position:fixed;left:0;right:0;bottom:0;height:74px;display:flex;align-items:center;gap:16px;
 padding:0 24px;background:#0b0f14;border-top:1px solid #1d242c;z-index:20}}
button{{font:800 15px/1 Inter,sans-serif;letter-spacing:.14em;padding:15px 28px;border-radius:10px;
 border:1px solid #2f3a46;background:#141c24;color:#e6eff7;cursor:pointer}}
#play{{background:#f5c531;color:#12161b;border-color:#f5c531}}
#t{{flex:1;accent-color:#f5c531}}
#clock{{font:600 14px/1 Consolas,monospace;color:#8b98a5;min-width:120px;text-align:right}}
</style></head><body>
<div id="stage"></div>
<div id="bar"><button id="play">PLAY</button><button id="rew">⟲</button>
<input id="t" type="range" min="0" step="0.05" value="0"><span id="clock">0.0 / {TOT:.1f}s</span></div>
<audio id="vo" preload="auto" src="data:audio/mpeg;base64,{AUD}"></audio>
<script>
const S={json.dumps(scenes)}; const TOTAL={TOT};
const stage=document.getElementById('stage');
stage.innerHTML=S.map((s,i)=>`<div class="scene"><div class="wrap">${{s.svg}}</div></div>`).join('');
const scenes=[...stage.children];
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x)), seg=(t,a,b)=>clamp((t-a)/(b-a),0,1), out=t=>1-Math.pow(1-t,3);
function fmt(n){{return n.toLocaleString('en-US');}}
window.renderAt=function(t){{
  let idx=0; for(let i=0;i<S.length;i++){{ if(t>=S[i].t0) idx=i; }}
  scenes.forEach((el,i)=>{{ const on=i===idx; el.classList.toggle('on',on); }});
  const local=t-S[idx].t0;
  const p=seg(local,0,0.8); scenes[idx].querySelector('.wrap').style.transform='scale('+(1.015-0.015*out(p)).toFixed(4)+')';
  const n1=document.getElementById('n1'); if(n1) n1.textContent=Math.round(22.8*out(seg(local,0.6,2.4)));
  const bars=scenes[idx].querySelectorAll('rect[fill="#f5c531"], rect[fill="#eef3f8"]');
  bars.forEach((b,k)=>{{ if(b.getAttribute('width')==='0'){{ const target=[0,450,315,230,175,140][k]||0;
    b.setAttribute('width',(target*out(seg(local,0.3+k*0.25,1.3+k*0.25))).toFixed(1)); }} }});
  const need=document.getElementById('need'); if(need) need.setAttribute('width',(520*out(seg(local,0.4,1.6))).toFixed(1));
  const have=document.getElementById('have'); if(have) have.setAttribute('width',(480*out(seg(local,0.8,2.0))).toFixed(1));
}};
const vo=document.getElementById('vo'), sl=document.getElementById('t'), cl=document.getElementById('clock'), pb=document.getElementById('play');
sl.max=String(TOTAL);
let playing=false,raf=null;
function loop(){{ if(!playing)return; const t=Math.min(vo.currentTime,TOTAL);
  renderAt(t); sl.value=String(t); cl.textContent=t.toFixed(1)+' / '+TOTAL.toFixed(1)+'s';
  if(t>=TOTAL){{ playing=false; pb.textContent='REPLAY'; return; }} raf=requestAnimationFrame(loop); }}
pb.onclick=()=>{{ if(!playing){{ if(vo.currentTime>=TOTAL) vo.currentTime=0; vo.play(); playing=true; pb.textContent='PAUSE'; loop(); }}
  else {{ vo.pause(); playing=false; pb.textContent='PLAY'; cancelAnimationFrame(raf); }} }};
document.getElementById('rew').onclick=()=>{{ vo.pause(); playing=false; pb.textContent='PLAY';
  cancelAnimationFrame(raf); vo.currentTime=0; renderAt(0); sl.value='0'; cl.textContent='0.0 / '+TOTAL.toFixed(1)+'s'; }};
sl.oninput=()=>{{ vo.currentTime=parseFloat(sl.value); renderAt(vo.currentTime);
  cl.textContent=parseFloat(sl.value).toFixed(1)+' / '+TOTAL.toFixed(1)+'s'; }};
document.addEventListener('keydown',e=>{{ if(e.code==='Space'){{e.preventDefault(); pb.click();}} }});
renderAt(0);
</script></body></html>"""
pathlib.Path(ROOT+"/BYTE-RC60.html").write_text(html,encoding="utf-8")
print("wrote BYTE-RC60.html", round(len(html)/1024/1024,2),"MB")
