import asyncio, edge_tts, os, re, subprocess, base64

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
VOICE = "en-US-AndrewNeural"
RATE = "+8%"
GAP = 0.25
TAIL = 0.8
NAME = "BYTE-01"
MAX_GAP = 2.0

def dur(p):
    return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                                 "-of","csv=p=0",p],capture_output=True,text=True).stdout.strip())

def align(text, words):
    low = text.lower(); out = []; cur = 0
    for t, w in words:
        wl = w.lower().strip(".,;:!?\"'()")
        idx = low.find(wl, cur) if wl else -1
        if idx < 0: idx = cur
        else: cur = idx + len(wl)
        out.append((idx, t))
    return out

def phrase_time(text, aligned, words, phrase):
    p = text.lower().find(phrase.lower())
    if p < 0: raise ValueError(f"cue phrase not in script: {phrase!r}")
    for ci, t in aligned:
        if ci >= p: return t
    return aligned[-1][1]

def row(k, v, tk, tv, colour="var(--white)", hot=False):
    cls = "bf-row bf-row--hot" if hot else "bf-row"
    return (f'<div class="{cls}" data-in="@{tk}@"><span class="bf-row__k">{k}</span>'
            f'<span class="bf-row__v" style="color:{colour}" data-in="@{tv}@">{v}</span></div>')

S = []

S.append(dict(vo="Your 24 gigabyte card runs Qwen 3.8 27B perfectly. Then you give it long context, and it needs 26 gigabytes.",
 cues={"a":"Your 24","b":"runs Qwen","f":"27B","c":"perfectly","d":"long context","e":"26 gigabytes"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap0@">Qwen 3.8 27B &middot; measured, not estimated</div>
      <div style="display:flex;align-items:flex-end;gap:120px">
        <div class="stat"><div class="bf-big" style="font-size:200px;color:var(--lime)" data-in="@a@">24<span style="font-size:78px">GB</span></div>
          <div class="bf-sub" data-in="@b@">your card</div></div>
        <div class="stat"><div class="bf-big" style="font-size:200px;color:var(--red)" data-in="@e@">26<span style="font-size:78px">GB</span></div>
          <div class="bf-sub" data-in="@d@">at 128K context</div></div>
      </div>
      <div class="chalk" data-in="@f@" style="font-family:var(--mono);font-size:22px;letter-spacing:.18em;color:var(--gray)">27B PARAMETERS</div>
      <div class="bf-cap" data-in="@c@" style="color:var(--lime)">it runs perfectly</div>
      <div class="bf-tape" data-in="@e@">it does not fit</div>
    </div>'''))

S.append(dict(vo="The model is not the problem. Qwen 3.8 27B at four bit is 16.68 gigabytes. That fits with seven to spare.",
 cues={"a":"The model","b":"Qwen 3.8","b2":"27B","c":"four bit","d":"16.68","e":"gigabytes","f":"seven to spare"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap1@">The model is not the problem</div>
      <div class="col">
        <div style="display:flex;justify-content:space-between;align-items:baseline">
          <span class="bf-row__k" data-in="@b@">Qwen 3.8 27B</span>
          <span class="bf-row__v" style="color:var(--lime);font-size:40px" data-in="@d@">16.68 GiB</span>
        </div>
        <div class="chalk" data-in="@b2@" style="align-self:flex-start;font-family:var(--mono);font-size:20px;letter-spacing:.16em;color:var(--gray)">Q4_K SMALL</div>
        <div class="bf-bar__track" style="height:72px;flex:0 0 auto">
          <div class="bf-bar__fill grow" style="--w:69%;background:var(--lime)" data-in="@e@"></div>
        </div>
        <div style="display:flex;justify-content:space-between" class="bf-sub">
          <span data-in="@e@">0</span><span style="color:var(--lime)" data-in="@f@">7 GB spare</span><span data-in="@c@">24 GB</span>
        </div>
      </div>
    </div>'''))

S.append(dict(vo="The problem is everything else. Every token in the context writes two more matrices into memory. The weights stay still. The cache does not.",
 cues={"a":"The problem","b":"Every token","c":"writes two","d":"matrices","e":"The weights stay","f":"The cache does not"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap2@">Weights stay still &middot; the cache does not</div>
      <div class="col">
        <div class="bf-bar" data-in="@a@"><span class="bf-bar__lab">Weights</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:69%;background:var(--lime)" data-in="@e@"></div></div>
          <span class="bf-bar__val" data-in="@a@">16.7 GB</span></div>
        <div class="bf-bar" data-in="@b@"><span class="bf-bar__lab">+ KV cache</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:24%;background:var(--yellow)" data-in="@b@"></div></div>
          <span class="bf-bar__val" style="color:var(--yellow)" data-in="@b@">grows</span></div>
        <div class="bf-bar" data-in="@c@"><span class="bf-bar__lab">at 128K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:72%;background:var(--red)" data-in="@c@"></div></div>
          <span class="bf-bar__val" style="color:var(--red)" data-in="@d@">17 GB</span></div>
      </div>
      <div class="bf-cap" data-in="@f@" style="color:var(--red)">Every token writes two matrices: key and value</div>
    </div>'''))

S.append(dict(vo="Here is the measured VRAM at every context length. Four K: 18 gigabytes. 32K: 20. 64K: 22. 128K: 26. And 256K: 34.",
 cues={"a":"Here is","g":"every context","b":"Four K","c":"18 gigabytes","d":"32K","e":"20.",
       "h":"64K","i":"22.","j":"128K","k":"26.","l":"256K","m":"34."},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap3@">Measured VRAM by context length</div>
      <div class="bf-sub" data-in="@g@" style="color:var(--gray)">llama.cpp &middot; single GPU &middot; Q4_K Small</div>
      <div class="col" style="gap:14px">
        ''' + row("4K","18 GB","b","c") + '''
        ''' + row("32K","20 GB","d","e") + '''
        ''' + row("64K","22 GB","h","i","var(--lime)") + '''
        ''' + row("128K","26 GB","j","k","var(--red)",True) + '''
        ''' + row("256K","34 GB","l","m","var(--red)",True) + '''
      </div>
    </div>'''))

S.append(dict(vo="On a 24 gigabyte card, 64K is the ceiling. That is 22 gigabytes used and two left for the system.",
 cues={"a":"On a 24","b":"64K","c":"the ceiling","d":"22","e":"two left"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap4@">On a 24 gigabyte card</div>
      <div class="col">
        <div class="bf-row" data-in="@a@"><span class="bf-row__k">Context ceiling</span>
          <span class="bf-row__v" style="color:var(--yellow)" data-in="@b@">64K</span></div>
        <div class="bf-bar" style="height:96px" data-in="@d@"><span class="bf-bar__lab" style="font-size:22px">22 OF 24 GB</span>
          <div class="bf-bar__track" style="height:64px"><div class="bf-bar__fill grow" style="--w:92%;background:var(--yellow)" data-in="@d@"></div></div>
          <span class="bf-bar__val" style="color:var(--red)" data-in="@e@">2 left</span></div>
      </div>
      <div class="bf-tape" data-in="@c@">the ceiling</div>
    </div>'''))

S.append(dict(vo="Long context costs speed as well. An RTX 3090 drops from 40 tokens a second to 34 at 64K. A 5090 falls from 75 to 23 at 128K.",
 cues={"a":"Long context","a2":"costs","b":"An RTX","c":"3090","d":"40","e":"34 at","f":"64K","g":"A 5090","h":"75","i":"23 at","j":"128K"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap5@">And it costs speed</div>
      <div class="col">
        <div class="bf-bar" data-in="@b@"><span class="bf-bar__lab" data-in="@c@">RTX 3090 &middot; 4K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:100%" data-in="@d@"></div></div>
          <span class="bf-bar__val" data-in="@d@">40</span></div>
        <div class="bf-bar" data-in="@e@"><span class="bf-bar__lab">RTX 3090 &middot; 64K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:85%;background:var(--yellow)" data-in="@e@"></div></div>
          <span class="bf-bar__val" style="color:var(--yellow)">34</span></div>
        <div class="bf-bar" data-in="@g@"><span class="bf-bar__lab" data-in="@j@">RTX 5090 &middot; 4K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:100%;background:var(--lime)" data-in="@h@"></div></div>
          <span class="bf-bar__val" style="color:var(--lime)" data-in="@h@">75</span></div>
        <div class="bf-bar" data-in="@i@"><span class="bf-bar__lab">RTX 5090 &middot; 128K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:31%;background:var(--red)" data-in="@i@"></div></div>
          <span class="bf-bar__val" style="color:var(--red)">23</span></div>
      </div>
      <div class="bf-sub" data-in="@f@">tokens per second</div>
    </div>'''))

S.append(dict(vo="So buy by context, not by card. 24 gigabytes buys 64K. 32 buys 128K. Past that you need unified memory.",
 cues={"a":"So buy","b":"not by card","c":"24 gigabytes","d":"buys 64K","e":"32 buys","f":"128K","g":"Past that","h":"unified memory"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap6@">Buy by context, not by card</div>
      <div class="col" style="gap:14px">
        <div class="bf-row" data-in="@c@"><span class="bf-row__k">24 GB</span><span class="bf-row__v" data-in="@d@">64K</span></div>
        <div class="bf-row bf-row--good" data-in="@e@"><span class="bf-row__k">32 GB</span><span class="bf-row__v" style="color:var(--lime)" data-in="@f@">128K</span></div>
        <div class="bf-row" data-in="@g@"><span class="bf-row__k">128 GB unified</span><span class="bf-row__v" data-in="@h@">256K+</span></div>
      </div>
      <div class="bf-sub" data-in="@b@" style="color:var(--dim)">the card is not the spec</div>
    </div>'''))

S.append(dict(vo="Measure the context you actually use, then buy the smallest card that holds it.",
 cues={"a":"Measure","b":"you actually use","c":"then buy"},
 html='''    <div class="ctr">
      <div class="bf-big" style="font-size:72px;text-align:center" data-in="@a@">Measure the context you actually use.</div>
      <div class="bf-cap" data-in="@b@" style="color:var(--yellow);font-size:24px">not the context the box advertises</div>
      <div class="bf-tape" data-in="@c@" style="font-size:30px;padding:16px 34px;transform:rotate(-3deg)">then buy the smallest card that holds it</div>
      <div class="bf-wm">byte forensics</div>
    </div>'''))

work = os.path.join(ROOT, "byte", "build")
A = os.path.join(work, "audio"); os.makedirs(A, exist_ok=True)
af = ("silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,"
      "areverse,silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,areverse")
WORDS = []

async def go():
    for i, sc in enumerate(S, 1):
        raw = os.path.join(A, f"raw{i}.mp3"); wav = os.path.join(A, f"n{i}.wav")
        c = edge_tts.Communicate(sc["vo"], VOICE, rate=RATE, boundary="WordBoundary")
        buf = bytearray(); ws = []
        async for ch in c.stream():
            if ch["type"] == "audio": buf += ch["data"]
            elif ch["type"] == "WordBoundary": ws.append((ch["offset"]/1e7, ch["text"]))
        open(raw, "wb").write(bytes(buf))
        o = subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",raw,"-af",
                            "silencedetect=noise=-45dB:d=0.05","-f","null","-"],
                           capture_output=True,text=True).stderr
        ends = re.findall(r"silence_end: ([0-9.]+)", o)
        lead = float(ends[0]) if ends else 0.0
        subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-i",raw,"-af",af,
                        "-ar","44100","-ac","1","-c:a","pcm_s16le",wav], check=True)
        WORDS.append([(max(0.0, x - lead + 0.04), w) for x, w in ws])
        os.remove(raw)
asyncio.run(go())

d = [dur(os.path.join(A, f"n{i}.wav")) for i in range(1, len(S)+1)]
starts, acc = [], 0.0
for i in range(len(d)):
    starts.append(acc); acc += d[i] + GAP
total = sum(d) + GAP*(len(d)-1) + TAIL

g = os.path.join(A,"g.wav"); t = os.path.join(A,"t.wav")
for path, ln in ((g, GAP), (t, TAIL)):
    subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi",
                    "-i","anullsrc=r=44100:cl=mono","-t",str(ln),"-c:a","pcm_s16le",path],check=True)
lst=[]
for i in range(1,len(S)+1):
    lst.append(f"file '{(A+'/n%d.wav'%i).replace(chr(92),'/')}'")
    if i < len(S): lst.append(f"file '{(A+'/g.wav').replace(chr(92),'/')}'")
lst.append(f"file '{(A+'/t.wav').replace(chr(92),'/')}'")
open(os.path.join(A,"l.txt"),"w").write("\n".join(lst))
vo_mp3 = os.path.join(work, "vo.mp3")
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","concat","-safe","0",
                "-i",os.path.join(A,"l.txt"),"-c:a","libmp3lame","-b:a","192k",vo_mp3],check=True)

cue_t = {}
for i, sc in enumerate(S):
    al = align(sc["vo"], WORDS[i])
    for tok, phrase in sc["cues"].items():
        wt = phrase_time(sc["vo"], al, WORDS[i], phrase)
        cue_t[(i, tok)] = max(starts[i]+0.05, min(starts[i]+wt-0.08, starts[i]+d[i]-0.10))

def rel(tok, i):
    """cue tokens are namespaced per scene — 'b' in scene 5 is not 'b' in scene 2"""
    if tok.startswith("cap"): return 0.15
    return round(cue_t[(i, tok)] - starts[i], 2)

sections = []
for i, sc in enumerate(S):
    h = re.sub(r'data-in="@(\w+)@"',
               lambda m, i=i: 'data-in="%s"' % rel(m.group(1), i), sc["html"])
    left = [v for v in re.findall(r'data-in="([^"]*)"', h) if not re.fullmatch(r"[0-9.]+", v)]
    assert not left, f"unresolved cues scene {i+1}: {left}"
    sections.append(f'  <section class="scene" data-scene="{i}">\n{h}\n  </section>')

events = []
for i, _ in enumerate(S):
    for v in re.findall(r'data-in="([0-9.]+)"', sections[i]):
        events.append(round(starts[i] + float(v), 3))
events = sorted(set(events))
gaps = [(q-p, p, q) for p, q in zip(events, events[1:])]
worst = max(gaps)[0] if gaps else 0
print(f"audio {dur(vo_mp3):.2f}s   timeline {total:.2f}s   events {len(events)}   avg {total/len(events):.2f}s")
for gg, p, q in sorted(gaps, reverse=True)[:5]:
    print(f"   gap {gg:5.2f}s  {p:6.2f} -> {q:6.2f}{'   OVER' if gg>MAX_GAP else ''}")
assert worst <= MAX_GAP, f"visual gap {worst:.2f}s exceeds {MAX_GAP}s"
print(f"max gap {worst:.2f}s  (limit {MAX_GAP}s)  OK")

wipes = [round(starts[3]-0.285,3), round(starts[6]-0.285,3)]
sfx = []
for si, tok, kind in [(0,"a","tick"),(0,"f","tick"),(0,"c","tick"),(0,"e","thud"),
                      (1,"b","tick"),(1,"e","thud"),
                      (2,"d","tick"),(2,"e","tick"),
                      (3,"b","tick"),(3,"m","thud"),
                      (4,"b","tick"),(4,"e","thud"),
                      (5,"d","tick"),(5,"h","tick"),
                      (6,"c","tick"),(6,"f","thud"),
                      (7,"b","tick")]:
    sfx.append((round(cue_t[(si, tok)], 3), kind))
for w in wipes: sfx.append((w,"whoosh"))
sfx.sort()

b64 = base64.b64encode(open(vo_mp3,"rb").read()).decode()
byte_css = open(os.path.join(ROOT,"core","byte.css"),encoding="utf-8").read().replace('url("fonts/','url("core/fonts/')
player_css = open(os.path.join(ROOT,"core","player.css"),encoding="utf-8").read()
player_js = open(os.path.join(ROOT,"core","player.js"),encoding="utf-8").read()
scenes_js = ",\n  ".join(f"{{s:{starts[i]:5.2f},  e:{starts[i]+d[i]:5.2f}}}" for i in range(len(d)))
sfx_js = "\n".join(f"  {{t:{x:6.3f}, f:'{k}'}}," for x,k in sfx)

html = f"""<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<title>How Much VRAM Does Qwen 3.8 27B Really Need?</title>
<style>
{byte_css}
{player_css}
  .ctr{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;
        justify-content:center;gap:34px;padding:0 110px}}
  .stat{{display:flex;flex-direction:column;align-items:center;gap:16px}}
  .col{{display:flex;flex-direction:column;gap:20px;width:1240px}}
  .grow{{width:0}}
  .grow.on{{width:var(--w)}}
  .no-js #start{{display:none!important}}
  .no-js .scene:first-of-type{{opacity:1!important;visibility:visible!important}}
  .no-js [data-in]{{opacity:1!important;transform:none!important}}
  .no-js .grow{{width:var(--w)!important}}
</style>
</head>
<body>
<script>document.documentElement.classList.remove("no-js");</script>
<div id="wrap"><div id="stage">

{chr(10).join(sections)}

</div></div>
<script>
window.EPISODE = {{
  kicker: "Byte Forensics",
  title: "How Much VRAM Does Qwen 3.8 27B Really Need?",
  subtitle: "measured 4K to 256K \\u00b7 one 24 GB card",
  total: {total:.2f},
  maxGap: {MAX_GAP},
  vo: "data:audio/mpeg;base64,{b64}",
  sfxBase: "audio/",
  labels: ['01 HOOK','02 THE MODEL','03 THE CACHE','04 MEASURED','05 CEILING','06 SPEED COST','07 VERDICT','08 CLOSE'],
  scenes: [
  {scenes_js}
  ],
  wipes: [{', '.join('%.3f'%w for w in wipes)}],
  wipeColors: ['yellow','blue'],
  sfx: [
{sfx_js}
  ]
}};
</script>
<script>
{player_js}
</script>
</body>
</html>
"""
out = os.path.join(ROOT, NAME + ".html")
open(out, "w", encoding="utf-8").write(html)
print(f"wrote {out}  ({len(html)//1024} KB)")
for f in os.listdir(A):
    if f.endswith((".wav",".txt")): os.remove(os.path.join(A,f))
