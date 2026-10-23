import os
from PIL import Image
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
def bright(path):
    im=Image.open(path).convert("RGB"); px=im.load(); n=0
    for y in range(0,im.height,2):
        for x in range(0,im.width,2):
            r,g,b=px[x,y]
            if r+g+b>330: n+=1          # near-white ink only
    return n
for f in ["EPISODE.html","EPISODE-02.html","EPISODE-03.html"]:
    a=bright(os.path.join(ROOT,"proof",f"t_{f}.png"))
    b=bright(os.path.join(ROOT,"proof",f"t_nojs_{f}.png"))
    print(f"{f:18} bright px with JS: {a:5d}   without JS: {b:5d}   {'OK' if a>300 and b>300 else 'BLANK'}")
