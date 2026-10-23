import cv2, numpy as np, json
p=r"C:\Users\jibra\Desktop\1\KAI\frames\NA9D49kQFuU\001302.jpg"
im=cv2.imread(p); h,w,_=im.shape
print("frame size:",w,"x",h)
def bg(y,x): 
    b,g,r=im[y,x]; return f"#{r:02X}{g:02X}{b:02X}"
print("bg corners:", bg(5,5), bg(5,w-6), bg(h-6,5), bg(h//2,w//2))
print("bg top strip mean:", [int(v) for v in im[0:40].reshape(-1,3).mean(axis=0)][::-1])
# horizontal scan across table row #2 to find border
y=380
row=im[y]
bright=np.where(row.max(axis=1)>200)[0]
print("bright x-runs at y=380 (first 12):", bright[:12])
# find card left/right edges: look for sustained bright columns in table region
region=im[330:430, 700:1900]
colmax=region.max(axis=(0,2))
edges=np.where(colmax>200)[0]+700
print("card edge x positions (sample):", edges[:6], "...", edges[-6:])
# border thickness at row 2 top edge
for yy in range(300,340):
    seg=im[yy,820:1800]
    if (seg.max(axis=1)>200).mean()>0.8:
        print("row#2 top border starts y=",yy); break
# vertical extent of a row
col=im[:, 900]
b=np.where(col.max(axis=1)>200)[0]
print("bright y positions at x=900:", b[:10])
# grain check: std in a flat bg patch
patch=im[h-200:h-100, 100:400].astype(np.float32)
print("flat bg patch: mean=%.1f std=%.2f (std>1.5 => grain/noise)"%(patch.mean(),patch.std()))
