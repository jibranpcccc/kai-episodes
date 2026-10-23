from PIL import Image
for t in (2,24):
    p=rf"C:\Users\jibra\Desktop\1\KAI\proof\render_t{t}.png"
    im=Image.open(p).convert("RGB"); px=im.load(); W,H=im.size
    b=sum(1 for y in range(0,H,3) for x in range(0,W,3) if sum(px[x,y])>330)
    print(f"t={t}s  {W}x{H}  bright={b}")
