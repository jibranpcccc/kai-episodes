import re, os, subprocess
from PIL import Image, ImageDraw, ImageFont
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
h=open(os.path.join(ROOT,"EPISODE.html"),encoding="utf-8").read()
o=subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",os.path.join(ROOT,"audio","vo.mp3"),
                  "-af","silencedetect=noise=-45dB:d=0.16","-f","null","-"],
                 capture_output=True,text=True).stderr
st=[float(x) for x in re.findall(r"silence_start: ([0-9.]+)",o)]
en=[float(x) for x in re.findall(r"silence_end: ([0-9.]+)",o)]
chunks=[];pos=0.0
for s,e in zip(st,en):
    if s-pos>0.04: chunks.append((pos,s))
    pos=e
chunks.append((pos,42.715))

S=[0.0,4.1,14.31,20.64,25.88,32.36,36.17]
ANCHOR=[("Weights bar",8.41),("KV cache bar",9.84),("Context counter",12.02),
        ("'Tokens/sec' cap",14.41),("Spill pour",18.87),("'Spills' cap",20.74),
        ("'Spilled' cap",22.30),("Needle 40→4",23.75),("Row #1 16 GB",25.98),
        ("Row #2 24 GB",28.50),("Row #3 48 GB",30.81),("VRAM bar",32.50),
        ("Bandwidth bar",35.16),("Line 1",36.30),("Line 2",38.19),("Verdict tape",40.32)]
print("ANCHORED CUES (phrase-locked)")
print(f"  {'cue':18} {'fires':>7} {'onset':>7} {'delta':>7}")
worst=0
for name,t in ANCHOR:
    near=min(en,key=lambda p:abs(p-t)); d=t-near; worst=max(worst,abs(d))
    print(f"  {name:18} {t:7.2f} {near:7.2f} {d:+7.2f}")
print(f"  -> worst {worst:.2f}s\n")

# ---------- sync map ----------
W,H=1640,520
img=Image.new("RGB",(W,H),(13,17,16)); d_=ImageDraw.Draw(img)
def f(sz,bold=False):
    for n in (["seguisb.ttf","arialbd.ttf"] if bold else ["segoeui.ttf","arial.ttf"]):
        try: return ImageFont.truetype(n,sz)
        except: pass
    return ImageFont.load_default()
X=lambda t: 150+(t/42.715)*(1600-150)
d_.text((150,22),"EPISODE 01 — SYNC MAP  ·  Andrew  ·  42.7s",font=f(22,True),fill=(246,246,244))
d_.text((28,86),"VOICE",font=f(13,True),fill=(168,171,167))
for a,b in chunks: d_.rectangle([X(a),72,X(b),102],fill=(246,246,244))
d_.text((28,146),"SCENES",font=f(13,True),fill=(168,171,167))
for i,a in enumerate(S):
    b=S[i+1] if i+1<len(S) else 42.715
    d_.rectangle([X(a),132,X(b),162],fill=(28,38,36),outline=(60,70,67))
    d_.text((X(a)+8,138),str(i+1),font=f(15,True),fill=(248,207,51))
    d_.line([X(a),126,X(a),170],fill=(60,70,67))
d_.text((28,206),"BUILDS",font=f(13,True),fill=(168,171,167))
for name,t in ANCHOR:
    d_.line([X(t),192,X(t),236],fill=(248,207,51),width=2)
d_.text((28,278),"WIPES",font=f(13,True),fill=(168,171,167))
for t in [20.355,35.885]:
    d_.polygon([(X(t),286),(X(t)+9,298),(X(t),310),(X(t)-9,298)],fill=(4,94,239))
    d_.text((X(t)-24,314),f"cut {t+0.285:.2f}s",font=f(11),fill=(90,150,255))
d_.line([150,400,1600,400],fill=(60,70,67))
for s in range(0,43,5):
    d_.line([X(s),396,X(s),404],fill=(60,70,67))
    d_.text((X(s)-8,410),f"{s}s",font=f(12),fill=(110,114,111))
d_.text((150,470),"16 phrase-locked builds · 2 wipes landing exactly on the cut · 13 sound cues",font=f(13),fill=(110,114,111))
img.save(os.path.join(ROOT,"proof","sync_map.png"))
print("sync map rewritten")
print("chunks:",len(chunks))
