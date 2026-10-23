from PIL import Image
im=Image.open(r"C:\Users\jibra\Desktop\1\KAI\proof\plain_ep02.png").convert("RGB")
px=im.load(); W,H=im.size
bright=sum(1 for y in range(0,H,2) for x in range(0,W,2) if sum(px[x,y])>330)
cols={}
for y in range(0,H,4):
    for x in range(0,W,4):
        c=px[x,y]; cols[c]=cols.get(c,0)+1
top=sorted(cols.items(),key=lambda kv:-kv[1])[:4]
print(f"plain {W}x{H} bright={bright}")
print("top colours:",[(f"#{r:02X}{g:02X}{b:02X}",n) for (r,g,b),n in top])
