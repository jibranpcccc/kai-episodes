from PIL import Image, ImageDraw, ImageFont
import os
ROOT=r"C:\Users\jibra\Desktop\1\KAI\proof"
def font(s):
    for n in ["seguisb.ttf","arialbd.ttf"]:
        try: return ImageFont.truetype(n,s)
        except: pass
    return ImageFont.load_default()
names=[("frame_s1.png","01 HOOK"),("frame_s2.png","02 WEIGHTS vs KV"),
       ("frame_s3.png","03 THE SPILL"),("frame_s4.png","04 THE COST"),
       ("frame_s5.png","05 THE TABLE"),("frame_s6.png","06 BANDWIDTH"),("frame_s7.png","07 VERDICT")]
tiles=[]
for f,t in names:
    p=os.path.join(ROOT,f)
    if os.path.exists(p): tiles.append((t,Image.open(p).convert("RGB").resize((700,394),Image.LANCZOS)))
cols=2; rows=(len(tiles)+1)//2
c=Image.new("RGB",(cols*710+10, rows*(394+28)+10),(15,15,18)); d=ImageDraw.Draw(c)
for i,(t,im) in enumerate(tiles):
    x=10+(i%cols)*710; y=10+(i//cols)*(394+28)
    c.paste(im,(x,y)); d.text((x+4,y+396),t,font=font(15),fill=(248,207,51))
c.save(os.path.join(ROOT,"episode_frames.jpg"),quality=90)
print("wrote",c.size,len(tiles))
