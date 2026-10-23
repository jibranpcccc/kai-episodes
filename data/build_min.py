import json, math, os, pathlib
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
tm=json.loads(pathlib.Path(os.path.join(ROOT,"data","min_timing.json")).read_text()) if False else json.loads(pathlib.Path(ROOT+"/data/min_timing.json").read_text())
AUDIO=pathlib.Path(ROOT+"/data/min_audio.b64").read_text()
starts=tm["starts"]; total=tm["total"]

def fan(cx,cy,r,blades=13):
    o=[f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f7f2e6" stroke="#22242a" stroke-width="2.6"/>']
    for k in range(blades):
        a0=k*360/blades*math.pi/180; a1=(k*360/blades+18)*math.pi/180
        x0=cx+r*0.36*math.cos(a0); y0=cy+r*0.36*math.sin(a0)
        x1=cx+r*0.95*math.cos(a1); y1=cy+r*0.95*math.sin(a1)
        mx=cx+r*0.74*math.cos(a0+0.30); my=cy+r*0.74*math.sin(a0+0.30)
        o.append(f'<path d="M{x0:.1f},{y0:.1f} Q{mx:.1f},{my:.1f} {x1:.1f},{y1:.1f}" fill="none" stroke="#22242a" stroke-width="1.9"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.33:.1f}" fill="#e7e0cf" stroke="#22242a" stroke-width="2.2"/>')
    return "".join(o)

def gpu(x,y,s,rot=-5):
    W,H=560*s,300*s
    g=[f'<g transform="translate({x},{y}) rotate({rot})">',
       f'<ellipse cx="{W*.5:.0f}" cy="{H*.99:.0f}" rx="{W*.45:.0f}" ry="{13*s:.0f}" fill="rgba(60,55,42,.18)"/>',
       f'<path d="M0,{40*s:.0f} h{24*s:.0f} v{190*s:.0f} h-{24*s:.0f} z" fill="#dfd8c6" stroke="#22242a" stroke-width="2"/>']
    for k in range(8):
        g.append(f'<line x1="{5*s:.0f}" y1="{(54+k*20)*s:.1f}" x2="{19*s:.0f}" y2="{(54+k*20)*s:.1f}" stroke="#22242a" stroke-width="2"/>')
    g.append(f'<rect x="{26*s:.0f}" y="0" width="{W-26*s:.0f}" height="{H*.72:.0f}" rx="{10*s:.0f}" fill="#efe9da" stroke="#22242a" stroke-width="2.8"/>')
    g.append(f'<rect x="{40*s:.0f}" y="{14*s:.0f}" width="{W-68*s:.0f}" height="{H*.72-28*s:.0f}" rx="{6*s:.0f}" fill="none" stroke="#4c4a44" stroke-width="1.4"/>')
    g.append(fan(W*0.34,H*0.36,min(W,H)*0.21)); g.append(fan(W*0.68,H*0.36,min(W,H)*0.21))
    for k in range(10):
        g.append(f'<line x1="{(W-52+k*5)*s:.1f}" y1="{22*s:.0f}" x2="{(W-52+k*5)*s:.1f}" y2="{H*0.66:.0f}" stroke="#4c4a44" stroke-width="1"/>')
    g.append(f'<rect x="{W*0.52:.0f}" y="{-18*s:.0f}" width="{86*s:.0f}" height="{20*s:.0f}" rx="3" fill="#22242a"/>')
    for k in range(22):
        g.append(f'<rect x="{(60+k*16)*s:.0f}" y="{H*0.72:.0f}" width="{9*s:.0f}" height="{14*s:.0f}" fill="#c9a227" stroke="#22242a" stroke-width="1"/>')
    g.append('</g>')
    return "".join(g)

def books(x,y,cols=5,rows=3,cw=104,ch=150,dx=92,dy=24):
    o=[f'<g transform="translate({x},{y})">']; palette=["#dfe5ee","#cfd8e6","#e6ddd0","#d7dfea","#e8e2d4"]
    i=0
    for r in range(rows):
        for c in range(cols):
            xx=c*dx+r*42; yy=(rows-1-r)*dy+r*7; col=palette[i%len(palette)]; i+=1
            o.append(f'<g transform="translate({xx},{yy}) skewY(-9)">'
                     f'<rect width="{cw}" height="{ch}" fill="{col}" stroke="#22242a" stroke-width="1.9"/>'
                     f'<rect width="13" height="{ch}" fill="rgba(34,36,42,.15)"/>'
                     f'<rect x="22" y="18" width="{cw-44}" height="16" fill="rgba(34,36,42,.55)"/>')
            for k in range(6):
                o.append(f'<line x1="24" y1="{52+k*15}" x2="{cw-18}" y2="{52+k*15}" stroke="rgba(34,36,42,.26)" stroke-width="1.6"/>')
            o.append(f'<rect x="{cw-42}" y="{ch-30}" width="26" height="16" fill="none" stroke="rgba(34,36,42,.35)" stroke-width="1.3"/></g>')
    o.append('</g>'); return "".join(o)

def card(x,y,w,h,label,num,sub=None,numid=None,fs=76):
    n_id=f' id="{numid}"' if numid else ''
    s=(f'<g transform="translate({x},{y})">'
       f'<rect width="{w}" height="{h}" rx="12" fill="#fffdf7" stroke="#1c1b18" stroke-width="2.4"/>'
       f'<rect x="12" y="12" width="{w-24}" height="{h-24}" rx="8" fill="none" stroke="rgba(28,27,24,.10)"/>'
       f'<circle cx="34" cy="40" r="8" fill="none" stroke="#1c1b18" stroke-width="2"/>'
       f'<text x="58" y="46" font-family="Consolas,monospace" font-size="17" letter-spacing="3.6" fill="#4a4740">{label}</text>'
       f'<text{n_id} x="30" y="{h-56}" font-family="Consolas,monospace" font-weight="700" font-size="{fs}" fill="#1c1b18">{num}</text>')
    if sub: s+=f'<text x="32" y="{h-24}" font-family="Consolas,monospace" font-size="18" letter-spacing="2.4" fill="#4a4740">{sub}</text>'
    return s+'</g>'

def scene(i, head, body, reveal):
    return {"i":i,"head":head,"body":body,"reveal":reveal}

S=[]
S.append(scene(0,"Two cards. $1,500.",
  gpu(70,300,0.80,-5)+card(1030,620,720,250,"BREAK-EVEN MATH","$1,500","2 × RTX 5060 Ti",numid="n1"),
  ["#card1","#card2"]))
S.append(scene(1,"They must write 1 billion tokens.",
  gpu(1180,300,0.62,-4)+card(96,620,820,250,"TOKENS TO PAY FOR THEMSELVES","0","1,000 million = 10,000 novels",numid="n2"),
  ["#count2"]))
S.append(scene(2,"That is 10,000 novels.",
  books(980,210)+card(96,700,560,200,"NOVELS","10,000","100,000 tokens each",numid="n3",fs=70),
  ["#scroll3"]))
S.append(scene(3,"One person: 5,000 years.",
  card(300,430,1200,300,"AT 2 NOVELS A YEAR","5,000","one reader, one card",numid="n4",fs=150),
  ["#card4"]))
S.append(scene(4,"A team of agents: 50 years.",
  card(300,430,1200,300,"AT 200 NOVELS A YEAR","50","a small agent team",numid="n5",fs=150),
  ["#card5"]))
S.append(scene(5,"Eight agents: 6 years.",
  card(300,430,1200,300,"AT 1,600 NOVELS A YEAR","6","eight agents running daily",numid="n6",fs=170),
  ["#card6"]))
S.append(scene(6,"$1.50 per million tokens.",
  card(220,400,900,300,"ONE BILLION TOKENS","$1,500","at $1.50 per million",numid="n7",fs=120)+
  f'<text x="1180" y="520" font-family="Georgia,serif" font-style="italic" font-size="46" fill="#b23a2f">exactly the card price</text>'+
  f'<path d="M1160 560 C 1100 600, 1060 620, 1010 640" fill="none" stroke="#b23a2f" stroke-width="3" stroke-dasharray="300" stroke-dashoffset="0"/>',
  ["#card7","#ann7"]))
S.append(scene(7,"Now run your numbers.",
  card(180,420,760,260,"YOUR CARD","$?","tell me in the comments",numid="n8",fs=120)+
  f'<text x="1060" y="500" font-family="Georgia,serif" font-size="42" fill="#1c1b18">tokens ÷ card price</text>'+
  f'<text x="1060" y="560" font-family="Consolas,monospace" font-size="22" letter-spacing="3" fill="#4a4740">THAT IS THE WHOLE FORMULA</text>',
  ["#card8","#ann8"]))

html = """<!doctype html><html><head><meta charset="utf-8"><title>BYTE · 60s</title><style>
html,body{margin:0;background:#07090b}
#stage{position:relative;width:1920px;height:1080px;overflow:hidden;
 background:radial-gradient(120% 100% at 50% 0%,#f8f5ee 0%,#f3f0e7 58%,#e7e2d3 100%)}
#stage:after{content:"";position:absolute;inset:0;pointer-events:none;
 background:radial-gradient(78% 62% at 50% 44%,rgba(0,0,0,0) 44%,rgba(70,62,44,.20) 100%)}
.scene{position:absolute;inset:0;opacity:0;visibility:hidden;transform:scale(1.012);transition:opacity .38s ease, transform .38s ease}
.scene.on{opacity:1;visibility:visible;transform:scale(1)}
svg.art{position:absolute;inset:0}
.rail{position:absolute;left:64px;right:64px;top:42px;display:flex;justify-content:space-between;
 border-top:1.5px solid #1c1b18;border-bottom:1px solid #b9b3a4;padding:10px 2px;
 font:600 15px/1 Consolas,monospace;letter-spacing:.30em;color:#4a4740}
.rail b{color:#1c1b18}
h1{position:absolute;left:64px;top:120px;margin:0;font:400 74px/1.1 Georgia,serif;color:#1c1b18;letter-spacing:-.015em}
.grain{position:absolute;inset:0;pointer-events:none;opacity:.5}
#bar-wrap{position:fixed;left:0;right:0;bottom:0;height:56px;display:flex;align-items:center;
 gap:16px;padding:0 20px;background:#0d1013;border-top:1px solid #232a30;z-index:9}
#play{font:700 14px/1 Consolas,monospace;letter-spacing:.2em;padding:11px 20px;border-radius:6px;
 border:1px solid #3a444d;background:#151b20;color:#d8e2ea;cursor:pointer}
#bar{flex:1;accent-color:#b8d94a}
</style></head><body><div id="stage"></div>
<script>
const AUDIO="__AUDIO__";
const S=__SCENES__;
const TOTAL=__TOTAL__;
const stage=document.getElementById('stage');
function build(){
  let h='';
  S.forEach((s,i)=>{
    h+=`<div class="scene" data-i="${i}">
      <div class="rail"><span><b>BYTE FORENSICS</b> · THE GPU PAYOFF MATH · QWEN 3.8 27B</span>
      <span><b>STEP ${i+1} OF 8</b></span><span>${(i+1)*10}s</span></div>
      <h1>${s.head}</h1>
      <svg class="art" viewBox="0 0 1920 1080">${s.body}</svg></div>`;
  });
  h+=`<svg class="grain" viewBox="0 0 1920 1080"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3"/><feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="linear" slope="0.055"/></feComponentTransfer></filter><rect width="1920" height="1080" filter="url(#g)"/></svg>`;
  stage.innerHTML=h;
}
build();
const scenes=[...document.querySelectorAll('.scene')];
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x)), seg=(t,a,b)=>clamp((t-a)/(b-a),0,1);
const out=t=>1-Math.pow(1-t,3), back=t=>{const c=2.4;return 1+(c+1)*Math.pow(t-1,3)+c*Math.pow(t-1,2);};
window.renderAt=function(t){
  const st=S.map(s=>s.t0);
  let idx=0; for(let i=0;i<st.length;i++){ if(t>=st[i]) idx=i; }
  scenes.forEach((el,i)=>el.classList.toggle('on', i===idx));
  const local=t-st[idx]; const dur=S[idx].dur;
  // count-ups
  const cu=(id,val,at)=>{const el=document.getElementById(id); if(!el) return;
    const p=seg(local,at,at+1.9); el.textContent=Math.round(val*out(p)).toLocaleString('en-US');};
  const ci=idx+1;
  cu('n1',1500,0.6); cu('n2',1000000000,0.6); cu('n3',10000,0.5);
  cu('n4',5000,0.4); cu('n5',50,0.4); cu('n6',6,0.35); cu('n7',1500,0.5);
  // pop-in for the card group
  // fade the drawing in as a whole (transform is owned by the SVG, never by JS)
  const art=scenes[idx].querySelector('svg.art');
  if(art){ const p=seg(local,0.05,0.75); art.style.opacity=(0.25+0.75*out(p)).toFixed(3); }
};
const vo=document.getElementById('vo');
const bar=document.getElementById('bar'), play=document.getElementById('play');
let raf=null, playing=false;
function tick(){
  if(!playing) return;
  window.renderAt(Math.min(vo.currentTime, TOTAL));
  bar.value=String(vo.currentTime);
  raf=requestAnimationFrame(tick);
}
function start(){
  vo.currentTime=0; vo.play(); playing=true; play.textContent='PAUSE'; tick();
}
play.onclick=()=>{
  if(!playing){ vo.play(); playing=true; play.textContent='PAUSE'; tick(); }
  else { vo.pause(); playing=false; play.textContent='PLAY'; cancelAnimationFrame(raf); }
};
vo.addEventListener('ended', ()=>{ playing=false; play.textContent='REPLAY'; });
bar.max=String(TOTAL);
bar.oninput=()=>{ vo.currentTime=parseFloat(bar.value); window.renderAt(vo.currentTime); };
window.renderAt(0);
</script></body></html>"""

# inject scene data with absolute starts/durs
for i,s in enumerate(S):
    s["t0"]=starts[i]; s["dur"]=tm["durs"][i]
html = html.replace("__SCENES__", json.dumps(S)).replace("__TOTAL__", str(total)).replace("__AUDIO__", AUDIO)
html = html.replace('<div id="stage"></div>', '<div id="stage"></div><div id="bar-wrap"><button id="play">PLAY</button><input id="bar" type="range" min="0" step="0.05" value="0"></div><audio id="vo" src="data:audio/mpeg;base64,'+AUDIO+'"></audio>')
pathlib.Path(os.path.join(ROOT,"BYTE-MIN.html")).write_text(html, encoding="utf-8")
print("wrote BYTE-MIN.html", round(len(html)/1024/1024,2), "MB")

