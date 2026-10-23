import asyncio, edge_tts, os, re, subprocess, base64

ROOT=r"C:\Users\jibra\Desktop\1\KAI"
VOICE="en-US-AndrewNeural"; RATE="+8%"; GAP=0.30; TAIL=2.6; MAX_GAP=2.0; TICK=1.45
NAME="BYTE-02"

def dur(p):
    return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
        "-of","csv=p=0",p],capture_output=True,text=True).stdout.strip())

def align(text,words):
    low=text.lower(); out=[]; cur=0
    for t,w in words:
        wl=w.lower().strip(".,;:!?\"'()")
        i=low.find(wl,cur) if wl else -1
        if i<0: i=cur
        else: cur=i+len(wl)
        out.append((i,t))
    return out

def phrase_time(text,al,words,ph):
    p=text.lower().find(ph.lower())
    if p<0: raise ValueError(f"cue not in script: {ph!r}")
    for ci,t in al:
        if ci>=p: return t
    return al[-1][1]

# ------------------------------------------------------------------ artwork
GPU='''<svg class="art" viewBox="0 0 440 172">
  <rect x="5" y="12" width="428" height="148" rx="14" class="s"/>
  <rect x="24" y="30" width="148" height="112" rx="8" class="s t"/>
  <g class="spin">
    <circle cx="98" cy="86" r="45" class="s t"/>
    <path d="M98 45a41 41 0 0 1 0 82" class="blade"/>
    <path d="M98 127a41 41 0 0 1 0-82" class="blade dim"/>
  </g>
  <text x="214" y="76" class="lime">24 GB</text>
  <text x="214" y="102" class="small">VRAM</text>
  <rect x="214" y="116" width="192" height="18" class="s t"/>
  <rect x="216" y="118" width="130" height="14" class="fy pulse"/>
  <rect x="396" y="58" width="26" height="54" rx="3" class="s t"/>
</svg>'''

CHIP='''<svg class="art" viewBox="0 0 240 240">
  <rect x="58" y="58" width="124" height="124" rx="12" class="s"/>
  <rect x="88" y="88" width="64" height="64" rx="6" class="s t"/>
  <g class="spin"><rect x="104" y="104" width="32" height="32" rx="4" class="fl pulse"/></g>
  <g class="s t">
    <path d="M78 58V34M98 58V34M118 58V34M138 58V34M158 58V34"/>
    <path d="M78 182v24M98 182v24M118 182v24M138 182v24M158 182v24"/>
    <path d="M58 78H34M58 98H34M58 118H34M58 138H34M58 158H34"/>
    <path d="M182 78h24M182 98h24M182 118h24M182 138h24M182 158h24"/>
  </g>
</svg>'''

LAPTOP='''<svg class="art" viewBox="0 0 380 250">
  <rect x="54" y="24" width="272" height="170" rx="10" class="s"/>
  <path d="M20 212H360L334 190H46Z" class="s"/>
  <rect x="78" y="50" width="146" height="14" rx="3" class="fl pulse"/>
  <rect x="78" y="78" width="216" height="9" rx="3" class="fg"/>
  <rect x="78" y="97" width="188" height="9" rx="3" class="fg"/>
  <rect x="78" y="116" width="204" height="9" rx="3" class="fg"/>
  <rect x="78" y="142" width="118" height="10" rx="3" class="fy"/>
</svg>'''

CACHE='''<svg class="art" viewBox="0 0 400 180">
  <g class="s t">
    <rect x="10" y="10" width="52" height="52" rx="5"/><rect x="72" y="10" width="52" height="52" rx="5"/>
    <rect x="134" y="10" width="52" height="52" rx="5"/><rect x="196" y="10" width="52" height="52" rx="5"/>
    <rect x="258" y="10" width="52" height="52" rx="5"/><rect x="320" y="10" width="52" height="52" rx="5"/>
    <rect x="10" y="72" width="52" height="52" rx="5"/><rect x="72" y="72" width="52" height="52" rx="5"/>
    <rect x="134" y="72" width="52" height="52" rx="5"/><rect x="196" y="72" width="52" height="52" rx="5"/>
  </g>
  <g class="fl pulse"><rect x="258" y="72" width="52" height="52" rx="5"/></g>
  <g class="fy pulse2"><rect x="320" y="72" width="52" height="52" rx="5"/></g>
  <text x="10" y="160" class="small">KEY</text>
  <text x="72" y="160" class="small">VALUE</text>
</svg>'''

ARROW='''<svg class="art" viewBox="0 0 300 60">
  <path d="M8 30H250" class="s" stroke-dasharray="10 12" stroke-dashoffset="0"><animate attributeName="stroke-dashoffset" values="0;-22" dur="1s" repeatCount="indefinite"/></path>
  <path d="M246 16l22 14-22 14" class="s"/>
</svg>'''

def num(v, dec=0, suffix="", cls="", style=""):
    d=f"{v:.{dec}f}"
    return (f'<span class="{cls}" data-count="{d}" data-suffix="{suffix}" style="{style}">{d}{suffix}</span>')

S=[]
def scene(tag,vo,cues,html): S.append(dict(tag=tag,vo=vo,cues=cues,html=html))

# ---------------------------------------------------------------- CH1
scene("ch1",
"Okay, so here's the thing that shouldn't be true. You've got a twenty-four gigabyte card. You want the biggest model it'll hold. So you go looking for the biggest one you can find, and you land on a thirty billion parameter model. Then somebody in the comments tells you the smarter buy is a twenty-seven billion parameter model, because the thirty B won't fit.",
{"a":"Okay, so","b":"twenty-four gigabyte card","c":"biggest one you can find","d":"thirty billion parameter model","e":"twenty-seven billion parameter model"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">a 24 GB card &middot; two models &middot; one wrong assumption</div>
      <div class="split">
        <div class="float" data-in="@b@">'''+GPU+'''</div>
        <div class="side">
          <div class="stat"><div class="bf-big big" style="color:var(--lime)" data-in="@d@">30<span class="u">B</span></div>
            <div class="bf-sub" data-in="@d@">the one you found</div></div>
          <div class="stat"><div class="bf-big big" style="color:var(--dim)" data-in="@e@">27<span class="u">B</span></div>
            <div class="bf-sub" data-in="@e@">the one they tell you to buy</div></div>
        </div>
      </div>
      <div class="bf-tape" data-in="@c@">it shouldn't fit &mdash; but it does</div>
    </div>''')

scene("ch1",
"Except it does fit. It fits better. On the same card, the thirty billion parameter model uses less memory, holds more context, and generates tokens faster than the twenty-seven billion one. Same quantization family, same inference engine, same GPU. And it's not a trick. It's three measurable things: the file size, the cache, and the context window.",
{"a":"Except it does fit","b":"uses less memory","c":"holds more context","d":"generates tokens faster","e":"three measurable things","f":"the context window"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">same card &middot; same engine &middot; same family</div>
      <div class="split wide">
        <div class="float" data-in="@a@">'''+CHIP+'''</div>
        <div class="col" style="flex:1">
          <div class="bf-row bf-row--good" data-in="@b@"><span class="bf-row__k">Memory used</span><span class="bf-row__v" style="color:var(--lime)">less</span></div>
          <div class="bf-row bf-row--good" data-in="@c@"><span class="bf-row__k">Context held</span><span class="bf-row__v" style="color:var(--lime)">more</span></div>
          <div class="bf-row bf-row--good" data-in="@d@"><span class="bf-row__k">Tokens / second</span><span class="bf-row__v" style="color:var(--lime)">faster</span></div>
          <div style="display:flex;gap:14px;margin-top:6px" data-in="@e@">
            <span class="chip">FILE SIZE</span><span class="chip">CACHE</span><span class="chip" data-in="@f@">CONTEXT</span>
          </div>
        </div>
      </div>
    </div>''')

# ---------------------------------------------------------------- CH2
scene("ch2",
"The rule everyone repeats is simple. More parameters means more memory. Bigger model, bigger card. And it's a good rule, because it's usually true. Muse Glimmer is a dense model with twenty-seven point eight five billion active parameters. Qwen three point eight twenty-seven B is twenty-seven point three two billion parameters. On paper these two are the same size class. Nine hundred million parameters apart, which is nothing. But the rule hides the thing that actually fills your VRAM. Your card doesn't store parameters. It stores a quantized file, and it stores a cache, and the cache grows with every token you give it.",
{"a":"The rule everyone repeats","b":"More parameters means more memory","c":"Muse Glimmer is a dense model","d":"Qwen three point eight","e":"same size class","f":"Nine hundred million","g":"doesn't store parameters","h":"stores a quantized file","i":"the cache grows"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">the rule</div>
      <div class="split wide">
        <div class="float" data-in="@a@">'''+CHIP+'''</div>
        <div class="col" style="flex:1">
          <div class="bf-big" style="font-size:44px" data-in="@b@">More parameters = more memory.</div>
          <div class="bf-row" data-in="@c@"><span class="bf-row__k">Muse Glimmer 30B</span><span class="bf-row__v">27.85 B</span></div>
          <div class="bf-row" data-in="@d@"><span class="bf-row__k">Qwen 3.8 27B</span><span class="bf-row__v">27.32 B</span></div>
          <div class="bf-row bf-row--good" data-in="@e@"><span class="bf-row__k">Difference</span><span class="bf-row__v" style="color:var(--lime)" data-in="@f@">0.53 B</span></div>
        </div>
      </div>
      <div class="bf-cap" data-in="@g@" style="color:var(--red)">but your card does not store parameters</div>
      <div style="display:flex;gap:16px" data-in="@h@"><span class="chip">QUANTIZED FILE</span><span class="chip" data-in="@i@">+ GROWING CACHE</span></div>
    </div>''')

# ---------------------------------------------------------------- CH3
scene("ch3",
"First, the file. At four-bit, Muse Glimmer thirty B is fourteen point seven eight gigabytes. Qwen three point eight twenty-seven B is sixteen point six eight gigabytes. Read that again. The thirty billion parameter model is almost two gigabytes smaller than the twenty-seven billion one. And that's not magic, and it's not compression cheating. Glimmer was measured at four-bit medium. Qwen was measured at four-bit small.",
{"a":"First, the file","b":"fourteen point seven eight","c":"sixteen point six eight","d":"Read that again","e":"almost two gigabytes smaller","f":"not compression cheating","g":"four-bit medium","h":"four-bit small"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">the file</div>
      <div class="col" style="width:1180px">
        <div class="bf-bar" data-in="@b@"><span class="bf-bar__lab">Muse Glimmer 30B</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:88%;background:var(--lime)" data-in="@b@"></div></div>
          <span class="bf-bar__val" style="color:var(--lime)" data-in="@b@">'''+num(14.78,2," GiB")+'''</span></div>
        <div class="bf-bar" data-in="@c@"><span class="bf-bar__lab">Qwen 3.8 27B</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:100%;background:var(--dim)" data-in="@c@"></div></div>
          <span class="bf-bar__val" style="color:var(--dim)" data-in="@c@">'''+num(16.68,2," GiB")+'''</span></div>
      </div>
      <div style="display:flex;gap:14px" data-in="@f@"><span class="chip" data-in="@g@">Q4_K MEDIUM</span><span class="chip" data-in="@h@">Q4_K SMALL</span></div>
      <div class="bf-tape" data-in="@d@">the bigger model is the smaller file</div>
    </div>''')

scene("ch3",
"Second, the cache. Every token in your context writes a key matrix and a value matrix into memory. Those matrices don't care how many parameters the model has. They care how many layers it has, how many heads, and how long your context is. So the bigger model, in the smaller file, with the leaner cache, fits a longer conversation into the same twenty-four gigabytes.",
{"a":"Second, the cache","b":"writes a key matrix","c":"a value matrix","d":"don't care how many parameters","e":"how many layers","f":"how long your context is","g":"fits a longer conversation"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">the cache</div>
      <div class="float" data-in="@a@">'''+CACHE+'''</div>
      <div class="split wide" style="gap:40px">
        <div class="bf-row" data-in="@e@"><span class="bf-row__k">Layers &amp; heads</span><span class="bf-row__v">sets the rate</span></div>
        <div class="bf-row bf-row--hot" data-in="@f@"><span class="bf-row__k">Context length</span><span class="bf-row__v" style="color:var(--red)">sets the total</span></div>
      </div>
      <div class="bf-tape" data-in="@g@">same 24 GB &middot; longer conversation</div>
    </div>''')

# ---------------------------------------------------------------- CH4
scene("ch4",
"Here's measured VRAM. Not estimated, not calculated from a formula. Measured. At four K context, Muse Glimmer sits at sixteen gigabytes. Qwen is at eighteen. At thirty-two K, Glimmer is still sixteen. Qwen is at twenty. At sixty-four K, Glimmer is seventeen. Qwen is twenty-two. At one twenty-eight K, Glimmer is eighteen. Qwen is twenty-six. And at two hundred fifty-six K, Glimmer peaks at twenty gigabytes. Qwen needs thirty-four.",
{"a":"Here's measured VRAM","b":"four K context","b2":"Qwen is at eighteen","c":"thirty-two K","c2":"twenty","d":"sixty-four K","d2":"twenty-two","e":"one twenty-eight K","e2":"twenty-six","f":"two hundred fifty-six K","f2":"thirty-four"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">measured VRAM &middot; not calculated</div>
      <div class="split wide" style="align-items:center">
        <div class="float" data-in="@a@" style="width:310px">'''+GPU+'''</div>
        <div class="col" style="flex:1;gap:10px">
          <div class="bf-row" data-in="@b@"><span class="bf-row__k">4K</span><span class="bf-row__v" style="color:var(--lime)">16</span><span class="bf-row__v" style="color:var(--dim)" data-in="@b2@">18</span></div>
          <div class="bf-row" data-in="@c@"><span class="bf-row__k">32K</span><span class="bf-row__v" style="color:var(--lime)">16</span><span class="bf-row__v" style="color:var(--dim)" data-in="@c2@">20</span></div>
          <div class="bf-row bf-row--good" data-in="@d@"><span class="bf-row__k">64K</span><span class="bf-row__v" style="color:var(--lime)">17</span><span class="bf-row__v" style="color:var(--yellow)" data-in="@d2@">22</span></div>
          <div class="bf-row bf-row--hot" data-in="@e@"><span class="bf-row__k">128K</span><span class="bf-row__v" style="color:var(--lime)">18</span><span class="bf-row__v" style="color:var(--red)" data-in="@e2@">26</span></div>
          <div class="bf-row bf-row--hot" data-in="@f@"><span class="bf-row__k">256K</span><span class="bf-row__v" style="color:var(--lime)">20</span><span class="bf-row__v" style="color:var(--red)" data-in="@f2@">34</span></div>
        </div>
      </div>
    </div>''')

# ---------------------------------------------------------------- CH5
scene("ch5",
"Now there's a second number everyone ignores, and it decides how the thing actually feels. Token generation is how fast words come out. Prefill is how long you wait before the first one. And prefill is where long context really hurts. On a three thousand ninety, Glimmer processes a four K prompt at fourteen hundred and seventy-seven tokens a second. Qwen does thirteen hundred and eight. At one twenty-eight K, Glimmer drops to eight hundred and fifty-three. At two hundred fifty-six K, five hundred and eighty-four.",
{"a":"second number everyone ignores","b":"Token generation","c":"Prefill is how long","d":"three thousand ninety","e":"fourteen hundred and seventy-seven","f":"thirteen hundred and eight","g":"one twenty-eight K","h":"eight hundred and fifty-three","i":"two hundred fifty-six K","j":"five hundred and eighty-four"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">the wait before the first word</div>
      <div style="display:flex;gap:70px;align-items:center">
        <div class="stat"><div class="bf-sub" data-in="@b@">generation</div><div class="bf-big" style="font-size:52px" data-in="@b@">words out</div></div>
        <div class="float" data-in="@a@">'''+ARROW+'''</div>
        <div class="stat"><div class="bf-sub" data-in="@c@" style="color:var(--yellow)">prefill</div><div class="bf-big" style="font-size:52px;color:var(--yellow)" data-in="@c@">time to first</div></div>
      </div>
      <div class="col" style="width:1120px">
        <div class="bf-bar" data-in="@d@"><span class="bf-bar__lab">Glimmer &middot; 4K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:100%;background:var(--lime)" data-in="@e@"></div></div>
          <span class="bf-bar__val" style="color:var(--lime)" data-in="@e@">'''+num(1477,0," t/s")+'''</span></div>
        <div class="bf-bar" data-in="@f@"><span class="bf-bar__lab">Qwen &middot; 4K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:88%;background:var(--dim)" data-in="@f@"></div></div>
          <span class="bf-bar__val" style="color:var(--dim)" data-in="@f@">'''+num(1308,0," t/s")+'''</span></div>
        <div class="bf-bar" data-in="@g@"><span class="bf-bar__lab">Glimmer &middot; 128K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:58%;background:var(--yellow)" data-in="@g@"></div></div>
          <span class="bf-bar__val" style="color:var(--yellow)" data-in="@h@">'''+num(853,0," t/s")+'''</span></div>
        <div class="bf-bar" data-in="@i@"><span class="bf-bar__lab">Glimmer &middot; 256K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:40%;background:var(--red)" data-in="@i@"></div></div>
          <span class="bf-bar__val" style="color:var(--red)" data-in="@j@">'''+num(584,0," t/s")+'''</span></div>
      </div>
    </div>''')

scene("ch5",
"On a five-oh-ninety the numbers are much higher, but the shape is the same. Glimmer starts at forty-six hundred and twenty-five tokens a second at four K, and falls to eighteen hundred and seventy-four at two hundred fifty-six K. Qwen three point eight starts at thirty-seven hundred and forty-nine, and by one twenty-eight K it's at four hundred and sixty-one. Four hundred and sixty-one tokens a second. That's the number that makes a long-context chat feel broken.",
{"a":"five-oh-ninety","b":"forty-six hundred and twenty-five","c":"eighteen hundred and seventy-four","d":"thirty-seven hundred and forty-nine","e":"four hundred and sixty-one","f":"makes a long-context chat feel broken"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">RTX 5090 &middot; prefill</div>
      <div class="col" style="width:1120px">
        <div class="bf-bar" data-in="@a@"><span class="bf-bar__lab">Glimmer &middot; 4K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:100%;background:var(--lime)" data-in="@b@"></div></div>
          <span class="bf-bar__val" style="color:var(--lime)" data-in="@b@">'''+num(4625,0," t/s")+'''</span></div>
        <div class="bf-bar" data-in="@c@"><span class="bf-bar__lab">Glimmer &middot; 256K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:41%;background:var(--yellow)" data-in="@c@"></div></div>
          <span class="bf-bar__val" style="color:var(--yellow)" data-in="@c@">'''+num(1874,0," t/s")+'''</span></div>
        <div class="bf-bar" data-in="@d@"><span class="bf-bar__lab">Qwen &middot; 4K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:81%;background:var(--dim)" data-in="@d@"></div></div>
          <span class="bf-bar__val" style="color:var(--dim)" data-in="@d@">'''+num(3749,0," t/s")+'''</span></div>
        <div class="bf-bar" data-in="@e@"><span class="bf-bar__lab">Qwen &middot; 128K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:10%;background:var(--red)" data-in="@e@"></div></div>
          <span class="bf-bar__val" style="color:var(--red)" data-in="@e@">'''+num(461,0," t/s")+'''</span></div>
      </div>
      <div class="bf-tape" data-in="@f@">461 t/s feels broken</div>
    </div>''')

# ---------------------------------------------------------------- CH6
scene("ch6",
"Now the part that made me check the numbers twice. On an RTX three thousand ninety, Glimmer generates forty-five point three tokens a second at four K. Qwen does forty point three. Close. Not embarrassing. At sixty-four K, Glimmer holds forty-two point four. Qwen drops to thirty-three point nine.",
{"a":"check the numbers twice","b":"three thousand ninety","c":"forty-five point three","d":"forty point three","e":"sixty-four K","f":"forty-two point four","g":"thirty-three point nine"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">RTX 3090 &middot; generation</div>
      <div class="split wide" style="align-items:center">
        <div class="float" data-in="@a@" style="width:290px">'''+GPU+'''</div>
        <div class="col" style="flex:1">
          <div class="bf-bar" data-in="@b@"><span class="bf-bar__lab">Glimmer &middot; 4K</span>
            <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:100%;background:var(--lime)" data-in="@c@"></div></div>
            <span class="bf-bar__val" style="color:var(--lime)" data-in="@c@">'''+num(45.3,1)+'''</span></div>
          <div class="bf-bar" data-in="@d@"><span class="bf-bar__lab">Qwen &middot; 4K</span>
            <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:89%;background:var(--dim)" data-in="@d@"></div></div>
            <span class="bf-bar__val" style="color:var(--dim)" data-in="@d@">'''+num(40.3,1)+'''</span></div>
          <div class="bf-bar" data-in="@e@"><span class="bf-bar__lab">Glimmer &middot; 64K</span>
            <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:94%;background:var(--lime)" data-in="@f@"></div></div>
            <span class="bf-bar__val" style="color:var(--lime)" data-in="@f@">'''+num(42.45,1)+'''</span></div>
          <div class="bf-bar" data-in="@g@"><span class="bf-bar__lab">Qwen &middot; 64K</span>
            <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:75%;background:var(--yellow)" data-in="@g@"></div></div>
            <span class="bf-bar__val" style="color:var(--yellow)" data-in="@g@">'''+num(33.95,1)+'''</span></div>
        </div>
      </div>
    </div>''')

scene("ch6",
"At one twenty-eight K, Glimmer is still doing thirty-eight point one. And Qwen isn't in that test, because on a twenty-four gigabyte card, Qwen three point eight at one twenty-eight K isn't practical. That's the benchmark's own wording, not my opinion. On a five-oh-ninety it's the same story with more headroom. Glimmer at four K: eighty-three point two. Qwen: seventy-four point eight. At one twenty-eight K, Glimmer is at seventy-five point eight, and Qwen has fallen to twenty-two point eight.",
{"a":"one twenty-eight K","b":"thirty-eight point one","c":"isn't practical","d":"benchmark's own wording","e":"five-oh-ninety","f":"eighty-three point two","g":"seventy-four point eight","h":"seventy-five point eight","i":"twenty-two point eight"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">RTX 5090 &middot; generation</div>
      <div class="col" style="width:1120px">
        <div class="bf-bar" data-in="@e@"><span class="bf-bar__lab">Glimmer &middot; 4K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:100%;background:var(--lime)" data-in="@f@"></div></div>
          <span class="bf-bar__val" style="color:var(--lime)" data-in="@f@">'''+num(83.2,1)+'''</span></div>
        <div class="bf-bar" data-in="@g@"><span class="bf-bar__lab">Qwen &middot; 4K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:90%;background:var(--dim)" data-in="@g@"></div></div>
          <span class="bf-bar__val" style="color:var(--dim)" data-in="@g@">'''+num(74.8,1)+'''</span></div>
        <div class="bf-bar" data-in="@h@"><span class="bf-bar__lab">Glimmer &middot; 128K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:91%;background:var(--lime)" data-in="@h@"></div></div>
          <span class="bf-bar__val" style="color:var(--lime)" data-in="@h@">'''+num(75.8,1)+'''</span></div>
        <div class="bf-bar" data-in="@i@"><span class="bf-bar__lab">Qwen &middot; 128K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:27%;background:var(--red)" data-in="@i@"></div></div>
          <span class="bf-bar__val" style="color:var(--red)" data-in="@i@">'''+num(22.8,1)+'''</span></div>
      </div>
      <div class="bf-row bf-row--hot" style="width:880px" data-in="@c@"><span class="bf-row__k">Qwen at 128K on 24 GB</span><span class="bf-row__v" style="color:var(--red)" data-in="@a@">not practical</span></div>
      <div class="bf-sub" data-in="@d@" style="color:var(--dim)">the benchmark's wording, not ours</div>
    </div>''')

scene("ch6",
"And here's the detail that actually surprised me. Qwen three point eight isn't just slower than Glimmer. At sixty-four K on a five-oh-ninety, Qwen three point six, the previous generation, is doing sixty-three point six tokens a second, against three point eight's twenty-six point two. The older Qwen is more than twice as fast at long context as the newer one. So newer doesn't mean faster, and more parameters doesn't mean more memory.",
{"a":"detail that actually surprised me","b":"Qwen three point six","c":"previous generation","d":"sixty-three point six","e":"twenty-six point two","f":"twice as fast","g":"newer doesn't mean faster"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">RTX 5090 &middot; 64K context</div>
      <div class="col" style="width:1120px">
        <div class="bf-bar" data-in="@b@"><span class="bf-bar__lab">Qwen 3.6 &middot; older</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:100%;background:var(--lime)" data-in="@c@"></div></div>
          <span class="bf-bar__val" style="color:var(--lime)" data-in="@d@">'''+num(63.66,2)+'''</span></div>
        <div class="bf-bar" data-in="@e@"><span class="bf-bar__lab">Qwen 3.8 &middot; newer</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:41%;background:var(--red)" data-in="@e@"></div></div>
          <span class="bf-bar__val" style="color:var(--red)" data-in="@e@">'''+num(26.22,2)+'''</span></div>
      </div>
      <div class="bf-tape" data-in="@a@">the older one is faster</div>
      <div class="bf-cap" data-in="@g@" style="color:var(--yellow)">newer &ne; faster &middot; bigger &ne; more memory</div>
    </div>''')

# ---------------------------------------------------------------- CH7
scene("ch7",
"And then there's the route people take when they can't stretch to a three thousand ninety. Two sixteen gigabyte cards. The benchmark tested exactly that. A pair of fifty-sixty Ti cards, thirty-two gigabytes total. It runs Qwen three point eight all the way to one twenty-eight K, because thirty-two gigabytes is enough. But look at the speed. Twenty-two point five tokens a second at four K. Fifteen point six at one twenty-eight K. Against a single three thousand ninety running Glimmer at forty-five and thirty-eight. So the two-card route buys capacity, not speed. Roughly a third of the tokens per second, plus multi-GPU overhead, plus two cards to cool. If you already own one sixteen gigabyte card, it's a real upgrade path. If you're buying from scratch, one twenty-four gigabyte card does more with less.",
{"a":"route people take","b":"Two sixteen gigabyte cards","c":"fifty-sixty Ti","d":"thirty-two gigabytes total","e":"one twenty-eight K","f":"look at the speed","g":"twenty-two point five","h":"Fifteen point six","i":"buys capacity","j":"buying from scratch"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">the two-card route</div>
      <div style="display:flex;gap:26px;align-items:center" data-in="@b@">
        <div class="float" style="width:255px">'''+GPU+'''</div>
        <div class="float" data-in="@c@" style="width:255px">'''+GPU+'''</div>
        <div class="chip" style="border-color:var(--yellow)" data-in="@d@">32 GB TOTAL</div>
      </div>
      <div class="col" style="width:1120px">
        <div class="bf-bar" data-in="@f@"><span class="bf-bar__lab">2&times; 5060 Ti &middot; 4K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:30%;background:var(--yellow)" data-in="@g@"></div></div>
          <span class="bf-bar__val" style="color:var(--yellow)" data-in="@g@">'''+num(22.5,1)+'''</span></div>
        <div class="bf-bar" data-in="@e@"><span class="bf-bar__lab">2&times; 5060 Ti &middot; 128K</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:21%;background:var(--red)" data-in="@h@"></div></div>
          <span class="bf-bar__val" style="color:var(--red)" data-in="@h@">'''+num(15.6,1)+'''</span></div>
        <div class="bf-bar" data-in="@i@"><span class="bf-bar__lab">1&times; 3090 + Glimmer</span>
          <div class="bf-bar__track"><div class="bf-bar__fill grow" style="--w:100%;background:var(--lime)" data-in="@i@"></div></div>
          <span class="bf-bar__val" style="color:var(--lime)">45.3 &rarr; 38.1</span></div>
      </div>
    </div>''')

# ---------------------------------------------------------------- CH8
scene("ch8",
"Three honest caveats, because this is where most videos stop. One. The quantization levels are different. Glimmer was measured at four-bit medium, Qwen at four-bit small. That's not a perfectly fair fight, and anyone telling you it is is selling you something. Two. These benchmarks measure hardware behaviour, not intelligence. The source is explicit: VRAM, context scaling, prompt processing, token generation. Not reasoning quality. Not coding quality. A model that runs fast and fits can still be the wrong model for you. Three. The agentic claims around Glimmer are not independently benchmarked. Tool use, task accuracy, reliability, unconfirmed. Treat them as marketing until you test them yourself. What is confirmed: the file size, the VRAM curve, the prefill rates, and the token rates. Those are measurements, and they hold.",
{"a":"Three honest caveats","b":"quantization levels are different","c":"not a perfectly fair fight","d":"measure hardware behaviour","e":"not intelligence","f":"not coding quality","g":"wrong model for you","h":"agentic claims","i":"not independently benchmarked","j":"treat them as marketing"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@" style="color:var(--red)">three caveats &middot; read these</div>
      <div class="col" style="width:1120px;gap:14px">
        <div class="chalk" data-in="@b@" style="display:flex;gap:20px;align-items:baseline">
          <span class="bf-row__k" style="width:54px">01</span>
          <span style="font-family:var(--mono);font-size:22px">Q4_K Medium vs Q4_K Small &mdash; different recipes</span></div>
        <div class="chalk" data-in="@d@" style="display:flex;gap:20px;align-items:baseline">
          <span class="bf-row__k" style="width:54px">02</span>
          <span style="font-family:var(--mono);font-size:22px" data-in="@e@">Hardware only &middot; not model quality</span></div>
        <div class="chalk" data-in="@h@" style="display:flex;gap:20px;align-items:baseline">
          <span class="bf-row__k" style="width:54px">03</span>
          <span style="font-family:var(--mono);font-size:22px" data-in="@i@">Agentic claims: unconfirmed</span></div>
      </div>
      <div class="bf-tape" data-in="@c@">not a fair fight</div>
      <div class="bf-cap" data-in="@j@" style="color:var(--yellow)">confirmed: file size &middot; VRAM curve &middot; token rates</div>
    </div>''')

# ---------------------------------------------------------------- CH9
scene("ch9",
"So if you're on twenty-four gigabytes and you want long context, Muse Glimmer thirty B is the one that fits. Two hundred fifty-six K in twenty gigabytes, at thirty-five to forty-five tokens a second on a three thousand ninety. If you specifically need Qwen's behaviour, then sixty-four K is your realistic ceiling on that card, and you should plan around it instead of discovering it at token ninety thousand. And if you're on a five-oh-ninety, you're not buying context anymore, because twenty gigabytes already covers Glimmer's whole window. You're buying speed. Eighty-three tokens a second at four K, sixty-nine at two hundred fifty-six K. Notice what none of those decisions were based on. Parameter count. Not once.",
{"a":"if you're on twenty-four gigabytes","b":"the one that fits","c":"sixty-four K is your realistic ceiling","d":"five-oh-ninety","e":"you're buying speed","f":"Parameter count","g":"Not once"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">the verdict</div>
      <div class="split wide" style="align-items:center">
        <div class="float" data-in="@d@">'''+LAPTOP+'''</div>
        <div class="col" style="flex:1;gap:14px">
          <div class="bf-row bf-row--good" data-in="@a@"><span class="bf-row__k">On 24 GB &middot; long context</span><span class="bf-row__v" style="color:var(--lime)" data-in="@b@">Glimmer 30B</span></div>
          <div class="bf-row" data-in="@c@"><span class="bf-row__k">Need Qwen behaviour</span><span class="bf-row__v">64K ceiling</span></div>
          <div class="bf-row" data-in="@d@"><span class="bf-row__k">On a 5090</span><span class="bf-row__v" style="color:var(--yellow)" data-in="@e@">buying speed</span></div>
        </div>
      </div>
      <div style="position:relative;display:inline-block" data-in="@f@">
        <span class="bf-big" style="font-size:52px;color:var(--dim)">PARAMETER COUNT</span>
        <span class="strike"></span>
      </div>
      <div class="bf-cap" data-in="@g@" style="color:var(--red)">not once</div>
    </div>''')

# ---------------------------------------------------------------- CH10
scene("ch10",
"So stop shopping by parameter count. Shop by the file, the cache, and the context you actually use. Those three numbers are on the page. The parameter count tells you the least. That's the forensic part. See you in the next one.",
{"a":"stop shopping by parameter count","b":"the file, the cache","c":"context you actually use","d":"tells you the least","e":"See you in the next one"},
'''    <div class="ctr">
      <div class="float" data-in="@cap@">'''+CHIP+'''</div>
      <div class="bf-big" style="font-size:62px;text-align:center" data-in="@a@">Stop shopping by parameter count.</div>
      <div style="display:flex;gap:16px" data-in="@b@">
        <span class="chip">FILE</span><span class="chip">CACHE</span><span class="chip" data-in="@c@">CONTEXT</span>
      </div>
      <div class="bf-cap" data-in="@d@" style="color:var(--yellow)">parameter count tells you the least</div>
      <div class="bf-wm" data-in="@e@">byte forensics</div>
    </div>''')

# ---------------------------------------------------------------- END SCREEN
scene("end",
"Full numbers are in the description, including the ones I did not put on screen. Next episode: the two-card route, in detail. Subscribe if you want it when it lands.",
{"a":"Full numbers","b":"Next episode","c":"two-card route","d":"Subscribe","e":"when it lands"},
'''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">that's the forensic part</div>
      <div class="bf-big" style="font-size:58px;text-align:center" data-in="@b@">Next: the two-card route</div>
      <div class="float" data-in="@c@" style="width:300px">'''+GPU+'''</div>
      <div style="display:flex;gap:16px" data-in="@a@">
        <span class="chip">FULL NUMBERS IN DESCRIPTION</span>
        <span class="chip" style="border-color:var(--lime);color:var(--lime)" data-in="@d@">SUBSCRIBE</span>
      </div>
      <div class="bf-tape" data-in="@e@">byte forensics</div>
    </div>''')

# ------------------------------------------------------------------ build
work=os.path.join(ROOT,"byte","b2"); A=os.path.join(work,"audio"); os.makedirs(A,exist_ok=True)
af=("silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,"
    "areverse,silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,areverse")
WORDS=[]
async def go():
    for i,sc in enumerate(S,1):
        raw=os.path.join(A,f"r{i}.mp3"); wav=os.path.join(A,f"n{i}.wav")
        c=edge_tts.Communicate(sc["vo"],VOICE,rate=RATE,boundary="WordBoundary")
        buf=bytearray(); ws=[]
        async for ch in c.stream():
            if ch["type"]=="audio": buf+=ch["data"]
            elif ch["type"]=="WordBoundary": ws.append((ch["offset"]/1e7,ch["text"]))
        open(raw,"wb").write(bytes(buf))
        o=subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",raw,"-af",
            "silencedetect=noise=-45dB:d=0.05","-f","null","-"],capture_output=True,text=True).stderr
        e=re.findall(r"silence_end: ([0-9.]+)",o); lead=float(e[0]) if e else 0.0
        subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-i",raw,"-af",af,
            "-ar","44100","-ac","1","-c:a","pcm_s16le",wav],check=True)
        WORDS.append([(max(0.0,x-lead+0.04),w) for x,w in ws]); os.remove(raw)
asyncio.run(go())

d=[dur(os.path.join(A,f"n{i}.wav")) for i in range(1,len(S)+1)]
starts,acc=[],0.0
for i in range(len(d)): starts.append(acc); acc+=d[i]+GAP
total=sum(d)+GAP*(len(d)-1)+TAIL

g=os.path.join(A,"g.wav"); t=os.path.join(A,"t.wav")
for path,ln in ((g,GAP),(t,TAIL)):
    subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi",
        "-i","anullsrc=r=44100:cl=mono","-t",str(ln),"-c:a","pcm_s16le",path],check=True)
lst=[]
for i in range(1,len(S)+1):
    lst.append(f"file '{(A+'/n%d.wav'%i).replace(chr(92),'/')}'")
    if i<len(S): lst.append(f"file '{(A+'/g.wav').replace(chr(92),'/')}'")
lst.append(f"file '{(A+'/t.wav').replace(chr(92),'/')}'")
open(os.path.join(A,"l.txt"),"w").write("\n".join(lst))
vo=os.path.join(work,"vo.mp3")
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","concat","-safe","0",
    "-i",os.path.join(A,"l.txt"),"-c:a","libmp3lame","-b:a","160k",vo],check=True)

cue={}
for i,sc in enumerate(S):
    al=align(sc["vo"],WORDS[i])
    for tok,ph in sc["cues"].items():
        wt=phrase_time(sc["vo"],al,WORDS[i],ph)
        cue[(i,tok)]=max(starts[i]+0.05,min(starts[i]+wt-0.08,starts[i]+d[i]-0.10))

def rel(tok,i):
    if tok.startswith("cap"): return 0.15
    return round(cue[(i,tok)]-starts[i],2)

bodies=[]
for i,sc in enumerate(S):
    h=re.sub(r'data-in="@(\w+)@"',lambda m,i=i:'data-in="%s"'%rel(m.group(1),i),sc["html"])
    left=[v for v in re.findall(r'data-in="([^"]*)"',h) if not re.fullmatch(r"[0-9.]+",v)]
    assert not left, f"unresolved scene {i+1}: {left}"
    bodies.append(h)

ev=sorted({starts[i]+0.15 for i in range(len(S))} |
    {starts[i]+float(v) for i,h in enumerate(bodies) for v in re.findall(r'data-in="([0-9.]+)"',h)})
fills={i:[] for i in range(len(S))}
for p,q in zip(ev+[total],(ev+[total])[1:]):
    gap=q-p
    if gap<=TICK: continue
    k=int(gap//TICK)
    for j in range(1,k+1):
        tt=p+gap*j/(k+1)
        si=max(i for i in range(len(starts)) if starts[i]<=tt)
        fills[si].append(round(tt-starts[si],2))

CHAPTER_TITLES={"ch1":"The hook","ch2":"The rule","ch3":"File and cache","ch4":"Measured VRAM",
  "ch5":"Prefill","ch6":"Token speed","ch7":"Two-card route","ch8":"The caveats",
  "ch9":"The verdict","ch10":"Close","end":"End screen"}
sections=[]
for i,h in enumerate(bodies):
    tag=S[i]["tag"]
    label=CHAPTER_TITLES.get(tag, tag.upper())
    h=(f'<div class="slate" data-in="0.15"><span class="slate-n">{i+1:02d}</span>'
       f'<span class="slate-t">{label}</span></div>' + h)
    if fills[i]:
        h=h+'\n      <div class="rail">'+''.join(f'<i data-in="{x}"></i>' for x in sorted(fills[i]))+'</div>'
    sections.append((i,h))

allEv=[]
for i,h in sections:
    for v in re.findall(r'data-in="([0-9.]+)"',h): allEv.append(round(starts[i]+float(v),3))
allEv=sorted(set(allEv))
gaps=[q-p for p,q in zip(allEv,allEv[1:])]
print(f"audio {dur(vo):.2f}s  timeline {total:.2f}s  events {len(allEv)}  avg {total/len(allEv):.2f}s")
print(f"max gap {max(gaps):.2f}s")
assert max(gaps)<=MAX_GAP, f"gap {max(gaps):.2f}s"

wipes=[round(starts[i]-0.285,3) for i in (2,4,6,8)]
sfx=[]
for i,sc in enumerate(S):
    for j,(tok,_) in enumerate(sc["cues"].items()):
        if j%3==0: sfx.append((round(cue[(i,tok)],3),"tick"))
for i in (1,3,5,9): sfx.append((round(starts[i]+0.2,3),"thud"))
for w in wipes: sfx.append((w,"whoosh"))
sfx.sort()

bed = os.path.join(ROOT,"audio","bed.mp3")
if not os.path.exists(bed):
    os.makedirs(os.path.dirname(bed), exist_ok=True)
    subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi",
        "-i","anoisesrc=color=pink:duration=600:sample_rate=44100",
        "-af","highpass=f=90,lowpass=f=420,tremolo=f=0.12:d=0.20,volume=0.35",
        "-ar","44100","-ac","1","-c:a","libmp3lame","-b:a","128k",bed],check=True)
    print("generated placeholder bed -> audio/bed.mp3  (drop your own track there to replace it)")

vo_n = os.path.join(work,"vo_norm.mp3")
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-i",vo,
    "-af","volume=6.4dB,alimiter=level_in=1:level_out=1:limit=0.80:attack=5:release=60",
    "-c:a","libmp3lame","-b:a","192k",vo_n],check=True)

# duck the bed under the voice and mix
mixed = os.path.join(work,"mixed.mp3")
D = dur(vo_n)
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error",
    "-i",vo_n,"-i",bed,
    "-filter_complex",
    f"[1:a]volume=0.10,afade=t=in:st=0:d=1.5,afade=t=out:st={max(0,D-3):.2f}:d=3[b];"
    f"[b][0:a]sidechaincompress=threshold=0.04:ratio=7:attack=15:release=420[d];"
    f"[0:a][d]amix=inputs=2:duration=first:normalize=0[m]",
    "-map","[m]","-c:a","libmp3lame","-b:a","192k",mixed],check=True)
vo_n = mixed
print(f"bed mixed, duration {dur(vo_n):.2f}s")
print(f"normalised -> {dur(vo_n):.2f}s")
b64=base64.b64encode(open(vo_n,"rb").read()).decode()
bcss=open(os.path.join(ROOT,"core","byte.css"),encoding="utf-8").read().replace('url("fonts/','url("core/fonts/')
pcss=open(os.path.join(ROOT,"core","player.css"),encoding="utf-8").read()
pjs=open(os.path.join(ROOT,"core","player.js"),encoding="utf-8").read()
scenes_js=",\n  ".join(f"{{s:{starts[i]:5.2f},  e:{starts[i]+d[i]:5.2f}}}" for i in range(len(d)))
sfx_js="\n".join(f"  {{t:{x:6.3f}, f:'{k}'}}," for x,k in sfx)
labels=", ".join(f"'{s['tag'].upper()}'" for s in S)

html=f"""<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<title>The 30B That Uses Less VRAM Than The 27B</title>
<style>
{bcss}
{pcss}
  .ctr{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;
        justify-content:center;gap:26px;padding:0 90px}}
  .col{{display:flex;flex-direction:column;gap:14px;width:1120px}}
  .split{{display:flex;align-items:center;gap:46px}}
  .split.wide{{width:1240px;justify-content:center;gap:64px}}
  .side{{display:flex;gap:70px}}
  .big{{font-size:150px;line-height:.9}}
  .u{{font-size:64px}}
  .chip{{font-family:var(--mono);font-size:18px;letter-spacing:.16em;padding:10px 18px;
         border:2px dashed rgba(237,234,227,.5);border-radius:8px;color:var(--gray)}}
  .strike{{position:absolute;left:-4%;right:-4%;top:52%;height:7px;background:var(--red);transform:rotate(-2deg)}}
  .grow{{width:0}} .grow.on{{width:var(--w)}}
  .bf-row{{gap:26px}} .bf-row__v{{min-width:100px;text-align:right;white-space:nowrap}}
  .slate{{position:absolute;left:58px;top:46px;display:flex;align-items:baseline;gap:16px;
         opacity:0;transition:opacity .35s ease;border-bottom:3px solid rgba(237,234,227,.32);padding:0 0 12px;min-width:560px}}
  .slate.on{{opacity:1}}
  .slate-n{{font-family:var(--mono);font-weight:800;font-size:104px;color:var(--yellow);letter-spacing:.02em}}
  .slate-t{{font-family:var(--mono);font-size:27px;letter-spacing:.22em;color:var(--gray);text-transform:uppercase}}
  .rail{{position:absolute;left:50%;transform:translateX(-50%);bottom:70px;display:flex;gap:9px}}
  .rail i{{width:2px;height:15px;background:rgba(237,234,227,.12);display:block}}
  .rail i.on{{background:rgba(237,234,227,.55)}}

  /* ---- artwork ---- */
  .art{{display:block;width:400px;height:auto;max-width:46vw;overflow:visible}}
  .float{{flex:0 0 auto;width:400px}}
  .float .art{{width:100%}}
  .art .s{{fill:none;stroke:var(--white);stroke-width:3}}
  .art .t{{stroke-width:2.2}}
  .art .blade{{fill:none;stroke:var(--gray);stroke-width:7}}
  .art .dim{{opacity:.45}}
  .art .fg{{fill:rgba(237,234,227,.25)}}
  .art .fl{{fill:var(--lime)}}
  .art .fy{{fill:var(--yellow)}}
  .art .lime{{fill:var(--lime);font-family:var(--mono);font-weight:800;font-size:30px}}
  .art .small{{fill:var(--dim);font-family:var(--mono);font-size:15px;letter-spacing:3px}}
  .spin{{transform-box:fill-box;transform-origin:center;animation:spin 2.6s linear infinite}}
  @keyframes spin{{to{{transform:rotate(360deg)}}}}
  .float{{animation:bob 4s ease-in-out infinite}}
  @keyframes bob{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-9px)}}}}
  .pulse{{animation:pl 1.8s ease-in-out infinite}}
  @keyframes pl{{0%,100%{{opacity:1}}50%{{opacity:.45}}}}
  .pulse2{{animation:pl 2.6s ease-in-out infinite}}

  .no-js #start{{display:none!important}}
  .no-js .scene:first-of-type{{opacity:1!important;visibility:visible!important}}
  .no-js [data-in]{{opacity:1!important;transform:none!important}}
  .no-js .grow{{width:var(--w)!important}}
</style>
</head>
<body>
<script>document.documentElement.classList.remove("no-js");</script>
<div id="wrap"><div id="stage">
{chr(10).join('<section class="scene" data-scene="%d">\n%s\n  </section>'%(i,h) for i,h in sections)}
</div></div>
<script>
window.EPISODE = {{
  kicker: "Byte Forensics · Episode 02",
  title: "The 30B That Uses Less VRAM Than The 27B",
  subtitle: "Muse Glimmer 30B vs Qwen 3.8 27B · measured",
  total: {total:.2f},
  maxGap: {MAX_GAP},
  vo: "data:audio/mpeg;base64,{b64}",
  sfxBase: "audio/",
  labels: [{labels}],
  scenes: [
  {scenes_js}
  ],
  wipes: [{', '.join('%.3f'%w for w in wipes)}],
  wipeColors: ['yellow','blue','yellow','blue'],
  sfx: [
{sfx_js}
  ]
}};
</script>
<script>
{pjs}
</script>
</body>
</html>
"""
out=os.path.join(ROOT,NAME+".html")
open(out,"w",encoding="utf-8").write(html)
print(f"wrote {out}  ({len(html)//1024} KB)  scenes={len(S)}")

# ---- SRT captions from the exact word timings ----
def ts(t, comma=True):
    h=int(t//3600); m=int(t%3600//60); sec=int(t%60); ms=int(round((t-int(t))*1000))
    if ms==1000: ms=0; sec+=1
    return f"{h:02d}:{m:02d}:{sec:02d}{',' if comma else '.'}{ms:03d}"
lines=[]; n=1
for i,sc in enumerate(S):
    ws=WORDS[i]
    vw=sc["vo"].split()
    same = len(vw)==len(ws)
    for j in range(0,len(ws),8):
        grp=ws[j:j+8]
        t0=starts[i]+grp[0][0]
        t1=starts[i]+(ws[j+8][0] if j+8<len(ws) else d[i])
        txt=" ".join(vw[j:j+8]) if same else " ".join(w for _,w in grp)
        txt=txt.replace(" -- "," - ")
        lines.append(f"{n}\n{ts(t0)} --> {ts(t1)}\n{txt}\n")
        n+=1
srt=os.path.join(ROOT,NAME+".srt")
open(srt,"w",encoding="utf-8").write("\n".join(lines))
print(f"wrote {srt}  ({n-1} captions)")

# ---- YouTube chapters (first scene of each chapter tag) ----
TITLES={"ch1":"The hook","ch2":"The rule","ch3":"File and cache","ch4":"Measured VRAM",
        "ch5":"Prefill: the wait before the first word","ch6":"Token speed",
        "ch7":"The two-card route","ch8":"The caveats","ch9":"The verdict","ch10":"Close","end":"End screen"}
seen=set(); chap=[]
for i,sc in enumerate(S):
    if sc["tag"] in seen: continue
    seen.add(sc["tag"])
    t=starts[i]
    chap.append(f"{int(t//60)}:{int(t%60):02d} {TITLES.get(sc['tag'], sc['tag'])}")
chap[0]=chap[0].split(" ",1)[0]+" "+TITLES["ch1"]
cp=os.path.join(ROOT,NAME+"-chapters.txt")
open(cp,"w",encoding="utf-8").write("\n".join(chap))
print(f"wrote {cp}")
for c in chap: print("   "+c)
for f in os.listdir(A):
    if f.endswith((".wav",".txt")): os.remove(os.path.join(A,f))
