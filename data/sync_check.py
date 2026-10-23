import re, subprocess, os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
mp3=os.path.join(ROOT,"audio","vo.mp3")
out=subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",mp3,"-af",
                    "silencedetect=noise=-45dB:d=0.25","-f","null","-"],
                   capture_output=True,text=True).stderr
starts=[float(x) for x in re.findall(r"silence_start: ([0-9.]+)",out)]
ends=[float(x) for x in re.findall(r"silence_end: ([0-9.]+)",out)]
durs=[float(x) for x in re.findall(r"silence_duration: ([0-9.]+)",out)]

print("SPEECH CHUNKS (between silences):")
chunks=[]; pos=0.0
for s,e,d in zip(starts,ends,durs):
    if s-pos>0.05: chunks.append((pos,s))
    pos=e
chunks.append((pos,51.228))
for i,(a,b) in enumerate(chunks,1):
    print(f"  {i:2d}  {a:6.2f} -> {b:6.2f}   ({b-a:4.2f}s)")

print("\nLONG GAPS (>1.0s) = my inter-segment gaps:")
long=[(s,e) for s,e,d in zip(starts,ends,durs) if d>1.0]
for s,e in long: print(f"  {s:6.2f} -> {e:6.2f}  ({e-s:.2f}s)")

print("\nSCENE BOUNDARY CHECK")
SC=[(0.00,4.35),(4.35,16.07),(16.07,23.74),(23.74,29.96),(29.96,36.98),(36.98,42.77),(42.77,51.23)]
print(f"  {'scene':6} {'my start':>9} {'speech resumes':>15} {'delta':>8}")
for i,(a,b) in enumerate(SC,1):
    on=next((e for s,e in long if e>a-0.6 and e<b), a)
    print(f"  {i:<6} {a:9.2f} {on:15.2f} {on-a:+8.3f}s")
print("\n  (positive delta = scene changes BEFORE the voice resumes = visual leads audio)")
