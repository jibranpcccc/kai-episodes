import subprocess, os
from PIL import Image, ImageChops, ImageDraw, ImageFont
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; P=os.path.join(ROOT,"proof")
ts=[150+1.45*i for i in range(7)]
ims=[]
for t in ts:
    f=os.path.join(P,f"seq_{t:.1f}.png")
    subprocess.run(["python","data/thumb.py","BYTE-03.html","--t",f"{t:.1f}","--out",f],cwd=ROOT,capture_output=True)
    ims.append(Image.open(f).convert("RGB"))
box=(300,80,980,330); diffs=[]
for a,b in zip(ims,ims[1:]):
    d=ImageChops.difference(a.crop(box),b.crop(box)).convert("L")
    diffs.append(round(sum(d.getdata())/(d.width*d.height),2))
print("art change between 1.45s frames:", diffs, " changed:", sum(1 for x in diffs if x>1.0),"/",len(diffs))
def fnt(s):
    for f in ["seguisb.ttf","arialbd.ttf"]:
        try: return ImageFont.truetype(f,s)
        except: pass
    return ImageFont.load_default()
c=Image.new("RGB",(len(ims)*300+6, 170),(22,22,26)); dr=ImageDraw.Draw(c)
for i,im in enumerate(ims):
    c.paste(im.crop(box).resize((290,120)),(3+i*300,30)); dr.text((6+i*300,8),f"{ts[i]:.1f}s",font=fnt(11),fill=(120,255,180))
c.save(os.path.join(P,"hw_sequence.jpg"),quality=90); print("ok")
