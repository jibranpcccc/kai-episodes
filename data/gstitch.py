from PIL import Image, ImageDraw, ImageFont
import os
R=r"C:\Users\jibra\Desktop\1\KAI\proof"
def f(s):
    for n in ["seguisb.ttf","arialbd.ttf"]:
        try: return ImageFont.truetype(n,s)
        except: pass
    return ImageFont.load_default()
items=[("EP02 price ruler",os.path.join(R,"g_ep02.png")),
       ("EP03 ring gauge",os.path.join(R,"g_ep03ring.png")),
       ("EP03 sparkline",os.path.join(R,"g_ep03spark.png"))]
imgs=[(t,Image.open(p).convert("RGB").resize((840,472),Image.LANCZOS)) for t,p in items if os.path.exists(p)]
if imgs:
    cols=2; rows=(len(imgs)+1)//2
    W=cols*846+6; H=rows*(472+30)+6
    c=Image.new("RGB",(W,H),(25,25,28)); d=ImageDraw.Draw(c)
    for i,(lab,im) in enumerate(imgs):
        x=3+(i%cols)*846; y=3+(i//cols)*(472+30)
        c.paste(im,(x,y+24)); d.text((x+4,y+4),lab,font=f(14),fill=(120,255,180))
    c.save(os.path.join(R,"graphics_proof.jpg"),quality=90); print("wrote graphics_proof.jpg",c.size)
