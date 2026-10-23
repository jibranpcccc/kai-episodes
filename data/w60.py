import asyncio, base64, json, os, subprocess, pathlib
import edge_tts
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; W=os.path.join(ROOT,"build","W60"); os.makedirs(W,exist_ok=True)
LINES=[
 "This card is fast at four K. At one hundred and twenty-eight K, it is a third of that.",
 "Here is the curve. Seventy-five tokens at four K. Fifty-two at sixteen. Thirty-eight at thirty-two. Twenty-eight at sixty-four. Twenty-two at one twenty-eight.",
 "Nothing changed in the silicon. What changed is the cache. Every token writes a key and a value.",
 "At one twenty-eight K the model needs twenty-six gigabytes. The card has twenty-four.",
 "So the ceiling is sixty-four K. Above that you are running the memory system.",
 "Measure your own window before you buy the card.",
]
async def rec():
    out=[]
    for i,line in enumerate(LINES):
        mp3=os.path.join(W,f"s{i}.mp3"); wav=os.path.join(W,f"s{i}.wav")
        words=[]
        c=edge_tts.Communicate(line,"en-US-AndrewNeural",rate="-6%",boundary="WordBoundary")
        audio=bytearray()
        async for ch in c.stream():
            if ch["type"]=="audio": audio+=ch["data"]
            elif ch["type"]=="WordBoundary": words.append((ch["offset"]/1e7, ch["text"]))
        open(mp3,"wb").write(bytes(audio))
        subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-i",mp3,"-ar","44100","-ac","1","-c:a","pcm_s16le",wav],check=True)
        d=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nw=1:nk=1",wav],capture_output=True,text=True).stdout.strip())
        out.append({"line":line,"wav":wav,"dur":d,"words":words})
        print(f"  s{i+1}: {d:.2f}s  {len(words)} words")
    return out
scenes=asyncio.run(rec())
GAP=0.6; starts=[]; t=0.0
for s in scenes: starts.append(t); t+=s["dur"]+GAP
total=t-GAP+1.0
g=os.path.join(W,"gap.wav"); subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi","-i","anullsrc=r=44100:cl=mono","-t",str(GAP),"-c:a","pcm_s16le",g],check=True)
tail=os.path.join(W,"tail.wav"); subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi","-i","anullsrc=r=44100:cl=mono","-t","1.0","-c:a","pcm_s16le",tail],check=True)
seq=[]
for i,s in enumerate(scenes):
    seq.append(s["wav"])
    if i<len(scenes)-1: seq.append(g)
seq.append(tail)
lst=os.path.join(W,"l.txt"); open(lst,"w",encoding="utf-8").write("\n".join(f"file '{p.replace(chr(92),'/')}'" for p in seq))
vo=os.path.join(W,"vo.mp3")
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","concat","-safe","0","-i",lst,
  "-af","loudnorm=I=-14:TP=-1.5:LRA=11,volume=1.2dB","-c:a","libmp3lame","-b:a","192k",vo],check=True)
data={"total":total,"starts":starts,"scenes":[{"dur":s["dur"],"words":s["words"],"line":s["line"]} for s in scenes]}
pathlib.Path(ROOT+"/data/w60.json").write_text(json.dumps(data))
pathlib.Path(ROOT+"/data/w60.b64").write_text(base64.b64encode(open(vo,"rb").read()).decode())
print(f"total {total:.1f}s")
