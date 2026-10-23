from PIL import Image
im=Image.open(r"C:\Users\jibra\Desktop\1\KAI\proof\ff_final.png").convert("RGB")
px=im.load(); W,H=im.size
bright=sum(1 for y in range(0,H,3) for x in range(0,W,3) if sum(px[x,y])>330)
# find horizontal extent of the stage box (non-pure-black)
xs=[x for x in range(0,W,4) if any(sum(px[x,y])>25 for y in range(0,H,20))]
print(f"firefox {W}x{H} bright={bright} stage-width~{max(xs)-min(xs) if xs else 0}px")
