import re, os

p = r"C:\Users\jibra\Desktop\1\KAI\data\make_episodes.py"
s = open(p, encoding="utf-8").read()

NEW_RENDER = '''def render_vo(vo_dir, lines):
    """Render each scene, capturing EdgE word boundaries for exact cue timing."""
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

            # how much silence the trim will remove from the front
            o = subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",raw,"-af",
                                "silencedetect=noise=-45dB:d=0.05","-f","null","-"],
                               capture_output=True,text=True).stderr
            ends = re.findall(r"silence_end: ([0-9.]+)", o)
            lead = float(ends[0]) if ends else 0.0

            subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-i",raw,"-af",af,
                            "-ar","44100","-ac","1","-c:a","pcm_s16le", wav], check=True)
            WORDS.append((t, [(max(0.0, x - lead), w) for x, w in ws]))
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
    open(os.path.join(vo_dir,"l.txt"),"w").write("\\n".join(lst))
    subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","concat","-safe","0",
                    "-i",os.path.join(vo_dir,"l.txt"),"-c:a","libmp3lame","-b:a","192k",
                    os.path.join(vo_dir,"vo.mp3")], check=True)
    return d, WORDS

'''

NEW_CUES = '''    # ---- cues are placed on the exact spoken word ----
    cue_t = {}; cue_info = []
    for i, s_spec in enumerate(spec["scenes"]):
        words = WORDS[i][1]
        aligned = align(s_spec["vo"], words)
        for tok, phrase in s_spec.get("cues", {}).items():
            wt = phrase_time(s_spec["vo"], aligned, words, phrase)
            t = max(starts[i] + 0.05, min(starts[i] + wt - 0.08, starts[i] + d[i] - 0.10))
            cue_t[tok] = t
            cue_info.append((i, tok, phrase, starts[i] + wt, t))

'''

# insert helpers just above build()
HELPERS = '''def align(text, words):
    """Map each spoken word back to its character index in the script."""
    low = text.lower(); out = []; cur = 0
    for t, w in words:
        wl = w.lower().strip(".,;:!?\\"'()")
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
        return words[0][0] if words else 0.0
    for ci, t in aligned:
        if ci >= p:
            return t
    return aligned[-1][1] if aligned else 0.0


'''

assert "def build(spec):" in s
s = s.replace("def build(spec):", HELPERS + "def build(spec):", 1)

# swap the renderer
s2, n1 = re.subn(r"def render_vo\(vo_dir, lines\):.*?\n    return d\n", NEW_RENDER, s, flags=re.S)
assert n1 == 1, f"render_vo replace count {n1}"
s = s2

# unpack the word data
old_call = '    d = render_vo(os.path.join(folder,"audio"), lines)'
assert old_call in s, "render_vo call not found"
s = s.replace(old_call, '    d, WORDS = render_vo(os.path.join(folder,"audio"), lines)')

# swap the cue resolver
s2, n2 = re.subn(r"    # absolute phrase onsets, per scene.*?cue_t\[tok\] = max\(starts\[i\]\+0\.10, min\(est, starts\[i\]\+d\[i\]-0\.15\)\n",
                 NEW_CUES, s, flags=re.S)
assert n2 == 1, f"cue block replace count {n2}"
s = s2

# report the cue map so it can be eyeballed
s = s.replace('''    print(f"\\n[{spec['id']}] {total:.2f}s  scenes={len(d)}  cues={len(cue_t)}  wipes={wipes}")''',
'''    print(f"\\n[{spec['id']}] {total:.2f}s  scenes={len(d)}  cues={len(cue_t)}  wipes={wipes}")
    print("   cue -> word time (should match the phrase)")
    for i, tok, phrase, wt, t in cue_info:
        print(f"     sc{i+1} {tok:9} {t:6.2f}s  phrase @{wt:6.2f}s  lead {t-wt:+.2f}  {phrase!r}")''')

open(p, "w", encoding="utf-8").write(s)
print("generator rewritten to use word boundaries")
