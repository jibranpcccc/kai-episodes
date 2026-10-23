from PIL import Image
import os
R=r"C:\Users\jibra\Desktop\1\KAI\proof"
for w in [900,1200,1600]:
    p=os.path.join(R,f"_zt_{w}.png"); im=Image.open(p).convert("RGB"); px=im.load(); W,H=im.size
    # find the yellow frame extent
    xs=[];ys=[]
    for y in range(0,H,2):
        for x in range(0,W,2):
            r,g,b=px[x,y]
            if r>200 and g>170 and b<120: xs.append(x); ys.append(y)
    if not xs: print(f"{W}x{H}: NO FRAME"); continue
    print(f"{W}x{H}: frame x[{min(xs)},{max(xs)}] y[{min(ys)},{max(ys)}]  "
          f"-> {'CENTRED & FITS' if min(xs)>=0 and max(xs)<=W-1 and min(ys)>=0 and max(ys)<=H-1 else 'OVERFLOW'}")
