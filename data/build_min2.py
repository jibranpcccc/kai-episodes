import json, math, os, pathlib
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
tm=json.loads(pathlib.Path(ROOT+"/data/min_timing.json").read_text())
AUDIO=pathlib.Path(ROOT+"/data/min_audio.b64").read_text()
starts=tm["starts"]; durs=tm["durs"]; total=tm["total"]

def blades(cx,cy,r,n=11):
    o=[f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="url(#fanDark)" stroke="rgba(255,255,255,.5)" stroke-width="2"/>']
    for k in range(n):
        a0=k*360/n*math.pi/180; a1=(k*360/n+19)*math.pi/180
        x0=cx+r*.30*math.cos(a0); y0=cy+r*.30*math.sin(a0)
        x1=cx+r*.94*math.cos(a1); y1=cy+r*.94*math.sin(a1)
        mx=cx+r*.74*math.cos(a0+.30); my=cy+r*.74*math.sin(a0+.30)
        o.append(f'<path d="M{x0:.1f},{y0:.1f} Q{mx:.1f},{my:.1f} {x1:.1f},{y1:.1f}" fill="rgba(255,255,255,.09)" stroke="rgba(255,255,255,.26)" stroke-width="1.3"/>')
    o.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r*.30:.0f}" fill="rgba(238,242,246,.94)"/>')
    o.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r*.11:.0f}" fill="#1d2228"/>')
    o.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r*1.015:.0f}" fill="none" stroke="rgba(120,230,255,.30)" stroke-width="5"/>')
    return "".join(o)

def gpu(x,y,w,nfans=3,rot=0):
    h=w*0.30
    g=[f'<g transform="translate({x},{y}) rotate({rot})">',
       f'<ellipse cx="{w/2:.0f}" cy="{h+16:.0f}" rx="{w*.42:.0f}" ry="16" fill="rgba(0,0,0,.55)" filter="url(#soft)"/>',
       f'<rect width="{w:.0f}" height="{h:.0f}" rx="{h*0.12:.0f}" fill="url(#whiteBody)" stroke="rgba(255,255,255,.85)" stroke-width="2.4"/>',
       f'<rect x="{w*.025:.0f}" y="{h*.07:.0f}" width="{w*.95:.0f}" height="{h*.80:.0f}" rx="{h*.08:.0f}" fill="url(#whiteInset)"/>']
    R=h*0.30; cy=h*0.47
    xs={1:[0.5],2:[0.32,0.68],3:[0.22,0.50,0.78]}[nfans]
    for cx in xs: g.append(blades(w*cx,cy,R))
    for i in range(nfans-1):
        xx=w*(xs[i]+xs[i+1])/2
        g.append(f'<rect x="{xx-3:.0f}" y="{cy-R*0.78:.0f}" width="6" height="{R*1.56:.0f}" rx="3" fill="rgba(120,230,255,.8)" filter="url(#glow)"/>')
    g.append(f'<rect x="{w*.10:.0f}" y="{h*.86:.0f}" width="{w*.52:.0f}" height="{h*.075:.0f}" rx="3" fill="rgba(201,162,39,.9)"/>')
    for k in range(24):
        g.append(f'<rect x="{w*.10+3+k*round(w*.52/24):.0f}" y="{h*.865:.0f}" width="{round(w*.52/24)-4}" height="{h*.06:.0f}" fill="rgba(40,32,10,.5)"/>')
    g.append('</g>')
    return "".join(g)

def card(x,y,w,h,kicker,num,sub,numid=None,fs=92,accent="#b8d94a"):
    nid=f' id="{numid}"' if numid else ""
    return (f'<g transform="translate({x},{y})">'
            f'<rect width="{w}" height="{h}" rx="14" fill="rgba(16,21,26,.92)" stroke="rgba(120,230,255,.28)" stroke-width="2"/>'
            f'<text x="30" y="44" font-family="Consolas,monospace" font-size="17" letter-spacing="5" fill="#6f7d8a">{kicker}</text>'
            f'<text{nid} x="28" y="{h-52}" font-family="Inter,Segoe UI,sans-serif" font-weight="800" font-size="{fs}" fill="{accent}">{num}</text>'
            f'<text x="30" y="{h-18}" font-family="Consolas,monospace" font-size="17" letter-spacing="3" fill="#7c8a97">{sub}</text>'
            f'</g>')

DEFS='''<defs>
<linearGradient id="whiteBody" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fcfdfe"/><stop offset=".45" stop-color="#e7ecf1"/><stop offset="1" stop-color="#c4ced8"/></linearGradient>
<linearGradient id="whiteInset" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#dee6ec"/><stop offset="1" stop-color="#a9b5c0"/></linearGradient>
<radialGradient id="fanDark" cx="50%" cy="42%" r="62%"><stop offset="0" stop-color="#3a434d"/><stop offset="1" stop-color="#11161b"/></radialGradient>
<radialGradient id="stageGlow" cx="50%" cy="34%" r="72%"><stop offset="0" stop-color="rgba(120,230,255,.11)"/><stop offset="1" stop-color="rgba(0,0,0,0)"/></radialGradient>
<filter id="glow"><feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="soft"><feGaussianBlur stdDeviation="12"/></filter></defs>'''

def head(kicker,h1,sub=""):
    s=(f'<text x="96" y="132" font-family="Consolas,monospace" font-size="20" letter-spacing="8" fill="#7fe3ff">{kicker}</text>'
       f'<text x="96" y="228" font-family="Inter,Segoe UI,sans-serif" font-weight="800" font-size="86" fill="#eef4f8" letter-spacing="-1.5">{h1}</text>')
    if sub: s+=f'<text x="96" y="284" font-family="Consolas,monospace" font-size="22" letter-spacing="4" fill="#7c8a97">{sub}</text>'
    return s

S=[]
S.append((head("STEP 1 · THE PRICE","Two cards. $1,500."), gpu(470,300,1120,3)+card(96,770,600,220,"BREAK-EVEN MATH","$1,500","2 × RTX 5060 Ti","n1",84)))
S.append((head("STEP 2 · THE TARGET","One billion tokens."), gpu(1080,300,720,3)+card(96,700,760,260,"TOKENS TO PAY FOR THEMSELVES","0","1,000 million = 10,000 novels","n2",78)))
S.append((head("STEP 3 · IN HUMAN UNITS","That is 10,000 novels."), gpu(300,300,380,2)+gpu(760,340,380,2)+gpu(1220,300,380,2)+card(300,760,900,200,"NOVELS","10,000","100,000 tokens each","n3",76)))
S.append((head("STEP 4 · ONE PERSON","5,000 years."), card(300,470,1300,300,"AT 2 NOVELS A YEAR","5,000","one reader, one card","n4",150,"#eef4f8")))
S.append((head("STEP 5 · A SMALL TEAM","50 years."), card(300,470,1300,300,"AT 200 NOVELS A YEAR","50","an agent team","n5",170,"#eef4f8")))
S.append((head("STEP 6 · EIGHT AGENTS","6 years."), card(300,470,1300,300,"AT 1,600 NOVELS A YEAR","6","eight agents, daily","n6",190,"#b8d94a")))
S.append((head("STEP 7 · THE MATH","$1.50 per million."), card(220,470,760,280,"ONE BILLION TOKENS","$1,500","$1.50 × 1,000 million","n7",120)+
          '<text x="1060" y="600" font-family="Consolas,monospace" font-size="30" letter-spacing="6" fill="#7fe3ff">= THE CARD PRICE</text>'))
S.append((head("STEP 8 · YOUR TURN","Now run yours."), card(200,460,700,260,"YOUR CARD","$?","tell me in the comments","n8",120)+
          '<text x="1000" y="560" font-family="Inter,Segoe UI,sans-serif" font-size="44" fill="#eef4f8">tokens ÷ card price</text>'
          '<text x="1000" y="620" font-family="Consolas,monospace" font-size="22" letter-spacing="4" fill="#7c8a97">THAT IS THE WHOLE FORMULA</text>'))

scenes=[]
for i,(body,extra) in enumerate(S):
    scenes.append({"i":i,"t0":starts[i],"dur":durs[i],
                   "svg":'<svg class="art" viewBox="0 0 1920 1080">'+body+extra+'</svg>'})

html=f"""<!doctype html><html><head><meta charset="utf-8"><title>BYTE · 60s</title><style>
html,body{{margin:0;background:#07090b;font-family:Inter,'Segoe UI',sans-serif}}
#stage{{position:relative;width:1920px;height:1080px;overflow:hidden;
 background:radial-gradient(120% 90% at 50% 0%,#131a21 0%,#0a0d11 55%,#070a0d 100%)}}
.scene{{position:absolute;inset:0;opacity:0;visibility:hidden;transition:opacity .32s ease}}
.scene.on{{opacity:1;visibility:visible}}
.wrap{{width:100%;height:100%;transform-origin:50% 50%}}
#barwrap{{position:fixed;left:0;right:0;bottom:0;height:58px;display:flex;align-items:center;gap:18px;
 padding:0 22px;background:#0b0f13;border-top:1px solid #1e262d;z-index:9}}
#play{{font:700 14px/1 Consolas,monospace;letter-spacing:.2em;padding:12px 22px;border-radius:6px;
 border:1px solid #2f3a44;background:#141b21;color:#d6e3ee;cursor:pointer}}
#bar{{flex:1;accent-color:#78e6ff}}
</style></head><body>
<div id="stage"></div>
<div id="barwrap"><button id="play">PLAY</button><input id="bar" type="range" min="0" step="0.05" value="0"></div>
<audio id="vo" preload="auto" src="data:audio/mpeg;base64,{AUDIO}"></audio>
<script>
const S={json.dumps(scenes)};
const TOTAL={total};
const stage=document.getElementById('stage');
stage.innerHTML=S.map((s,i)=>`<div class="scene" data-i="${{i}}"><div class="wrap">${{s.svg}}</div></div>`).join('');
const scenes=[...stage.children];
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x)),seg=(t,a,b)=>clamp((t-a)/(b-a),0,1);
const out=t=>1-Math.pow(1-t,3);
function fmt(n){{return n.toLocaleString('en-US');}}
window.renderAt=function(t){{
  let idx=0; for(let i=0;i<S.length;i++){{ if(t>=S[i].t0) idx=i; }}
  scenes.forEach((el,i)=>{{
    const on=i===idx;
    el.classList.toggle('on',on);
    const w=el.firstElementChild;
    const local=Math.max(0,t-S[idx].t0);
    const p=seg(local,0,0.9);
    w.style.transform='scale('+(1.02-0.02*out(p)).toFixed(4)+')';
  }});
  const local=t-S[idx].t0;
  const upd=(id,val,at)=>{{const el=document.getElementById(id); if(!el)return;
    const p=seg(local,at,at+2.0); el.textContent=fmt(Math.round(val*out(p)));}};
  upd('n1',1500,0.4); upd('n2',1000000000,0.4); upd('n3',10000,0.3);
  upd('n4',5000,0.3); upd('n5',50,0.3); upd('n6',6,0.25); upd('n7',1500,0.3);
}};
const vo=document.getElementById('vo'),bar=document.getElementById('bar'),play=document.getElementById('play');
bar.max=String(TOTAL);
let raf=null,playing=false;
function loop(){{ if(!playing)return; renderAt(Math.min(vo.currentTime,TOTAL)); bar.value=String(vo.currentTime); raf=requestAnimationFrame(loop); }}
function start(){{ vo.currentTime=0; vo.play(); playing=true; play.textContent='PAUSE'; loop(); }}
play.onclick=()=>{{ if(!playing) start(); else {{ vo.pause(); playing=false; play.textContent='PLAY'; cancelAnimationFrame(raf); }} }};
vo.onended=()=>{{ playing=false; play.textContent='REPLAY'; }};
bar.oninput=()=>{{ vo.currentTime=parseFloat(bar.value); renderAt(vo.currentTime); }};
renderAt(0);
</script></body></html>"""
pathlib.Path(ROOT+"/BYTE-MIN2.html").write_text(html,encoding="utf-8")
print("wrote BYTE-MIN2.html", round(len(html)/1024/1024,2),"MB")
