# -*- coding: utf-8 -*-
with open(r"C:\Users\jibra\Desktop\1\KAI\data\fusion_build.py", "r", encoding="utf-8") as f:
    text = f.read()

target = '''# ==================================================================== TTS
async def record(W, work):
    os.makedirs(work, exist_ok=True)
    words, files = [], []
    for i, w in enumerate(W, 1):
        raw = os.path.join(work, "r%d.mp3" % i)
        wav = os.path.join(work, "n%d.wav" % i)
        buf, ws = bytearray(), []
        for attempt in range(5):
            try:
                import edge_tts
                c = edge_tts.Communicate(w["vo"], VOICE, rate=RATE, boundary="WordBoundary")
                buf, ws = bytearray(), []
                async for ch in c.stream():
                    if ch["type"] == "audio":
                        buf += ch["data"]
                    elif ch["type"] == "WordBoundary":
                        ws.append((ch["offset"] / 1e7, ch["text"]))
                if buf:
                    break
            except Exception:
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
    return words, files'''

replacement = '''# ==================================================================== TTS
async def record(W, work):
    os.makedirs(work, exist_ok=True)
    sem = asyncio.Semaphore(6)

    async def record_one(i, w):
        raw = os.path.join(work, "r%d.mp3" % i)
        wav = os.path.join(work, "n%d.wav" % i)
        jsf = os.path.join(work, "n%d.json" % i)
        if os.path.exists(wav) and os.path.exists(jsf) and os.path.getsize(wav) > 1000:
            try:
                ws_cached = json.loads(open(jsf, "r", encoding="utf-8").read())
                return ws_cached, wav
            except Exception:
                pass
        async with sem:
            buf, ws = bytearray(), []
            for attempt in range(5):
                try:
                    import edge_tts
                    c = edge_tts.Communicate(w["vo"], VOICE, rate=RATE, boundary="WordBoundary")
                    buf, ws = bytearray(), []
                    async for ch in c.stream():
                        if ch["type"] == "audio":
                            buf += ch["data"]
                        elif ch["type"] == "WordBoundary":
                            ws.append((ch["offset"] / 1e7, ch["text"]))
                    if buf:
                        break
                except Exception:
                    if attempt == 4:
                        raise
                    await asyncio.sleep(1 + attempt)
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
            res_words = [(max(0.0, x - lead + 0.04), t) for x, t in ws]
            open(jsf, "w", encoding="utf-8").write(json.dumps(res_words))
            if os.path.exists(raw):
                os.remove(raw)
            return res_words, wav

    tasks = [record_one(i, w) for i, w in enumerate(W, 1)]
    results = await asyncio.gather(*tasks)
    words = [r[0] for r in results]
    files = [r[1] for r in results]
    return words, files'''

text_norm = text.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')
replacement_norm = replacement.replace('\r\n', '\n')

if target_norm in text_norm:
    text_norm = text_norm.replace(target_norm, replacement_norm)
    with open(r"C:\Users\jibra\Desktop\1\KAI\data\fusion_build.py", "w", encoding="utf-8") as f:
        f.write(text_norm)
    print("Successfully upgraded record() in fusion_build.py")
else:
    print("Target not found")
