import re, os

p = r"C:\Users\jibra\Desktop\1\KAI\data\make_episodes.py"
src = open(p, encoding="utf-8").read().replace("\r\n", "\n")
lines = src.split("\n")

# ---- 1. locate the cue block by marker lines (no regex escaping) ----
start = next(i for i, l in enumerate(lines) if "# absolute phrase onsets" in l)
end   = next(i for i, l in enumerate(lines) if "cue_t[tok] = max(" in l)
print(f"cue block: lines {start+1}..{end+1}")

NEW_CUES = '''    # ---- cues ride on the exact spoken word ----
    cue_t = {}; cue_info = []
    for i, s_spec in enumerate(spec["scenes"]):
        words = WORDS[i][1]
        aligned = align(s_spec["vo"], words)
        for tok, phrase in s_spec.get("cues", {}).items():
            wt = phrase_time(s_spec["vo"], aligned, words, phrase)
            t = max(starts[i] + 0.05, min(starts[i] + wt - 0.08, starts[i] + d[i] - 0.10))
            cue_t[tok] = t
            cue_info.append((i, tok, phrase, starts[i] + wt, t))
'''.split("\n")

lines = lines[:start] + NEW_CUES + lines[end+1:]
src = "\n".join(lines)

# ---- 2. helpers + renderer swap + unpack ----
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
if "def align(text, words):" not in src:
    src = src.replace("def build(spec):", HELPERS + "def build(spec):", 1)

if "boundary=\"WordBoundary\"" not in src:
    OLD_RENDER_HEAD = '''    async def go():
        for i, t in enumerate(lines, 1):
            raw = os.path.join(vo_dir, f"raw{i}.mp3")
            wav = os.path.join(vo_dir, f"n{i}.wav")
            await edge_tts.Communicate(t, VOICE, rate=RATE).save(raw)
            subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-i",raw,"-af",af,
                            "-ar","44100","-ac","1","-c:a","pcm_s16le", wav], check=True)
            os.remove(raw)
    asyncio.run(go())'''
    NEW_RENDER_HEAD = '''    WORDS = []

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
            WORDS.append((t, [(max(0.0, x - lead), w) for x, w in ws]))
            os.remove(raw)
    asyncio.run(go())'''
    assert OLD_RENDER_HEAD in src, "render head not found"
    src = src.replace(OLD_RENDER_HEAD, NEW_RENDER_HEAD, 1)
    src = src.replace("    return d\n\n\ndef build",
                      "    return d, WORDS\n\n\ndef build", 1)

src = src.replace('    d = render_vo(os.path.join(folder,"audio"), lines)',
                  '    d, WORDS = render_vo(os.path.join(folder,"audio"), lines)')

# ---- 3. print the cue map for eyeballing ----
if "cue -> word time" not in src:
    src = src.replace(
      '''    print(f"\\n[{spec['id']}] {total:.2f}s  scenes={len(d)}  cues={len(cue_t)}  wipes={wipes}")''',
      '''    print(f"\\n[{spec['id']}] {total:.2f}s  scenes={len(d)}  cues={len(cue_t)}  wipes={wipes}")
    for i, tok, phrase, wt, t in cue_info:
        print(f"     sc{i+1} {tok:9} cue={t:6.2f}  word={wt:6.2f}  lead={t-wt:+.2f}  {phrase!r}")''')

open(p, "w", encoding="utf-8", newline="\n").write(src)
print("patched OK")
