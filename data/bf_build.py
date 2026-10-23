import asyncio, edge_tts, os, re, subprocess, base64, shutil

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
VOICE = "en-US-AndrewNeural"
RATE = "+8%"
GAP = 0.25
TAIL = 0.8
NAME = "BYTE-01"

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

# ------------------------------------------------------------------ script
SCENES = [
 dict(vo="Your 24 gigabyte card runs Qwen 3.8 27B perfectly. Then you give it long context, and it needs 26 gigabytes.",
      cues={"s1a":"Your 24 gigabyte card","s1b":"26 gigabytes"},
      html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap0@">Qwen 3.8 27B &middot; measured, not estimated</div>
      <div style="display:flex;align-items:flex-end;gap:120px">
        <div class="stat"><div class="bf-big" style="font-size:210px;color:var(--lime)" data-in="@s1a@">24<span style="font-size:82px">GB</span></div>
          <div class="bf-sub" data-in="@s1a@">your card</div></div>
        <div class="stat"><div class="bf-big" style="font-size:210px;color:var(--red)" data-in="@s1b@">26<span style="font-size:82px">GB</span></div>
          <div class="bf-sub" data-in="@s1b@">at 128K context</div></div>
      </div>
      <div class="bf-tape" data-in="@s1b@">it does not fit</div>
    </div>'''),

 dict(vo="The model is not the problem. Qwen 3.8 27B at four bit is 16.68 gigabytes. That fits with seven to spare.",
      cues={"s2a":"Qwen 3.8 27B at four bit","s2b":"seven to spare"},
      html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap1@">The model is not the problem</div>
      <div class="col">
        <div style="display:flex;justify-content:space-between;align-items:baseline" data-in="@s2a@">
          <span class="bf-row__k">Qwen 3.8 27B &middot; Q4_K Small</span>
          <span class="bf-row__v" style="color:var(--lime);font-size:40px">16.68 GiB</span>
        </div>
        <div class="bf-bar__track" style="height:72px;flex:0 0 auto">
          <div class="bf-bar__fill grow" style="--w:69%;background:var(--lime)" data-in="@s2a@"></div>
        </div>
        <div style="display:flex;justify-content:space-between" class="bf-sub">
          <span>0</span><span style="color:var(--lime)">7 GB spare</span><span>24 GB</span>
        </div>
      </div>
      <div class="bf-cap" data-in="@s2b@" style="color:var(--lime)">The weights were never the problem</div>
    </div>'''),

 dict(vo="The problem is everything else. Every token in the context writes two more matrices into memory. The weights stay still. The cache does not.",
      cues={"s3a":"The problem is everything else","s3b":"Every token"},
      html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap2@">Weights stay still &middot; the cache does not</div>
      <div class="col">
        <div class="bf-bar" data-in="@s3a@"><span class="bf-bar__lab">Weights</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:69%;background:var(--lime)" data-in="@s3a@"></div></div>
          <span class="bf-bar__val">16.7 GB</span></div>
        <div class="bf-bar" data-in="@s3b@"><span class="bf-bar__lab">+ KV cache</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:72%;background:var(--yellow)" data-in="@s3b@"></div></div>
          <span class="bf-bar__val" style="color:var(--yellow)">grows</span></div>
      </div>
      <div class="bf-cap" data-in="@s3b@" style="color:var(--red)">Every token writes two matrices: key and value</div>
    </div>'''),

 dict(vo="Here is the measured VRAM at every context length. Four K: 18 gigabytes. 32K: 20. 64K: 22. 128K: 26. And 256K: 34.",
      cues={"s4a":"Four K","s4b":"32K","s4c":"64K","s4d":"128K","s4e":"256K"},
      html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap3@">Measured VRAM by context length</div>
      <div class="col" style="gap:16px">
        <div class="bf-row" data-in="@s4a@"><span class="bf-row__k">4K</span><span class="bf-row__v">18 GB</span></div>
        <div class="bf-row" data-in="@s4b@"><span class="bf-row__k">32K</span><span class="bf-row__v">20 GB</span></div>
        <div class="bf-row bf-row--good" data-in="@s4c@"><span class="bf-row__k">64K</span><span class="bf-row__v" style="color:var(--lime)">22 GB</span></div>
        <div class="bf-row bf-row--hot" data-in="@s4d@"><span class="bf-row__k">128K</span><span class="bf-row__v" style="color:var(--red)">26 GB</span></div>
        <div class="bf-row bf-row--hot" data-in="@s4e@"><span class="bf-row__k">256K</span><span class="bf-row__v" style="color:var(--red)">34 GB</span></div>
      </div>
    </div>'''),

 dict(vo="On a 24 gigabyte card, 64K is the ceiling. That is 22 gigabytes used and two left for the system.",
      cues={"s5a":"64K is the ceiling","s5b":"two left"},
      html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap4@">On 24 gigabytes</div>
      <div class="col" data-in="@s5a@">
        <div class="bf-bar" style="height:96px"><span class="bf-bar__lab" style="font-size:22px">22 of 24 GB</span>
          <div class="bf-bar__track" style="height:64px"><div class="bf-bar__fill grow" style="--w:92%;background:var(--yellow)" data-in="@s5a@"></div></div>
          <span class="bf-bar__val" style="color:var(--red)">2 left</span></div>
      </div>
      <div class="bf-tape" data-in="@s5b@">64K is the line</div>
    </div>'''),

 dict(vo="Long context costs speed as well. An RTX 3090 drops from 40 tokens a second to 34 at 64K. A 5090 falls from 75 to 23 at 128K.",
      cues={"s6a":"An RTX 3090","s6b":"A 5090"},
      html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap5@">And it costs speed</div>
      <div class="col">
        <div class="bf-bar" data-in="@s6a@"><span class="bf-bar__lab">RTX 3090 &middot; 4K&rarr;64K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:100%" data-in="@s6a@"></div></div>
          <span class="bf-bar__val">40 &rarr; 34</span></div>
        <div class="bf-bar" data-in="@s6b@"><span class="bf-bar__lab">RTX 5090 &middot; 4K&rarr;128K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:31%;background:var(--red)" data-in="@s6b@"></div></div>
          <span class="bf-bar__val" style="color:var(--red)">75 &rarr; 23</span></div>
      </div>
      <div class="bf-sub" data-in="@s6b@">tokens per second</div>
    </div>'''),

 dict(vo="So buy by context, not by card. 24 gigabytes buys 64K. 32 buys 128K. Past that you need unified memory.",
      cues={"s7a":"24 gigabytes buys","s7b":"32 buys","s7c":"Past that"},
      html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap6@">Buy by context, not by card</div>
      <div class="col" style="gap:16px">
        <div class="bf-row" data-in="@s7a@"><span class="bf-row__k">24 GB</span><span class="bf-row__v">64K</span></div>
        <div class="bf-row bf-row--good" data-in="@s7b@"><span class="bf-row__k">32 GB</span><span class="bf-row__v" style="color:var(--lime)">128K</span></div>
        <div class="bf-row" data-in="@s7c@"><span class="bf-row__k">128 GB unified</span><span class="bf-row__v">256K+</span></div>
      </div>
    </div>'''),

 dict(vo="Measure the context you actually use, then buy the smallest card that holds it.",
      cues={"s8a":"Measure the context","s8b":"then buy"},
      html='''    <div class="ctr">
      <div class="bf-big" style="font-size:74px;text-align:center" data-in="@s8a@">Measure the context you actually use.</div>
      <div class="bf-tape" data-in="@s8b@" style="font-size:32px;padding:16px 34px;transform:rotate(-3deg)">then buy the smallest card that holds it</div>
      <div class="bf-wm">byte forensics</div>
    </div>'''),
]

# ------------------------------------------------------------------ build
work = os.path.join(ROOT, "byte", "build")
os.makedirs(os.path.join(work, "audio"), exist_ok=True)
A = os.path.join(work, "audio")

af = ("silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,"
      "areverse,silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,areverse")
WORDS = []

async def go():
    for i, sc in enumerate(SCENES, 1):
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

d = [dur(os.path.join(A, f"n{i}.wav")) for i in range(1, len(SCENES)+1)]
starts, acc = [], 0.0
for i in range(len(d)):
    starts.append(acc); acc += d[i] + GAP
total = sum(d) + GAP*(len(d)-1) + TAIL

# concat
g = os.path.join(A, "g.wav"); t = os.path.join(A, "t.wav")
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi","-i","anullsrc=r=44100:cl=mono",
                "-t",str(GAP),"-c:a","pcm_s16le",g],check=True)
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi","-i","anullsrc=r=44100:cl=mono",
                "-t",str(TAIL),"-c:a","pcm_s16le",t],check=True)
lst=[]
for i in range(1,len(SCENES)+1):
    lst.append(f"file '{(A+'/n%d.wav'%i).replace(chr(92),'/')}'")
    if i < len(SCENES): lst.append(f"file '{(A+'/g.wav').replace(chr(92),'/')}'")
lst.append(f"file '{(A+'/t.wav').replace(chr(92),'/')}'")
open(os.path.join(A,"l.txt"),"w").write("\n".join(lst))
vo_mp3 = os.path.join(work, "vo.mp3")
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","concat","-safe","0",
                "-i",os.path.join(A,"l.txt"),"-c:a","libmp3lame","-b:a","192k",vo_mp3],check=True)
print(f"audio: {dur(vo_mp3):.2f}s  timeline: {total:.2f}s")

# cues on exact words
cue_t = {}
for i, sc in enumerate(SCENES):
    al = align(sc["vo"], WORDS[i])
    for tok, phrase in sc["cues"].items():
        wt = phrase_time(sc["vo"], al, WORDS[i], phrase)
        cue_t[tok] = max(starts[i]+0.05, min(starts[i]+wt-0.08, starts[i]+d[i]-0.10))
        print(f"   sc{i+1} {tok:4} cue={cue_t[tok]:6.2f}  word={starts[i]+wt:6.2f}  {phrase!r}")

def rel(tok):
    if tok.startswith("cap"):
        return 0.15          # caption lands as the scene opens
    for i, sc in enumerate(SCENES):
        if tok in sc["cues"]: return round(cue_t[tok]-starts[i], 2)
    raise KeyError(tok)

sections = []
for i, sc in enumerate(SCENES):
    h = re.sub(r'data-in="@(\w+)@"', lambda m: 'data-in="%s"' % rel(m.group(1)), sc["html"])
    left = [v for v in re.findall(r'data-in="([^"]*)"', h) if not re.fullmatch(r"[0-9.]+", v)]
    assert not left, f"unresolved cues in scene {i+1}: {left}"
    sections.append(f'  <section class="scene" data-scene="{i}">\n{h}\n  </section>')

# wipes land full-cover on cuts 4 and 7 (0-based scenes 3 and 6)
wipes = [round(starts[3]-0.285,3), round(starts[6]-0.285,3)]

sfx = []
for tok, kind in [("s2a","tick"),("s2b","tick"),("s3a","tick"),("s3b","thud"),
                  ("s4a","tick"),("s4b","tick"),("s4c","tick"),("s4d","tick"),("s4e","thud"),
                  ("s5b","thud"),("s6a","tick"),("s6b","thud"),("s7b","tick"),("s8b","thud")]:
    sfx.append((round(cue_t[tok],3), kind))
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
        justify-content:center;gap:56px;padding:0 110px}}
  .stat{{display:flex;flex-direction:column;align-items:center;gap:18px}}
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
  vo: "data:audio/mpeg;base64,{b64}",
  sfxBase: "audio/",
  labels: ['01 THE HOOK','02 THE MODEL','03 THE CACHE','04 THE MEASUREMENT','05 THE CEILING','06 THE SPEED COST','07 THE VERDICT','08 CLOSE'],
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
print(f"\nwrote {out}  ({len(html)//1024} KB)")
for f in os.listdir(A):
    if f.endswith((".wav",".txt")): os.remove(os.path.join(A,f))
