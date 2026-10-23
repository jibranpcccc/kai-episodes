"""Full episode, A-style: every window gets its own layout and diagram."""
import asyncio, base64, os, re, subprocess

import edge_tts

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
VOICE = "en-US-AndrewNeural"
RATE = "-30%"
GAP = 0.32
TAIL = 2.0
NAME = "BYTE-03-A"

GPU = open(os.path.join(ROOT, "data", "art_gpu.svg"), encoding="utf-8").read()
CHIP = ('<svg viewBox="0 0 240 240" class="art"><rect x="58" y="58" width="124" height="124" rx="14" '
        'fill="rgba(255,255,255,.025)" stroke="rgba(237,234,227,.85)" stroke-width="2"/>'
        '<rect x="88" y="88" width="64" height="64" rx="8" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.4)" stroke-width="1.5"/>'
        '<g class="spin"><rect x="106" y="106" width="28" height="28" rx="5" fill="rgba(180,227,61,.9)"/></g>'
        '<g stroke="rgba(237,234,227,.45)" stroke-width="1.5"><path d="M78 58V34M98 58V34M118 58V34M138 58V34M158 58V34"/>'
        '<path d="M78 182v24M98 182v24M118 182v24M138 182v24M158 182v24"/>'
        '<path d="M58 78H34M58 98H34M58 118H34M58 138H34M58 158H34"/>'
        '<path d="M182 78h24M182 98h24M182 118h24M182 138h24M182 158h24"/></g></svg>')
LAPTOP = ('<svg viewBox="0 0 380 250" class="art"><rect x="54" y="24" width="272" height="170" rx="12" '
          'fill="rgba(255,255,255,.025)" stroke="rgba(237,234,227,.85)" stroke-width="2"/>'
          '<path d="M20 212H360L334 190H46Z" fill="rgba(255,255,255,.02)" stroke="rgba(237,234,227,.85)" stroke-width="2"/>'
          '<rect x="78" y="50" width="146" height="14" rx="4" fill="rgba(180,227,61,.85)"/>'
          '<rect x="78" y="80" width="216" height="9" rx="4" fill="rgba(237,234,227,.22)"/>'
          '<rect x="78" y="99" width="188" height="9" rx="4" fill="rgba(237,234,227,.22)"/>'
          '<rect x="78" y="118" width="204" height="9" rx="4" fill="rgba(237,234,227,.22)"/>'
          '<rect x="78" y="144" width="118" height="10" rx="4" fill="rgba(245,213,71,.8)"/></svg>')


RAM = ('<svg viewBox="0 0 460 140" class="art">'
       '<rect x="10" y="30" width="440" height="80" rx="8" fill="rgba(255,255,255,.025)" '
       'stroke="rgba(237,234,227,.85)" stroke-width="2"/>'
       '<rect x="30" y="46" width="56" height="48" rx="4" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.45)" stroke-width="1.2"/>'
       '<rect x="96" y="46" width="56" height="48" rx="4" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.45)" stroke-width="1.2"/>'
       '<rect x="162" y="46" width="56" height="48" rx="4" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.45)" stroke-width="1.2"/>'
       '<rect x="228" y="46" width="56" height="48" rx="4" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.45)" stroke-width="1.2"/>'
       '<rect x="294" y="46" width="56" height="48" rx="4" fill="rgba(180,227,61,.85)"/>'
       '<rect x="360" y="46" width="56" height="48" rx="4" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.45)" stroke-width="1.2"/>'
       '<rect x="24" y="104" width="196" height="10" rx="3" fill="rgba(245,213,71,.7)"/>'
       '<rect x="46" y="104" width="7" height="10" fill="rgba(0,0,0,.65)"/>'
       '<rect x="72" y="104" width="7" height="10" fill="rgba(0,0,0,.65)"/>'
       '<rect x="98" y="104" width="7" height="10" fill="rgba(0,0,0,.65)"/>'
       '<rect x="124" y="104" width="7" height="10" fill="rgba(0,0,0,.65)"/>'
       '</svg>')

SLOT = ('<svg viewBox="0 0 480 200" class="art">'
        '<rect x="20" y="30" width="440" height="140" rx="10" fill="rgba(255,255,255,.02)" '
        'stroke="rgba(237,234,227,.55)" stroke-width="2"/>'
        '<rect x="44" y="86" width="392" height="34" rx="6" fill="rgba(0,0,0,.4)" '
        'stroke="rgba(237,234,227,.7)" stroke-width="2"/>'
        '<g fill="rgba(245,213,71,.8)">'
        '<rect x="60" y="96" width="14" height="14" rx="2"/><rect x="88" y="96" width="14" height="14" rx="2"/>'
        '<rect x="116" y="96" width="14" height="14" rx="2"/><rect x="144" y="96" width="14" height="14" rx="2"/>'
        '<rect x="172" y="96" width="14" height="14" rx="2"/><rect x="200" y="96" width="14" height="14" rx="2"/>'
        '<rect x="228" y="96" width="14" height="14" rx="2"/><rect x="256" y="96" width="14" height="14" rx="2"/></g>'
        '<rect x="300" y="96" width="120" height="14" rx="4" fill="rgba(237,234,227,.25)"/>'
        '<rect x="60" y="46" width="150" height="10" rx="3" fill="rgba(56,217,232,.75)"/>'
        '<rect x="240" y="46" width="90" height="10" rx="3" fill="rgba(237,234,227,.2)"/>'
        '<text x="60" y="152" class="small">PCIE &middot; 16 LANES</text>'
        '</svg>')

CACHE = ('<svg viewBox="0 0 420 260" class="art">'
         '<rect x="20" y="20" width="380" height="220" rx="10" fill="rgba(255,255,255,.02)" '
         'stroke="rgba(237,234,227,.5)" stroke-width="1.5"/>'
         '<text x="34" y="46" class="small">KEY</text><text x="200" y="46" class="small">VALUE</text>'
         + "".join(
             f'<rect x="{34+j*86}" y="{62+k*44}" width="34" height="30" rx="4" '
             f'fill="{"rgba(245,213,71,.85)" if (j+k)%3==0 else "rgba(237,234,227,.10)"}"/>'
             f'<rect x="{200+j*48}" y="{62+k*44}" width="34" height="30" rx="4" '
             f'fill="{"rgba(180,227,61,.85)" if (j+k)%2==0 else "rgba(237,234,227,.10)"}"/>'
             for k in range(4) for j in range(2))
         + '</svg>')

W = []


def win(layout, vo, cues, **data):
    W.append(dict(layout=layout, vo=vo, cues=cues, **data))


def cues_of(*pairs):
    return {k: v for k, v in pairs}


# ── 01 hook ────────────────────────────────────────────────────────────────
win("stat", "A twenty-four gigabyte card. A two hundred and fifty-six K window. Those two numbers are supposed to be incompatible, and for one model they are. Nightly, the two get confused, and the bill arrives later.",
    {"a": "twenty-four gigabyte", "b": "two hundred and fifty-six", "t": "incompatible"},
    art=GPU, big=[("24", "GB", "var(--cyan)"), ("256", "K", "var(--lime)")],
    labels=["your card", "the window"], tape="context is not free")

# ── 02 callout ─────────────────────────────────────────────────────────────
win("callout", "Look at the card itself. The fan keeps it alive. The memory chips hold the model. And the slot is the only path in and out. None of those three parts is what the model file decides.",
    {"f": "The fan", "m": "memory chips", "s": "the slot"},
    art=GPU, marks=[("fan · cooling", "lt"), ("memory · the model", "rt"), ("slot · the bus", "lb")])

# ── 03 stat pair ───────────────────────────────────────────────────────────
win("pair", "Two model files. Sixteen point six eight gigabytes for Qwen. Fourteen point seven eight for Glimmer. The bigger model is the smaller file. Read that twice, because it breaks the rule everyone repeats.",
    {"l": "Two model files", "a": "Sixteen point six eight", "b": "Fourteen point seven eight", "t": "smaller file"},
    art=GPU, pair=[("Qwen 3.8 27B", "16.68 GiB", "var(--dim)"), ("Glimmer 30B", "14.78 GiB", "var(--lime)")],
    tape="bigger model, smaller file")

# ── 04 list ────────────────────────────────────────────────────────────────
win("list", "Two things live in your VRAM. The weights, a fixed file you download once. And the cache, which grows with every single token you give it. One is a constant you can see before you download anything.",
    {"k": "Two things", "a": "The weights", "b": "the cache"},
    art=CHIP, rows=[("WEIGHTS", "fixed file", "good"), ("KV CACHE", "grows every token", "hot")],
    kicker="what actually lives in vram")

# ── 05 chart ───────────────────────────────────────────────────────────────
win("chart", "Here is the measured memory as the window opens. Sixteen gigabytes at four K. Twenty six at one twenty-eight. And thirty four at two fifty-six. Every one of those numbers came from the same card.",
    {"k": "measured memory", "a": "Sixteen gigabytes", "b": "Twenty six", "c": "thirty four"},
    bars=[("4K", "16 GB", 47, "var(--lime)"), ("128K", "26 GB", 76, "var(--yellow)"), ("256K", "34 GB", 100, "var(--red)")],
    kicker="vram by context length", note="measured, not calculated")

# ── 06 table ───────────────────────────────────────────────────────────────
win("table", "The curve, first half. Four K, sixteen against eighteen. Thirty-two K, sixteen against twenty. Both fit a twenty-four gigabyte card with room to spare, and this is where every tutorial stops.",
    {"k": "The curve, first half", "r0": "Four K", "r1": "Thirty-two K"},
    rows=[("4K", "16", "18", "good"), ("32K", "16", "20", "good")],
    kicker="glimmer vs qwen")

win("table", "Second half. Sixty-four K, seventeen against twenty-two. Two fifty-six K, twenty against thirty-four. That last row is where the twenty-four gigabyte card runs out of room.",
    {"k": "Second half", "r0": "Sixty-four K", "r1": "two fifty-six K"},
    rows=[("64K", "17", "22", "hot"), ("256K", "20", "34", "hot")],
    kicker="where it breaks")

# ── 07 quote ───────────────────────────────────────────────────────────────
win("quote", "So the line is not the model. The line is the window. On a twenty-four gigabyte card, two fifty-six K fits one model and breaks the other. That is the single sentence worth taking from this video.",
    {"a": "the line is not the model", "b": "The line is the window", "t": "two fifty-six K fits"},
    line="The line is the window, not the model.", accent="var(--lime)", tape="24 GB is the line")

# ── 08 callout cache ───────────────────────────────────────────────────────
win("callout", "Every token writes a key matrix and a value matrix into memory. Those matrices do not care how many parameters the model has. They care how long your context is. They scale with context, not with parameter count.",
    {"k": "Every token", "a": "key matrix", "b": "how long your context"},
    art=CACHE, marks=[("key matrix", "lt"), ("value matrix", "rt"), ("context length", "lb")])

# ── 09 stat gap ────────────────────────────────────────────────────────────
win("stat", "The file difference was two gigabytes. At two fifty-six K the cache difference is fourteen. That is the entire argument, in two numbers. The cache did the rest while nobody was looking.",
    {"a": "two gigabytes", "b": "fourteen", "t": "entire argument"},
    art=RAM, big=[("2", "GB", "var(--dim)"), ("14", "GB", "var(--red)")],
    labels=["file difference", "cache difference"], tape="the file was never the problem")

# ── 10 list myths ──────────────────────────────────────────────────────────
win("list", "Three myths. More parameters does not mean more memory. A bigger number on the box does not mean a better experience. And a faster card does not fix a capacity problem. Each one is the reason somebody buys the wrong card.",
    {"k": "Three myths", "a": "More parameters", "b": "A bigger number", "c": "a faster card"},
    art=CHIP, rows=[("PARAMETERS", "not memory", "hot"), ("BOX NUMBERS", "not experience", "hot"), ("FASTER CARD", "not capacity", "hot")],
    kicker="all three are false")

# ── 11 pair cards ──────────────────────────────────────────────────────────
win("pair", "Both cards are twenty-four gigabytes. A three thousand ninety and a five-oh-ninety hold exactly the same model, the same file, and the same window.",
    {"l": "Both cards", "a": "three thousand ninety", "b": "five-oh-ninety", "t": "same window"},
    art=GPU, pair=[("RTX 3090", "24 GB", "var(--dim)"), ("RTX 5090", "24 GB", "var(--cyan)")],
    tape="same memory")

# ── 12 chart speed ─────────────────────────────────────────────────────────
win("chart", "What changes is speed. Forty-five tokens a second on the three thousand ninety. Eighty-three on the five-oh-ninety. Twice the speed, and not one extra gigabyte.",
    {"k": "What changes is speed", "a": "Forty-five tokens", "b": "Eighty-three", "n": "not one extra gigabyte"},
    bars=[("3090 · 4K", "45.3", 54, "var(--lime)"), ("5090 · 4K", "83.2", 100, "var(--cyan)")],
    kicker="tokens per second", note="same 24 GB")

# ── 13 quote ───────────────────────────────────────────────────────────────
win("quote", "Speed is not capacity. If the model does not fit, a faster card does not make it fit. It just runs out of memory more quickly.",
    {"a": "Speed is not capacity", "b": "does not make it fit", "t": "runs out of memory"},
    line="Speed is not capacity.", accent="var(--yellow)", tape="a faster card does not fix capacity")

# ── 14 list options ────────────────────────────────────────────────────────
win("list", "So what works? Option one, the model with the smaller cache. Option two, sixty-four K and plan around it. Option three, quantize harder and lose quality.",
    {"k": "So what works", "a": "Option one", "b": "Option two", "c": "Option three"},
    art=GPU, rows=[("SMALLER CACHE", "full window", "good"), ("64K CEILING", "plan around it", "hot"), ("QUANTIZE HARDER", "quality loss", "hot")],
    kicker="three real options")

# ── 15 callout quant ───────────────────────────────────────────────────────
win("callout", "Quantization is the escape hatch. Four-bit becomes three-bit or two-bit, the file shrinks, and the cache shrinks with it. You fit more, and you get a worse model.",
    {"k": "Quantization", "a": "the file shrinks", "b": "worse model"},
    art=CHIP, marks=[("4-bit", "lt"), ("3-bit", "rt"), ("quality cost", "lb")])

# ── 16 pair two cards ──────────────────────────────────────────────────────
win("pair", "Two sixteen gigabyte cards give you thirty-two gigabytes. One three thousand ninety gives you twenty-four. On paper the pair wins, and on paper is where it ends.",
    {"l": "Two sixteen gigabyte", "a": "thirty-two gigabytes", "b": "twenty-four", "t": "on paper"},
    art=SLOT, pair=[("2 × 5060 Ti", "32 GB", "var(--orange)"), ("1 × 3090", "24 GB", "var(--lime)")],
    tape="on paper it wins")

# ── 17 chart two cards ─────────────────────────────────────────────────────
win("chart", "In practice, twenty-two tokens a second for the pair. Fifteen at one twenty-eight K. Against forty-five and thirty-eight from the single card.",
    {"k": "In practice", "a": "twenty-two tokens", "b": "fifteen", "c": "forty-five"},
    bars=[("2 cards · 4K", "22.5", 50, "var(--orange)"), ("2 cards · 128K", "15.6", 35, "var(--red)"),
          ("1 card · 128K", "38.1", 84, "var(--lime)")],
    kicker="tokens per second", note="measured")

# ── 18 quote ───────────────────────────────────────────────────────────────
win("quote", "Two cards buy capacity, not speed. Every layer boundary crosses a bus, and every batch waits for the slowest half.",
    {"a": "buy capacity", "b": "crosses a bus", "t": "slowest half"},
    line="Two cards buy capacity, not speed.", accent="var(--orange)", tape="the bus is the cost")

# ── 19 table machines ──────────────────────────────────────────────────────
win("table", "Three machines, one model. The three thousand ninety does forty-five. The M5 Max does thirty-one. The small unified box does twelve.",
    {"k": "Three machines", "r0": "three thousand ninety", "r1": "M5 Max", "r2": "unified box"},
    rows=[("3090 · 4K", "45.3", "24 GB", "good"), ("M5 Max · 4K", "31.4", "128 GB", "hot"), ("GB10 · 4K", "12.2", "128 GB", "hot")],
    kicker="same model, three machines")

# ── 20 stat prefill ────────────────────────────────────────────────────────
win("stat", "And the number nobody publishes. Prefill, the wait before the first word. Fourteen hundred tokens a second at four K, down to five hundred and eighty-four at two fifty-six.",
    {"a": "Prefill", "b": "Fourteen hundred", "c": "five hundred and eighty-four"},
    art=CHIP, big=[("1477", "t/s", "var(--lime)"), ("584", "t/s", "var(--red)")],
    labels=["4K prompt", "256K prompt"], tape="the wait before the first word")

# ── 21 chart prefill ───────────────────────────────────────────────────────
win("chart", "On the same card, Qwen prefills a four K prompt at thirteen hundred and eight. At sixty-four K it is seven hundred and seventeen. That is the fall.",
    {"k": "On the same card", "a": "thirteen hundred and eight", "b": "seven hundred and seventeen"},
    bars=[("Qwen · 4K", "1,308", 100, "var(--cyan)"), ("Qwen · 64K", "717", 55, "var(--red)")],
    kicker="prefill, tokens per second", note="measured")

# ── 22 quote ───────────────────────────────────────────────────────────────
win("quote", "Turn it into time. A hundred thousand token prompt is twenty-two seconds on one setup and three and a half minutes on another. That is the difference between an assistant and a loading screen.",
    {"a": "twenty-two seconds", "b": "three and a half minutes", "t": "loading screen"},
    line="22 seconds, or 3½ minutes.", accent="var(--red)", tape="same prompt, same card")

# ── 23 list caveats ────────────────────────────────────────────────────────
win("list", "Three honest caveats. The quantization levels are different. These are hardware measurements, not quality measurements. And the agentic claims are not independently benchmarked.",
    {"k": "Three honest caveats", "a": "quantization levels", "b": "hardware measurements", "c": "agentic claims"},
    art=CHIP, rows=[("01", "different quantization", "hot"), ("02", "hardware, not quality", "hot"), ("03", "agentic: unconfirmed", "hot")],
    kicker="read these")

# ── 24 callout desktop ─────────────────────────────────────────────────────
win("callout", "One thing no benchmark includes is your desktop. The compositor wants memory. The browser wants memory. Two monitors take more. Leave a gigabyte, ideally two.",
    {"k": "your desktop", "a": "The compositor", "b": "Leave a gigabyte"},
    art=LAPTOP, marks=[("compositor", "lt"), ("browser", "rt"), ("two monitors", "lb")])

# ── 25 stat usable ─────────────────────────────────────────────────────────
win("stat", "So twenty-four is really twenty-two. Plan for that number and the model fits. Plan for twenty-four and you will meet the cliff at the worst possible moment.",
    {"a": "twenty-two", "b": "the cliff", "t": "worst possible moment"},
    art=GPU, big=[("24", "GB", "var(--dim)"), ("22", "GB", "var(--lime)")],
    labels=["on the box", "usable"], tape="plan for 22")

# ── 26 list order ──────────────────────────────────────────────────────────
win("list", "The order of operations is simple. Pick the window you actually need. Find the model that fits it. Then buy the fastest card with that much memory.",
    {"k": "The order of operations", "a": "Pick the window", "b": "Find the model", "c": "buy the fastest card"},
    art=GPU, rows=[("01", "pick the window", "good"), ("02", "find the model", "good"), ("03", "buy the card", "good")],
    kicker="in that order")

# ── 27 quote close ─────────────────────────────────────────────────────────
win("quote", "So stop shopping by parameter count. Shop by the file, the cache, and the context you actually use. Those three numbers are on the page. The parameter count tells you the least.",
    {"a": "stop shopping", "b": "the file, the cache", "t": "tells you the least"},
    line="Shop by the window, not the model.", accent="var(--lime)", tape="file · cache · context")

# ── 28 end ─────────────────────────────────────────────────────────────────
win("stat", "Full numbers are in the description, including the ones I did not put on screen. Next episode, the two-card route in detail. Subscribe if you want it when it lands.",
    {"a": "Full numbers", "b": "Next episode", "c": "Subscribe"},
    art=GPU, big=[("→", "", "var(--lime)")], labels=["next: the two-card route"], tape="byte forensics")


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
        specs = [
            (150, 158, 330, 196, 56, 150, w["marks"][0][0], "start"),
            (852, 214, 690, 238, 940, 206, w["marks"][1][0], "end"),
            (150, 398, 320, 392, 56, 428, w["marks"][2][0], "start"),
        ]
        groups = ""
        for key, (x1, y1, x2, y2, tx, ty, label, anchor) in zip(["f", "m", "s"], specs):
            groups += (f'<g data-in="@{key}@" class="annlabel">'
                       f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>'
                       f'<circle cx="{x2}" cy="{y2}" r="5" class="dot"/>'
                       f'<text x="{tx}" y="{ty}" text-anchor="{anchor}">{label.upper()}</text></g>')
        return (f'<div class="stagewrap"><svg class="ann" viewBox="0 0 1000 520">'
                f'<svg x="250" y="110" width="500" height="310" viewBox="{vb}" '
                f'preserveAspectRatio="xMidYMid meet">{inner}</svg>{groups}</svg></div>')

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
  .ann{display:block;width:1240px;height:auto;overflow:visible}
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
  .art{display:block;width:100%;height:auto}
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


async def record(work):
    os.makedirs(work, exist_ok=True)
    words, files = [], []
    for i, w in enumerate(W, 1):
        raw = os.path.join(work, f"r{i}.mp3"); wav = os.path.join(work, f"n{i}.wav")
        c = edge_tts.Communicate(w["vo"], VOICE, rate=RATE, boundary="WordBoundary")
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


def build():
    work = os.path.join(ROOT, "build", NAME)
    words, files = asyncio.run(record(work))
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
        def sub(m, i=i, w=w):
            key = m.group(1)
            if key == "cap": return 'data-in="0.15"'
            if key in w["cues"]:
                phrase = w["cues"][key]
                t = phrase_time(w["vo"], words[i], phrase)
                return 'data-in="%.2f"' % max(0.05, min(t - 0.08, d[i] - 0.12))
            if key.startswith("s") and key[1:].isdigit():
                j = int(key[1:]); key2 = ["a", "b", "c"][j] if j < 3 else "a"
                phrase = w["cues"].get(key2)
            elif key.startswith("p"):
                j = int(key[1:]); phrase = w["cues"].get(["l", "a", "b"][j])
            elif key.startswith("b"):
                j = int(key[1:]); phrase = w["cues"].get(["k", "a", "b", "c"][j])
            elif key.startswith("r"):
                j = int(key[1:]); phrase = w["cues"].get(["r0", "r1", "r2", "r3"][j])
            else:
                phrase = w["cues"].get(key)
            if phrase is None:
                return 'data-in="0.3"'
            t = phrase_time(w["vo"], words[i], phrase)
            return 'data-in="%.2f"' % max(0.05, min(t - 0.08, d[i] - 0.12))
        h = re.sub(r'data-in="@(\w+)@"', sub, h)
        secs.append(f'  <section class="scene" data-scene="{i}">\n{h}\n  </section>')

    vo_n = os.path.join(work, "vo_norm.mp3")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", vo,
                    "-af", "volume=6.4dB,alimiter=level_in=1:level_out=1:limit=0.80:attack=5:release=60",
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
    build()
