"""Builds two 60-second comparison clips.

  A.html  - hand-authored windows, each with its own layout/diagram
  B.html  - the current template generator (first 60s of BYTE-03)
"""
import asyncio, base64, os, re, subprocess, tempfile

import edge_tts

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
VOICE = "en-US-AndrewNeural"
RATE = "-13%"
GAP = 0.35
TAIL = 1.2


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "csv=p=0", p], capture_output=True, text=True).stdout)


# ─────────────────────────────────────────────── A: bespoke windows
CALLOUT_CSS = """
  .stagewrap{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}
  .sceneA{position:absolute;inset:0}
  .kicker{font-family:var(--mono);font-size:20px;letter-spacing:.24em;color:var(--dim);text-transform:uppercase}
  .bigline{font-family:var(--sans);font-size:96px;line-height:.95;color:var(--white)}
  .huge{font-family:var(--sans);font-size:230px;line-height:.85}
  .lab{font-family:var(--mono);font-size:22px;letter-spacing:.14em;text-transform:uppercase;color:var(--gray)}
  .pair{display:flex;gap:80px;align-items:flex-end;justify-content:center}
  .callout{position:absolute;font-family:var(--mono);font-size:19px;letter-spacing:.12em;
           color:var(--gray);text-transform:uppercase;white-space:nowrap}
  .callout::before{content:"";position:absolute;left:-78px;top:50%;width:64px;height:1px;
           background:linear-gradient(90deg,rgba(237,234,227,.65),rgba(237,234,227,.15))}
  .callout::after{content:"";position:absolute;left:-82px;top:50%;width:7px;height:7px;margin-top:-3px;
           border-radius:50%;background:var(--yellow)}
  .callout.r::before{left:auto;right:-78px;transform:scaleX(-1)}
  .callout.r::after{left:auto;right:-82px}
  .rowline{display:flex;align-items:center;gap:26px}
  .rowline .n{font-family:var(--mono);font-weight:800;font-size:34px;width:120px;color:var(--gray)}
  .rowline .t{font-family:var(--mono);font-size:30px;color:var(--white)}
  .hl{position:absolute;left:-26px;right:-26px;height:70px;border-radius:14px;
      background:rgba(245,213,71,.10);border:1.5px solid rgba(245,213,71,.75);
      box-shadow:0 0 22px rgba(245,213,71,.18);opacity:0;transition:opacity .25s}
  .axis{display:flex;gap:18px;align-items:center}
  .axis .tick{font-family:var(--mono);font-size:16px;color:var(--dim)}
  .art .s{fill:none;stroke:var(--white);stroke-width:3}
  .art .t{stroke-width:2.2}
  .art .blade{fill:none;stroke:var(--gray);stroke-width:7}
  .art .dim{opacity:.45}
  .art .fg{fill:rgba(237,234,227,.25)}
  .art .fl{fill:var(--lime)}
  .art .fy{fill:var(--yellow)}
  .art .lime{fill:var(--lime);font-family:var(--mono);font-weight:800;font-size:30px}
  .art .small{fill:var(--dim);font-family:var(--mono);font-size:15px;letter-spacing:3px}
  .art{display:block;width:100%;height:auto}
  .spin{transform-box:fill-box;transform-origin:center;animation:spin 2.6s linear infinite}
  @keyframes spin{to{transform:rotate(360deg)}}
  .float{animation:bob 5s ease-in-out infinite}
  @keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
  .pulse{animation:pl 1.8s ease-in-out infinite}
  @keyframes pl{0%,100%{opacity:1}50%{opacity:.45}}
"""

A_SCENES = [
    dict(vo="A graphics card is not one number. It is memory, and bandwidth, and a cache that grows every single token you feed it.",
         cues={"k": "graphics card", "big": "memory", "lab": "cache that grows"},
         html='''<div class="stagewrap"><div style="display:flex;align-items:center;gap:70px">
  <div class="float" data-in="@k@" style="width:520px">__GPU__</div>
  <div>
    <div class="kicker" data-in="@k@">the whole argument</div>
    <div class="huge" style="color:var(--lime)" data-in="@big@"><span data-count="24">24</span><span style="font-size:90px">GB</span></div>
    <div class="lab" data-in="@lab@" style="margin-top:14px">cache grows, not the file</div>
  </div>
</div></div>'''),

    dict(vo="Two cards, same memory, different windows. One holds sixty four K. The other holds two hundred and fifty six.",
         cues={"c1": "Two cards", "c2": "different windows", "big": "two hundred and fifty"},
         html='''<div class="stagewrap"><div style="text-align:center">
  <div class="kicker" data-in="@c1@">same 24 GB &middot; different windows</div>
  <div class="pair" style="margin-top:40px">
    <div data-in="@c2@"><div style="width:420px;opacity:.55">__GPU__</div>
      <div class="lab" style="margin-top:16px">Qwen &middot; 64K</div></div>
    <div data-in="@big@"><div style="width:420px">__GPU__</div>
      <div class="lab" style="margin-top:16px;color:var(--lime)">Glimmer &middot; 256K</div></div>
  </div>
</div></div>'''),

    dict(vo="So look at the card itself. The fan keeps it alive. The memory chips hold the file. And the slot is the only way anything gets in or out.",
         cues={"fan": "The fan", "mem": "memory chips", "slot": "the slot"},
         html='''<div class="stagewrap"><div style="position:relative;width:1000px;height:460px">
  <div class="float" style="width:760px;position:absolute;left:120px;top:80px">__GPU__</div>
  <div class="callout" data-in="@fan@" style="left:120px;top:60px">fan &middot; cooling</div>
  <div class="callout r" data-in="@mem@" style="right:110px;top:250px">memory &middot; the file</div>
  <div class="callout" data-in="@slot@" style="left:150px;bottom:40px">slot &middot; the bus</div>
</div></div>'''),

    dict(vo="Watch the number climb as the window opens. Sixteen at four K. Twenty at thirty two. Twenty six at one twenty eight. And thirty four at two fifty six.",
         cues={"a": "Watch the number", "r1": "Sixteen", "r2": "Twenty at", "r3": "Twenty six", "r4": "thirty four"},
         html='''<div class="stagewrap"><div style="width:1150px">
  <div class="kicker" data-in="@a@">vram as the window opens</div>
  <div style="position:relative;margin-top:34px">
    <div class="hl" data-in="@r1@" style="top:0"></div>
    <div class="rowline"><span class="n">4K</span><span class="t">16 GB</span></div>
    <div class="rowline" style="margin-top:18px"><span class="n">32K</span><span class="t">20 GB</span></div>
    <div class="rowline" style="margin-top:18px"><span class="n">128K</span><span class="t">26 GB</span></div>
    <div class="rowline" style="margin-top:18px"><span class="n">256K</span><span class="t">34 GB</span></div>
  </div>
</div></div>'''),

    dict(vo="Put it on a chart and the shape is obvious. The lime bar is what fits. The red bar is what does not.",
         cues={"k": "Put it on a chart", "l": "The lime bar", "r": "The red bar"},
         html='''<div class="stagewrap"><div style="width:1150px">
  <div class="kicker" data-in="@k@">what actually fits on 24 GB</div>
  <div class="axis" style="margin-top:40px;opacity:.55">
    <span class="tick">0</span>
    <div style="flex:1;height:56px;background:rgba(255,255,255,.06);position:relative">
      <div class="grow" style="--w:59%;background:var(--lime);height:100%" data-in="@l@"></div>
    </div>
    <span class="lab" style="color:var(--lime)">20 GB</span>
  </div>
  <div class="axis" style="margin-top:26px;opacity:.55">
    <span class="tick">0</span>
    <div style="flex:1;height:56px;background:rgba(255,255,255,.06);position:relative">
      <div class="grow" style="--w:100%;background:var(--red);height:100%" data-in="@r@"></div>
    </div>
    <span class="lab" style="color:var(--red)">34 GB</span>
  </div>
  <div class="lab" style="margin-top:34px;color:var(--yellow)" data-in="@r@">24 GB is the line between them</div>
</div></div>'''),

    dict(vo="That is the whole thing. Same card, same budget, four times the context. Measure the window, then buy.",
         cues={"a": "That is the whole thing", "b": "four times", "c": "Measure the window"},
         html='''<div class="stagewrap"><div style="text-align:center">
  <div class="bigline" data-in="@a@">Same card. Four times the context.</div>
  <div class="huge" style="color:var(--lime);margin-top:10px" data-in="@b@"><span data-count="4">4</span><span style="font-size:100px">&times;</span></div>
  <div class="bf-tape" style="margin-top:30px" data-in="@c@">measure the window, then buy</div>
</div></div>'''),
]


async def record(lines, work):
    os.makedirs(work, exist_ok=True)
    words, files = [], []
    for i, sc in enumerate(lines, 1):
        raw = os.path.join(work, f"r{i}.mp3"); wav = os.path.join(work, f"n{i}.wav")
        c = edge_tts.Communicate(sc["vo"], VOICE, rate=RATE, boundary="WordBoundary")
        buf, ws = bytearray(), []
        async for ch in c.stream():
            if ch["type"] == "audio":
                buf += ch["data"]
            elif ch["type"] == "WordBoundary":
                ws.append((ch["offset"] / 1e7, ch["text"]))
        open(raw, "wb").write(bytes(buf))
        o = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", raw, "-af",
                            "silencedetect=noise=-45dB:d=0.05", "-f", "null", "-"],
                           capture_output=True, text=True).stderr
        e = re.findall(r"silence_end: ([0-9.]+)", o)
        lead = float(e[0]) if e else 0.0
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", raw,
                        "-af", "silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,areverse,"
                               "silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,areverse",
                        "-ar", "44100", "-ac", "1", "-c:a", "pcm_s16le", wav], check=True)
        words.append([(max(0.0, x - lead + 0.04), w) for x, w in ws])
        files.append(wav)
        os.remove(raw)
    return words, files


def phrase_time(text, words, phrase):
    p = text.lower().find(phrase.lower())
    if p < 0: return None
    low, cur = text.lower(), 0
    for t, w in words:
        wl = w.lower().strip(".,;:!?\"'()")
        i = low.find(wl, cur) if wl else -1
        if i < 0: i = cur
        else: cur = i + len(wl)
        if i >= p: return t
    return words[-1][0]


def concat(files, out):
    lst = out + ".txt"
    with open(lst, "w") as f:
        for p in files: f.write(f"file '{p.replace(chr(92),'/')}'\n")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat",
                    "-safe", "0", "-i", lst, "-c:a", "libmp3lame", "-b:a", "160k", out], check=True)
    os.remove(lst)


def build_a():
    work = os.path.join(ROOT, "build", "demoA")
    words, files = asyncio.run(record(A_SCENES, work))
    # concat with gaps
    gap = os.path.join(work, "g.wav")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "lavfi",
                    "-i", "anullsrc=r=44100:cl=mono", "-t", str(GAP), "-c:a", "pcm_s16le", gap], check=True)
    seq = []
    for i, f in enumerate(files):
        seq.append(f)
        if i < len(files) - 1: seq.append(gap)
    vo = os.path.join(work, "vo.mp3")
    concat(seq, vo)

    d = [dur(f) for f in files]
    starts, acc = [], 0.0
    for x in d:
        starts.append(acc); acc += x + GAP
    total = sum(d) + GAP * (len(d) - 1) + TAIL

    css = open(os.path.join(ROOT, "core", "byte.css"), encoding="utf-8").read().replace('url("fonts/', 'url("core/fonts/')
    pcss = open(os.path.join(ROOT, "core", "player.css"), encoding="utf-8").read()
    pjs = open(os.path.join(ROOT, "core", "player.js"), encoding="utf-8").read()
    art = open(os.path.join(ROOT, "data", "art_gpu.svg"), encoding="utf-8").read()

    secs = []
    for i, sc in enumerate(A_SCENES):
        h = sc["html"].replace("__GPU__", art)
        def sub(m, i=i):
            key = m.group(1)
            if key == "cap": return 'data-in="0.15"'
            t = phrase_time(sc["vo"], words[i], sc["cues"][key])
            if t is None: t = 0.4
            return 'data-in="%.2f"' % max(0.05, min(t - 0.08, d[i] - 0.1))
        h = re.sub(r'data-in="@(\w+)@"', sub, h)
        secs.append(f'  <section class="scene" data-scene="{i}">\n{h}\n  </section>')

    b64 = base64.b64encode(open(vo, "rb").read()).decode()
    scenes_js = ",\n  ".join(f"{{s:{starts[i]:5.2f},  e:{starts[i]+d[i]:5.2f}}}" for i in range(len(d)))
    html = f"""<!DOCTYPE html><html lang="en" class="no-js"><head><meta charset="utf-8"><title>A - bespoke windows</title>
<style>
{css}
{pcss}
{CALLOUT_CSS}
  .grow{{width:0}} .grow.on{{width:var(--w)}}
  .no-js #start{{display:none!important}}
</style></head><body>
<script>document.documentElement.classList.remove("no-js");</script>
<div id="wrap"><div id="stage">
{chr(10).join(secs)}
</div></div>
<script>
window.EPISODE = {{
  kicker: "A · hand-authored windows", title: "A — bespoke layouts",
  subtitle: "one idea per window, own diagram", total: {total:.2f}, maxGap: 9.0,
  vo: "data:audio/mpeg;base64,{b64}", sfxBase: "audio/", labels: ['01','02','03','04','05','06'],
  scenes: [
  {scenes_js}
  ], wipes: [], wipeColors: [], sfx: []
}};
</script><script>{pjs}</script></body></html>"""
    out = os.path.join(ROOT, "COMPARE-A.html")
    open(out, "w", encoding="utf-8").write(html)
    print(f"A: {total:.1f}s, {len(A_SCENES)} bespoke windows -> {out}")


def build_b(first_n=5):
    src = open(os.path.join(ROOT, "BYTE-03.html"), encoding="utf-8").read()
    scenes = [(float(a), float(b)) for a, b in re.findall(r"\{s:\s*([0-9.]+),\s*e:\s*([0-9.]+)\}", src)]
    secs = re.findall(r'<section class="scene[^"]*" data-scene="\d+">.*?</section>', src, re.S)
    keep = min(first_n, len(scenes))
    end = scenes[keep - 1][1] + 0.4

    m = re.search(r'vo:\s*"data:audio/mpeg;base64,([A-Za-z0-9+/=]+)"', src)
    audio = base64.b64decode(m.group(1))
    with tempfile.TemporaryDirectory() as td:
        i, o = os.path.join(td, "i.mp3"), os.path.join(td, "o.mp3")
        open(i, "wb").write(audio)
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", i,
                        "-t", f"{end:.2f}", "-c:a", "libmp3lame", "-b:a", "160k", o], check=True)
        b64 = base64.b64encode(open(o, "rb").read()).decode()

    body = "\n".join(secs[:keep])
    out_html = re.sub(r'<section class="scene[^"]*" data-scene="\d+">.*?</section>', "", src, flags=re.S)
    out_html = out_html.replace('<div id="wrap"><div id="stage">',
                                '<div id="wrap"><div id="stage">\n' + body + "\n", 1)
    out_html = re.sub(r'vo:\s*"data:audio/mpeg;base64,[A-Za-z0-9+/=]+"',
                      f'vo: "data:audio/mpeg;base64,{b64}"', out_html, count=1)
    out_html = re.sub(r"scenes:\s*\[[^\]]*\]",
                      "scenes: [\n  " + ",\n  ".join(f"{{s:{a:.2f}, e:{b:.2f}}}" for a, b in scenes[:keep]) + "\n  ]",
                      out_html, count=1)
    out_html = re.sub(r"total:\s*[0-9.]+", f"total: {end:.2f}", out_html, count=1)
    out_html = out_html.replace("<title>", "<title>B - template windows : ")
    out = os.path.join(ROOT, "COMPARE-B.html")
    open(out, "w", encoding="utf-8").write(out_html)
    print(f"B: {end:.1f}s, {keep} template windows -> {out}")


if __name__ == "__main__":
    build_a()
    build_b()
