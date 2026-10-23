import cv2, numpy as np
a=cv2.imread(r"C:\Users\jibra\Desktop\1\KAI\frames\NA9D49kQFuU\001302.jpg",cv2.IMREAD_GRAYSCALE)
col=a[:,1500]
bright=col>170
# find runs of bright pixels = horizontal borders
runs=[];s=None
for i,v in enumerate(bright):
    if v and s is None: s=i
    if not v and s is not None:
        runs.append((s,i-1)); s=None
if s is not None: runs.append((s,len(bright)-1))
print("bright runs at x=1500 (top,bottom,thickness):")
for s,e in runs:
    print(f"   y {s:4d}-{e:4d}  thick={e-s+1}")
print("\nrow edges -> derive card tops/bottoms")
tops=[s for s,e in runs if 200<s<900]
print("edges:",tops)
if len(tops)>=4:
    gaps=np.diff(tops)
    print("deltas between consecutive edges:",list(gaps))
