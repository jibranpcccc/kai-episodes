import re,os,subprocess
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
for ep in ["ep02","ep03"]:
    d=os.path.join(ROOT,"episodes",ep)
    h=open(os.path.join(d,"index.html"),encoding="utf-8").read()
    tot=float(re.search(r"total: ([\d.]+)",h).group(1))
    vo=os.path.join(d,"audio","vo.mp3")
    vd=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
        "-of","csv=p=0",vo],capture_output=True,text=True).stdout.strip())
    print(f"\n{ep}  total={tot}s  vo={vd:.2f}s  delta={vd-tot:+.2f}s")
    # assets
    for m in re.findall(r'(?:href|src)="([^"]+)"',h):
        if m.startswith("http"): continue
        p=os.path.join(d,m.replace("/",os.sep))
        print(("  OK   " if os.path.exists(p) else "  MISS ")+m)
    for n in ["tick","whoosh","thud"]:
        p=os.path.join(ROOT,"audio",n+".mp3")
        assert os.path.exists(p), p
    # cue count
    print("  data-in cues:",len(re.findall(r'data-in="',h)),
          " sfx:",len(re.findall(r"\{t:[0-9.]+, f:'",h)),
          " scenes:",len(re.findall(r'class="scene"',h)))
    print("  audio dir:",os.listdir(os.path.join(d,"audio")))
