import os, glob, json, subprocess, numpy as np, cv2
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
ids=[l.strip() for l in open(os.path.join(ROOT,"data","ids.txt")) if l.strip()]
fc=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
out={}
for vid in ids:
    mp4=os.path.join(ROOT,"videos",vid+".mp4")
    if not os.path.exists(mp4): print("missing",vid); continue
    tmp=os.path.join(ROOT,"data","_coarse"); os.makedirs(tmp,exist_ok=True)
    for f in glob.glob(tmp+r"\*.jpg"): os.remove(f)
    # 1 frame every 4s at 640x360
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-i",mp4,"-vf","fps=1/4,scale=640:-2","-q:v","4",tmp+r"\f%05d.jpg"],check=False)
    fr=sorted(glob.glob(tmp+r"\*.jpg"))
    st=[];faces=0
    prev=None; cuts=0
    for i,f in enumerate(fr):
        im=cv2.imread(f)
        if im is None: continue
        g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY).astype(np.float32)
        b,gg,r=im[:,:,0].astype(np.float32),im[:,:,1].astype(np.float32),im[:,:,2].astype(np.float32)
        mx=im.max(axis=2).astype(np.float32); mn=im.min(axis=2).astype(np.float32)
        sat=np.where(mx>60,(mx-mn)/np.maximum(mx,1),0); S=sat>0.45
        st.append([g.mean(),(g<32).mean(),(g>205).mean(),
                   float((S&(r>120)&(r>gg+50)&(r>b+50)).mean()),
                   float((S&(r>140)&(gg>110)&(b<100)&(np.abs(r-gg)<95)).mean()),
                   float((S&(b>90)&(b>r+40)).mean())])
        if prev is not None and np.abs(g-prev).mean()>12: cuts+=1
        prev=g
        if i%5==0:
            gf=cv2.equalizeHist(g.astype(np.uint8))
            if len(fc.detectMultiScale(gf,1.15,6,minSize=(40,40))): faces+=1
    a=np.array(st)
    n=max(len(st),1)
    out[vid]=dict(frames_sampled=len(st),bright=round(float(a[:,0].mean()),1),dark=round(float(a[:,1].mean()),3),
                  ink=round(float(a[:,2].mean()),4),red=round(float(a[:,3].mean()),4),
                  yellow=round(float(a[:,4].mean()),4),blue=round(float(a[:,5].mean()),4),
                  cuts_4s=cuts, face_share=round(faces/max((len(st)+4)//5,1),3))
    print(vid, out[vid], flush=True)
json.dump(out,open(os.path.join(ROOT,"data","coarse_all.json"),"w"),indent=1)
print("saved coarse_all.json")
