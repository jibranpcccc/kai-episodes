from PIL import Image
p=r"C:\Users\jibra\Desktop\1\KAI\proof\ff_ep02.png"
im=Image.open(p).convert("RGB"); px=im.load(); W,H=im.size
bright=sum(1 for y in range(0,H,2) for x in range(0,W,2) if sum(px[x,y])>330)
dark=sum(1 for y in range(0,H,2) for x in range(0,W,2) if sum(px[x,y])<30)
tot=len(range(0,H,2))*len(range(0,W,2))
print(f"FIREFOX render {W}x{H}  bright={bright}  pureblack={dark} ({dark/tot*100:.0f}%)")
print("verdict:", "RENDERS CONTENT" if bright>300 else "BLANK")
