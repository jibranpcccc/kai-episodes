import re, os, subprocess
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
h=open(os.path.join(ROOT,"EPISODE.html"),encoding="utf-8").read()
o=subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",os.path.join(ROOT,"audio","vo.mp3"),
                  "-af","silencedetect=noise=-45dB:d=0.16","-f","null","-"],
                 capture_output=True,text=True).stderr
P=[float(x) for x in re.findall(r"silence_end: ([0-9.]+)",o)]
S=[float(x) for x in re.findall(r"s: ?([0-9.]+)", re.search(r"const SCENES = \[.*?\];",h,re.S).group(0))]
print("audio duration:", subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
      "-of","csv=p=0",os.path.join(ROOT,"audio","vo.mp3")],capture_output=True,text=True).stdout.strip())
print("scenes:",S)

rows=[]
for n in range(7):
    blk=re.search(r'<section class="scene" data-scene="%d">(.*?)</section>'%n,h,re.S).group(1)
    for v in re.findall(r'data-in="([0-9.]+)"',blk):
        rows.append((n,S[n]+float(v)))
for k in ['segw','segk','ctx','pour','ndl']:
    v=float(re.search(r"rel>=([0-9.]+) && !fired\.has\('%s'\)"%k,h).group(1))
    sc={'segw':1,'segk':1,'ctx':1,'pour':2,'ndl':3}[k]
    rows.append((sc,S[sc]+v))
rows.sort(key=lambda r:r[1])

print(f"\n{'t':>7} {'nearest phrase onset':>21} {'delta':>8}")
print("-"*40)
worst=0
for sc,t in rows:
    near=min(P,key=lambda p:abs(p-t)); d=t-near
    tag="" if abs(d)<=0.32 else "  <-- check"
    worst=max(worst,abs(d))
    print(f"{t:7.2f} {near:21.2f} {d:+8.2f}{tag}")
print("-"*40)
print(f"worst distance to a phrase boundary: {worst:.2f}s")
W=[float(x) for x in re.search(r"const WIPES = \[([0-9., ]+)\]",h).group(1).split(",")]
cuts=[S[3],S[6]]
print("\nWIPES")
for w,c in zip(W,cuts):
    print(f"  wipe {w:.2f} -> cover {w+0.285:.3f}  cut {c:.2f}  delta {w+0.285-c:+.3f}")
