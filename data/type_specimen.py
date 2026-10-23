from PIL import Image, ImageDraw, ImageFont
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
im=Image.open(ROOT+r"\frames\NA9D49kQFuU\001302.jpg").convert("RGB")
crops=[
 ("chip: '4-BIT · 128K CONTEXT'",(146,225,478,270),3),
 ("row label + value: 'MAC STUDIO' / '40'",(840,420,1790,470),2),
 ("hero number: '70 tok/s'",(270,640,580,730),3),
 ("rank markers: '#1 #2'",(730,270,790,310),6),
 ("watermark: '<kaiexplainsyt>'",(1740,1030,1900,1065),5),
]
pad=10; W=1500
tiles=[]
for label,box,s in crops:
    c=im.crop(box)
    c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
    tiles.append((label,c))
H=sum(t[1].height+34+pad for t in tiles)+pad+40
canvas=Image.new("RGB",(W,H),(20,20,24)); d=ImageDraw.Draw(canvas)
def font(sz):
    for n in ["seguisb.ttf","arialbd.ttf"]:
        try: return ImageFont.truetype(n,sz)
        except: pass
    return ImageFont.load_default()
d.text((10,10),"TYPE SPECIMEN  (frames from NA9D49kQFuU, upscaled)",font=font(22),fill=(255,255,255))
y=46
for label,c in tiles:
    d.text((10,y),label,font=font(15),fill=(120,255,180)); y+=22
    cw=min(c.width,W-20); canvas.paste(c.crop((0,0,cw,c.height)),(10,y)); y+=c.height+pad
canvas.save(ROOT+r"\data\type_specimen.jpg",quality=95)
print("wrote type_specimen.jpg",canvas.size)
# measure cap height of 'MAC STUDIO'
c=im.crop((840,420,1300,470)).convert("L")
import numpy as np
a=np.asarray(c)
rows=np.where((a>150).sum(axis=1)>0)[0]
print("MAC STUDIO ink rows:",rows.min(),rows.max(),"cap height px ≈",rows.max()-rows.min()+1)
c2=im.crop((270,640,430,730)).convert("L"); a2=np.asarray(c2)
r2=np.where((a2>150).sum(axis=1)>0)[0]
print("'70' ink rows:",r2.min(),r2.max(),"digit height px ≈",r2.max()-r2.min()+1)
