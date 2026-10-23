from PIL import Image, ImageDraw, ImageFont
import os
R=r"C:\Users\jibra\Desktop\1\KAI\proof"
def f(s):
    for n in ["seguisb.ttf","arialbd.ttf"]:
        try: return ImageFont.truetype(n,s)
        except: pass
    return ImageFont.load_default()
tiles=[("EP 02 · t=23s",os.path.join(R,"proof_ep02.png")),("EP 03 · t=21.5s",os.path.join(R,"proof_ep03.png"))]
imgs=[(t,Image.open(p).convert("RGB")) for t,p in tiles if os.path.exists(p)]
W=sum(i.width for _,i in imgs)+20; H=max(i.height for _,i in imgs)+40
c=Image.new("RGB",(W,H),(25,25,28)); d=ImageDraw.Draw(c)
x=6
for lab,im in imgs:
    c.paste(im,(x,32)); d.text((x+4,8),lab,font=f(15),fill=(120,255,180)); x+=im.width+8
c.save(os.path.join(R,"both_eps.jpg"),quality=92); print("wrote both_eps.jpg",c.size)
