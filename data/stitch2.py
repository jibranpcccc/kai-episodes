from PIL import Image, ImageDraw, ImageFont
import os
ROOT=r"C:\Users\jibra\Desktop\1\KAI\proof"
def f(s):
    for n in ["seguisb.ttf","arialbd.ttf"]:
        try: return ImageFont.truetype(n,s)
        except: pass
    return ImageFont.load_default()
groups=[("ep02","EPISODE 02 — The Second Price Tag",[0,2,3,4]),
        ("ep03","EPISODE 03 — Two Users, Half the Speed",[0,1,2,3])]
for ep,title,sc in groups:
    tw,th=740,416
    c=Image.new("RGB",(tw*2+18, (th+30)*2+50),(15,15,18)); d=ImageDraw.Draw(c)
    d.text((10,10),title,font=f(20),fill=(248,207,51))
    for i,n in enumerate(sc):
        p=os.path.join(ROOT,f"{ep}_s{n}.png")
        if not os.path.exists(p): continue
        im=Image.open(p).convert("RGB").resize((tw,th),Image.LANCZOS)
        x=6+(i%2)*(tw+6); y=42+(i//2)*(th+30)
        c.paste(im,(x,y))
        d.text((x+4,y+th+4),f"scene {n+1}",font=f(14),fill=(120,255,180))
    c.save(os.path.join(ROOT,f"{ep}_frames.jpg"),quality=90)
    print("wrote",ep,"frames",c.size)
