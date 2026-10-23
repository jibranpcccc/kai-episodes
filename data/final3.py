import os
from PIL import Image
R=r"C:\Users\jibra\Desktop\1\KAI\proof"
for f in ["EPISODE.html","EPISODE-02.html","EPISODE-03.html"]:
    p=os.path.join(R,"final_"+f+".png")
    if not os.path.exists(p): print(f,"MISSING"); continue
    im=Image.open(p).convert("RGB"); px=im.load(); W,H=im.size
    bright=sum(1 for y in range(0,H,2) for x in range(0,W,2) if sum(px[x,y])>330)
    # does ink reach the middle band? (proves it is centred, not clipped)
    mid=sum(1 for y in range(H//3,2*H//3,2) for x in range(W//3,2*W//3,2) if sum(px[x,y])>330)
    print(f"{f:18} {W}x{H}  bright={bright:5d}  centre-band={mid:5d}  {'OK' if bright>300 and mid>50 else 'SUSPECT'}")
