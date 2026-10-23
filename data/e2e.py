import re,os,subprocess
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
for f,aud in [("EPISODE-02.html","audio/ep02_vo.mp3"),("EPISODE-03.html","audio/ep03_vo.mp3")]:
    h=open(os.path.join(ROOT,f),encoding="utf-8").read()
    blk=re.search(r"const SCENES = \[(.*?)\];",h,re.S) or re.search(r"scenes: \[(.*?)\n  \]",h,re.S)
    starts=[float(x) for x in re.findall(r"s:\s*([0-9.]+)", blk.group(1))]
    total=float(re.search(r"total: ([0-9.]+)",h).group(1))
    p=os.path.join(ROOT,aud.replace("/",os.sep))
    ad=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],
        capture_output=True,text=True).stdout.strip())
    o=subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",p,"-af",
                      "silencedetect=noise=-45dB:d=0.14","-f","null","-"],
                     capture_output=True,text=True).stderr
    ends=[float(x) for x in re.findall(r"silence_end: ([0-9.]+)",o)]
    print(f"\n{f}   cues assume {total:.2f}s   audio is {ad:.2f}s   drift {ad-total:+.3f}s")
    print(f"   scene starts: {[round(x,2) for x in starts]}")
    worst=0
    for i,s0 in enumerate(starts[1:],start=2):
        if not ends: continue
        near=min(ends,key=lambda e:abs(e-s0))
        d=s0-near; worst=max(worst,abs(d))
        print(f"   scene {i} at {s0:6.2f}s   nearest speech resume {near:6.2f}s   delta {d:+.3f}s")
    print(f"   -> worst scene-boundary error: {worst*1000:.0f} ms")
