import os
from PIL import Image
R=r"C:\Users\jibra\Desktop\1\KAI\proof"
for f in ["EPISODE.html","EPISODE-02.html","EPISODE-03.html"]:
    p=os.path.join(R,"fx_"+f+".png"); im=Image.open(p).convert("RGB"); px=im.load(); W,H=im.size
    bright=sum(1 for y in range(0,H,2) for x in range(0,W,2) if sum(px[x,y])>330)
    print(f"{f:18} {W}x{H} bright={bright:5d} {'OK' if bright>300 else 'BLANK'}")
