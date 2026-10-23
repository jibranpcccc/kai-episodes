from PIL import Image, ImageDraw, ImageFont
import os
R=r"C:\Users\jibra\Desktop\1\KAI\proof"
def f(s):
    for n in ["seguisb.ttf","arialbd.ttf"]:
        try: return ImageFont.truetype(n,s)
        except: pass
    return ImageFont.load_default()
pairs=[("EP 02 @ 24.0s",os.path.join(R,"sync_ep02.png")),("EP 03 @ 21.2s",os.path.join(R,"sync_ep03.png"))]
imgs=[(t,Image.open(p).convert("RGB")) for t,p in pairs if os.path.exists(p)]
W=sum(i.width for _,i in imgs)+18; H=max(i.height for _,i in imgs)+38
c=Image.new("RGB",(W,H),(25,25,28)); d=ImageDraw.Draw(c); x=6
for lab,im in imgs:
    c.paste(im,(x,30)); d.text((x+4,8),lab,font=f(14),fill=(120,255,180)); x+=im.width+6
c.save(os.path.join(R,"sync_both.jpg"),quality=92); print("wrote sync_both.jpg")
