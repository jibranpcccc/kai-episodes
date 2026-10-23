import asyncio, base64, json, os, subprocess, pathlib
import edge_tts
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; WORK=os.path.join(ROOT,"build","RC"); os.makedirs(WORK,exist_ok=True)
SCRIPT=[
 "This is the card everyone benchmarks at four K. Short prompts, huge numbers. At a hundred and twenty-eight K of context, it drops to a third of that.",
 "Here is the curve. Seventy-five tokens at four K. Fifty-two at sixteen. Thirty-eight at thirty-two. Twenty-eight at sixty-four. Twenty-two at a hundred and twenty-eight.",
 "Nothing changed in the silicon. What changed is the cache. Every token you add writes a key and a value, and those grow with the conversation.",
 "At a hundred and twenty-eight K this model needs twenty-six gigabytes. The card has twenty-four. That two gigabytes is the whole story.",
 "So the ceiling is sixty-four K. Above that you are not running the model. You are running the memory system.",
 "Measure your own window before you buy the card. That is the whole method.",
]
async def rec():
    durs,files=[],[]
    for i,txt in enumerate(SCRIPT):
        mp3=os.path.join(WORK,f"s{i}.mp3"); wav=os.path.join(WORK,f"s{i}.wav")
        await edge_tts.Communicate(txt,"en-US-AndrewNeural",rate="-6%").save(mp3)
        subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-i",mp3,"-ar","44100","-ac","1","-c:a","pcm_s16le",wav],check=True)
        d=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nw=1:nk=1",wav],capture_output=True,text=True).stdout.strip())
        files.append(wav); durs.append(d); print(f"  s{i+1}: {d:.2f}s")
    return durs,files
durs,files=asyncio.run(rec())
GAP=0.55; starts=[]; t=0.0
for d in durs: starts.append(t); t+=d+GAP
total=t-GAP+1.2
g=os.path.join(WORK,"gap.wav"); subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi","-i","anullsrc=r=44100:cl=mono","-t",str(GAP),"-c:a","pcm_s16le",g],check=True)
tail=os.path.join(WORK,"tail.wav"); subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi","-i","anullsrc=r=44100:cl=mono","-t","1.2","-c:a","pcm_s16le",tail],check=True)
seq=[]
for i,f in enumerate(files):
    seq.append(f)
    if i<len(files)-1: seq.append(g)
seq.append(tail)
lst=os.path.join(WORK,"l.txt"); open(lst,"w",encoding="utf-8").write("\n".join(f"file '{p.replace(chr(92),'/')}'" for p in seq))
vo=os.path.join(WORK,"vo.mp3")
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","concat","-safe","0","-i",lst,
  "-af","loudnorm=I=-14:TP=-1.5:LRA=11,volume=1.2dB","-c:a","libmp3lame","-b:a","192k",vo],check=True)
ad=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nw=1:nk=1",vo],capture_output=True,text=True).stdout.strip())
print(f"total {total:.1f}s  audio {ad:.1f}s")
pathlib.Path(ROOT+"/data/rc_timing.json").write_text(json.dumps({"starts":starts,"durs":durs,"total":total}))
pathlib.Path(ROOT+"/data/rc_audio.b64").write_text(base64.b64encode(open(vo,"rb").read()).decode())
