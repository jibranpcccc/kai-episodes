import asyncio, edge_tts, os, re, subprocess, json, shutil

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
VOICE = "en-US-AndrewNeural"
RATE  = "+8%"
GAP   = 0.25
TAIL  = 0.7   # hold the end card

def dur(p):
    return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                                 "-of","csv=p=0",p],capture_output=True,text=True).stdout.strip())

def onsets(p):
    o = subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",p,"-af",
                        "silencedetect=noise=-45dB:d=0.16","-f","null","-"],
                       capture_output=True,text=True).stderr
    return [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", o)]

def render_vo(vo_dir, lines):
    os.makedirs(vo_dir, exist_ok=True)
    af = ("silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,"
          "areverse,silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,areverse")
    WORDS = []

    async def go():
        for i, t in enumerate(lines, 1):
            raw = os.path.join(vo_dir, f"raw{i}.mp3")
            wav = os.path.join(vo_dir, f"n{i}.wav")
            c = edge_tts.Communicate(t, VOICE, rate=RATE, boundary="WordBoundary")
            buf = bytearray(); ws = []
            async for ch in c.stream():
                if ch["type"] == "audio":
                    buf += ch["data"]
                elif ch["type"] == "WordBoundary":
                    ws.append((ch["offset"] / 1e7, ch["text"]))
            open(raw, "wb").write(bytes(buf))
            o = subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",raw,"-af",
                                "silencedetect=noise=-45dB:d=0.05","-f","null","-"],
                               capture_output=True,text=True).stderr
            ends = re.findall(r"silence_end: ([0-9.]+)", o)
            lead = float(ends[0]) if ends else 0.0
            subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-i",raw,"-af",af,
                            "-ar","44100","-ac","1","-c:a","pcm_s16le", wav], check=True)
            WORDS.append((t, [(max(0.0, x - lead + 0.04), w) for x, w in ws]))
            os.remove(raw)
    asyncio.run(go())
    d = [dur(os.path.join(vo_dir, f"n{i}.wav")) for i in range(1, len(lines)+1)]
    sil = os.path.join(vo_dir, "g.wav")
    subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi",
                    "-i","anullsrc=r=44100:cl=mono","-t",str(GAP),"-c:a","pcm_s16le", sil], check=True)
    lst = []
    for i in range(1, len(lines)+1):
        lst.append(f"file '{(vo_dir+'/n%d.wav'%i).replace(chr(92),'/')}'")
        if i < len(lines): lst.append(f"file '{(vo_dir+'/g.wav').replace(chr(92),'/')}'")
    tail = os.path.join(vo_dir,"t.wav")
    subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi",
                    "-i","anullsrc=r=44100:cl=mono","-t",str(TAIL),"-c:a","pcm_s16le", tail], check=True)
    lst.append(f"file '{(vo_dir+'/t.wav').replace(chr(92),'/')}'")
    open(os.path.join(vo_dir,"l.txt"),"w").write("\n".join(lst))
    subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","concat","-safe","0",
                    "-i",os.path.join(vo_dir,"l.txt"),"-c:a","libmp3lame","-b:a","192k",
                    os.path.join(vo_dir,"vo.mp3")], check=True)
    return d, WORDS

def frac(text, phrase):
    try: return text.lower().index(phrase.lower()) / max(len(text),1)
    except ValueError: return 0.0

def align(text, words):
    """Map each spoken word back to its character index in the script."""
    low = text.lower(); out = []; cur = 0
    for t, w in words:
        wl = w.lower().strip(".,;:!?\"'()")
        idx = low.find(wl, cur) if wl else -1
        if idx < 0:
            idx = cur
        else:
            cur = idx + len(wl)
        out.append((idx, t))
    return out


def phrase_time(text, aligned, words, phrase):
    """Time the phrase actually starts speaking."""
    p = text.lower().find(phrase.lower())
    if p < 0:
        raise ValueError(f"cue phrase not found in script: {phrase!r}")
    for ci, t in aligned:
        if ci >= p:
            return t
    return aligned[-1][1] if aligned else 0.0


def build(spec):
    folder = os.path.join(ROOT, spec["folder"])
    os.makedirs(folder, exist_ok=True)
    lines = [s["vo"] for s in spec["scenes"]]
    d, WORDS = render_vo(os.path.join(folder,"audio"), lines)
    starts, acc = [], 0.0
    for i in range(len(d)):
        starts.append(acc); acc += d[i] + GAP
    total = sum(d) + GAP*(len(d)-1) + TAIL

    # ---- cues ride on the exact spoken word ----
    cue_t = {}; cue_info = []
    for i, s_spec in enumerate(spec["scenes"]):
        words = WORDS[i][1]
        aligned = align(s_spec["vo"], words)
        for tok, phrase in s_spec.get("cues", {}).items():
            wt = phrase_time(s_spec["vo"], aligned, words, phrase)
            t = max(starts[i] + 0.05, min(starts[i] + wt - 0.08, starts[i] + d[i] - 0.10))
            cue_t[tok] = t
            cue_info.append((i, tok, phrase, starts[i] + wt, t))


    def rel(tok):
        for i, s in enumerate(spec["scenes"]):
            if tok in s.get("cues", {}):
                return round(cue_t[tok] - starts[i], 2)
        raise KeyError(tok)

    scenes_html = []
    for i, s in enumerate(spec["scenes"]):
        html = s["html"]
        html = re.sub(r'data-in="@(\w+)@"', lambda m: 'data-in="%s"' % rel(m.group(1)), html)
        leftover = re.findall(r'data-in="([^"]*)"', html)
        bad = [v for v in leftover if not re.fullmatch(r'[0-9.]+', v)]
        assert not bad, f"UNRESOLVED CUES in {spec['id']}: {bad}" 
        scenes_html.append(f'  <section class="scene" data-scene="{i}">\n{html}\n  </section>')

    # wipes land full-cover on the cut: start = cut - 0.285
    wipe_scenes = spec["wipes"]
    wipes = [round(starts[i]-0.285, 3) for i in wipe_scenes]

    sfx = []
    for tok in spec["sfx_ticks"]: sfx.append((round(cue_t[tok],3), "tick"))
    for tok in spec["sfx_thuds"]: sfx.append((round(cue_t[tok],3), "thud"))
    for w in wipes: sfx.append((w, "whoosh"))
    sfx.sort()

    scenes_js = ",\n  ".join(f"{{s:{starts[i]:5.2f},  e:{starts[i]+d[i]:5.2f}}}" for i in range(len(d)))
    sfx_js = "\n".join(f"  {{t:{t:6.3f}, f:'{k}'}}," for t, k in sfx)
    labels_js = ", ".join("'%s'" % l for l in spec["labels"])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{spec['title']}</title>
<link rel="stylesheet" href="../../core/kai.css">
<link rel="stylesheet" href="../../core/player.css">
<style>
  .ctr{{position:absolute;inset:0;display:flex;flex-direction:column;
        align-items:center;justify-content:center;gap:64px;padding:0 120px}}
  .stat{{display:flex;flex-direction:column;align-items:center;gap:16px}}
  .stat .n{{font-family:var(--sans);font-weight:800;letter-spacing:-.035em;line-height:1.04}}
  .stat .u{{font-family:var(--mono);font-size:19px;font-weight:700;letter-spacing:.20em;
           color:var(--dim);text-transform:uppercase}}
  .col{{display:flex;flex-direction:column;gap:26px;width:1240px}}
  .node--sel{{border-color:var(--blue);box-shadow:0 0 0 3px rgba(4,94,239,.35);
              background:rgba(4,94,239,.08)}}
  /* ---- graph furniture ---- */
  .scene::before{{content:"";position:absolute;inset:0;pointer-events:none;opacity:.5;
    background-image:radial-gradient(#1A2422 1px,transparent 1px);background-size:30px 30px}}
  .ruler{{position:absolute;left:0;right:0;margin:0 auto;bottom:158px;width:1100px;height:74px}}
  .ruler__line{{position:absolute;left:0;right:0;top:36px;height:2px;background:#3C4241}}
  .ruler__tick{{position:absolute;top:29px;width:2px;height:16px;background:#3C4241;transform:translateX(-50%)}}
  .ruler__tick span{{position:absolute;top:20px;left:50%;transform:translateX(-50%);font-family:var(--mono);
    font-weight:700;font-size:13px;letter-spacing:.14em;color:#6E7270;white-space:nowrap}}
  .ruler__dot{{position:absolute;top:31px;width:12px;height:12px;border-radius:50%;background:var(--yellow);
    transform:translateX(-50%);box-shadow:0 0 0 4px rgba(248,207,51,.18)}}
  .ruler__lab{{position:absolute;top:0;transform:translateX(-50%);font-family:var(--mono);font-weight:800;
    font-size:17px;color:var(--yellow);letter-spacing:.04em}}
  .ring{{position:absolute;right:120px;top:50%;margin-top:-100px;width:200px;height:200px}}
  .spark{{position:absolute;left:0;right:0;margin:0 auto;bottom:72px;width:520px;height:220px}}

  /* scale the chart furniture up to reference density */
  .bar{{height:66px}}
  .bar .bar__track{{height:44px}}
  .bar .bar__lab{{width:210px;font-size:19px}}
  .bar .bar__val{{width:155px;font-size:28px}}
  .prod__frame{{width:252px;height:196px}}
  .prod__cap{{font-size:17px;letter-spacing:.18em}}
</style>
</head>
<body>
<div id="wrap"><div id="stage">

{chr(10).join(scenes_html)}

</div></div>

<script>
window.EPISODE = {{
  kicker: "{spec['kicker']}",
  title: "{spec['title']}",
  subtitle: "{spec['subtitle']}",
  total: {total:.2f},
  vo: "audio/vo.mp3",
  sfxBase: "../../audio/",
  labels: [{labels_js}],
  scenes: [
  {scenes_js}
  ],
  wipes: [{', '.join('%.3f'%w for w in wipes)}],
  wipeColors: [{', '.join("'%s'"%c for c in spec.get('wipeColors',['yellow']*len(wipes)))}],
  sfx: [
{sfx_js}
  ]
}};
</script>
<script src="../../core/player.js"></script>
</body>
</html>
"""
    # publish the master audio next to the page it belongs to, and prove they match
    import shutil as _sh
    master = os.path.join(folder, "audio", "vo.mp3")
    pub = os.path.join(ROOT, "audio", spec["id"] + "_vo.mp3")
    os.makedirs(os.path.dirname(pub), exist_ok=True)
    _sh.copyfile(master, pub)
    ad = dur(pub)
    assert abs(ad - total) < 0.08, f"{spec['id']}: audio {ad:.2f}s vs cue timeline {total:.2f}s"
    print(f"   audio published: {pub}  {ad:.2f}s  (cue timeline {total:.2f}s, drift {ad-total:+.3f}s)")
    open(os.path.join(folder,"index.html"),"w",encoding="utf-8").write(html)
    for f in os.listdir(os.path.join(folder,"audio")):
        if f.endswith((".wav",".txt")): os.remove(os.path.join(folder,"audio",f))
    print(f"\n[{spec['id']}] {total:.2f}s  scenes={len(d)}  cues={len(cue_t)}  wipes={wipes}")
    for i, tok, phrase, wt, t in cue_info:
        print(f"     sc{i+1} {tok:9} cue={t:6.2f}  word={wt:6.2f}  lead={t-wt:+.2f}  {phrase!r}")
    for i,x in enumerate(d,1): print(f"   seg{i} {x:5.2f}s  start {starts[i-1]:6.2f}")
    return total

# =====================================================================
EP = []

EP.append(dict(
 id="ep02", folder="episodes/ep02",
 title="The Second Price Tag",
 kicker="Episode 02",
 subtitle="Electricity · local AI",
 labels=['01 HOOK','02 THE ARITHMETIC','03 IDLE','04 THE REAL BILL','05 THE FIX','06 VERDICT'],
 wipes=[3,5], wipeColors=['yellow','blue'],
 sfx_ticks=['paid','rates','idle','row1','row2','row3','pl','bars'],
 sfx_thuds=['bill','total','verdict'],
 scenes=[
  dict(vo="That GPU has a second price tag, and it isn't on the box.",
       cues={'paid':'That GPU has','bill':'second price tag'},
       html="""    <div class="ctr">
      <div class="cap" data-in="@paid@">The second price tag</div>
      <div style="display:flex;align-items:flex-end;gap:96px">
        <div class="stat"><div class="n wt" style="font-size:168px" data-in="@paid@">$1,600</div>
          <div class="u" data-in="@paid@">what you paid</div></div>
        <div class="big dim" style="font-size:96px;padding-bottom:44px" data-in="@bill@">&plus;</div>
        <div class="stat"><div class="n red" style="font-size:168px" data-in="@bill@">$294</div>
          <div class="u" data-in="@bill@">what it costs to run</div></div>
      </div>
    </div>"""),
  dict(vo="Four hundred and fifty watts under load, eight hours a day. At sixteen cents a kilowatt hour, that's one thousand three hundred and fourteen kilowatt hours a year.",
       cues={'rates':'At sixteen cents','total':'one thousand three hundred'},
       html="""    <div class="ctr">
      <div class="cap" data-in="@rates@">The arithmetic nobody does</div>
      <div style="display:flex;align-items:center;gap:20px">
        <div class="node" data-in="@rates@">450 W</div><span class="arrow">&times;</span>
        <div class="node" data-in="@rates@">8 H / DAY</div><span class="arrow">&times;</span>
        <div class="node" data-in="@rates@">365</div><span class="arrow">=</span>
        <div class="node node--sel" style="font-size:31px" data-in="@total@">1,314 kWh</div>
      </div>
      <div class="cap" data-in="@total@" style="color:var(--yellow)">at $0.16 / kWh</div>
    </div>"""),
  dict(vo="But the number nobody measures is idle. It still draws ninety watts for the other sixteen hours, whether you're using it or not.",
       cues={'idle':'is idle','idlebar':'It still draws ninety watts'},
       html="""    <div class="ctr">
      <div class="cap" data-in="@idle@">Load vs idle</div>
      <div class="col">
        <div class="bar" data-in="@idle@"><span class="bar__lab">Under load</span>
          <div class="bar__track"><div class="bar__fill grow" style="--w:100%;background:var(--yellow)" data-in="@idle@"></div></div>
          <span class="bar__val" style="color:var(--yellow)">450 W</span></div>
        <div class="bar" data-in="@idlebar@"><span class="bar__lab">Idle</span>
          <div class="bar__track"><div class="bar__fill grow" style="--w:20%" data-in="@idlebar@"></div></div>
          <span class="bar__val">90 W</span></div>
      </div>
      <div class="cap" data-in="@idlebar@" style="color:var(--red)">Idle runs the other 16 h</div>
    </div>"""),
  dict(vo="Load only, two hundred and ten dollars. Add the idle hours, two hundred and ninety four. Run it flat out round the clock, six hundred and thirty one.",
       cues={'row1':'Load only','row2':'Add the idle hours','row3':'Run it flat out'},
       html="""    <div class="ctr">
      <div class="cap">What it actually costs, per year</div>

      <div class="ruler" data-in="@row3@">
        <div class="ruler__line"></div>
        <div class="ruler__tick" style="left:0%"><span>$0</span></div>
        <div class="ruler__tick" style="left:100%"><span>$700</span></div>
        <div class="ruler__dot" style="left:30%"></div><div class="ruler__lab" style="left:30%">$210</div>
        <div class="ruler__dot" style="left:42%"></div><div class="ruler__lab" style="left:42%">$294</div>
        <div class="ruler__dot" style="left:90%"></div><div class="ruler__lab" style="left:90%">$631</div>
      </div>
      <div class="col" style="gap:22px">
        <div class="row" data-in="@row1@"><span class="row__rank">#1</span>
          <span class="row__name">Load only</span><span class="row__val">$210</span></div>
        <div class="row" data-in="@row2@"><span class="row__rank">#2</span>
          <span class="row__name">Plus idle</span><span class="row__val">$294</span></div>
        <div class="row row--sel" data-in="@row3@"><span class="cm"></span><span class="row__rank">#3</span>
          <span class="row__name">Round the clock</span><span class="row__val" style="color:var(--azure)">$631</span></div>
      </div>
    </div>"""),
  dict(vo="Cap the power limit at seventy percent, and you lose twelve percent of your speed for thirty percent less power.",
       cues={'pl':'Cap the power limit','bars':'you lose twelve percent'},
       html="""    <div class="ctr">
      <div class="cap" data-in="@pl@">Cap the power limit</div>
      <div class="col" style="width:1000px">
        <div class="bar" data-in="@pl@"><span class="bar__lab">Power</span>
          <div class="bar__track"><div class="bar__fill grow" style="--w:70%;background:var(--yellow)" data-in="@pl@"></div></div>
          <span class="bar__val" style="color:var(--yellow)">&minus;30%</span></div>
        <div class="bar" data-in="@bars@"><span class="bar__lab">Speed lost</span>
          <div class="bar__track"><div class="bar__fill grow" style="--w:88%" data-in="@bars@"></div></div>
          <span class="bar__val">&minus;12%</span></div>
      </div>
      <div class="tape" data-in="@bars@" style="font-size:29px;padding:14px 30px">70% power limit</div>
    </div>"""),
  dict(vo="So measure the wall, not the box.",
       cues={'verdict':'So measure'},
       html="""    <div class="ctr">
      <div class="tape" data-in="@verdict@" style="font-size:44px;padding:22px 44px;transform:rotate(-4deg)">
        Measure the wall, not the box</div>
      <div class="wm">&lt;yourchannel&gt;</div>
    </div>"""),
 ]))

EP.append(dict(
 id="ep03", folder="episodes/ep03",
 title="Two Users, Half the Speed",
 kicker="Episode 03",
 subtitle="Concurrency · local AI",
 labels=['01 HOOK','02 WHY','03 THE CACHE','04 THE MATH','05 THE FIX','06 VERDICT'],
 wipes=[3,5], wipeColors=['blue','yellow'],
 sfx_ticks=['one','gpu','kv','r1','r2','r3','r4','need'],
 sfx_thuds=['two','tape'],
 scenes=[
  dict(vo="One user gets forty tokens a second. Add a second user, and each of them gets twenty two.",
       cues={'one':'One user gets','two':'Add a second user'},
       html="""    <div class="ctr">
      <div class="cap" data-in="@one@">Same card · same model</div>
      <div style="display:flex;align-items:flex-end;gap:170px">
        <div class="stat"><div class="n az" style="font-size:190px" data-in="@one@">40</div>
          <div class="u" data-in="@one@">one user · tok/s</div></div>
        <div class="stat"><div class="n red" style="font-size:190px" data-in="@two@">22</div>
          <div class="u" data-in="@two@">two users · each</div></div>
      </div>
    </div>"""),
  dict(vo="The GPU isn't slower. The model now has to hold two conversations in memory at once, and memory is the thing you run out of first.",
       cues={'gpu':'The GPU isn','memory':'and memory is the thing'},
       html="""    <div class="ctr">
      <div class="cap" data-in="@gpu@">The GPU is not the problem</div>
      <div style="display:flex;align-items:center;gap:70px">
        <div class="prod" data-in="@gpu@"><div class="prod__frame"><span class="big wt" style="font-size:52px">1&times;</span></div>
          <div class="prod__cap">one conversation</div></div>
        <span class="arrow" data-in="@memory@" style="font-size:44px">&rarr;</span>
        <div class="prod" data-in="@memory@"><div class="prod__frame" style="border-color:var(--red)"><span class="big red" style="font-size:52px">2&times;</span></div>
          <div class="prod__cap" style="color:var(--red)">two in memory</div></div>
      </div>
      <div class="cap" data-in="@memory@" style="color:var(--yellow)">Memory is what you run out of first</div>
    </div>"""),
  dict(vo="The KV cache doubles, and the KV cache is what decides how many people fit.",
       cues={'kv':'The KV cache doubles','fits':'how many people fit'},
       html="""    <div class="ctr">
      <div class="cap" data-in="@kv@">The KV cache doubles</div>

      <svg class="ring" data-in="@fits@" viewBox="0 0 120 120">
        <circle cx="60" cy="60" r="52" fill="none" stroke="#1B2422" stroke-width="9"/>
        <circle cx="60" cy="60" r="52" fill="none" stroke="#F8CF33" stroke-width="9" stroke-linecap="round"
                stroke-dasharray="326.7" stroke-dashoffset="55.5" transform="rotate(-90 60 60)"/>
        <text x="60" y="57" text-anchor="middle" font-family="Inter,sans-serif" font-weight="800"
              font-size="25" fill="#F6F6F4">83%</text>
        <text x="60" y="74" text-anchor="middle" font-family="monospace" font-size="8.5"
              fill="#6E7270" letter-spacing="1.2">VRAM USED</text>
      </svg>
      <div class="col" style="width:900px;gap:14px">
        <div class="bar" data-in="@kv@" style="height:74px"><span class="bar__lab" style="width:230px">User one</span>
          <div class="bar__track" style="height:54px"><div class="bar__fill grow" style="--w:42%" data-in="@kv@"></div></div>
          <span class="bar__val">10 GB</span></div>
        <div class="bar" data-in="@fits@" style="height:74px"><span class="bar__lab" style="width:230px">User two</span>
          <div class="bar__track" style="height:54px"><div class="bar__fill grow" style="--w:84%;background:var(--yellow)" data-in="@fits@"></div></div>
          <span class="bar__val" style="color:var(--yellow)">20 GB</span></div>
      </div>
      <div class="cap" data-in="@fits@" style="color:var(--red)">The cache, not the weights, fills the card</div>
    </div>"""),
  dict(vo="One user, forty. Two, twenty two each. Four, nine. Eight, four.",
       cues={'r1':'One user, forty','r2':'Two, twenty two','r3':'Four, nine','r4':'Eight, four'},
       html="""    <div class="ctr">
      <div class="cap">Tokens per second, per user</div>

      <svg class="spark" data-in="@r4@" viewBox="0 0 260 110">
        <line x1="10" y1="100" x2="250" y2="100" stroke="#24302D" stroke-width="1.5"/>
        <polyline points="10,28.9 89.2,60.9 168.4,84 250,92.9" fill="none" stroke="#2294D6"
                  stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="10" cy="28.9" r="4" fill="#2294D6"/>
        <circle cx="89.2" cy="60.9" r="4" fill="#2294D6"/>
        <circle cx="168.4" cy="84" r="4" fill="#2294D6"/>
        <circle cx="250" cy="92.9" r="4" fill="#E12A27"/>
      </svg>
      <div class="col" style="gap:22px">
        <div class="row" data-in="@r1@"><span class="row__rank">#1</span><span class="row__name">1 user</span>
          <span class="row__val" style="color:var(--azure)">40</span></div>
        <div class="row" data-in="@r2@"><span class="row__rank">#2</span><span class="row__name">2 users</span>
          <span class="row__val" style="color:var(--azure)">22 each</span></div>
        <div class="row" data-in="@r3@"><span class="row__rank">#3</span><span class="row__name">4 users</span>
          <span class="row__val">9 each</span></div>
        <div class="row row--sel" data-in="@r4@"><span class="cm"></span><span class="row__rank">#4</span>
          <span class="row__name">8 users</span><span class="row__val" style="color:var(--red)">4 each</span></div>
      </div>
    </div>"""),
  dict(vo="You don't need a bigger GPU. You need less context per person, and that's a setting, not a purchase.",
       cues={'need':'You don','setting':'and that'},
       html="""    <div class="ctr">
      <div class="big wt" style="font-size:74px;text-align:center" data-in="@need@">You don't need a bigger GPU.</div>
      <div class="big yel" style="font-size:74px;text-align:center" data-in="@need@">You need less context.</div>
      <div class="cap" data-in="@setting@" style="color:var(--dim)">That is a setting, not a purchase</div>
    </div>"""),
  dict(vo="Halve the context, and you double the users on the same card.",
       cues={'tape':'Halve the context'},
       html="""    <div class="ctr">
      <div class="tape" data-in="@tape@" style="font-size:42px;padding:22px 44px;transform:rotate(-4deg)">
        Half the context, twice the users</div>
      <div class="cap" data-in="@tape@" style="color:var(--azure);font-size:22px">2 users &rarr; 4 on the same card</div>
      <div class="wm">&lt;yourchannel&gt;</div>
    </div>"""),
 ]))

if __name__ == "__main__":
    for s in EP:
        build(s)
