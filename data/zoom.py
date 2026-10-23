from PIL import Image
im=Image.open(r"C:\Users\jibra\Desktop\1\KAI\proof\_zoomtest.png").convert("RGB")
px=im.load(); w,h=im.size
# is the yellow frame visible and scaled to the viewport width?
yellow=sum(1 for y in range(0,h,2) for x in range(0,w,2) if px[x,y][0]>200 and px[x,y][1]>170 and px[x,y][2]<120)
print("image",im.size,"yellow px:",yellow)
print("top-left px:",px[2,2]," right edge px:",px[w-3,h//2])
