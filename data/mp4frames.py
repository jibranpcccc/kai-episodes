from PIL import Image, ImageDraw, ImageFont
import os
R=r"C:\Users\jibra\Desktop\1\KAI\proof"
def f(s):
    for n in ["seguisb.ttf","arialbd.ttf"]:
        try: return ImageFont.truetype(n,s)
        except: pass
    return ImageFont.load_default()
items=[("EP02 frame @24s from the MP4",os.path.join(R,"frommp4_ep02.png")),
       ("EP03 frame @21s from the MP4",os.path.join(R,"frommp4_ep03.png"))]
imgs=[(t,Image.open(p).convert("RGB").resize((820,461),Image.LANCZOS)) for t,p in items if os.path.exists(p)]
W=sum(i.width for _,i in imgs)+18; H=max(i.height for _,i in imgs)+36
c=Image.new("RGB",(W,H),(25,25,28)); d=ImageDraw.Draw(c); x=6
for lab,im in imgs:
    c.paste(im,(x,28)); d.text((x+4,7),lab,font=f(13),fill=(120,255,180)); x+=im.width+6
c.save(os.path.join(R,"github_output.jpg"),quality=90); print("wrote github_output.jpg")
