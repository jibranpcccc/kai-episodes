import csv, numpy as np, os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
rows=list(csv.DictReader(open(os.path.join(ROOT,"data","frames_NA9D49kQFuU.csv"),encoding="utf-8")))
cut=np.array([float(r["cut"]) for r in rows])
t=np.array([float(r["t"]) for r in rows])
dur=t[-1]
print(f"duration {dur:.0f}s  frames {len(rows)}  (2 fps)")
print("\nframe-diff distribution (mean abs diff 0-255):")
for p in [50,75,90,95,99,99.5]:
    print(f"  p{p:<4} = {np.percentile(cut,p):6.2f}")
print(f"  max   = {cut.max():6.2f}")
print("\nstatic share (diff<1):  %.1f%%" % ((cut<1).mean()*100))
print("micro-build share (1-4): %.1f%%" % (((cut>=1)&(cut<4)).mean()*100))
print("big change share (>12):  %.1f%%" % ((cut>12).mean()*100))
for th,name in [(2,"build events"),(6,"major changes"),(12,"slide changes")]:
    n=(cut>th).sum()
    print(f"{name:14} (>{th:>2}) = {n:4d}  => {n/(dur/60):5.1f}/min   avg gap {dur/max(n,1):5.1f}s")
print("\n--- composition: content bounding box (luma>40) ---")
import cv2, glob
files=sorted(glob.glob(os.path.join(ROOT,"frames","NA9D49kQFuU","*.jpg")))
bw=[];bh=[];cx=[];cy=[]
for f in files[::6]:
    im=cv2.imread(f, cv2.IMREAD_GRAYSCALE)
    if im is None: continue
    m=(im>40).astype(np.uint8)
    if m.sum()<500: continue
    ys,xs=np.where(m>0)
    bw.append((xs.max()-xs.min())/im.shape[1]); bh.append((ys.max()-ys.min())/im.shape[0])
    cx.append(((xs.min()+xs.max())/2)/im.shape[1]-0.5); cy.append(((ys.min()+ys.max())/2)/im.shape[0]-0.5)
print(f"content width  : median {np.median(bw)*100:5.1f}% of frame  (p10 {np.percentile(bw,10)*100:.0f}%  p90 {np.percentile(bw,90)*100:.0f}%)")
print(f"content height : median {np.median(bh)*100:5.1f}% of frame  (p10 {np.percentile(bh,10)*100:.0f}%  p90 {np.percentile(bh,90)*100:.0f}%)")
print(f"center offset X: median {np.median(cx)*100:+.1f}%   Y: median {np.median(cy)*100:+.1f}%  (0 = perfectly centred)")
print(f"=> safe margins ≈ left/right {100-np.median(bw)*100:.0f}% each side")
