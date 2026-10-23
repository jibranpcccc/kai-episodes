import csv, os, glob, numpy as np
from PIL import Image, ImageDraw, ImageFont
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
def font(sz):
    for n in ["seguisb.ttf","arialbd.ttf","segoeui.ttf"]:
        try: return ImageFont.truetype(n,sz)
        except: pass
    return ImageFont.load_default()

def extremes(vid,out):
    rows=list(csv.DictReader(open(os.path.join(ROOT,"data",f"frames_{vid}.csv"),encoding="utf-8")))
    def top(key,n=4):
        s=sorted(rows,key=lambda r:float(r[key]),reverse=True)
        keep=[];seen=set()
        for r in s:
            sec=int(float(r["t"]))
            if sec in seen: continue
            seen.add(sec); keep.append((r,key))
            if len(keep)>=n: break
        return keep
    picks=[]
    for k in ["ink" if False else "bright","edge","red","yel","blu"]:
        picks+=top(k,3)
    cols=4; rowsn=(len(picks)+cols-1)//cols
    tw=470; th=int(tw*9/16); pad=6; cap=30
    W=cols*(tw+pad)+pad; H=rowsn*(th+cap+pad)+pad+40
    c=Image.new("RGB",(W,H),(12,12,14)); d=ImageDraw.Draw(c)
    d.text((8,9),f"VISUAL EXTREMES  {vid}   (bright / edge / red / yellow / blue peaks)",font=font(19),fill=(255,255,255))
    for i,(r,k) in enumerate(picks):
        idx=int(r["idx"]); f=os.path.join(ROOT,"frames",vid,f"{idx:06d}.jpg")
        if not os.path.exists(f): continue
        im=Image.open(f).convert("RGB").resize((tw,th),Image.LANCZOS)
        x=pad+(i%cols)*(tw+pad); y=40+pad+(i//cols)*(th+cap+pad)
        c.paste(im,(x,y))
        d.text((x+3,y+th+2),f"{float(r['t']):5.0f}s {k}={float(r[k]):.3f}",font=font(14),fill=(120,255,180))
    c.save(out,quality=92); print("wrote",out,c.size)

extremes("NA9D49kQFuU",os.path.join(ROOT,"data","extremes_NA9D49kQFuU.jpg"))
