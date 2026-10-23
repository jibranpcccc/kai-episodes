import json, os, glob, sys
from PIL import Image, ImageDraw, ImageFont

ROOT=r"C:\Users\jibra\Desktop\1\KAI"
def font(sz):
    for n in ["seguisb.ttf","arialbd.ttf","segoeui.ttf","arial.ttf"]:
        try: return ImageFont.truetype(n,sz)
        except: pass
    return ImageFont.load_default()

def board(vid, t0, t1, out, title, cols=3, rows=3, tw=632):
    d=os.path.join(ROOT,"frames",vid)
    files=sorted(glob.glob(d+r"\*.jpg"))
    if not files: print("no frames for",vid); return
    total=len(files)/2.0
    th=int(tw*9/16); pad=6; cap=30
    W=cols*(tw+pad)+pad; H=rows*(th+cap+pad)+pad+44
    canvas=Image.new("RGB",(W,H),(12,12,14)); dr=ImageDraw.Draw(canvas)
    dr.text((pad+2,10),title,font=font(21),fill=(255,255,255))
    n=cols*rows
    span=max(t1-t0,1)
    for k in range(n):
        t=t0+span*(k+0.5)/n
        idx=min(int(round(t*2)),len(files)-1)
        im=Image.open(files[idx]).convert("RGB").resize((tw,th),Image.LANCZOS)
        x=pad+(k%cols)*(tw+pad); y=44+pad+(k//cols)*(th+cap+pad)
        canvas.paste(im,(x,y))
        mm,ss=divmod(int(t),60)
        dr.text((x+3,y+th+3),f"{mm}:{ss:02d}",font=font(15),fill=(120,255,180))
    canvas.save(out,quality=92)
    print("wrote",out,canvas.size)

if __name__=="__main__":
    vid=sys.argv[1]
    info=json.load(open(os.path.join(ROOT,"videos",vid+".info.json"),encoding="utf-8"))
    dur=info["duration"]; chs=info.get("chapters") or []
    if not chs: chs=[{"start_time":0,"title":"full"}]
    bounds=[(c["start_time"], (chs[i+1]["start_time"] if i+1<len(chs) else dur), c["title"]) for i,c in enumerate(chs)]
    for i,(a,b,name) in enumerate(bounds):
        safe="".join(ch if ch.isalnum() or ch in " -_" else "" for ch in name)[:46].strip()
        board(vid,a,b,os.path.join(ROOT,"data",f"board_{vid}_{i+1:02d}.jpg"),
              f"{vid}  [{i+1}/{len(bounds)}]  {int(a)//60}:{int(a)%60:02d}-{int(b)//60}:{int(b)%60:02d}  {name}")
