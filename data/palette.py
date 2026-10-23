import glob, os, numpy as np, cv2, json
from sklearn.cluster import KMeans
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
vid="NA9D49kQFuU"
files=sorted(glob.glob(os.path.join(ROOT,"frames",vid,"*.jpg")))
sel=files[::40][:60]
px=[]
for f in sel:
    im=cv2.imread(f)
    if im is None: continue
    im=cv2.resize(im,(640,360),interpolation=cv2.INTER_AREA)
    hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    v=im.reshape(-1,3).astype(np.float32)
    mx=v.max(axis=1); mn=v.min(axis=1)
    sat=np.where(mx>50,(mx-mn)/np.maximum(mx,1),0)
    m=(sat>0.5)&(mx>70)          # saturated accents
    px.append(v[m])
px=np.vstack([p for p in px if len(p)>0])
print("accent pixels sampled:",len(px))
km=KMeans(n_clusters=6,n_init=4,random_state=0).fit(px[::3])
for c,lbl in sorted(zip(km.cluster_centers_,np.bincount(km.labels_,minlength=6)),key=lambda t:-t[1]):
    r,g,b=c[::-1]
    print(f"  #{int(r):02X}{int(g):02X}{int(b):02X}  share={lbl/len(km.labels_)*100:5.1f}%")

print("\n--- neutral ink (text/lines) ---")
gr=[]
for f in sel:
    im=cv2.imread(f)
    if im is None: continue
    im=cv2.resize(im,(640,360),interpolation=cv2.INTER_AREA)
    v=im.reshape(-1,3).astype(np.float32)
    mx=v.max(axis=1); mn=v.min(axis=1)
    sat=np.where(mx>10,(mx-mn)/np.maximum(mx,1),0)
    m=(sat<0.25)&(mx>70)
    gr.append(v[m])
gr=np.vstack(gr)
km2=KMeans(n_clusters=5,n_init=4,random_state=0).fit(gr[::5])
for c,lbl in sorted(zip(km2.cluster_centers_,np.bincount(km2.labels_,minlength=5)),key=lambda t:-t[1]):
    r,g,b=c[::-1]
    print(f"  #{int(r):02X}{int(g):02X}{int(b):02X}  share={lbl/len(km2.labels_)*100:5.1f}%")
