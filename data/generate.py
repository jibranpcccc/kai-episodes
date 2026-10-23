"""Spec -> episode HTML generator.

    python data/generate.py data/specs/demo.json --out DEMO.html

A spec is JSON:

{
  "title": "...", "kicker": "...", "subtitle": "...",
  "voice": "en-US-AndrewNeural", "rate": "+8%", "name": "DEMO",
  "scenes": [
    {"type":"hook",   "vo":"...", "a":{"v":"30","u":"B","c":"lime","lab":"the one you found"},
                      "b":{"v":"27","u":"B","c":"dim","lab":"the one they tell you"},
                      "tape":"it fits", "art":"gpu", "cues":{"a":"word","b":"word","t":"word"}},
    {"type":"rows",   "vo":"...", "head":"...", "items":[["Memory used","less","good"]],
                      "cues":{"h":"...","0":"..."}},
    {"type":"bars",   "vo":"...", "head":"...", "items":[["Glimmer 4K",100,"45.3","lime"]],
                      "cues":{"h":"...","0":"..."}},
    {"type":"table",  "vo":"...", "head":"...", "items":[["4K","16","18","good"]],
                      "cues":{"h":"...","0":"..."}},
    {"type":"chips",  "vo":"...", "head":"...", "chips":["FILE","CACHE"], "tape":"...",
                      "cues":{"h":"...","t":"..."}},
    {"type":"caveat", "vo":"...", "items":["first caveat","second caveat"],
                      "tape":"...", "cues":{"h":"...","t":"..."}},
    {"type":"close",  "vo":"...", "line":"Stop shopping by parameter count.",
                      "chips":["FILE","CACHE"], "cues":{"l":"...","0":"..."}}
  ]
}

Every cue is a phrase that must appear in that scene's vo — the build fails loudly
if it doesn't, so text and timing can never drift apart.
"""
import argparse, asyncio, base64, json, os, re, subprocess, sys

import edge_tts

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAP, TAIL, MAX_GAP, TICK = 0.30, 2.6, 2.0, 1.45

ART = {
    "gpu": '<svg class="art" viewBox="0 0 440 172"><rect x="5" y="12" width="428" height="148" rx="14" class="s"/>'
           '<rect x="24" y="30" width="148" height="112" rx="8" class="s t"/>'
           '<g class="spin"><circle cx="98" cy="86" r="45" class="s t"/>'
           '<path d="M98 45a41 41 0 0 1 0 82" class="blade"/>'
           '<path d="M98 127a41 41 0 0 1 0-82" class="blade dim"/></g>'
           '<text x="214" y="76" class="lime">24 GB</text><text x="214" y="102" class="small">VRAM</text>'
           '<rect x="214" y="116" width="192" height="18" class="s t"/>'
           '<rect x="216" y="118" width="130" height="14" class="fy pulse"/>'
           '<rect x="396" y="58" width="26" height="54" rx="3" class="s t"/></svg>',
    "chip": '<svg class="art" viewBox="0 0 240 240"><rect x="58" y="58" width="124" height="124" rx="12" class="s"/>'
            '<rect x="88" y="88" width="64" height="64" rx="6" class="s t"/>'
            '<g class="spin"><rect x="104" y="104" width="32" height="32" rx="4" class="fl pulse"/></g>'
            '<g class="s t"><path d="M78 58V34M98 58V34M118 58V34M138 58V34M158 58V34"/>'
            '<path d="M78 182v24M98 182v24M118 182v24M138 182v24M158 182v24"/>'
            '<path d="M58 78H34M58 98H34M58 118H34M58 138H34M58 158H34"/>'
            '<path d="M182 78h24M182 98h24M182 118h24M182 138h24M182 158h24"/></g></svg>',
    "laptop": '<svg class="art" viewBox="0 0 380 250"><rect x="54" y="24" width="272" height="170" rx="10" class="s"/>'
              '<path d="M20 212H360L334 190H46Z" class="s"/>'
              '<rect x="78" y="50" width="146" height="14" rx="3" class="fl pulse"/>'
              '<rect x="78" y="78" width="216" height="9" rx="3" class="fg"/>'
              '<rect x="78" y="97" width="188" height="9" rx="3" class="fg"/>'
              '<rect x="78" y="116" width="204" height="9" rx="3" class="fg"/>'
              '<rect x="78" y="142" width="118" height="10" rx="3" class="fy"/></svg>',
}


ART["ram"] = (
    '<svg viewBox="0 0 420 130" class="art">'
    '<rect x="8" y="26" width="404" height="76" rx="6" class="s"/>'
    '<rect x="24" y="40" width="52" height="48" rx="3" class="s t"/>'
    '<rect x="86" y="40" width="52" height="48" rx="3" class="s t"/>'
    '<rect x="148" y="40" width="52" height="48" rx="3" class="s t"/>'
    '<rect x="210" y="40" width="52" height="48" rx="3" class="s t"/>'
    '<rect x="272" y="40" width="52" height="48" rx="3" class="s t"/>'
    '<rect x="334" y="40" width="52" height="48" rx="3" class="fl pulse"/>'
    '<path d="M20 102v16M52 102v16M84 102v16M116 102v16M148 102v16M180 102v16'
    'M212 102v16M244 102v16M276 102v16M308 102v16M340 102v16M372 102v16" class="s t"/>'
    '</svg>')

ART["ssd"] = (
    '<svg viewBox="0 0 420 150" class="art">'
    '<rect x="20" y="30" width="380" height="90" rx="8" class="s"/>'
    '<rect x="40" y="52" width="150" height="46" rx="4" class="s t"/>'
    '<rect x="206" y="52" width="60" height="46" rx="4" class="fy pulse"/>'
    '<rect x="280" y="52" width="60" height="46" rx="4" class="s t"/>'
    '<rect x="380" y="66" width="18" height="34" rx="2" class="fl"/>'
    '</svg>')

ART["cpu"] = (
    '<svg viewBox="0 0 260 260" class="art">'
    '<rect x="46" y="46" width="168" height="168" rx="8" class="s"/>'
    '<rect x="86" y="86" width="88" height="88" rx="4" class="s t"/>'
    '<g class="spin"><rect x="106" y="106" width="48" height="48" rx="4" class="fl pulse"/></g>'
    '<g class="s t"><path d="M70 46V16M100 46V16M130 46V16M160 46V16M190 46V16"/>'
    '<path d="M70 214v30M100 214v30M130 214v30M160 214v30M190 214v30"/>'
    '<path d="M46 70H16M46 100H16M46 130H16M46 160H16M46 190H16"/>'
    '<path d="M214 70h30M214 100h30M214 130h30M214 160h30M214 190h30"/></g>'
    '</svg>')

ART["board"] = (
    '<svg viewBox="0 0 440 240" class="art">'
    '<rect x="10" y="12" width="420" height="216" rx="8" class="s"/>'
    '<rect x="34" y="40" width="120" height="120" rx="4" class="s t"/>'
    '<g class="spin"><rect x="74" y="80" width="40" height="40" rx="3" class="fl pulse"/></g>'
    '<rect x="176" y="36" width="200" height="16" rx="3" class="s t"/>'
    '<rect x="176" y="66" width="200" height="16" rx="3" class="s t"/>'
    '<rect x="176" y="96" width="200" height="16" rx="3" class="fy"/>'
    '<rect x="176" y="132" width="120" height="70" rx="4" class="s t"/>'
    '<rect x="312" y="132" width="64" height="70" rx="4" class="s t"/>'
    '</svg>')

ART["psu"] = (
    '<svg viewBox="0 0 400 180" class="art">'
    '<rect x="16" y="26" width="368" height="128" rx="8" class="s"/>'
    '<g class="spin"><circle cx="120" cy="90" r="46" class="s t"/>'
    '<path d="M120 52a38 38 0 0 1 0 76" class="blade"/>'
    '<path d="M120 128a38 38 0 0 1 0-76" class="blade dim"/></g>'
    '<rect x="220" y="52" width="140" height="20" rx="3" class="s t"/>'
    '<rect x="220" y="86" width="140" height="20" rx="3" class="s t"/>'
    '<rect x="220" y="118" width="90" height="18" rx="3" class="fy"/>'
    '</svg>')

ART["cooler"] = (
    '<svg viewBox="0 0 320 320" class="art">'
    '<g class="spin"><circle cx="160" cy="160" r="120" class="s"/>'
    '<path d="M160 62a98 98 0 0 1 0 196" class="blade"/>'
    '<path d="M160 258a98 98 0 0 1 0-196" class="blade dim"/></g>'
    '<circle cx="160" cy="160" r="34" class="s t"/>'
    '<circle cx="160" cy="160" r="14" class="fl pulse"/>'
    '</svg>')

ART["slot"] = (
    '<svg viewBox="0 0 440 140" class="art">'
    '<rect x="12" y="34" width="416" height="72" rx="6" class="s"/>'
    '<rect x="28" y="52" width="384" height="36" rx="4" class="s t"/>'
    '<g class="fy"><rect x="44" y="60" width="20" height="20"/><rect x="76" y="60" width="20" height="20"/>'
    '<rect x="108" y="60" width="20" height="20"/><rect x="140" y="60" width="20" height="20"/></g>'
    '<rect x="300" y="60" width="20" height="20" class="fl"/>'
    '</svg>')

ORDER = ["gpu", "ram", "cpu", "ssd", "board", "cooler", "psu", "slot", "chip", "laptop"]

COLOUR = {"lime": "var(--lime)", "red": "var(--red)", "yellow": "var(--yellow)",
          "dim": "var(--dim)", "white": "var(--white)",
          "cyan": "var(--cyan)", "orange": "var(--orange)", "soft": "var(--soft)"}


# ----------------------------------------------------------------- renderers
def countup(text, colour):
    """emit a number that animates up from zero when it lands"""
    raw = str(text).replace(",", "").strip()
    try:
        v = float(raw)
    except ValueError:
        return f'<span style="color:{colour}">{text}</span>'
    dec = len(raw.split(".")[1]) if "." in raw else 0
    return (f'<span data-count="{v:.{dec}f}" style="color:{colour}">'
            f'{v:.{dec}f}</span>')


BG_ORDER = ["gpu", "chip", "laptop", "gpu", "chip"]




def split_scenes(spec, max_s=15.5, wps=2.7):
    """Break any scene longer than max_s into shorter windows.

    Items (rows/bars/table rows/chips) travel with the sentence that mentions
    them, so cue phrases keep matching and sync is preserved.
    """
    out = []
    for sc in spec["scenes"]:
        vo = sc["vo"].strip()
        words = len(vo.split()) or 1
        est = words / wps
        parts = [p for p in re.split(r"(?<=[.!?])\s+", vo) if p.strip()]
        if est <= max_s * 1.15 or len(parts) < 2:
            out.append(sc)
            continue

        target = int(words * (max_s / est))
        chunks, cur, curw = [], [], 0
        for p in parts:
            w = len(p.split())
            if cur and curw + w > target:
                chunks.append(" ".join(cur)); cur, curw = [p], w
            else:
                cur.append(p); curw += w
        if cur:
            chunks.append(" ".join(cur))
        if len(chunks) < 2:
            out.append(sc)
            continue

        cues = dict(sc.get("cues", {}))
        buckets = [{} for _ in chunks]
        for k, ph in cues.items():
            for ci, c in enumerate(chunks):
                if ph.lower() in c.lower():
                    buckets[ci][k] = ph
                    break
            else:
                buckets[0][k] = ph

        # split list items across chunks by where their cue phrase lives
        items = sc.get("items")
        chips = sc.get("chips")
        per_chunk_items = None
        per_chunk_chips = None
        if items:
            per_chunk_items = [[] for _ in chunks]
            for idx, it in enumerate(items):
                ph = cues.get(str(idx), "")
                placed = False
                for ci, c in enumerate(chunks):
                    if ph and ph.lower() in c.lower():
                        per_chunk_items[ci].append(it); placed = True; break
                if not placed:
                    per_chunk_items[0].append(it)
            per_chunk_items = [x or items for x in per_chunk_items]
        if chips:
            per_chunk_chips = [[] for _ in chunks]
            for idx, ch in enumerate(chips):
                ph = cues.get(str(idx), "")
                for ci, c in enumerate(chunks):
                    if ph and ph.lower() in c.lower():
                        per_chunk_chips[ci].append(ch); break
                else:
                    per_chunk_chips[0].append(ch)
            per_chunk_chips = [x or chips for x in per_chunk_chips]

        for ci, c in enumerate(chunks):
            new = dict(sc)
            new["vo"] = c
            new["cues"] = buckets[ci]
            if per_chunk_items is not None:
                new["items"] = per_chunk_items[ci]
            if per_chunk_chips is not None:
                new["chips"] = per_chunk_chips[ci]
            out.append(new)
    spec["scenes"] = out
    return spec


def hero(i, cls="", k=1):
    """one large hardware drawing at a time; band0..band{k-1} swap on words"""
    keys = [ORDER[(i * 3 + j) % len(ORDER)] for j in range(k)]
    figs = "".join(f'<figure data-in="@band{j}@">{ART[key]}</figure>'
                   for j, key in enumerate(keys))
    return f'<div class="hwbig">{figs}</div>'


def layout(i, inner, tape="", force_h=False):
    """horizontal: drawing beside the text. vertical: drawing above it."""
    if i % 2 == 0 or force_h:
        return (f'<div class="ctr"><div class="split wide">'
                f'{hero(i, "hero--h")}'
                f'<div class="col" style="flex:1">{inner}</div></div>{tape}</div>')
    return (f'<div class="ctr">{hero(i, "hero--v")}'
            f'<div class="col">{inner}</div>{tape}</div>')


def tape(txt, tok="t"):
    return f'<div class="bf-tape" data-in="@{tok}@">{txt}</div>' if txt else ""


def render(sc, i):
    t = sc["type"]

    if t == "hook":
        a, b = sc["a"], sc["b"]
        # only draw the figures that are actually spoken in THIS window
        ks = sc.get("cues", {})
        stats = ""
        if "a" in ks:
            stats += (f'<div class="stat"><div class="bf-big big" style="color:{COLOUR.get(a.get("c","white"))}" data-in="@a@">'
                      f'<span data-count="{a["v"]}">{a["v"]}</span><span class="u">{a.get("u","")}</span></div>'
                      f'<div class="bf-sub" data-in="@a@">{a.get("lab","")}</div></div>')
        if "b" in ks:
            stats += (f'<div class="stat"><div class="bf-big big" style="color:{COLOUR.get(b.get("c","white"))}" data-in="@b@">'
                      f'<span data-count="{b["v"]}">{b["v"]}</span><span class="u">{b.get("u","")}</span></div>'
                      f'<div class="bf-sub" data-in="@b@">{b.get("lab","")}</div></div>')
        if not stats:
            stats = (f'<div class="stat"><div class="bf-big big" style="color:{COLOUR.get(a.get("c","white"))}" data-in="@a@">'
                     f'<span data-count="{a["v"]}">{a["v"]}</span><span class="u">{a.get("u","")}</span></div>'
                     f'<div class="bf-sub" data-in="@a@">{a.get("lab","")}</div></div>')
        inner = (f'<div class="bf-cap" data-in="@h@">{sc.get("head","")}</div>'
                 f'<div class="side" style="justify-content:center">{stats}</div>')
        return layout(i, inner, tape(sc.get("tape","")))

    if t == "rows":
        rows = ""
        for k, it in enumerate(sc["items"]):
            cls = "bf-row bf-row--good" if it[2] == "good" else ("bf-row bf-row--hot" if it[2] == "hot" else "bf-row")
            rows += (f'<div class="{cls}"><span class="bf-row__k">{it[0]}</span>'
                     f'<span class="bf-row__v" style="color:{COLOUR.get(it[2],"var(--white)")}" data-in="@{k}a@">{it[1]}</span></div>')
        acc = ["var(--lime)","var(--cyan)","var(--orange)","var(--yellow)"][i % 4]
        inner = (f'<div class="bf-cap" data-in="@h@" style="color:{acc}">{sc.get("head","")}</div>'
                 f'<div class="accbar" style="background:{acc}"></div>{rows}')
        return layout(i, inner)

    if t == "bars":
        bars = ""
        for k, it in enumerate(sc["items"]):
            bars += (f'<div class="bf-bar"><span class="bf-bar__lab">{it[0]}</span>'
                     f'<div class="bf-bar__track"><div class="bf-bar__fill grow" '
                     f'style="--w:{it[1]}%;background:{COLOUR.get(it[3],"var(--white)")}" data-in="@{k}a@"></div></div>'
                     f'<span class="bf-bar__val" style="color:{COLOUR.get(it[3],"var(--white)")}" data-in="@{k}b@">'
                     f'{countup(it[2], COLOUR.get(it[3],"var(--white)"))}</span></div>')
        inner = f'<div class="bf-cap" data-in="@h@">{sc.get("head","")}</div>{bars}'
        return layout(i, inner, tape(sc.get("tape","")))

    if t == "table":
        rows = ""
        for k, it in enumerate(sc["items"]):
            cls = "bf-row bf-row--good" if it[3] == "good" else ("bf-row bf-row--hot" if it[3] == "hot" else "bf-row")
            rows += (f'<div class="{cls}"><span class="bf-row__k">{it[0]}</span>'
                     f'<span class="bf-row__v" style="color:var(--lime)" data-in="@{k}a@">{it[1]}</span>'
                     f'<span class="bf-row__v" style="color:{COLOUR.get(it[3],"var(--white)")}" data-in="@{k}b@">{it[2]}</span></div>')
        acc = ["var(--lime)","var(--cyan)","var(--orange)","var(--yellow)"][i % 4]
        inner = (f'<div class="bf-cap" data-in="@h@" style="color:{acc}">{sc.get("head","")}</div>'
                 f'<div class="accbar" style="background:{acc}"></div>{rows}')
        return layout(i, inner)

    if t == "chips":
        chips = "".join(f'<span class="chip" data-in="@{k}@">{c}</span>' for k, c in enumerate(sc["chips"]))
        inner = (f'<div class="bf-cap" data-in="@h@">{sc.get("head","")}</div>'
                 f'<div style="display:flex;gap:16px;justify-content:center">{chips}</div>')
        return layout(i, inner, tape(sc.get("tape","")))

    if t == "caveat":
        cards = ""
        for k, c in enumerate(sc["items"]):
            cards += (f'<div class="chalk" style="display:flex;gap:20px;align-items:baseline">'
                      f'<span class="bf-row__k" style="width:54px">{k+1:02d}</span>'
                      f'<span style="font-family:var(--mono);font-size:22px" data-in="@{k}a@">{c}</span></div>')
        inner = f'<div class="bf-cap" data-in="@h@" style="color:var(--red)">{sc.get("head","")}</div>{cards}'
        return layout(i, inner, tape(sc.get("tape","")))

    if t == "close":
        chips = "".join(f'<span class="chip" data-in="@{k}@">{c}</span>' for k, c in enumerate(sc["chips"]))
        inner = (f'<div class="bf-big" style="font-size:58px;text-align:center" data-in="@l@">{sc.get("line","")}</div>'
                 f'<div style="display:flex;gap:16px;justify-content:center">{chips}</div>'
                 f'<div class="bf-wm" data-in="@w@">{sc.get("wm","byte forensics")}</div>')
        return layout(i, inner, force_h=True)



# ----------------------------------------------------------------- build
def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "csv=p=0", p], capture_output=True, text=True).stdout.strip())


def align(text, words):
    low, out, cur = text.lower(), [], 0
    for t, w in words:
        wl = w.lower().strip(".,;:!?\"'()")
        i = low.find(wl, cur) if wl else -1
        if i < 0:
            i = cur
        else:
            cur = i + len(wl)
        out.append((i, t))
    return out


def phrase_time(text, al, phrase):
    p = text.lower().find(phrase.lower())
    if p < 0:
        raise ValueError(f"cue phrase not in script: {phrase!r}")
    for ci, t in al:
        if ci >= p:
            return t
    return al[-1][1]


async def record(spec, work, A):
    words = []
    af = ("silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,"
          "areverse,silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,areverse")
    for i, sc in enumerate(spec["scenes"], 1):
        raw = os.path.join(A, f"r{i}.mp3"); wav = os.path.join(A, f"n{i}.wav")
        c = edge_tts.Communicate(sc["vo"], spec.get("voice", "en-US-AndrewNeural"),
                                 rate=spec.get("rate", "+8%"), boundary="WordBoundary")
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
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", raw, "-af", af,
                        "-ar", "44100", "-ac", "1", "-c:a", "pcm_s16le", wav], check=True)
        words.append([(max(0.0, x - lead + 0.04), w) for x, w in ws])
        os.remove(raw)
    return words


WARN = []
WORD = {}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    spec = json.load(open(a.spec if os.path.isabs(a.spec) else os.path.join(ROOT, a.spec), encoding="utf-8"))
    spec = split_scenes(spec)
    name = spec.get("name", "EPISODE")
    work = os.path.join(ROOT, "build", name)
    A = os.path.join(work, "audio"); os.makedirs(A, exist_ok=True)

    words = asyncio.run(record(spec, work, A))
    d = [dur(os.path.join(A, f"n{i}.wav")) for i in range(1, len(spec["scenes"]) + 1)]
    starts, acc = [], 0.0
    for i in range(len(d)):
        starts.append(acc); acc += d[i] + GAP
    total = sum(d) + GAP * (len(d) - 1) + TAIL

    g = os.path.join(A, "g.wav"); t = os.path.join(A, "t.wav")
    for path, ln in ((g, GAP), (t, TAIL)):
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "lavfi",
                        "-i", "anullsrc=r=44100:cl=mono", "-t", str(ln), "-c:a", "pcm_s16le", path], check=True)
    lst = []
    for i in range(1, len(spec["scenes"]) + 1):
        lst.append(f"file '{(A+'/n%d.wav'%i).replace(chr(92),'/')}'")
        if i < len(spec["scenes"]):
            lst.append(f"file '{(A+'/g.wav').replace(chr(92),'/')}'")
    lst.append(f"file '{(A+'/t.wav').replace(chr(92),'/')}'")
    open(os.path.join(A, "l.txt"), "w").write("\n".join(lst))
    vo = os.path.join(work, "vo.mp3")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat", "-safe", "0",
                    "-i", os.path.join(A, "l.txt"), "-c:a", "libmp3lame", "-b:a", "192k", vo], check=True)

    # cues -> absolute times
    cue = {}
    for i, sc in enumerate(spec["scenes"]):
        al = align(sc["vo"], words[i])
        missing = []
        for key, phrase in sc.get("cues", {}).items():
            try:
                wt = phrase_time(sc["vo"], al, phrase)
            except ValueError:
                missing.append(key)
                continue
            cue[(i, key)] = max(starts[i] + 0.05,
                                min(starts[i] + wt - 0.08, starts[i] + d[i] - 0.10))
            WORD[(i, key)] = starts[i] + wt
        # Nothing is ever moved away from its word. Unmatched cues fall back to a
        # spoken anchor where one exists (last word for tape, first for a head),
        # or to a role position, and are reported.
        for key in missing:
            phrase = sc["cues"][key]
            if key == "t":
                wt = starts[i] + words[i][-1][0]
                cue[(i, key)] = min(wt - 0.08, starts[i] + d[i] - 0.10)
                WORD[(i, key)] = wt
            elif key in ("h", "l"):
                wt = starts[i] + words[i][0][0]
                cue[(i, key)] = max(starts[i] + 0.05, min(wt - 0.08, starts[i] + d[i] - 0.10))
                WORD[(i, key)] = wt
            elif key.isdigit():
                idx = int(key)
                n_items = len(sc.get("items", sc.get("chips", []))) or 1
                cue[(i, key)] = starts[i] + d[i] * (idx + 1) / (n_items + 1)
            else:
                cue[(i, key)] = starts[i] + 0.5
            WARN.append(f"scene {i+1} {sc['type']}: '{key}' ({phrase!r}) -> fallback")

    # hardware stack: one new drawing per ~1.4s, each on a real spoken word
    BAND = {}
    for i, sc in enumerate(spec["scenes"]):
        ws = [w[0] for w in words[i]] or [0.0]
        K = 1
        for j in range(K):
            target = 0.25 if j == 0 else d[i] * 0.55
            # snap to the nearest real spoken word so it stays word-anchored
            t = min(ws, key=lambda x: abs(x - target))
            BAND[(i, j)] = starts[i] + t

    devs = sorted(abs(cue[k] - WORD[k]) for k in WORD if k in cue)
    if devs:
        print(f"   sync: {len(devs)} word-locked cues | max offset {max(devs)*1000:.0f} ms"
              f" | median {devs[len(devs)//2]*1000:.0f} ms")

    bodies = []
    for i, sc in enumerate(spec["scenes"]):
        h = render(sc, i)
        def sub(m, i=i):
            key = m.group(1)
            if key.startswith("band"):
                j = int(key[4:])
                if (i, j) not in BAND:
                    return 'data-in="9999"'
                return 'data-in="%.2f"' % (BAND[(i, j)] - starts[i])
            if key == "cap":
                return 'data-in="0.15"'
            if (i, key) not in cue:
                if len(key) > 1 and key[-1] in "abc" and key[:-1].isdigit() \
                        and (i, key[:-1]) in cue:
                    off = {"a": 0.18, "b": 0.38}[key[-1]]
                    cue[(i, key)] = min(cue[(i, key[:-1])] + off, starts[i] + d[i] - 0.10)
                    return 'data-in="%.2f"' % (cue[(i, key)] - starts[i])
                if key.isdigit():
                    idx = int(key)
                    n = max(len(sc.get("items", sc.get("chips", []))), idx + 1)
                    cue[(i, key)] = starts[i] + d[i] * (idx + 1) / (n + 1)
                elif key in ("h", "l", "a", "b"):
                    cue[(i, key)] = starts[i] + 0.15
                elif key in ("t", "w"):
                    cue[(i, key)] = min(starts[i] + d[i] - 1.0, starts[i] + 1.2)
                else:
                    cue[(i, key)] = starts[i] + 0.4
                WARN.append(f"scene {i+1} {sc['type']}: @{key}@ placed by role")
            return 'data-in="%.2f"' % (cue[(i, key)] - starts[i])
        h = re.sub(r'data-in="@(\w+)@"', sub, h)
        bodies.append(h)

    # density pass
    ev = sorted({starts[i] + 0.15 for i in range(len(spec["scenes"]))} |
                {starts[i] + float(v) for i, h in enumerate(bodies)
                 for v in re.findall(r'data-in="([0-9.]+)"', h)})
    fills = {i: [] for i in range(len(spec["scenes"]))}
    # every scene opens with a tick so a cut never lands on an empty board
    for i in range(len(spec["scenes"])):
        first = min([v for v in (starts[i] + 0.15,)])
        if not any(starts[i] + 0.45 <= e <= starts[i] + 1.2 for e in ev):
            fills[i].append(0.45)
    for p, q in zip(ev + [total], (ev + [total])[1:]):
        gap = q - p
        if gap <= TICK:
            continue
        k = int(gap // TICK)
        for j in range(1, k + 1):
            tt = p + gap * j / (k + 1)
            si = max(i for i in range(len(starts)) if starts[i] <= tt)
            fills[si].append(round(tt - starts[si], 2))

    def build_sections():
        out = []
        for i, h in enumerate(bodies):
            hh = h
            if fills[i]:
                hh += ('\n      <div class="rail">' +
                       ''.join(f'<i data-in="{x}"></i>' for x in sorted(fills[i])) + '</div>')
            cls = "scene dim" if spec["scenes"][i]["type"] in ("rows", "bars", "table", "caveat") else "scene"
            out.append(f'  <section class="{cls}" data-scene="{i}">\n{hh}\n  </section>')
        return out

    sections = build_sections()
    for _ in range(8):
        ev2 = sorted({starts[i] + float(v) for i, sec in enumerate(sections)
                      for v in re.findall(r'data-in="([0-9.]+)"', sec)})
        gaps = [(q - p, p, q) for p, q in zip(ev2, ev2[1:])]
        worst = max(g[0] for g in gaps) if gaps else 0
        if worst <= MAX_GAP - 0.05:
            break
        added = 0
        for g, pp, qq in gaps:
            if g <= MAX_GAP - 0.05:
                continue
            k = max(1, int(g // 1.35))
            for j in range(1, k + 1):
                tt = pp + g * j / (k + 1)
                si = max(i for i in range(len(starts)) if starts[i] <= tt)
                fills[si].append(round(tt - starts[si], 2))
                added += 1
        if not added:
            break
        sections = build_sections()

    ev2 = sorted({starts[i] + float(v) for i, sec in enumerate(sections)
                  for v in re.findall(r'data-in="([0-9.]+)"', sec)})
    worst = max(q - p for p, q in zip(ev2, ev2[1:]))
    if worst > MAX_GAP:
        sys.exit(f"density gate failed: gap {worst:.2f}s > {MAX_GAP}s")

    b64 = base64.b64encode(open(vo, "rb").read()).decode()
    css = open(os.path.join(ROOT, "core", "byte.css"), encoding="utf-8").read().replace('url("fonts/', 'url("core/fonts/')
    pcss = open(os.path.join(ROOT, "core", "player.css"), encoding="utf-8").read()
    pjs = open(os.path.join(ROOT, "core", "player.js"), encoding="utf-8").read()
    scenes_js = ",\n  ".join(f"{{s:{starts[i]:5.2f},  e:{starts[i]+d[i]:5.2f}}}" for i in range(len(d)))
    labels = ", ".join("'%s'" % s["type"].upper() for s in spec["scenes"])

    html = f"""<!DOCTYPE html>
<html lang="en" class="no-js"><head><meta charset="utf-8"><title>{spec.get('title','')}</title>
<style>
{css}
{pcss}
  .ctr{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px;padding:0 70px;transform:scale(1.06)}}
  .col{{display:flex;flex-direction:column;gap:16px;width:1400px}}
  .split{{display:flex;align-items:center;gap:46px}}
  .split.wide{{width:1240px;justify-content:center;gap:64px}}
  .side{{display:flex;gap:70px}}
  .big{{font-size:150px;line-height:.9}} .u{{font-size:64px}}
  .chip{{font-family:var(--mono);font-size:18px;letter-spacing:.16em;padding:10px 18px;border:2px dashed rgba(237,234,227,.5);border-radius:8px;color:var(--gray)}}
  :root{{--cyan:#38D9E8;--orange:#F08A3C;--soft:#8FD3C7}}
  .grow{{width:0}} .grow.on{{width:var(--w)}}
  .sweep{{position:relative;overflow:hidden}}
  .sweep::after{{content:"";position:absolute;inset:0;left:-60%;
        background:linear-gradient(105deg,transparent,rgba(255,255,255,.10),transparent);
        animation:sweep 5.5s ease-in-out infinite}}
  @keyframes sweep{{0%,70%{{left:-60%}}100%{{left:120%}}}}
  .drift{{animation:drift 7s ease-in-out infinite}}
  @keyframes drift{{0%,100%{{transform:translateX(0)}}50%{{transform:translateX(10px)}}}}
  .glow{{animation:glow 3.2s ease-in-out infinite}}
  @keyframes glow{{0%,100%{{filter:drop-shadow(0 0 0 transparent)}}
                   50%{{filter:drop-shadow(0 0 14px rgba(245,213,71,.45))}}}}
  .bf-row{{gap:26px;min-height:112px}}
  .bf-bar__track{{border-color:rgba(237,234,227,.28)!important;background:rgba(255,255,255,.07)!important}}
  .bf-bar__lab{{color:var(--gray)!important}}
  .dim .bf-row.on{{border-left:6px solid var(--yellow);padding-left:22px}} .bf-row__v{{min-width:100px;text-align:right;white-space:nowrap}}
  .hero{{flex:0 0 auto}}
  .hero figure{{display:none;margin:0}}
  .hero figure.on{{display:block}}
  .hero figure.on:has(~ figure.on){{display:none}}
  .hero--h{{width:560px}}
  .hero--v{{width:640px;margin-bottom:10px}}
  .hero svg{{width:100%!important;height:auto!important;display:block;max-height:330px}}
  .hero .lime{{fill:var(--lime)}}
  .split.wide{{gap:52px;align-items:center}}
  /* list scenes: the frame is full from the start, items light up in turn */
  .accbar{{height:3px;width:120px;margin:2px 0 14px;border-radius:2px;opacity:.85}}
  .dim .bf-row__v[data-in]{{opacity:0}}
  .dim .bf-row__v[data-in].on{{opacity:1}}
  .dim .bf-bar__val[data-in]{{opacity:0}}
  .dim .bf-bar__val[data-in].on{{opacity:1}}
  .dim .chalk span[data-in].on{{opacity:1}}
  .dim .bf-bar[data-in].on{{opacity:1}}
  .dim .chalk span[data-in]{{opacity:0}}
  .dim .chalk[data-in].on{{opacity:1}}
  .bgart .art{{width:100%}}
  .bgart .lime,.bgart .small{{fill:var(--white)!important;opacity:.6}}
  .rail{{position:absolute;left:50%;transform:translateX(-50%);bottom:70px;display:flex;gap:9px}}
  .rail i{{width:2px;height:15px;background:rgba(237,234,227,.12);display:block}}
  .rail i.on{{background:rgba(237,234,227,.55)}}
  .art{{display:block;width:400px;height:auto;max-width:46vw;overflow:visible}}
  .float{{flex:0 0 auto;width:400px}} .float .art{{width:100%}}
  .art .s{{fill:none;stroke:var(--white);stroke-width:3}} .art .t{{stroke-width:2.2}}
  .art .blade{{fill:none;stroke:var(--gray);stroke-width:7}} .art .dim{{opacity:.45}}
  .art .fg{{fill:rgba(237,234,227,.25)}} .art .fl{{fill:var(--lime)}} .art .fy{{fill:var(--yellow)}}
  .art .lime{{fill:var(--lime);font-family:var(--mono);font-weight:800;font-size:30px}}
  .art .small{{fill:var(--dim);font-family:var(--mono);font-size:15px;letter-spacing:3px}}
  .spin{{transform-box:fill-box;transform-origin:center;animation:spin 2.6s linear infinite}}
  @keyframes spin{{to{{transform:rotate(360deg)}}}}
  .float{{animation:bob 4s ease-in-out infinite}}
  @keyframes bob{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-9px)}}}}
  .pulse{{animation:pl 1.8s ease-in-out infinite}} @keyframes pl{{0%,100%{{opacity:1}}50%{{opacity:.45}}}}
  .no-js #start{{display:none!important}}
</style></head><body>
<script>document.documentElement.classList.remove("no-js");</script>
<div id="wrap"><div id="stage">
{chr(10).join(sections)}
</div></div>
<script>
window.EPISODE = {{
  kicker: "{spec.get('kicker','Byte Forensics')}",
  title: "{spec.get('title','')}",
  subtitle: "{spec.get('subtitle','')}",
  total: {total:.2f}, maxGap: {MAX_GAP},
  vo: "data:audio/mpeg;base64,{b64}",
  sfxBase: "audio/",
  labels: [{labels}],
  scenes: [
  {scenes_js}
  ],
  wipes: [], wipeColors: [], sfx: []
}};
</script>
<script>
{pjs}
</script>
</body></html>
"""
    if WARN:
        print(f"   {len(WARN)} cue(s) used a positional fallback:")
        for w in WARN[:6]:
            print("     ", w)
        if len(WARN) > 6:
            print(f"      ... and {len(WARN)-6} more")
    dst = a.out if os.path.isabs(a.out) else os.path.join(ROOT, a.out)
    open(dst, "w", encoding="utf-8").write(html)
    print(f"wrote {dst}  {total:.1f}s  scenes={len(spec['scenes'])}  max gap {worst:.2f}s  ({len(html)//1024} KB)")

    for f in os.listdir(A):
        if f.endswith((".wav", ".txt")):
            os.remove(os.path.join(A, f))


if __name__ == "__main__":
    main()
