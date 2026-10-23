import cv2, numpy as np
a=cv2.imread(r"C:\Users\jibra\Desktop\1\KAI\frames\NA9D49kQFuU\001302.jpg",cv2.IMREAD_GRAYSCALE)
b=cv2.imread(r"C:\Users\jibra\Desktop\1\KAI\proof\replica.png",cv2.IMREAD_GRAYSCALE)
def bbox(img):
    m=(img>45).astype(np.uint8)
    m[1000:,1650:]=0          # remove watermark
    ys,xs=np.where(m>0)
    return xs.min(),ys.min(),xs.max(),ys.max()
for name,img in [("ORIGINAL",a),("REPLICA",b)]:
    x0,y0,x1,y1=bbox(img)
    print(f"{name:9} bbox x[{x0},{x1}] y[{y0},{y1}]  w={x1-x0} h={y1-y0}  centre=({(x0+x1)//2},{(y0+y1)//2})")
ax0,ay0,ax1,ay1=bbox(a); bx0,by0,bx1,by1=bbox(b)
print(f"\ndelta: dx={bx0-ax0:+d}  dy={by0-ay0:+d}   (how far the replica must move)")
print(f"height delta={ (by1-by0)-(ay1-ay0):+d}   width delta={ (bx1-bx0)-(ax1-ax0):+d}")
