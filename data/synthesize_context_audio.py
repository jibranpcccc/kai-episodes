# -*- coding: utf-8 -*-
"""
Synthesize calm documentary speech (-4% rate, ~153 WPM) for all 72 scenes of Episode 13.
Uses edge-tts with en-US-AndrewNeural and trims leading/trailing silence via FFmpeg.
Produces exact cache files n{i}-{key}.wav and n{i}-{key}.json in build/BYTE-CONTEXT.
"""
import asyncio
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = r"c:\Users\jibra\Desktop\1\KAI\repo"
work = os.path.join(ROOT, "build", "BYTE-CONTEXT")
VOICE = "en-US-AndrewNeural"
RATE = "-4%"

with open(os.path.join(ROOT, "data", "script_ep13_raw.txt"), "r", encoding="utf-8") as f:
    raw = f.read()

sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', raw.replace('\n', ' ')) if s.strip()]
scenes_vo = []
cur, cur_words = [], 0
for s in sents:
    sw = len(s.split())
    if "Separate model or application output limits" in s:
        if cur: scenes_vo.append(" ".join(cur))
        cur, cur_words = [s], sw
        continue
    if "If you want the model to generate eight thousand tokens" in s:
        if cur: scenes_vo.append(" ".join(cur))
        cur, cur_words = [s], sw
        continue
    if "That is the shock." in s:
        if cur: scenes_vo.append(" ".join(cur))
        cur, cur_words = [s], sw
        continue
    if (cur_words + sw > 36 and cur_words >= 16) or (cur_words >= 22 and sw >= 14):
        scenes_vo.append(" ".join(cur))
        cur = [s]
        cur_words = sw
    else:
        cur.append(s)
        cur_words += sw
if cur:
    scenes_vo.append(" ".join(cur))

assert len(scenes_vo) == 72, f"Expected 72 scenes, got {len(scenes_vo)}"

# Clean work directory to remove old +4% cache
os.makedirs(work, exist_ok=True)
for old_f in glob.glob(os.path.join(work, "n*.*")) + glob.glob(os.path.join(work, "r*.*")):
    try:
        os.remove(old_f)
    except Exception:
        pass

print(f"Cleared old audio cache in {work}. Synthesizing 72 scenes at {RATE} ({VOICE})...")

sem = asyncio.Semaphore(6)

async def synthesize_one(i, vo):
    key = hashlib.sha1(("%s|%s|%s" % (vo, VOICE, RATE)).encode("utf-8")).hexdigest()[:16]
    raw = os.path.join(work, f"r{i}-{key}.mp3")
    wav = os.path.join(work, f"n{i}-{key}.wav")
    jsf = os.path.join(work, f"n{i}-{key}.json")
    
    if os.path.exists(wav) and os.path.exists(jsf) and os.path.getsize(wav) > 1000:
        return
        
    async with sem:
        import edge_tts
        for attempt in range(5):
            try:
                c = edge_tts.Communicate(vo, VOICE, rate=RATE, boundary="WordBoundary")
                buf, ws = bytearray(), []
                async for ch in c.stream():
                    if ch["type"] == "audio":
                        buf += ch["data"]
                    elif ch["type"] == "WordBoundary":
                        ws.append((ch["offset"] / 1e7, ch["text"]))
                if buf:
                    break
            except Exception as ex:
                if attempt == 4:
                    raise ex
                await asyncio.sleep(1 + attempt)
                
        with open(raw, "wb") as f:
            f.write(bytes(buf))
            
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
        with open(jsf, "w", encoding="utf-8") as f:
            json.dump(res_words, f)
            
        if os.path.exists(raw):
            os.remove(raw)
            
        print(f"  [{i}/72] Synthesized: dur={res_words[-1][0]:.2f}s words={len(res_words)}")

async def main():
    tasks = [synthesize_one(i + 1, scenes_vo[i]) for i in range(72)]
    await asyncio.gather(*tasks)
    print("All 72 audio scenes synthesized successfully at calm -4% rate!")

if __name__ == "__main__":
    asyncio.run(main())
