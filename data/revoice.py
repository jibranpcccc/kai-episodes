import asyncio, edge_tts, os, subprocess, re
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; A=os.path.join(ROOT,"audio")
VOICE="en-US-AndrewNeural"; RATE="+8%"; GAP=0.25
LINES=[
 "Everyone buying a GPU for local AI is measuring the wrong number.",
 "Twenty-four gigabytes of VRAM doesn't run a twenty-four gigabyte model. The weights are only half. The other half is the KV cache, and it grows with every token of context.",
 "A twenty-four gig model at thirty-two K context needs six more gigabytes. So the card that fits it, doesn't.",
 "It spills into system RAM, at a tenth of the speed. Forty tokens a second becomes four.",
 "Sixteen gigs, comfortable at eight K. Twenty-four, fine at thirty-two K. Forty-eight, real work.",
 "Above seventy B, you're not buying VRAM. You're buying bandwidth.",
 "So stop asking how many gigabytes. Ask how many tokens per second you need, and buy the smallest card that still holds your context.",
]
async def gen():
    for i,t in enumerate(LINES,1):
        raw=os.path.join(A,f"n{i}_raw.mp3"); wav=os.path.join(A,f"n{i}.wav")
        await edge_tts.Communicate(t, VOICE, rate=RATE).save(raw)
        # trim leading + trailing silence, normalise to 44.1k mono
        af=("silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,"
            "areverse,silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,areverse")
        subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-i",raw,
                        "-af",af,"-ar","44100","-ac","1","-c:a","pcm_s16le",wav],check=True)
        os.remove(raw)
        print(f"  seg{i} ok")
asyncio.run(gen())

def dur(p):
    return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],
                                capture_output=True,text=True).stdout.strip())
print("\nTRIMMED SEGMENTS")
d=[dur(os.path.join(A,f"n{i}.wav")) for i in range(1,8)]
for i,x in enumerate(d,1): print(f"  seg{i}  {x:6.2f}s")
total=sum(d)+GAP*6
print(f"  speech {sum(d):.2f}s + 6 gaps = {total:.2f}s  (was 51.23s)")

# build the master with fixed 0.25s gaps
sil=os.path.join(A,"g.wav")
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi",
                "-i","anullsrc=r=44100:cl=mono","-t",str(GAP),"-c:a","pcm_s16le",sil],check=True)
lst=[]
for i in range(1,8):
    lst.append(f"file '{A.replace(chr(92),'/')}/n{i}.wav'")
    if i<7: lst.append(f"file '{A.replace(chr(92),'/')}/g.wav'")
open(os.path.join(A,"l.txt"),"w").write("\n".join(lst))
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","concat","-safe","0",
                "-i",os.path.join(A,"l.txt"),"-c:a","libmp3lame","-b:a","192k",
                os.path.join(A,"vo.mp3")],check=True)
print(f"\nNEW vo.mp3 = {dur(os.path.join(A,'vo.mp3')):.2f}s")

print("\nINTERNAL PAUSE STRUCTURE PER SEGMENT (for phrase-locked cues)")
for i in range(1,8):
    o=subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",os.path.join(A,f"n{i}.wav"),
                      "-af","silencedetect=noise=-45dB:d=0.16","-f","null","-"],
                     capture_output=True,text=True).stderr
    st=[float(x) for x in re.findall(r"silence_start: ([0-9.]+)",o)]
    en=[float(x) for x in re.findall(r"silence_end: ([0-9.]+)",o)]
    print(f"  seg{i}: pauses {[round(e,2) for e in en]}")
