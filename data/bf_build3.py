import asyncio, edge_tts, os, re, subprocess, base64

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
VOICE = "en-US-AndrewNeural"
RATE = "+8%"
GAP = 0.30
TAIL = 1.0
MAX_GAP = 2.0
TICK = 1.55
NAME = "BYTE-02"

def dur(p):
    return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                                 "-of","csv=p=0",p],capture_output=True,text=True).stdout.strip())

def align(text, words):
    low=text.lower(); out=[]; cur=0
    for t,w in words:
        wl=w.lower().strip(".,;:!?\"'()")
        i=low.find(wl,cur) if wl else -1
        if i<0: i=cur
        else: cur=i+len(wl)
        out.append((i,t))
    return out

def phrase_time(text, al, words, ph):
    p=text.lower().find(ph.lower())
    if p<0: raise ValueError(f"cue not in script: {ph!r}")
    for ci,t in al:
        if ci>=p: return t
    return al[-1][1]

def bar(lab, pct, val, colour, tk_lab, tk_fill, tk_val=None, h=64):
    return (f'<div class="bf-bar" data-in="@{tk_lab}@"><span class="bf-bar__lab">{lab}</span>'
            f'<div class="bf-bar__track" style="height:{h}px"><div class="bf-bar__fill grow" '
            f'style="--w:{pct}%;background:{colour}" data-in="@{tk_fill}@"></div></div>'
            f'<span class="bf-bar__val" style="color:{colour}" data-in="@{tk_val or tk_fill}@">{val}</span></div>')

def row(k, v, tk, tv, colour="var(--white)", cls="bf-row"):
    return (f'<div class="{cls}" data-in="@{tk}@"><span class="bf-row__k">{k}</span>'
            f'<span class="bf-row__v" style="color:{colour}" data-in="@{tv}@">{v}</span></div>')

S=[]

# ---------------------------------------------------------------- CH 1
S.append(dict(tag="ch1", vo="Okay, so here's the thing that shouldn't be true. You've got a twenty-four gigabyte card. You want the biggest model it'll hold. So you go looking for the biggest one you can find, and you land on a thirty billion parameter model. Then somebody in the comments tells you the smarter buy is a twenty-seven billion parameter model, because the thirty B won't fit.",
 cues={"a":"Okay, so","b":"twenty-four gigabyte card","c":"biggest one you can find","d":"thirty billion parameter model","e":"twenty-seven billion parameter model"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">a 24 GB card &middot; two models &middot; one wrong assumption</div>
      <div style="display:flex;align-items:flex-end;gap:130px">
        <div class="stat"><div class="bf-big" style="font-size:190px;color:var(--lime)" data-in="@d@">30<span style="font-size:74px">B</span></div>
          <div class="bf-sub" data-in="@d@">the one you found</div></div>
        <div class="stat"><div class="bf-big" style="font-size:190px;color:var(--dim)" data-in="@e@">27<span style="font-size:74px">B</span></div>
          <div class="bf-sub" data-in="@e@">the one they tell you to buy</div></div>
      </div>
      <div class="chalk" data-in="@c@" style="font-family:var(--mono);font-size:21px;letter-spacing:.16em;color:var(--gray)">SAME 24 GB &middot; SAME ENGINE</div>
      <div class="bf-tape" data-in="@b@">it shouldn't fit &mdash; but it does</div>
    </div>'''))

S.append(dict(tag="ch1", vo="Except it does fit. It fits better. On the same card, the thirty billion parameter model uses less memory, holds more context, and generates tokens faster than the twenty-seven billion one. Same quantization family, same inference engine, same GPU. And it's not a trick. It's three measurable things: the file size, the cache, and the context window. Once you see it, you can't unsee it. So in this one we put Muse Glimmer thirty B against Qwen three point eight twenty-seven B, on the same cards, at the same context lengths, and we only look at the numbers that decide whether it runs.",
 cues={"a":"Except it does fit","b":"uses less memory","c":"holds more context","d":"generates tokens faster","e":"three measurable things","f":"the context window"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">same card &middot; same engine &middot; same family</div>
      <div class="col" style="width:1180px;gap:16px">
        <div class="bf-row bf-row--good" data-in="@b@"><span class="bf-row__k">Memory used</span><span class="bf-row__v" style="color:var(--lime)">less</span></div>
        <div class="bf-row bf-row--good" data-in="@c@"><span class="bf-row__k">Context held</span><span class="bf-row__v" style="color:var(--lime)">more</span></div>
        <div class="bf-row bf-row--good" data-in="@d@"><span class="bf-row__k">Tokens / second</span><span class="bf-row__v" style="color:var(--lime)">faster</span></div>
      </div>
      <div style="display:flex;gap:16px" data-in="@e@">
        <span class="chalk" style="font-family:var(--mono);font-size:19px;letter-spacing:.14em;padding:10px 18px">FILE SIZE</span>
        <span class="chalk" style="font-family:var(--mono);font-size:19px;letter-spacing:.14em;padding:10px 18px">CACHE</span>
        <span class="chalk" style="font-family:var(--mono);font-size:19px;letter-spacing:.14em;padding:10px 18px" data-in="@f@">CONTEXT</span>
      </div>
      <div class="bf-tape" data-in="@a@">once you see it you cannot unsee it</div>
    </div>'''))

# ---------------------------------------------------------------- CH 2
S.append(dict(tag="ch2", vo="The rule everyone repeats is simple. More parameters means more memory. Bigger model, bigger card. And it's a good rule, because it's usually true. Muse Glimmer is a dense model with twenty-seven point eight five billion active parameters. Qwen three point eight twenty-seven B is twenty-seven point three two billion parameters. On paper these two are the same size class. Nine hundred million parameters apart, which is nothing. But the rule hides the thing that actually fills your VRAM. Your card doesn't store parameters. It stores a quantized file, and it stores a cache, and the cache grows with every token you give it.",
 cues={"a":"The rule everyone repeats","b":"More parameters means more memory","c":"Muse Glimmer is a dense model","d":"Qwen three point eight","e":"same size class","f":"Nine hundred million","g":"doesn't store parameters","h":"stores a quantized file","i":"the cache grows"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">the rule</div>
      <div class="bf-big" style="font-size:66px;text-align:center" data-in="@b@">More parameters = more memory.</div>
      <div class="col" style="width:1100px;gap:14px">
        <div class="bf-row" data-in="@c@"><span class="bf-row__k">Muse Glimmer 30B</span><span class="bf-row__v">27.85 B</span></div>
        <div class="bf-row" data-in="@d@"><span class="bf-row__k">Qwen 3.8 27B</span><span class="bf-row__v">27.32 B</span></div>
        <div class="bf-row bf-row--good" data-in="@e@"><span class="bf-row__k">Difference</span><span class="bf-row__v" style="color:var(--lime)" data-in="@f@">0.53 B</span></div>
      </div>
      <div class="bf-cap" data-in="@g@" style="color:var(--red)">but your card does not store parameters</div>
      <div style="display:flex;gap:18px" data-in="@h@">
        <span class="chalk" style="font-family:var(--mono);font-size:20px;letter-spacing:.14em;padding:12px 20px">QUANTIZED FILE</span>
        <span class="chalk" style="font-family:var(--mono);font-size:20px;letter-spacing:.14em;padding:12px 20px" data-in="@i@">+ GROWING CACHE</span>
      </div>
    </div>'''))

# ---------------------------------------------------------------- CH 3
S.append(dict(tag="ch3", vo="First, the file. At four-bit, Muse Glimmer thirty B is fourteen point seven eight gigabytes. Qwen three point eight twenty-seven B is sixteen point six eight gigabytes. Read that again. The thirty billion parameter model is almost two gigabytes smaller than the twenty-seven billion one. And that's not magic, and it's not compression cheating. Glimmer was measured at four-bit medium. Qwen was measured at four-bit small.",
 cues={"a":"First, the file","b":"fourteen point seven eight","c":"sixteen point six eight","d":"Read that again","e":"almost two gigabytes smaller","f":"not compression cheating","g":"four-bit medium","h":"four-bit small"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">the file</div>
      <div class="col" style="width:1240px">
        ''' + bar("Muse Glimmer 30B","88","14.78 GiB","var(--lime)","b","b","e") + '''
        ''' + bar("Qwen 3.8 27B","100","16.68 GiB","var(--dim)","c","c","c") + '''
      </div>
      <div style="display:flex;gap:16px" data-in="@f@">
        <span class="chalk" style="font-family:var(--mono);font-size:20px;letter-spacing:.14em;padding:12px 20px" data-in="@g@">Q4_K MEDIUM</span>
        <span class="chalk" style="font-family:var(--mono);font-size:20px;letter-spacing:.14em;padding:12px 20px" data-in="@h@">Q4_K SMALL</span>
      </div>
      <div class="bf-tape" data-in="@d@">the bigger model is the smaller file</div>
    </div>'''))

S.append(dict(tag="ch3", vo="Second, the cache. Every token in your context writes a key matrix and a value matrix into memory. Those matrices don't care how many parameters the model has. They care how many layers it has, how many heads, and how long your context is. So the bigger model, in the smaller file, with the leaner cache, fits a longer conversation into the same twenty-four gigabytes.",
 cues={"a":"Second, the cache","b":"writes a key matrix","c":"a value matrix","d":"don't care how many parameters","e":"how many layers","f":"how long your context is","g":"fits a longer conversation"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">the cache</div>
      <div style="display:flex;align-items:center;gap:26px">
        <div class="chalk" style="font-family:var(--mono);font-size:22px;padding:18px 26px" data-in="@b@">KEY</div>
        <div class="chalk" style="font-family:var(--mono);font-size:22px;padding:18px 26px" data-in="@c@">VALUE</div>
        <div class="bf-cap" data-in="@d@" style="color:var(--red)">per token</div>
      </div>
      <div class="col" style="width:1100px;gap:14px">
        <div class="bf-row" data-in="@e@"><span class="bf-row__k">Layers &amp; heads</span><span class="bf-row__v">sets the rate</span></div>
        <div class="bf-row bf-row--hot" data-in="@f@"><span class="bf-row__k">Context length</span><span class="bf-row__v" style="color:var(--red)">sets the total</span></div>
      </div>
      <div class="bf-tape" data-in="@g@">same 24 GB &middot; longer conversation</div>
    </div>'''))

# ---------------------------------------------------------------- CH 4
S.append(dict(tag="ch4", vo="Here's measured VRAM. Not estimated, not calculated from a formula. Measured. At four K context, Muse Glimmer sits at sixteen gigabytes. Qwen is at eighteen. At thirty-two K, Glimmer is still sixteen. Qwen is at twenty. At sixty-four K, Glimmer is seventeen. Qwen is twenty-two. At one twenty-eight K, Glimmer is eighteen. Qwen is twenty-six. And at two hundred fifty-six K, Glimmer peaks at twenty gigabytes. Qwen needs thirty-four.",
 cues={"a":"Here's measured VRAM","b":"four K context","b2":"Qwen is at eighteen","c":"thirty-two K","c2":"twenty","d":"sixty-four K","d2":"twenty-two","e":"one twenty-eight K","e2":"twenty-six","f":"two hundred fifty-six K","f2":"thirty-four"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">measured VRAM &middot; not calculated</div>
      <div class="bf-sub" data-in="@a@">llama.cpp &middot; single GPU &middot; full offload</div>
      <div class="col" style="width:1180px;gap:12px">
        <div class="bf-row" data-in="@b@"><span class="bf-row__k">4K</span><span class="bf-row__v" style="color:var(--lime)">16</span><span class="bf-row__v" style="color:var(--dim)" data-in="@b2@">18</span></div>
        <div class="bf-row" data-in="@c@"><span class="bf-row__k">32K</span><span class="bf-row__v" style="color:var(--lime)">16</span><span class="bf-row__v" style="color:var(--dim)" data-in="@c2@">20</span></div>
        <div class="bf-row bf-row--good" data-in="@d@"><span class="bf-row__k">64K</span><span class="bf-row__v" style="color:var(--lime)">17</span><span class="bf-row__v" style="color:var(--yellow)" data-in="@d2@">22</span></div>
        <div class="bf-row bf-row--hot" data-in="@e@"><span class="bf-row__k">128K</span><span class="bf-row__v" style="color:var(--lime)">18</span><span class="bf-row__v" style="color:var(--red)" data-in="@e2@">26</span></div>
        <div class="bf-row bf-row--hot" data-in="@f@"><span class="bf-row__k">256K</span><span class="bf-row__v" style="color:var(--lime)">20</span><span class="bf-row__v" style="color:var(--red)" data-in="@f2@">34</span></div>
      </div>
      <div class="bf-sub" data-in="@f2@" style="color:var(--dim)">Glimmer (lime) &nbsp;vs&nbsp; Qwen 3.8 (red)</div>
    </div>'''))

# ---------------------------------------------------------------- CH 5
S.append(dict(tag="ch5", vo="Now there's a second number everyone ignores, and it decides how the thing actually feels. Token generation is how fast words come out. Prefill is how long you wait before the first one. And prefill is where long context really hurts. On a three thousand ninety, Glimmer processes a four K prompt at fourteen hundred and seventy-seven tokens a second. Qwen does thirteen hundred and eight. At one twenty-eight K, Glimmer drops to eight hundred and fifty-three. At two hundred fifty-six K, five hundred and eighty-four.",
 cues={"a":"second number everyone ignores","b":"Token generation","c":"Prefill is how long","d":"three thousand ninety","e":"fourteen hundred and seventy-seven","f":"thirteen hundred and eight","g":"one twenty-eight K","h":"eight hundred and fifty-three","i":"two hundred fifty-six K","j":"five hundred and eighty-four"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">the wait before the first word</div>
      <div style="display:flex;gap:60px">
        <div class="stat"><div class="bf-sub" data-in="@b@">generation</div><div class="bf-big" style="font-size:74px" data-in="@b@">words out</div></div>
        <div class="stat"><div class="bf-sub" data-in="@c@" style="color:var(--yellow)">prefill</div><div class="bf-big" style="font-size:74px;color:var(--yellow)" data-in="@c@">time to first</div></div>
      </div>
      <div class="col" style="width:1180px">
        ''' + bar("Glimmer &middot; 4K prompt","100","1,477 t/s","var(--lime)","d","e","e") + '''
        ''' + bar("Qwen 3.8 &middot; 4K prompt","88","1,308 t/s","var(--dim)","f","f","f") + '''
        ''' + bar("Glimmer &middot; 128K","58","853 t/s","var(--yellow)","g","g","h") + '''
        ''' + bar("Glimmer &middot; 256K","40","584 t/s","var(--red)","i","i","j") + '''
      </div>
    </div>'''))

S.append(dict(tag="ch5", vo="On a five-oh-ninety the numbers are much higher, but the shape is the same. Glimmer starts at forty-six hundred and twenty-five tokens a second at four K, and falls to eighteen hundred and seventy-four at two hundred fifty-six K. Qwen three point eight starts at thirty-seven hundred and forty-nine, and by one twenty-eight K it's at four hundred and sixty-one. Four hundred and sixty-one tokens a second. That's the number that makes a long-context chat feel broken.",
 cues={"a":"five-oh-ninety","b":"forty-six hundred and twenty-five","c":"eighteen hundred and seventy-four","d":"thirty-seven hundred and forty-nine","e":"four hundred and sixty-one","f":"makes a long-context chat feel broken"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">RTX 5090 &middot; prefill</div>
      <div class="col" style="width:1180px">
        ''' + bar("Glimmer &middot; 4K","100","4,625 t/s","var(--lime)","a","b","b") + '''
        ''' + bar("Glimmer &middot; 256K","41","1,874 t/s","var(--yellow)","c","c","c") + '''
        ''' + bar("Qwen 3.8 &middot; 4K","81","3,749 t/s","var(--dim)","d","d","d") + '''
        ''' + bar("Qwen 3.8 &middot; 128K","10","461 t/s","var(--red)","e","e","e") + '''
      </div>
      <div class="bf-tape" data-in="@f@">461 t/s feels broken</div>
    </div>'''))

# ---------------------------------------------------------------- CH 6
S.append(dict(tag="ch6", vo="Now the part that made me check the numbers twice. On an RTX three thousand ninety, Glimmer generates forty-five point three tokens a second at four K. Qwen does forty point three. Close. Not embarrassing. At sixty-four K, Glimmer holds forty-two point four. Qwen drops to thirty-three point nine.",
 cues={"a":"check the numbers twice","b":"three thousand ninety","c":"forty-five point three","d":"forty point three","e":"sixty-four K","f":"forty-two point four","g":"thirty-three point nine"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">RTX 3090 &middot; generation</div>
      <div class="col" style="width:1180px">
        ''' + bar("Glimmer &middot; 4K","100","45.3","var(--lime)","b","c","c") + '''
        ''' + bar("Qwen 3.8 &middot; 4K","89","40.3","var(--dim)","d","d","d") + '''
        ''' + bar("Glimmer &middot; 64K","94","42.5","var(--lime)","e","f","f") + '''
        ''' + bar("Qwen 3.8 &middot; 64K","75","33.9","var(--yellow)","g","g","g") + '''
      </div>
      <div class="bf-sub" data-in="@a@">tokens per second</div>
    </div>'''))

S.append(dict(tag="ch6", vo="At one twenty-eight K, Glimmer is still doing thirty-eight point one. And Qwen isn't in that test, because on a twenty-four gigabyte card, Qwen three point eight at one twenty-eight K isn't practical. That's the benchmark's own wording, not my opinion. On a five-oh-ninety it's the same story with more headroom. Glimmer at four K: eighty-three point two. Qwen: seventy-four point eight. At one twenty-eight K, Glimmer is at seventy-five point eight, and Qwen has fallen to twenty-two point eight.",
 cues={"a":"one twenty-eight K","b":"thirty-eight point one","c":"isn't practical","d":"benchmark's own wording","e":"five-oh-ninety","f":"eighty-three point two","g":"seventy-four point eight","h":"seventy-five point eight","i":"twenty-two point eight"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">RTX 5090 &middot; generation</div>
      <div class="col" style="width:1180px">
        ''' + bar("Glimmer &middot; 4K","100","83.2","var(--lime)","e","f","f") + '''
        ''' + bar("Qwen 3.8 &middot; 4K","90","74.8","var(--dim)","g","g","g") + '''
        ''' + bar("Glimmer &middot; 128K","91","75.8","var(--lime)","h","h","h") + '''
        ''' + bar("Qwen 3.8 &middot; 128K","27","22.8","var(--red)","i","i","i") + '''
      </div>
      <div class="bf-row bf-row--hot" style="width:900px" data-in="@c@"><span class="bf-row__k">Qwen at 128K on 24 GB</span><span class="bf-row__v" style="color:var(--red)" data-in="@a@">not practical</span></div>
      <div class="bf-sub" data-in="@d@" style="color:var(--dim)">the benchmark's wording, not ours</div>
    </div>'''))

S.append(dict(tag="ch6", vo="And here's the detail that actually surprised me. Qwen three point eight isn't just slower than Glimmer. At sixty-four K on a five-oh-ninety, Qwen three point six, the previous generation, is doing sixty-three point six tokens a second, against three point eight's twenty-six point two. The older Qwen is more than twice as fast at long context as the newer one. So newer doesn't mean faster, and more parameters doesn't mean more memory.",
 cues={"a":"detail that actually surprised me","b":"Qwen three point six","c":"previous generation","d":"sixty-three point six","e":"twenty-six point two","f":"twice as fast","g":"newer doesn't mean faster"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">RTX 5090 &middot; 64K context</div>
      <div class="col" style="width:1180px">
        ''' + bar("Qwen 3.6 &middot; older","100","63.66","var(--lime)","b","c","d") + '''
        ''' + bar("Qwen 3.8 &middot; newer","41","26.22","var(--red)","e","e","e") + '''
      </div>
      <div class="bf-tape" data-in="@a@">the older one is faster</div>
      <div class="bf-cap" data-in="@g@" style="color:var(--yellow)">newer &ne; faster &middot; bigger &ne; more memory</div>
    </div>'''))

# ---------------------------------------------------------------- CH 7
S.append(dict(tag="ch7", vo="And then there's the route people take when they can't stretch to a three thousand ninety. Two sixteen gigabyte cards. The benchmark tested exactly that. A pair of fifty-sixty Ti cards, thirty-two gigabytes total. It runs Qwen three point eight all the way to one twenty-eight K, because thirty-two gigabytes is enough. But look at the speed. Twenty-two point five tokens a second at four K. Fifteen point six at one twenty-eight K. Against a single three thousand ninety running Glimmer at forty-five and thirty-eight. So the two-card route buys capacity, not speed. Roughly a third of the tokens per second, plus multi-GPU overhead, plus two cards to cool. If you already own one sixteen gigabyte card, it's a real upgrade path. If you're buying from scratch, one twenty-four gigabyte card does more with less.",
 cues={"a":"route people take","b":"Two sixteen gigabyte cards","c":"fifty-sixty Ti","d":"thirty-two gigabytes total","e":"one twenty-eight K","f":"look at the speed","g":"twenty-two point five","h":"Fifteen point six","i":"buys capacity","j":"buying from scratch"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">the two-card route</div>
      <div style="display:flex;gap:22px" data-in="@b@">
        <div class="chalk" style="width:190px;height:120px;display:grid;place-items:center;font-family:var(--mono);font-size:20px">16 GB</div>
        <div class="chalk" style="width:190px;height:120px;display:grid;place-items:center;font-family:var(--mono);font-size:20px" data-in="@c@">16 GB</div>
        <div class="chalk" style="width:190px;height:120px;display:grid;place-items:center;font-family:var(--mono);font-size:20px;border-color:var(--yellow)" data-in="@d@">32 GB</div>
      </div>
      <div class="col" style="width:1180px">
        ''' + bar("2&times; 5060 Ti &middot; 4K","30","22.5","var(--yellow)","f","g","g") + '''
        ''' + bar("2&times; 5060 Ti &middot; 128K","21","15.6","var(--red)","e","h","h") + '''
        ''' + bar("1&times; 3090 + Glimmer","100","45.3 &rarr; 38.1","var(--lime)","i","i","i") + '''
      </div>
      <div class="bf-cap" data-in="@j@" style="color:var(--lime)">capacity, not speed</div>
    </div>'''))

# ---------------------------------------------------------------- CH 8
S.append(dict(tag="ch8", vo="Three honest caveats, because this is where most videos stop. One. The quantization levels are different. Glimmer was measured at four-bit medium, Qwen at four-bit small. That's not a perfectly fair fight, and anyone telling you it is is selling you something. Two. These benchmarks measure hardware behaviour, not intelligence. The source is explicit: VRAM, context scaling, prompt processing, token generation. Not reasoning quality. Not coding quality. A model that runs fast and fits can still be the wrong model for you. Three. The agentic claims around Glimmer are not independently benchmarked. Tool use, task accuracy, reliability, unconfirmed. Treat them as marketing until you test them yourself. What is confirmed: the file size, the VRAM curve, the prefill rates, and the token rates. Those are measurements, and they hold.",
 cues={"a":"Three honest caveats","b":"quantization levels are different","c":"not a perfectly fair fight","d":"measure hardware behaviour","e":"not intelligence","f":"not coding quality","g":"wrong model for you","h":"agentic claims","i":"not independently benchmarked","j":"treat them as marketing"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@" style="color:var(--red)">three caveats &middot; read these</div>
      <div class="col" style="width:1180px;gap:16px">
        <div class="chalk" data-in="@b@" style="display:flex;gap:20px;align-items:baseline"><span class="bf-row__k" style="width:60px">01</span><span class="bf-row__k" style="font-size:24px">Different quantization: Q4_K Medium vs Q4_K Small</span></div>
        <div class="chalk" data-in="@d@" style="display:flex;gap:20px;align-items:baseline"><span class="bf-row__k" style="width:60px">02</span><span class="bf-row__k" style="font-size:24px" data-in="@e@">Measures hardware, not model quality</span></div>
        <div class="chalk" data-in="@h@" style="display:flex;gap:20px;align-items:baseline"><span class="bf-row__k" style="width:60px">03</span><span class="bf-row__k" style="font-size:24px" data-in="@i@">Agentic claims: unconfirmed</span></div>
      </div>
      <div class="bf-tape" data-in="@c@">not a fair fight</div>
      <div class="bf-cap" data-in="@j@" style="color:var(--yellow)">what holds: file size &middot; VRAM curve &middot; token rates</div>
    </div>'''))

# ---------------------------------------------------------------- CH 9
S.append(dict(tag="ch9", vo="So if you're on twenty-four gigabytes and you want long context, Muse Glimmer thirty B is the one that fits. Two hundred fifty-six K in twenty gigabytes, at thirty-five to forty-five tokens a second on a three thousand ninety. If you specifically need Qwen's behaviour, then sixty-four K is your realistic ceiling on that card, and you should plan around it instead of discovering it at token ninety thousand. And if you're on a five-oh-ninety, you're not buying context anymore, because twenty gigabytes already covers Glimmer's whole window. You're buying speed. Eighty-three tokens a second at four K, sixty-nine at two hundred fifty-six K. Notice what none of those decisions were based on. Parameter count. Not once.",
 cues={"a":"if you're on twenty-four gigabytes","b":"the one that fits","c":"sixty-four K is your realistic ceiling","d":"five-oh-ninety","e":"you're buying speed","f":"Parameter count","g":"Not once"},
 html='''    <div class="ctr">
      <div class="bf-cap" data-in="@cap@">the verdict</div>
      <div class="col" style="width:1180px;gap:14px">
        <div class="bf-row bf-row--good" data-in="@a@"><span class="bf-row__k">On 24 GB &middot; long context</span><span class="bf-row__v" style="color:var(--lime)" data-in="@b@">Glimmer 30B</span></div>
        <div class="bf-row" data-in="@c@"><span class="bf-row__k">Need Qwen behaviour</span><span class="bf-row__v">64K ceiling</span></div>
        <div class="bf-row" data-in="@d@"><span class="bf-row__k">On a 5090</span><span class="bf-row__v" style="color:var(--yellow)" data-in="@e@">buying speed</span></div>
      </div>
      <div style="position:relative;display:inline-block" data-in="@f@">
        <span class="bf-big" style="font-size:64px;color:var(--dim)">PARAMETER COUNT</span>
        <span style="position:absolute;left:-4%;right:-4%;top:52%;height:7px;background:var(--red);transform:rotate(-2deg)"></span>
      </div>
      <div class="bf-cap" data-in="@g@" style="color:var(--red)">not once</div>
    </div>'''))

# ---------------------------------------------------------------- CH 10
S.append(dict(tag="ch10", vo="So stop shopping by parameter count. Shop by the file, the cache, and the context you actually use. Those three numbers are on the page. The parameter count tells you the least. That's the forensic part. See you in the next one.",
 cues={"a":"stop shopping by parameter count","b":"the file, the cache","c":"context you actually use","d":"tells you the least","e":"See you in the next one"},
 html='''    <div class="ctr">
      <div class="bf-big" style="font-size:70px;text-align:center" data-in="@a@">Stop shopping by parameter count.</div>
      <div style="display:flex;gap:18px" data-in="@b@">
        <span class="chalk" style="font-family:var(--mono);font-size:24px;padding:16px 24px">FILE</span>
        <span class="chalk" style="font-family:var(--mono);font-size:24px;padding:16px 24px">CACHE</span>
        <span class="chalk" style="font-family:var(--mono);font-size:24px;padding:16px 24px" data-in="@c@">CONTEXT</span>
      </div>
      <div class="bf-cap" data-in="@d@" style="color:var(--yellow)">parameter count tells you the least</div>
      <div class="bf-wm" data-in="@e@">byte forensics</div>
    </div>'''))

# ---------------------------------------------------------------- audio
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
                          "silencedetect=noise=-45dB:d=0.05","-f","null","-"],
                         capture_output=True,text=True).stderr
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
                "-i",os.path.join(A,"l.txt"),"-c:a","libmp3lame","-b:a","192k",vo],check=True)

cue={}
for i,sc in enumerate(S):
    al=align(sc["vo"],WORDS[i])
    for tok,ph in sc["cues"].items():
        wt=phrase_time(sc["vo"],al,WORDS[i],ph)
        cue[(i,tok)]=max(starts[i]+0.05,min(starts[i]+wt-0.08,starts[i]+d[i]-0.10))

def rel(tok,i):
    if tok.startswith("cap"): return 0.15
    return round(cue[(i,tok)]-starts[i],2)

# build sections, then run ONE global density pass (gaps can straddle scene cuts)
bodies=[]
for i,sc in enumerate(S):
    h=re.sub(r'data-in="@(\w+)@"',lambda m,i=i:'data-in="%s"'%rel(m.group(1),i),sc["html"])
    left=[v for v in re.findall(r'data-in="([^"]*)"',h) if not re.fullmatch(r"[0-9.]+",v)]
    assert not left, f"unresolved scene {i+1}: {left}"
    bodies.append(h)

ev=sorted({starts[i]+0.15 for i in range(len(S))} |
          {starts[i]+float(v) for i,h in enumerate(bodies)
           for v in re.findall(r'data-in="([0-9.]+)"',h)})
fills={i:[] for i in range(len(S))}
bounds=ev+[total]
for p,q in zip(bounds,bounds[1:]):
    gap=q-p
    if gap<=TICK: continue
    k=int(gap//TICK)
    for j in range(1,k+1):
        t=p+gap*j/(k+1)
        si=max(i for i in range(len(starts)) if starts[i]<=t)
        fills[si].append(round(t-starts[si],2))

sections=[]
for i,h in enumerate(bodies):
    if fills[i]:
        h=(h+'\n      <div class="rail">'
           + ''.join(f'<i data-in="{x}"></i>' for x in sorted(fills[i]))
           + '</div>')
    sections.append((i,h))

events=[]
for i,h in sections:
    for v in re.findall(r'data-in="([0-9.]+)"',h): events.append(round(starts[i]+float(v),3))
events=sorted(set(events))
gaps=[(q-p,p,q) for p,q in zip(events,events[1:])]
worst=max(gaps)[0]
print(f"audio {dur(vo):.2f}s  timeline {total:.2f}s  events {len(events)}  avg {total/len(events):.2f}s")
for gg,p,q in sorted(gaps,reverse=True)[:4]:
    print(f"   gap {gg:5.2f}s @ {p:6.2f}{'  OVER' if gg>MAX_GAP else ''}")
assert worst<=MAX_GAP, f"gap {worst:.2f}s > {MAX_GAP}"
print(f"max gap {worst:.2f}s  OK")

wipes=[round(starts[i]-0.285,3) for i in (2,4,6,8)]
sfx=[]
for i,sc in enumerate(S):
    for j,(tok,kind) in enumerate(sc["cues"].items()):
        if j%3==0: sfx.append((round(cue[(i,tok)],3), "tick"))
for i in (1,3,5,9):
    sfx.append((round(starts[i]+0.2,3),"thud"))
for w in wipes: sfx.append((w,"whoosh"))
sfx.sort()

b64=base64.b64encode(open(vo,"rb").read()).decode()
bcss=open(os.path.join(ROOT,"core","byte.css"),encoding="utf-8").read().replace('url("fonts/','url("core/fonts/')
pcss=open(os.path.join(ROOT,"core","player.css"),encoding="utf-8").read()
pjs=open(os.path.join(ROOT,"core","player.js"),encoding="utf-8").read()
scenes_js=",\n  ".join(f"{{s:{starts[i]:5.2f},  e:{starts[i]+d[i]:5.2f}}}" for i in range(len(d)))
sfx_js="\n".join(f"  {{t:{x:6.3f}, f:'{k}'}}," for x,k in sfx)
labels=", ".join(f"'{t.upper()}'" for t in [s["tag"] for s in S])

html=f"""<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<title>The 30B That Uses Less VRAM Than The 27B</title>
<style>
{bcss}
{pcss}
  .ctr{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;
        justify-content:center;gap:30px;padding:0 100px}}
  .stat{{display:flex;flex-direction:column;align-items:center;gap:14px}}
  .col{{display:flex;flex-direction:column;gap:16px;width:1200px}}
  .bf-row{{gap:30px}}
  .bf-row__v{{min-width:110px;text-align:right;white-space:nowrap}}
  .bf-row__v + .bf-row__v{{min-width:90px}}
  .grow{{width:0}} .grow.on{{width:var(--w)}}
  .bf-bar{{height:78px}}
  .bf-bar .bf-bar__track{{height:52px}}
  .bf-bar .bf-bar__lab{{font-size:20px;width:250px}}
  .bf-bar .bf-bar__val{{font-size:30px;width:210px;white-space:nowrap}}
  .rail{{position:absolute;left:50%;transform:translateX(-50%);bottom:74px;display:flex;gap:9px}}
  .rail i{{width:2px;height:16px;background:rgba(237,234,227,.13);display:block}}
  .rail i.on{{background:rgba(237,234,227,.6)}}
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
for f in os.listdir(A):
    if f.endswith((".wav",".txt")): os.remove(os.path.join(A,f))
