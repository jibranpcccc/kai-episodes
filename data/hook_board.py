import os, glob, sys
from PIL import Image, ImageDraw, ImageFont
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
def font(sz):
    for n in ["seguisb.ttf","arialbd.ttf","segoeui.ttf","arial.ttf"]:
        try: return ImageFont.truetype(n,sz)
        except: pass
    return ImageFont.load_default()
def grid(vid,t0,t1,n,out,title,cols=4):
    files=sorted(glob.glob(os.path.join(ROOT,"frames",vid,"*.jpg")))
    rows=(n+cols-1)//cols; tw=470; th=int(tw*9/16); pad=6; cap=26
    W=cols*(tw+pad)+pad; H=rows*(th+cap+pad)+pad+40
    c=Image.new("RGB",(W,H),(12,12,14)); d=ImageDraw.Draw(c)
    d.text((8,9),title,font=font(20),fill=(255,255,255))
    for k in range(n):
        t=t0+(t1-t0)*k/max(n-1,1)
        idx=min(int(round(t*2)),len(files)-1)
        im=Image.open(files[idx]).convert("RGB").resize((tw,th),Image.LANCZOS)
        x=pad+(k%cols)*(tw+pad); y=40+pad+(k//cols)*(th+cap+pad)
        c.paste(im,(x,y))
        d.text((x+3,y+th+2),f"{t:5.1f}s",font=font(14),fill=(120,255,180))
    c.save(out,quality=92); print("wrote",out,c.size)
grid("NA9D49kQFuU",0,12,12,os.path.join(ROOT,"data","hook_NA9D49kQFuU.jpg"),"OPENING 0-12s  (1 frame/sec)  NA9D49kQFuU")
grid("NA9D49kQFuU",1099,1117,8,os.path.join(ROOT,"data","end_NA9D49kQFuU.jpg"),"ENDING 18:19-18:37  NA9D49kQFuU",cols=4)
