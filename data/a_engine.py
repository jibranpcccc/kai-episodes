"""Shared episode engine: spec (list of windows) -> HTML."""
import asyncio, base64, os, re, subprocess, sys

import edge_tts

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VOICE = "en-US-AndrewNeural"
RATE = "-30%"
GAP = 0.32
TAIL = 2.0

from art_lib import (GPU, CHIP, LAPTOP, RAM, SLOT, CACHE, DIE, HEATSINK, TWODIE, PCB, QUANT,
                     TOWER, SYSRAM, PCIELINK, DUALBOARD, PSU, RISER, MINIPC,
                     LAPCUT, SODIMM, TWOGEN, GAUGE, WAFER, SUPERCHIP, ROUTER2)  # noqa: E402

# ─────────────────────────────────────────────────────────── renderers
def render(w, i):
    lay = w["layout"]
    if lay == "stat":
        stats = "".join(
            f'<div class="stat"><div class="bf-big big" style="color:{c}" data-in="@s{k}@">'
            f'<span data-count="{v}">{v}</span><span class="u">{u}</span></div>'
            f'<div class="lab" style="margin-top:12px" data-in="@s{k}@">{lb}</div></div>'
            for k, ((v, u, c), lb) in enumerate(zip(w["big"], w["labels"])))
        return f'''<div class="stagewrap"><div class="wrapc">
  <div class="float" data-in="@a@" style="width:520px">{w["art"]}</div>
  <div class="pair">{stats}</div>
  <div class="bf-tape" style="margin-top:26px" data-in="@t@">{w["tape"]}</div>
</div></div>'''

    if lay == "callout":
        m = re.match(r'<svg[^>]*viewBox="([^"]+)"[^>]*>(.*)</svg>', w["art"], re.S)
        vb, inner = m.group(1), m.group(2)
        vbnum = [float(x) for x in vb.replace(",", " ").split()]
        vw, vh = (vbnum[-2], vbnum[-1]) if len(vbnum) >= 4 else (vbnum[0], vbnum[1])

        # anchor points live in the drawing's own coordinate space, so the dot
        # sits on the part it names instead of floating beside it
        ANCH = {
            (480, 190): [(118, 88), (330, 122), (100, 166)],   # gpu: fan, vram bar, pins
            (420, 260): [(51, 77), (217, 77), (150, 214)],     # cache: key, value, rows
            (460, 140): [(323, 70), (72, 70), (120, 110)],     # ram: lit chip, chip, pins
            (480, 200): [(120, 103), (300, 103), (60, 152)],   # slot: fingers, slot, board
            (240, 240): [(120, 120), (78, 60), (160, 182)],    # chip: core, pin, pin
            (380, 250): [(150, 60), (210, 150), (190, 206)],   # laptop: screen top, screen body, base
            (300, 300): [(150, 150), (74, 74), (230, 230)],    # die: core, corner, corner
            (420, 200): [(120, 110), (300, 110), (200, 40)],   # heatsink: fin, fin, screw
            (520, 240): [(120, 115), (400, 115), (260, 200)],  # two dies: a, b, caption
            (460, 240): [(90, 95), (340, 143), (250, 90)],     # pcb: chip, module, trace line
            (420, 160): [(80, 80), (200, 80), (300, 80)],      # quant: 4/3/2-bit
            (300, 380): [(110, 134), (120, 210), (150, 300)],  # tower: lit gpu, bays, psu
            (460, 220): [(200, 74), (200, 113), (200, 152)],   # sysram: slot, slot, slot
            (520, 200): [(90, 100), (430, 100), (260, 100)],   # pcie: vram, ram, link
            (480, 260): [(240, 67), (240, 119), (420, 188)],   # dualboard: slot1, slot2, chip
            (440, 210): [(122, 100), (268, 64), (268, 124)],   # psu: fan, cable, cable
            (480, 180): [(95, 88), (280, 80), (406, 88)],      # riser: board, ribbon, card
            (448, 200): [(120, 100), (265, 78), (265, 123)],   # minipc: fan, line, line
            (470, 240): [(146, 105), (297, 105), (230, 190)],  # lapcut: cpu, shared, hinge
            (380, 120): [(156, 56), (325, 56), (190, 88)],     # sodimm: cell, cell, module edge
            (530, 240): [(124, 117), (396, 117), (260, 210)],  # twogen: old, new, caption
            (380, 250): [(190, 190), (250, 86), (190, 46)],    # gauge: hub, needle tip, scale top
            (310, 300): [(150, 150), (86, 86), (214, 214)],    # wafer: die, die, die
            (500, 260): [(146, 103), (342, 103), (100, 197)],  # gpu2: fan, fan, gold fingers
            (492, 160): [(56, 55), (220, 55), (250, 102)],    # ram2: chip, chip, contacts
            (500, 258): [(250, 96), (250, 220), (250, 200)],   # laptop2: screen, base, hinge
            (300, 418): [(160, 60), (150, 150), (150, 320)],   # tower2: top fans, gpu, psu
            (432, 306): [(160, 150), (322, 105), (322, 212)],  # die2: gpu die, cpu, memory
            (304, 306): [(152, 150), (152, 30), (78, 60)],     # wafer2: centre, edge, die
            (524, 240): [(99, 108), (368, 96), (262, 108)],    # router2: laptop, device, link
            (490, 270): [(136, 124), (346, 88), (346, 160)],   # superchip: gpu, cpu, memory
        }
        pts = ANCH.get((vw, vh))
        if pts is None:
            pts = [(vw * 0.5, vh * 0.5), (vw * 0.25, vh * 0.3), (vw * 0.75, vh * 0.75)]

        BX, BY, BW, BH = 470.0, 26.0, 910.0, 568.0
        sc = min(BW / vw, BH / vh)
        ox = BX + (BW - vw * sc) / 2
        oy = BY + (BH - vh * sc) / 2
        dots = [(ox + ax * sc, oy + ay * sc) for ax, ay in pts]

        # label each dot from the nearest free side, with a short leader so the
        # line can never cross the drawing
        # labels stack on the side of their dot, staggered so they never collide
        # numbered callouts: a badge sits ON the part, a legend lists them beside
        # the drawing. No leader lines, so nothing can ever cross the artwork.
        keys = list(w.get("cues", {}))[:3]
        badges = ""
        legend = ""
        rows = [268, 330, 392]
        for k, (dx, dy) in enumerate(dots):
            badges += (f'<g class="badge"><circle cx="{dx:.1f}" cy="{dy:.1f}" r="17"/>'
                       f'<text x="{dx:.1f}" y="{dy+7:.1f}" text-anchor="middle">{k+1}</text></g>')
            legend += (f'<g data-in="@{keys[k] if k < len(keys) else "x"}@" class="legrow">'
                       f'<circle cx="62" cy="{rows[k]-6}" r="15"/>'
                       f'<text x="62" y="{rows[k]}" text-anchor="middle">{k+1}</text>'
                       f'<text x="96" y="{rows[k]}" class="legtxt">{w["marks"][k][0].upper()}</text></g>')
        return (f'<div class="stagewrap"><svg class="ann" viewBox="0 0 1400 620">'
                f'<svg x="{BX}" y="{BY}" width="{BW}" height="{BH}" viewBox="{vb}" '
                f'preserveAspectRatio="xMidYMid meet">{inner}</svg>{badges}{legend}</svg></div>')

    if lay == "pair":
        cells = "".join(
            f'<div data-in="@{k}@"><div style="width:380px;opacity:{1 if k=="p1" else .55}">{w["art"]}</div>'
            f'<div class="lab" style="margin-top:14px;color:{c}">{n}</div>'
            f'<div class="hugen" style="color:{c}">{v}</div></div>'
            for k, (n, v, c) in zip(["p0", "p1"], w["pair"]))
        return f'''<div class="stagewrap"><div style="text-align:center">
  <div class="kicker" data-in="@l@">side by side</div>
  <div class="pair" style="margin-top:30px">{cells}</div>
  <div class="bf-tape" style="margin-top:26px" data-in="@t@">{w["tape"]}</div>
</div></div>'''

    if lay == "list":
        rows = "".join(
            f'<div class="rowbox" data-in="@{k}@"><span class="rn">{n}</span>'
            f'<span class="rt" style="color:{ "var(--lime)" if c=="good" else "var(--red)" }">{t}</span></div>'
            for k, (n, t, c) in zip(["a", "b", "c"], w["rows"]))
        return f'''<div class="stagewrap"><div class="wrapc">
  <div class="kicker" data-in="@k@">{w["kicker"]}</div>
  <div class="float" data-in="@k@" style="width:520px;margin:14px 0">{w["art"]}</div>
  <div style="width:100%">{rows}</div>
</div></div>'''

    if lay == "chart":
        bars = "".join(
            f'<div class="axis2"><span class="tick">{n}</span>'
            f'<div class="track"><div class="fill" style="--w:{p}%;background:{c}" data-in="@b{k}@"></div></div>'
            f'<span class="val" style="color:{c}" data-in="@b{k}@">{v}</span></div>'
            for k, (n, v, p, c) in enumerate(w["bars"]))
        art = w.get("art", GPU)
        return f'''<div class="stagewrap"><div class="wrapc">
  <div class="float" data-in="@k@" style="width:230px;margin-bottom:6px">{art}</div>
  <div class="kicker" data-in="@k@">{w["kicker"]}</div>
  <div style="width:100%;margin-top:20px">{bars}</div>
  <div class="lab" style="margin-top:22px;color:var(--dim)" data-in="@k@">{w["note"]}</div>
</div></div>'''

    if lay == "table":
        rows = "".join(
            f'<div class="trow"><span class="tk">{a}</span>'
            f'<span class="tv" data-in="@r{k}@" style="color:var(--lime)">{b}</span>'
            f'<span class="tv" data-in="@r{k}@" style="color:{ "var(--lime)" if c=="good" else "var(--red)" }">{c}</span></div>'
            for k, (a, b, c, _) in enumerate(w["rows"]))
        art = w.get("art", RAM)
        return f'''<div class="stagewrap"><div class="wrapc">
  <div class="float" data-in="@k@" style="width:250px;margin-bottom:6px">{art}</div>
  <div class="kicker" data-in="@k@">{w["kicker"]}</div>
  <div style="width:100%;margin-top:14px">{rows}</div>
</div></div>'''

    # quote
    art = w.get("art", GPU)
    return f'''<div class="stagewrap"><div style="text-align:center;max-width:1400px">
  <div class="float" data-in="@a@" style="width:260px;margin:0 auto 18px">{art}</div>
  <div class="bigline" data-in="@a@" style="color:{w["accent"]}">{w["line"]}</div>
  <div class="bf-tape" style="margin-top:34px" data-in="@t@">{w["tape"]}</div>
</div></div>'''


EXTRA_CSS = """
  :root{--cyan:#38D9E8;--orange:#F08A3C;--soft:#8FD3C7}
  .stagewrap{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;padding:0 70px}
  .wrapc{display:flex;flex-direction:column;align-items:center;width:1400px;transform:scale(1.12)}
  .bf-big{font-family:var(--sans);color:var(--white);letter-spacing:-.01em}
  .big{font-size:168px;line-height:.86}
  .u{font-size:70px}
  .stat{display:flex;flex-direction:column;align-items:center}
  .pair{display:flex;gap:80px;align-items:flex-end;justify-content:center}
  .hugen{font-family:var(--mono);font-weight:800;font-size:44px;margin-top:4px}
  .rowbox{display:flex;align-items:center;gap:26px;min-height:104px;padding:0 30px;
          border:1.5px solid rgba(237,234,227,.35);border-radius:14px;margin-bottom:14px;
          background:rgba(255,255,255,.02)}
  .rowbox .rn{font-family:var(--mono);font-weight:800;font-size:30px;color:var(--gray);min-width:90px}
  .rowbox .rt{font-family:var(--mono);font-size:28px}
  .axis2{display:flex;align-items:center;gap:22px;margin-bottom:22px}
  .axis2 .tick{font-family:var(--mono);font-size:20px;color:var(--gray);width:230px;text-align:right}
  .track{flex:1;height:48px;border-radius:10px;background:rgba(255,255,255,.05);
         border:1.5px solid rgba(237,234,227,.18);overflow:hidden}
  .fill{height:100%;width:0;transition:width .25s ease-out}
  .fill.on{width:var(--w)}
  .axis2 .val{font-family:var(--mono);font-weight:800;font-size:28px;width:130px}
  .trow{display:flex;align-items:center;min-height:96px;padding:0 30px;border:1.5px solid rgba(237,234,227,.3);
        border-radius:12px;margin-bottom:12px;background:rgba(255,255,255,.02)}
  .trow .tk{flex:1;font-family:var(--mono);font-size:28px;color:var(--white)}
  .trow .tv{font-family:var(--mono);font-size:28px;width:150px;text-align:right}
  .kicker{font-family:var(--mono);font-size:20px;letter-spacing:.24em;color:var(--cyan);text-transform:uppercase}
  .lab{font-family:var(--mono);font-size:22px;letter-spacing:.14em;text-transform:uppercase;color:var(--gray)}
  .bigline{font-family:var(--sans);font-size:104px;line-height:.98}
  .ann{display:block;width:1280px;height:auto;overflow:visible}
  .annlabel line{stroke:rgba(237,234,227,.45);stroke-width:1.5}
  .annlabel circle{fill:var(--yellow)}
  .annlabel text{fill:rgba(237,234,227,.75);font-family:var(--mono);font-size:19px;letter-spacing:3px}
  .art .s{fill:none;stroke:rgba(237,234,227,.85);stroke-width:2}
  .art .t{stroke-width:1.5}
  .art .blade{fill:none;stroke:rgba(237,234,227,.3);stroke-width:6}
  .art .dim{opacity:.45}
  .art .fg{fill:rgba(237,234,227,.22)}
  .art .fl{fill:var(--lime)}
  .art .fy{fill:var(--yellow)}
  .art .lime{fill:var(--lime);font-family:var(--mono);font-weight:800;font-size:30px}
  .art .small{fill:rgba(237,234,227,.45);font-family:var(--mono);font-size:15px;letter-spacing:3px}
  .art{display:block;width:100%;height:auto;max-height:none}
  .float svg{max-height:340px;width:auto;margin:0 auto;display:block}
  .hero2 svg{max-height:430px;width:auto;margin:0 auto;display:block}
  /* ---------- depth + light ---------- */
  body{background:radial-gradient(125% 95% at 50% -10%, #161b20 0%, #0c0f12 52%, #06080a 100%)!important}
  .stagewrap{filter:drop-shadow(0 30px 60px rgba(0,0,0,.55))}
  .art{filter:drop-shadow(0 18px 34px rgba(0,0,0,.45)) drop-shadow(0 2px 0 rgba(255,255,255,.02))}
  .big{text-shadow:0 0 46px rgba(56,217,232,.16), 0 6px 24px rgba(0,0,0,.5)}
  .kicker{letter-spacing:.34em;text-shadow:0 0 22px rgba(56,217,232,.25)}
  .ann{filter:drop-shadow(0 18px 40px rgba(0,0,0,.5))}
  .ann .badge circle{fill:#f5d547;stroke:rgba(8,10,12,.85);stroke-width:3}
  .ann .badge text{fill:#0a0d10;font-size:20px;font-weight:700;letter-spacing:0}
  .ann .legrow circle{fill:#f5d547}
  .ann .legrow text{fill:#0a0d10;font-size:16px;font-weight:700}
  .ann .legtxt{fill:#e9eef2!important;font-size:26px;letter-spacing:.14em;font-weight:400}
  .annlabel line{stroke:rgba(237,234,227,.55);stroke-width:1.5}
  .annlabel .dot{fill:#f5d547;filter:drop-shadow(0 0 8px rgba(245,213,71,.9))}


  
  .spin{transform-box:fill-box;transform-origin:center;animation:spin 2.6s linear infinite}
  @keyframes spin{to{transform:rotate(360deg)}}
  .float{animation:bob 5s ease-in-out infinite}
  @keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
  .pulse{animation:pl 1.8s ease-in-out infinite}
  @keyframes pl{0%,100%{opacity:1}50%{opacity:.45}}
"""


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "csv=p=0", p], capture_output=True, text=True).stdout)


async def record(W, work):
    os.makedirs(work, exist_ok=True)
    words, files = [], []
    for i, w in enumerate(W, 1):
        raw = os.path.join(work, f"r{i}.mp3"); wav = os.path.join(work, f"n{i}.wav")
        buf, ws = bytearray(), []
        for attempt in range(5):
            try:
                c = edge_tts.Communicate(w["vo"], VOICE, rate=RATE, boundary="WordBoundary")
                buf, ws = bytearray(), []
                async for ch in c.stream():
                    if ch["type"] == "audio":
                        buf += ch["data"]
                    elif ch["type"] == "WordBoundary":
                        ws.append((ch["offset"] / 1e7, ch["text"]))
                if buf:
                    break
            except Exception as e:
                if attempt == 4:
                    raise
                await asyncio.sleep(2 + attempt * 2)
        open(raw, "wb").write(bytes(buf))
        o = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", raw, "-af",
                            "silencedetect=noise=-45dB:d=0.05", "-f", "null", "-"],
                           capture_output=True, text=True).stderr
        e = re.findall(r"silence_end: ([0-9.]+)", o)
        lead = float(e[0]) if e else 0.0
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", raw,
                        "-af", "silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,"
                               "areverse,silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,areverse",
                        "-ar", "44100", "-ac", "1", "-c:a", "pcm_s16le", wav], check=True)
        words.append([(max(0.0, x - lead + 0.04), t) for x, t in ws])
        files.append(wav)
        os.remove(raw)
    return words, files


def phrase_time(text, ws, phrase):
    p = text.lower().find(phrase.lower())
    if p < 0: raise ValueError(f"cue not in script: {phrase!r}")
    low, cur = text.lower(), 0
    for t, w in ws:
        wl = w.lower().strip(".,;:!?\"'()")
        i = low.find(wl, cur) if wl else -1
        if i < 0: i = cur
        else: cur = i + len(wl)
        if i >= p: return t
    return ws[-1][0]


def build(W, NAME, RATE="-30%"):
    globals()["RATE"] = RATE
    work = os.path.join(ROOT, "build", NAME)
    words, files = asyncio.run(record(W, work))
    g = os.path.join(work, "g.wav")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "lavfi",
                    "-i", "anullsrc=r=44100:cl=mono", "-t", str(GAP), "-c:a", "pcm_s16le", g], check=True)
    tail = os.path.join(work, "t.wav")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "lavfi",
                    "-i", "anullsrc=r=44100:cl=mono", "-t", str(TAIL), "-c:a", "pcm_s16le", tail], check=True)
    seq = []
    for i, f in enumerate(files):
        seq.append(f)
        if i < len(files) - 1: seq.append(g)
    seq.append(tail)
    lst = os.path.join(work, "l.txt")
    with open(lst, "w") as fh:
        for p in seq: fh.write(f"file '{p.replace(chr(92),'/')}'\n")
    vo = os.path.join(work, "vo.mp3")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat",
                    "-safe", "0", "-i", lst, "-c:a", "libmp3lame", "-b:a", "160k", vo], check=True)

    d = [dur(f) for f in files]
    starts, acc = [], 0.0
    for x in d:
        starts.append(acc); acc += x + GAP
    total = sum(d) + GAP * (len(d) - 1) + TAIL

    css = open(os.path.join(ROOT, "core", "byte.css"), encoding="utf-8").read().replace('url("fonts/', 'url("core/fonts/')
    pcss = open(os.path.join(ROOT, "core", "player.css"), encoding="utf-8").read()
    pjs = open(os.path.join(ROOT, "core", "player.js"), encoding="utf-8").read()

    secs = []
    for i, w in enumerate(W):
        h = render(w, i)
        toks = re.findall(r'data-in="@(\w+)@"', h)
        # every reveal lands on a real spoken word, spread in document order
        ws = [t for t, _ in words[i]] or [0.0]
        n = max(1, len(toks))
        times = []
        # the first two elements are the composition itself (art / kicker / first
        # row): they must be on screen immediately or the window looks empty
        lead = [0.12, 0.34]
        for k in range(n):
            if k < len(lead):
                times.append(lead[k])
                continue
            j = k - len(lead)
            idx = min(len(ws) - 1, int((j + 0.5) * len(ws) / max(1, n - len(lead))))
            times.append(max(lead[-1] + 0.2, min(ws[idx] - 0.06, d[i] - 0.12)))
        seq = iter(times)
        h = re.sub(r'data-in="@(\w+)@"', lambda m: 'data-in="%.2f"' % next(seq), h)
        secs.append(f'  <section class="scene" data-scene="{i}">\n{h}\n  </section>')

    vo_n = os.path.join(work, "vo_master.mp3")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", vo,
                    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11,volume=1.2dB",
                    "-c:a", "libmp3lame", "-b:a", "192k", vo_n], check=True)
    vo = vo_n
    b64 = base64.b64encode(open(vo, "rb").read()).decode()
    scenes_js = ",\n  ".join(f"{{s:{starts[i]:5.2f},  e:{starts[i]+d[i]:5.2f}}}" for i in range(len(d)))
    html = f"""<!DOCTYPE html><html lang="en" class="no-js"><head><meta charset="utf-8">
<title>Your 24GB Card Cannot Do 128K</title><style>
{css}
{pcss}
{EXTRA_CSS}
  .no-js #start{{display:none!important}}
</style></head><body>
<script>document.documentElement.classList.remove("no-js");</script>
<div id="wrap"><div id="stage">
{chr(10).join(secs)}
</div></div>
<script>
window.EPISODE = {{
  kicker: "Byte Forensics", title: "Your 24GB Card Cannot Do 128K",
  subtitle: "measured VRAM, window by window", total: {total:.2f}, maxGap: 20.0,
  vo: "data:audio/mpeg;base64,{b64}", sfxBase: "audio/",
  labels: {[f"'W{k+1:02d}'" for k in range(len(W))]},
  scenes: [
  {scenes_js}
  ], wipes: [], wipeColors: [], sfx: []
}};
</script><script>{pjs}</script></body></html>"""
    out = os.path.join(ROOT, NAME + ".html")
    open(out, "w", encoding="utf-8").write(html)
    print(f"wrote {out}  {total:.1f}s  windows={len(W)}  ({len(html)//1024} KB)")

    def ts(t):
        h = int(t // 3600); m = int(t % 3600 // 60); sec = int(t % 60)
        ms = int(round((t - int(t)) * 1000))
        if ms == 1000: ms = 0; sec += 1
        return f"{h:02d}:{m:02d}:{sec:02d},{ms:03d}"

    lines, n = [], 1
    for i, w in enumerate(W):
        ws = words[i]
        for j in range(0, len(ws), 8):
            grp = ws[j:j+8]
            t0 = starts[i] + grp[0][0]
            t1 = starts[i] + (ws[j+8][0] if j+8 < len(ws) else d[i])
            vw = w["vo"].split()
            txt = " ".join(vw[j:j+8]) if len(vw) == len(ws) else " ".join(x for _, x in grp)
            lines.append(f"{n}\n{ts(t0)} --> {ts(t1)}\n{txt}\n")
            n += 1
    srt = os.path.join(ROOT, NAME + ".srt")
    open(srt, "w", encoding="utf-8").write("\n".join(lines))
    print(f"wrote {srt}  ({n-1} captions)")

    chap = []
    for i, w in enumerate(W):
        t = starts[i]
        chap.append(f"{int(t//60)}:{int(t%60):02d} {w.get('kicker') or w['layout'].title()} {i+1:02d}")
    cp = os.path.join(ROOT, NAME + "-chapters.txt")
    open(cp, "w", encoding="utf-8").write("\n".join(chap))
    print(f"wrote {cp}  ({len(chap)} chapters)")
    for i, x in enumerate(d):
        if x > 20: print(f"   window {i+1} is {x:.1f}s")


if __name__ == "__main__":
    import importlib
    mod = importlib.import_module(sys.argv[1])
    build(mod.W, mod.NAME)
