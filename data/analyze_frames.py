import sys, os, glob, csv, json
import numpy as np, cv2

ROOT=r"C:\Users\jibra\Desktop\1\KAI"
fc=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
prof=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_profileface.xml")
print("cascades loaded:", not fc.empty(), not prof.empty())

def analyze(vid, face_every=4):
    d=os.path.join(ROOT,"frames",vid)
    files=sorted(glob.glob(d+r"\*.jpg"))
    if not files: print("no frames"); return None
    out=[]; prev=None
    for i,f in enumerate(files):
        im=cv2.imread(f)
        if im is None: continue
        small=cv2.resize(im,(480,270),interpolation=cv2.INTER_AREA)
        g=cv2.cvtColor(small,cv2.COLOR_BGR2GRAY).astype(np.float32)
        mean=float(g.mean()); std=float(g.std())
        dark=float((g<32).mean()); bright=float((g>205).mean())
        edges=cv2.Canny(g.astype(np.uint8),60,160)
        edge=float(edges.mean()/255)
        b,gg,r=small[:,:,0].astype(np.float32),small[:,:,1].astype(np.float32),small[:,:,2].astype(np.float32)
        mx=small.max(axis=2).astype(np.float32); mn=small.min(axis=2).astype(np.float32)
        sat=np.where(mx>60,(mx-mn)/np.maximum(mx,1),0); S=sat>0.45
        red=float((S&(r>120)&(r>gg+50)&(r>b+50)).mean())
        yel=float((S&(r>140)&(gg>110)&(b<100)&(np.abs(r-gg)<95)).mean())
        blu=float((S&(b>90)&(b>r+40)).mean())
        # motion / cut score vs previous
        cut=0.0
        if prev is not None:
            cut=float(np.abs(g-prev).mean())
        prev=g
        face=0; nf=0
        if i%face_every==0:
            gf=cv2.cvtColor(cv2.resize(im,(640,360)),cv2.COLOR_BGR2GRAY)
            gf=cv2.equalizeHist(gf)
            fs=fc.detectMultiScale(gf,1.15,6,minSize=(48,48))
            nf=len(fs); face=1 if nf>0 else 0
        out.append([i, round(i/2.0,1), round(mean,2), round(std,2), round(dark,4), round(bright,4),
                    round(edge,5), round(red,4), round(yel,4), round(blu,4), round(cut,2), face, nf])
    csvp=os.path.join(ROOT,"data",f"frames_{vid}.csv")
    with open(csvp,"w",newline="",encoding="utf-8") as fh:
        w=csv.writer(fh); w.writerow(["idx","t","mean","std","dark","bright","edge","red","yel","blu","cut","face","nfaces"]); w.writerows(out)
    a=np.array([[o[2],o[3],o[4],o[5],o[6],o[7],o[8],o[9],o[10],o[11]] for o in out],dtype=np.float32)
    cuts=[o[1] for o in out if o[10]>12]
    summ=dict(vid=vid,n=len(out),mean_brightness=round(float(a[:,0].mean()),1),
              dark_share=round(float(a[:,2].mean()),3), white_ink=round(float(a[:,3].mean()),3),
              edge=round(float(a[:,4].mean()),4), red=round(float(a[:,5].mean()),4),
              yellow=round(float(a[:,6].mean()),4), blue=round(float(a[:,7].mean()),4),
              cuts=len(cuts), cuts_per_min=round(len(cuts)/((len(out)/2)/60),1) if len(out)>2 else 0,
              face_share=round(float(a[:,9].mean()),3),
              cuts_t=cuts[:80])
    json.dump(summ,open(os.path.join(ROOT,"data",f"summary_{vid}.json"),"w"),indent=1)
    print(json.dumps({k:v for k,v in summ.items() if k!="cuts_t"}))
    return summ

if __name__=="__main__":
    for vid in sys.argv[1:]:
        analyze(vid)
