from PIL import Image, ImageDraw, ImageFont
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
def font(sz):
    for n in ["seguisb.ttf","arialbd.ttf"]:
        try: return ImageFont.truetype(n,sz)
        except: pass
    return ImageFont.load_default()
a=Image.open(ROOT+r"\frames\NA9D49kQFuU\001302.jpg").convert("RGB")
b=Image.open(ROOT+r"\proof\replica.png").convert("RGB")
W=1400; H=int(a.height*W/a.width)
a=a.resize((W,H),Image.LANCZOS); b=b.resize((W,H),Image.LANCZOS)
c=Image.new("RGB",(W,H*2+90),(20,20,24)); d=ImageDraw.Draw(c)
d.text((10,10),"ORIGINAL  —  NA9D49kQFuU @ 10:51  (685,000 views)",font=font(21),fill=(120,255,180))
c.paste(a,(0,40))
d.text((10,H+52),"REPLICA  —  rebuilt from scratch in HTML/CSS with our design tokens",font=font(21),fill=(248,207,51))
c.paste(b,(0,H+82))
c.save(ROOT+r"\proof\compare.jpg",quality=90); print("compare:",c.size)
