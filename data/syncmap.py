import re, os
from PIL import Image, ImageDraw, ImageFont
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
W,H=1640,520
img=Image.new("RGB",(W,H),(13,17,16)); d=ImageDraw.Draw(img)
def f(sz,bold=False):
    for n in (["seguisb.ttf","arialbd.ttf"] if bold else ["segoeui.ttf","arial.ttf"]):
        try: return ImageFont.truetype(n,sz)
        except: pass
    return ImageFont.load_default()
TOTAL=51.23; X0,X1=150,1600
def X(t): return X0+(t/TOTAL)*(X1-X0)

# speech chunks measured from the mp3
chunks=[(0.00,3.26),(4.44,8.25),(9.03,10.18),(11.00,12.61),(12.89,14.97),(16.16,20.01),
        (20.79,21.87),(22.27,22.64),(23.84,26.20),(27.07,28.88),(30.06,30.95),(31.28,33.04),
        (33.37,34.94),(35.33,35.88),(37.07,38.10),(38.40,39.86),(40.66,41.66),(42.88,44.81),
        (45.60,47.61),(47.93,50.52)]
scenes=[(0.00,4.35),(4.35,16.07),(16.07,23.74),(23.74,29.96),(29.96,36.98),(36.98,42.77),(42.77,51.23)]
cues=[(8.88,"weights"),(10.85,"KV cache"),(12.79,"32K"),(18.60,"+6GB"),(20.67,"spill"),
      (26.92,"40→4"),(30.31,"16GB"),(31.51,"24GB"),(33.31,"48GB"),(40.66,"bw bar"),
      (41.03,"tape"),(42.97,"line 1"),(45.60,"line 2"),(47.93,"verdict")]
wipes=[23.455,42.485]
sfx=[(8.88,'tick'),(10.85,'tick'),(16.25,'tick'),(18.60,'tick'),(20.70,'tick'),(23.455,'whoosh'),
     (30.28,'thud'),(31.45,'tick'),(33.35,'tick'),(37.20,'tick'),(40.70,'tick'),(42.485,'whoosh'),(47.95,'thud')]

d.text((150,22),"EPISODE 01 — SYNC MAP   (voice chunks measured from audio/vo.mp3)",font=f(22,True),fill=(246,246,244))

# VOICE lane
d.text((28,86),"VOICE",font=f(13,True),fill=(168,171,167))
for a,b in chunks:
    d.rectangle([X(a),72,X(b),102],fill=(246,246,244))
# SCENE lane
d.text((28,146),"SCENES",font=f(13,True),fill=(168,171,167))
for i,(a,b) in enumerate(scenes):
    d.rectangle([X(a),132,X(b),162],fill=(28,38,36),outline=(60,70,67))
    d.text((X(a)+8,138),str(i+1),font=f(15,True),fill=(248,207,51))
    d.line([X(a),126,X(a),170],fill=(60,70,67))
# CUES lane
d.text((28,206),"BUILDS",font=f(13,True),fill=(168,171,167))
for t,lab in cues:
    d.line([X(t),192,X(t),236],fill=(248,207,51),width=2)
    d.text((X(t)-len(lab)*3,240),lab,font=f(11),fill=(248,207,51))
# WIPE lane
d.text((28,278),"WIPES",font=f(13,True),fill=(168,171,167))
for t in wipes:
    d.polygon([(X(t),286),(X(t)+9,298),(X(t),310),(X(t)-9,298)],fill=(4,94,239))
    d.text((X(t)-24,314),f"cut {t+0.285:.2f}s",font=f(11),fill=(90,150,255))
# SFX lane
d.text((28,352),"SFX",font=f(13,True),fill=(168,171,167))
col={'tick':(150,150,150),'whoosh':(4,94,239),'thud':(225,42,39)}
for t,k in sfx:
    d.line([X(t),342,X(t),366],fill=col[k],width=3)

# axis
d.line([X0,400,X1,400],fill=(60,70,67))
for s in range(0,56,5):
    d.line([X(s),396,X(s),404],fill=(60,70,67))
    d.text((X(s)-8,410),f"{s}s",font=f(12),fill=(110,114,111))

d.text((150,470),"yellow = visual build   ·   blue = colour wipe (full cover on the cut)   ·   red = thud   ·   grey = tick",
       font=f(13),fill=(110,114,111))
img.save(os.path.join(ROOT,"proof","sync_map.png"))
print("wrote proof/sync_map.png",img.size)
