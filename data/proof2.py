from PIL import Image, ImageDraw, ImageFont
import os
ROOT=r"C:\Users\jibra\Desktop\1\KAI\proof"
def f(s):
    for n in ["seguisb.ttf","arialbd.ttf"]:
        try: return ImageFont.truetype(n,s)
        except: pass
    return ImageFont.load_default()
files=[("t_EPISODE-02.html.png","EP 02 · with JS"),("t_nojs_EPISODE-02.html.png","EP 02 · JS blocked")]
tiles=[]
for fn,lab in files:
    p=os.path.join(ROOT,fn)
    if os.path.exists(p):
        im=Image.open(p).convert("RGB"); im=im.resize((620,int(im.height*620/im.width)),Image.LANCZOS)
        tiles.append((lab,im))
W=sum(t[1].width for t in tiles)+30; H=max(t[1].height for t in tiles)+50
c=Image.new("RGB",(W,H),(25,25,28)); d=ImageDraw.Draw(c)
x=10
for lab,im in tiles:
    c.paste(im,(x,38)); d.text((x,12),lab,font=f(16),fill=(120,255,180)); x+=im.width+10
c.save(os.path.join(ROOT,"standalone_proof.jpg"),quality=92)
print("wrote standalone_proof.jpg",c.size)
