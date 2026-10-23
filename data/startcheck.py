from PIL import Image, ImageDraw, ImageFont
import os
ROOT=r"C:\Users\jibra\Desktop\1\KAI\proof"
def f(s):
    for n in ["seguisb.ttf","arialbd.ttf"]:
        try: return ImageFont.truetype(n,s)
        except: pass
    return ImageFont.load_default()
names=[("start_EPISODE.png","EP 01"),("start_ep02.png","EP 02"),("start_ep03.png","EP 03")]
tiles=[]
for fn,lab in names:
    p=os.path.join(ROOT,fn)
    if not os.path.exists(p): continue
    im=Image.open(p).convert("RGB")
    im=im.resize((480,int(im.height*480/im.width)),Image.LANCZOS)
    # non-black share = is anything rendered?
    px=im.load(); n=0
    for y in range(0,im.height,3):
        for x in range(0,im.width,3):
            r,g,b=px[x,y]
            if r+g+b>30: n+=1
    tiles.append((lab,im,n))
W=sum(t[1].width for t in tiles)+10*(len(tiles)+1)
H=max(t[1].height for t in tiles)+46
c=Image.new("RGB",(W,H),(20,20,24)); d=ImageDraw.Draw(c)
x=10
for lab,im,n in tiles:
    c.paste(im,(x,34))
    d.text((x+4,10),f"{lab}  ({n} lit samples)",font=f(15),fill=(120,255,180))
    x+=im.width+10
c.save(os.path.join(ROOT,"start_check.jpg"),quality=90)
print("wrote start_check.jpg",c.size,"tiles",len(tiles))
for lab,im,n in tiles: print(f"  {lab}: {n} lit samples -> {'OK' if n>200 else 'BLANK'}")
