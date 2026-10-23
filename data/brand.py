import glob, os, numpy as np, cv2
from sklearn.cluster import KMeans
ROOT=r"C:\Users\jibra\Desktop\1\KAI"

# 1) true canvas black from an almost-empty first frame
im=cv2.imread(os.path.join(ROOT,"frames","NA9D49kQFuU","000000.jpg"))
pts=[(60,60),(60,1820),(1020,60),(1020,1820),(540,960),(300,1500),(900,300)]
print("canvas samples (hex):", [f"#{int(im[y,x][2]):02X}{int(im[y,x][1]):02X}{int(im[y,x][0]):02X}" for y,x in pts])
print("mean bg:", [int(v) for v in im.reshape(-1,3).mean(axis=0)][::-1])

# 2) brand accents from high-quality thumbnails
px=[]
for f in glob.glob(os.path.join(ROOT,"thumbs","*.jpg"))[:149]:
    a=cv2.imread(f)
    if a is None: continue
    a=cv2.resize(a,(480,270),interpolation=cv2.INTER_AREA)
    v=a.reshape(-1,3).astype(np.float32)
    mx=v.max(axis=1); mn=v.min(axis=1)
    sat=np.where(mx>60,(mx-mn)/np.maximum(mx,1),0)
    m=(sat>0.55)&(mx>90)
    px.append(v[m])
px=np.vstack([p for p in px if len(p)>50])
print("accent px:",len(px))
km=KMeans(n_clusters=8,n_init=6,random_state=0).fit(px[::2])
lab=np.bincount(km.labels_,minlength=8)
order=np.argsort(-lab)
print("\nTHUMBNAIL BRAND ACCENTS:")
for i in order:
    b,g,r=km.cluster_centers_[i]
    print(f"  #{int(r):02X}{int(g):02X}{int(b):02X}   {lab[i]/lab.sum()*100:5.1f}%")

# 3) ink whites from thumbnails
px2=[]
for f in glob.glob(os.path.join(ROOT,"thumbs","*.jpg"))[:149]:
    a=cv2.imread(f)
    if a is None: continue
    a=cv2.resize(a,(480,270),interpolation=cv2.INTER_AREA)
    v=a.reshape(-1,3).astype(np.float32)
    mx=v.max(axis=1); mn=v.min(axis=1)
    sat=np.where(mx>10,(mx-mn)/np.maximum(mx,1),0)
    m=(sat<0.12)&(mx>200)
    px2.append(v[m])
px2=np.vstack([p for p in px2 if len(p)>50])
print("\nINK WHITES:", f"#{int(np.median(px2[:,2])):02X}{int(np.median(px2[:,1])):02X}{int(np.median(px2[:,0])):02X}",
      " mean:", f"#{int(px2[:,2].mean()):02X}{int(px2[:,1].mean()):02X}{int(px2[:,0].mean()):02X}")
