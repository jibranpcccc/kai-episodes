import re, os, subprocess, json
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; A=os.path.join(ROOT,"audio")
P=os.path.join(ROOT,"EPISODE.html")
GAP=0.25

def dur(p): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                        "-of","csv=p=0",p],capture_output=True,text=True).stdout.strip())
d=[dur(os.path.join(A,f"n{i}.wav")) for i in range(1,8)]
starts=[];acc=0.0
for i in range(7):
    starts.append(acc); acc+=d[i]+GAP
TOTAL=sum(d)+GAP*6
print("NEW SCENES");  print("  starts:",[round(x,2) for x in starts]);  print("  total :",round(TOTAL,2))

# global pause ends in the new master
o=subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",os.path.join(A,"vo.mp3"),
                  "-af","silencedetect=noise=-45dB:d=0.16","-f","null","-"],
                 capture_output=True,text=True).stderr
PAUSES=[float(x) for x in re.findall(r"silence_end: ([0-9.]+)",o)]
print("  detected phrase onsets:",[round(p,2) for p in PAUSES])

OLD_START=[0.00,4.35,16.07,23.74,29.96,36.98,42.77]
OLD_DUR  =[4.35,11.72,7.67,6.22,7.02,5.79,8.46]
OLD_REL={0:[0.10,0.45,0.75,1.05,1.30,1.60,2.15],
         1:[0.20,4.53,6.50,8.44],
         2:[0.15,2.53,5.05,5.45],
         3:[0.15,2.30],
         4:[0.10,0.35,1.55,3.35],
         5:[0.10,0.35,3.68,4.05],
         6:[0.20,2.83,5.16,7.23]}
OLD_JS={('segw',1):4.53,('segk',1):6.50,('ctx',1):8.44,('pour',2):4.60,('ndl',3):3.18}

def snap(abs_t):
    if not PAUSES: return abs_t
    best=min(PAUSES,key=lambda p:abs(p-abs_t))
    return best-0.12 if abs(best-abs_t)<=0.70 else abs_t

NEW={}
for sc,vals in OLD_REL.items():
    frac=[v/OLD_DUR[sc] for v in vals]
    NEW[sc]=[round(min(max(snap(starts[sc]+f*d[sc])-starts[sc],0.10), d[sc]-0.15),2) for f in frac]
NEWJS={}
for (k,sc),v in OLD_JS.items():
    f=v/OLD_DUR[sc]
    NEWJS[k]=round(min(max(snap(starts[sc]+f*d[sc])-starts[sc],0.10), d[sc]-0.15),2)

print("\nCUE REMAP  (old abs -> new abs)")
for sc in OLD_REL:
    for i,(ov,nv) in enumerate(zip(OLD_REL[sc],NEW[sc])):
        print(f"  scene{sc+1} cue{i}  {OLD_START[sc]+ov:6.2f}  ->  {starts[sc]+nv:6.2f}")
for k,v in NEWJS.items():
    sc={'segw':1,'segk':1,'ctx':1,'pour':2,'ndl':3}[k]
    print(f"  scene{sc+1} {k:5}  {OLD_START[sc]+OLD_JS[(k,sc)]:6.2f}  ->  {starts[sc]+v:6.2f}")

# ---------- rewrite the HTML ----------
h=open(P,encoding="utf-8").read()
for sc,vals in NEW.items():
    m=re.search(r'(<section class="scene" data-scene="%d">.*?</section>)'%sc,h,re.S)
    blk=m.group(1); it=iter(vals)
    nb=re.sub(r'data-in="[0-9.]+"',lambda _:'data-in="%s"'%next(it),blk,count=len(vals))
    h=h.replace(blk,nb)
for k,v in NEWJS.items():
    h=re.sub(r"rel>=[0-9.]+( && !fired\.has\('%s'\))"%k, lambda m: "rel>=%.2f"%v+m.group(1), h)

sc_arr=",\n  ".join(f"{{s:{starts[i]:5.2f},  e:{starts[i]+d[i]:5.2f}}}" for i in range(7))
h=re.sub(r"const SCENES = \[.*?\];", "const SCENES = [\n  "+sc_arr+"\n];", h, flags=re.S)
h=re.sub(r"const TOTAL = [0-9.]+;", f"const TOTAL = {TOTAL:.2f};", h)

w1=starts[3]-0.285; w2=starts[6]-0.285
h=re.sub(r"const WIPES = \[[0-9., ]+\];", f"const WIPES = [{w1:.3f}, {w2:.3f}];", h)

sfx=[(NEW[1][1]+starts[1],'tick'),(NEW[1][2]+starts[1],'tick'),
     (starts[2]+NEW[2][0],'tick'),(starts[2]+NEW[2][1],'tick'),(starts[2]+NEWJS['pour'],'tick'),
     (w1,'whoosh'),
     (starts[4]+NEW[4][1],'thud'),(starts[4]+NEW[4][2],'tick'),(starts[4]+NEW[4][3],'tick'),
     (starts[5]+NEW[5][1],'tick'),(starts[5]+NEW[5][2],'tick'),
     (w2,'whoosh'),(starts[6]+NEW[6][2],'thud')]
sfx_txt="const SFX = [\n"+"\n".join(f"  {{t:{t:6.2f}, f:'{k}'}}," for t,k in sorted(sfx))+"\n];"
h=re.sub(r"const SFX = \[.*?\];", sfx_txt, h, flags=re.S)

# clock labels
h=h.replace("Episode 01 &nbsp;·&nbsp; 51 seconds", f"Episode 01 &nbsp;·&nbsp; {TOTAL:.0f} seconds")
h=re.sub(r'<div id="tc">[^<]+</div>', f'<div id="tc">0.0 / {TOTAL:.1f}</div>', h)
h=h.replace('"Version", ','')  # no-op guard
open(P,"w",encoding="utf-8").write(h)
print(f"\nHTML rewritten. scenes={len(NEW)} wipes=({w1:.2f},{w2:.2f}) dur={TOTAL:.2f}")
json.dump({"d":d,"starts":starts,"total":TOTAL,"new":NEW,"newjs":NEWJS,"wipes":[w1,w2]},
          open(os.path.join(ROOT,"data","sync_v2.json"),"w"),indent=1)
