from PIL import Image
p=r"C:\Users\jibra\Desktop\1\KAI\proof\ff_scene4.png"
im=Image.open(p).convert("RGB"); px=im.load(); W,H=im.size
bright=sum(1 for y in range(0,H,2) for x in range(0,W,2) if sum(px[x,y])>330)
print(f"FIREFOX scene render {W}x{H} bright={bright} ->", "OK" if bright>400 else "BLANK")
