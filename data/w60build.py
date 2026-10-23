import asyncio, base64, json, os, subprocess, pathlib
import edge_tts
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; W=os.path.join(ROOT,"build","W60"); os.makedirs(W,exist_ok=True)
LINES=[
 "This card is fast at four K. At one hundred and twenty-eight K, it is a third of that.",
 "Here is the curve. Seventy-five tokens at four K. Fifty-two at sixteen. Thirty-eight at thirty-two. Twenty-eight at sixty-four. Twenty-two at one twenty-eight.",
 "Nothing changed in the silicon. What changed is the cache. Every token writes a key and a value.",
 "At one twenty-eight K the model needs twenty-six gigabytes. The card has twenty-four.",
 "So the ceiling is sixty-four K. Above that you are running the memory system.",
 "That is the number that decides what fits. Not the number on the box.",
 "Load the model. Read the VRAM. Then double the context and watch.",
 "When the number stops climbing, you have found your ceiling.",
]
async def rec():
    out=[]
    for i,line in enumerate(LINES):
        mp3=os.path.join(W,f"s{i}.mp3"); wav=os.path.join(W,f"s{i}.wav"); words=[]
        c=edge_tts.Communicate(line,"en-US-AndrewNeural",rate="-6%",boundary="WordBoundary")
        audio=bytearray()
        async for ch in c.stream():
            if ch["type"]=="audio": audio+=ch["data"]
            elif ch["type"]=="WordBoundary": words.append([round(ch["offset"]/1e7,3), ch["text"]])
        open(mp3,"wb").write(bytes(audio))
        subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-i",mp3,"-ar","44100","-ac","1","-c:a","pcm_s16le",wav],check=True)
        d=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nw=1:nk=1",wav],capture_output=True,text=True).stdout.strip())
        out.append({"line":line,"wav":wav,"dur":d,"words":words}); print(f"  s{i+1}: {d:.2f}s {len(words)}w")
    return out
sc=asyncio.run(rec())
GAP=0.55; starts=[]; t=0.0
for s in sc: starts.append(t); t+=s["dur"]+GAP
TOTAL=t-GAP+1.0
g=os.path.join(W,"g.wav"); subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi","-i","anullsrc=r=44100:cl=mono","-t",str(GAP),"-c:a","pcm_s16le",g],check=True)
tl=os.path.join(W,"t.wav"); subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi","-i","anullsrc=r=44100:cl=mono","-t","1.0","-c:a","pcm_s16le",tl],check=True)
seq=[]
for i,s in enumerate(sc):
    seq.append(s["wav"])
    if i<len(sc)-1: seq.append(g)
seq.append(tl)
lst=os.path.join(W,"l.txt"); open(lst,"w",encoding="utf-8").write("\n".join(f"file '{p.replace(chr(92),'/')}'" for p in seq))
vo=os.path.join(W,"vo.mp3")
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","concat","-safe","0","-i",lst,
  "-af","loudnorm=I=-14:TP=-1.5:LRA=11,volume=1.2dB","-c:a","libmp3lame","-b:a","192k",vo],check=True)
AUD=base64.b64encode(open(vo,"rb").read()).decode()
print("total", round(TOTAL,1))

# ---------------- build ----------------
def fan(cx,cy,r):
    o=[f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="#232b33" stroke="#eef3f8" stroke-width="3"/>']
    for k in range(11):
        a0=k*360/11*3.14159/180;a1=(k*360/11+20)*3.14159/180
        o.append(f'<path d="M{cx+r*.30*__import__("math").cos(a0):.1f},{cy+r*.30*__import__("math").sin(a0):.1f} '
                 f'Q{cx+r*.72*__import__("math").cos(a0+.32):.1f},{cy+r*.72*__import__("math").sin(a0+.32):.1f} '
                 f'{cx+r*.93*__import__("math").cos(a1):.1f},{cy+r*.93*__import__("math").sin(a1):.1f}" fill="#39434d" stroke="#20272e" stroke-width="1.5"/>')
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

BARS=[("4K","74.8",100),("16K","52.2",70),("32K","38.0",51),("64K","28.9",39),("128K","22.8",31)]
def bars_svg():
    o=['<g>']
    for i,(lab,v,w) in enumerate(BARS):
        y=300+i*94
        o.append(f'<text x="120" y="{y+30}" font-family="Consolas,monospace" font-size="20" letter-spacing="2" fill="#8b98a5">{lab}</text>')
        o.append(f'<rect data-bar="{w*8.6}" x="220" y="{y}" width="0" height="42" rx="5" fill="{"#eef3f8" if i==0 else "#f5c531"}"/>')
        o.append(f'<text data-num="{v}" x="{240+w*8.6:.0f}" y="{y+30}" font-family="Inter,sans-serif" font-weight="700" font-size="26" fill="#f2f6fa">0.0</text>')
    o.append('</g>'); return "".join(o)

SCENES=[]
# 1 hook
SCENES.append(f'<svg class="art" viewBox="0 0 1920 1080">{gpu(760,180,560)}'
  '<g data-stamp="1"><g transform="translate(1420,300) rotate(-7)"><rect width="240" height="66" rx="20" fill="rgba(10,12,16,.94)" stroke="#f5c531" stroke-width="2.5"/>'
  '<text x="120" y="44" text-anchor="middle" font-family="Inter,sans-serif" font-weight="700" font-size="26" fill="#f5c531">4K ONLY</text></g></g>'
  '<g transform="translate(1150,620)"><rect width="660" height="190" rx="16" fill="rgba(15,17,24,.92)" stroke="rgba(155,140,255,.3)" stroke-width="2"/>'
  '<text x="28" y="46" font-family="Consolas,monospace" font-size="16" letter-spacing="5" fill="#7b8794">AT 128K CONTEXT</text>'
  '<text data-num="22.8" x="28" y="152" font-family="Inter,sans-serif" font-weight="800" font-size="96" fill="#f5c531">0.0</text>'
  '<text x="300" y="152" font-family="Consolas,monospace" font-size="22" fill="#8b98a5">tokens / second</text></g></svg>')
# 2 curve
SCENES.append(f'<svg class="art" viewBox="0 0 1920 1080">{bars_svg()}</svg>')
# 3 cause
chips="".join(f'<g data-chip="{i}"><rect x="150" y="{330+i*84}" width="34" height="34" rx="7" fill="#9b8cff"/>'
              f'<text x="204" y="{358+i*84}" font-family="Consolas,monospace" font-size="24" fill="#c9d3dd">token {i+1} · key + value</text></g>' for i in range(6))
SCENES.append(f'<svg class="art" viewBox="0 0 1920 1080">{chips}'
  '<g data-stamp="1"><g transform="translate(1180,360) rotate(-6)"><rect width="320" height="66" rx="20" fill="rgba(10,12,16,.94)" stroke="#f87171" stroke-width="2.5"/>'
  '<text x="160" y="44" text-anchor="middle" font-family="Inter,sans-serif" font-weight="700" font-size="26" fill="#f87171">NOT THE GPU</text></g></g></svg>')
# 4 limit
SCENES.append('<svg class="art" viewBox="0 0 1920 1080">'
  '<text x="150" y="330" font-family="Consolas,monospace" font-size="20" letter-spacing="4" fill="#8b98a5">NEEDED</text>'
  '<rect id="need" x="150" y="360" width="0" height="60" rx="8" fill="#f87171"/>'
  '<text x="150" y="470" font-family="Consolas,monospace" font-size="20" letter-spacing="4" fill="#8b98a5">THE CARD</text>'
  '<rect id="have" x="150" y="500" width="0" height="60" rx="8" fill="#eef3f8"/>'
  '<g data-stamp="1"><g transform="translate(1180,420) rotate(-6)"><rect width="300" height="76" rx="22" fill="rgba(10,12,16,.94)" stroke="#f87171" stroke-width="3"/>'
  '<text x="150" y="52" text-anchor="middle" font-family="Inter,sans-serif" font-weight="800" font-size="32" fill="#f87171">2 GB OVER</text></g></g></svg>')
# 5 ceiling
SCENES.append('<svg class="art" viewBox="0 0 1920 1080">'
  '<text data-num="64" x="150" y="470" font-family="Inter,sans-serif" font-weight="800" font-size="220" fill="#f5c531">0</text>'
  '<text x="150" y="560" font-family="Consolas,monospace" font-size="26" letter-spacing="4" fill="#8b98a5">THE PRACTICAL CEILING</text>'
  '<g data-stamp="1"><g transform="translate(1220,380) rotate(6)"><rect width="360" height="70" rx="20" fill="rgba(10,12,16,.94)" stroke="#43d17a" stroke-width="2.5"/>'
  '<text x="180" y="46" text-anchor="middle" font-family="Inter,sans-serif" font-weight="700" font-size="27" fill="#43d17a">PLAN AROUND IT</text></g></g></svg>')
# 6 number on box
SCENES.append('<svg class="art" viewBox="0 0 1920 1080">'
  '<g data-stamp="1"><rect x="150" y="300" width="640" height="240" rx="18" fill="rgba(15,17,24,.92)" stroke="rgba(255,255,255,.12)" stroke-width="2"/>'
  '<text x="180" y="360" font-family="Consolas,monospace" font-size="18" letter-spacing="5" fill="#7b8794">ON THE BOX</text>'
  '<text x="180" y="480" font-family="Inter,sans-serif" font-weight="800" font-size="110" fill="#6d7a86">24 GB</text></g>'
  '<g data-stamp="2"><rect x="900" y="300" width="760" height="240" rx="18" fill="rgba(15,17,24,.92)" stroke="rgba(245,197,49,.4)" stroke-width="2"/>'
  '<text x="930" y="360" font-family="Consolas,monospace" font-size="18" letter-spacing="5" fill="#7b8794">WHAT FITS</text>'
  '<text x="930" y="480" font-family="Inter,sans-serif" font-weight="800" font-size="110" fill="#f5c531">64K</text></g></svg>')
# 7 method
SCENES.append('<svg class="art" viewBox="0 0 1920 1080">'
  + "".join(f'<g data-chip="{i}"><circle cx="200" cy="{320+i*130}" r="26" fill="#9b8cff"/>'
            f'<text x="200" y="{332+i*130}" text-anchor="middle" font-family="Inter,sans-serif" font-weight="800" font-size="26" fill="#0d1014">{i+1}</text>'
            f'<text x="252" y="{334+i*130}" font-family="Inter,sans-serif" font-size="34" fill="#e8ecf4">{t}</text></g>'
            for i,t in enumerate(["load the model","read the VRAM","double the context"]))
  + '</svg>')
# 8 ceiling found
SCENES.append('<svg class="art" viewBox="0 0 1920 1080">'
  '<circle data-ring="1" cx="960" cy="480" r="150" fill="none" stroke="#43d17a" stroke-width="6"/>'
  '<text x="960" y="510" text-anchor="middle" font-family="Inter,sans-serif" font-weight="800" font-size="90" fill="#43d17a">FOUND</text></svg>')

# words + html
scene_html=[]; all_words=[]
for i,s in enumerate(sc):
    spans="".join(f'<span class="w" id="w{i}_{j}">{w[1]} </span>' for j,w in enumerate(s["words"]))
    scene_html.append(f'<div class="scene"><div class="artwrap">{SCENES[i]}</div><div class="cap">{spans}</div></div>')
    for j,w in enumerate(s["words"]):
        all_words.append({"id":f"w{i}_{j}","t":round(starts[i]+w[0],3)})

html=f"""<!doctype html><html><head><meta charset="utf-8"><title>BYTE 60 · word sync</title><style>
html,body{{margin:0;background:#06070a;font-family:Inter,'Segoe UI',sans-serif}}
#stage{{position:relative;width:1920px;height:1080px;overflow:hidden;background:radial-gradient(120% 90% at 26% 12%,#191537 0%,#0a0b10 55%,#06070a 100%)}}
.scene{{position:absolute;inset:0;opacity:0;visibility:hidden}}
.scene.on{{opacity:1;visibility:visible}}
.artwrap{{position:absolute;inset:0}}
.art{{width:100%;height:100%}}
.cap{{position:absolute;left:96px;right:96px;bottom:110px;font-family:Inter,'Segoe UI',sans-serif;
 font-size:58px;line-height:1.22;font-weight:700;color:#f2f6fa;letter-spacing:-.5px}}
.w{{opacity:0;transition:opacity .12s linear;color:#f2f6fa}}
.w.live{{opacity:1}}
.w.done{{opacity:.42}}
#bar{{position:fixed;left:0;right:0;bottom:0;height:74px;display:flex;align-items:center;gap:16px;padding:0 24px;
 background:#0b0f14;border-top:1px solid #1d242c;z-index:20}}
button{{font:800 15px/1 Inter,sans-serif;letter-spacing:.14em;padding:15px 28px;border-radius:10px;
 border:1px solid #2f3a46;background:#141c24;color:#e6eff7;cursor:pointer}}
#play{{background:#f5c531;color:#12161b;border-color:#f5c531}}
#t{{flex:1;accent-color:#f5c531}}
#clock{{font:600 14px/1 Consolas,monospace;color:#8b98a5;min-width:120px;text-align:right}}
</style></head><body>
<div id="stage">{''.join(scene_html)}</div>
<div id="bar"><button id="play">PLAY</button><button id="rew">⟲</button>
<input id="t" type="range" min="0" step="0.02" value="0"><span id="clock">0.0 / {TOTAL:.1f}s</span></div>
<audio id="vo" preload="auto" src="data:audio/mpeg;base64,{AUD}"></audio>
<script>
const ST={json.dumps(starts)}; const TOTAL={TOTAL}; const WORDS={json.dumps(all_words)};
window.WORDS=WORDS; window.ST=ST;
const scenes=[...document.querySelectorAll('.scene')];
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x)),seg=(t,a,b)=>clamp((t-a)/(b-a),0,1),out=t=>1-Math.pow(1-t,3);
const WORD_BY_ID={{}}; WORDS.forEach((w,i)=>{{ WORD_BY_ID[w.id]=i; }});
window.renderAt=function(t){{
  let idx=0; for(let i=0;i<ST.length;i++){{ if(t>=ST[i]) idx=i; }}
  scenes.forEach((el,i)=>el.classList.toggle('on',i===idx));
  const sc=scenes[idx], local=t-ST[idx];
  // words
  WORDS.forEach((w,i)=>{{
    const el=document.getElementById(w.id); if(!el) return;
    const prev=i>0?WORDS[i-1].t:w.t-0.4, next=i<WORDS.length-1?WORDS[i+1].t:w.t+0.8;
    el.classList.toggle('live', t>=w.t && t<next);
    el.classList.toggle('done', t>=next);
  }});
  sc.querySelectorAll('[data-bar]').forEach((b,k)=>{{
    const to=parseFloat(b.dataset.bar), at=0.3+k*0.55;
    b.setAttribute('width',(to*out(seg(local,at,at+1.0))).toFixed(1));
  }});
  sc.querySelectorAll('[data-num]').forEach((el,k)=>{{
    const to=parseFloat(el.dataset.num), at=0.4+k*0.55;
    el.textContent=(to*out(seg(local,at,at+1.1))).toFixed(to>=100?0:1);
  }});
  sc.querySelectorAll('[data-chip]').forEach((c,k)=>{{
    const q=seg(local,0.4+k*0.45,0.95+k*0.45); c.style.opacity=(0.12+0.88*out(q)).toFixed(2);
  }});
  sc.querySelectorAll('[data-stamp]').forEach((st,k)=>{{
    const q=seg(local,0.8+k*0.5,1.35+k*0.5);
    st.style.opacity=q>0?1:0; st.style.transform='scale('+(1.5-0.5*out(q)).toFixed(3)+')';
    st.style.transformOrigin='center';
  }});
  const need=sc.querySelector('#need'); if(need) need.setAttribute('width',(560*out(seg(local,0.4,1.6))).toFixed(1));
  const have=sc.querySelector('#have'); if(have) have.setAttribute('width',(500*out(seg(local,1.0,2.2))).toFixed(1));
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
pathlib.Path(ROOT+"/BYTE-WORD60.html").write_text(html,encoding="utf-8")
pathlib.Path(ROOT+"/data/w60_verify.json").write_text(json.dumps({"words":all_words,"total":TOTAL}))
pathlib.Path(ROOT+"/data/w60.json").write_text(json.dumps({"total":TOTAL,"starts":starts,"scenes":[{"dur":s["dur"],"words":s["words"],"line":s["line"]} for s in sc]}))
pathlib.Path(ROOT+"/data/w60.b64").write_text(AUD)
print("built. words:",len(all_words))
