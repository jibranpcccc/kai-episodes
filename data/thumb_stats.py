import csv, os, json
import numpy as np
from PIL import Image

ROOT=r"C:\Users\jibra\Desktop\1\KAI"
rows=list(csv.DictReader(open(ROOT+r"\data\videos_ranked.csv",encoding="utf-8")))
rows.sort(key=lambda r:int(r["rank"]))

def stats(path):
    im=Image.open(path).convert("RGB")
    a=np.asarray(im).astype(np.float32)
    h,w,_=a.shape
    g=a.mean(axis=2)
    # black background share (very dark pixels)
    dark=(g<32).mean()
    # bright text-ish share
    bright=(g>200).mean()
    # accent hues: red, yellow, blue in saturated pixels
    r,gg,b=a[:,:,0],a[:,:,1],a[:,:,2]
    mx=a.max(axis=2); mn=a.min(axis=2)
    sat=np.where(mx>60,(mx-mn)/np.maximum(mx,1),0)
    S=sat>0.45
    red   = (S & (r>120) & (r>gg+50) & (r>b+50)).mean()
    yellow= (S & (r>140) & (gg>110) & (b<100) & (abs(r-gg)<95)).mean()
    blue  = (S & (b>90)  & (b>r+40)).mean()
    return dict(dark=dark,bright=bright,red=red,yellow=yellow,blue=blue,mean=float(g.mean()),std=float(g.std()))

out=[]
for r in rows:
    p=os.path.join(ROOT,"thumbs",r["id"]+".jpg")
    if not os.path.exists(p): continue
    s=stats(p)
    s["rank"]=int(r["rank"]); s["views"]=int(r["views"]); s["vpd"]=float(r["vpd"] or 0); s["id"]=r["id"]
    out.append(s)

import statistics as st
top=[o for o in out if o["rank"]<=12]
rest=[o for o in out if o["rank"]>40]
def m(lst,k): return st.mean([o[k] for o in lst])
print(f"{'metric':10} {'TOP12':>8} {'rest':>8}")
for k in ["dark","bright","red","yellow","blue","mean","std"]:
    print(f"{k:10} {m(top,k)*100:7.1f}% {m(rest,k)*100:7.1f}%")

# correlation of hue presence with velocity (log)
v=np.array([np.log1p(o["vpd"]) for o in out])
for k in ["dark","bright","red","yellow","blue","std"]:
    x=np.array([o[k] for o in out])
    c=np.corrcoef(x,v)[0,1]
    print(f"corr({k:7}, log vpd) = {c:+.3f}")
