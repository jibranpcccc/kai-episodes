import csv, numpy as np, os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
rows=list(csv.DictReader(open(os.path.join(ROOT,"data","frames_NA9D49kQFuU.csv"),encoding="utf-8")))
t=np.array([float(r["t"]) for r in rows]); y=np.array([float(r["yel"]) for r in rows]); b=np.array([float(r["blu"]) for r in rows])
def groups(mask,gap=1.0):
    out=[];cur=[]
    for i,f in enumerate(mask):
        if f:
            if cur and t[i]-t[cur[-1]]>gap: out.append(cur);cur=[]
            cur.append(i)
        else:
            if cur: out.append(cur);cur=[]
    if cur: out.append(cur)
    return out
wipes=[g for g in groups((y>0.30)|(b>0.30)) if len(g)>=1]
print(f"colour-wipe events: {len(wipes)}  ({(len(wipes))/(t[-1]/60):.2f}/min)")
for g in wipes:
    kind="YELLOW" if y[g[len(g)//2]]>b[g[len(g)//2]] else "BLUE"
    print(f"   {t[g[0]]:7.1f}s -> {t[g[-1]]:7.1f}s  {kind:6}  peak={max(y[g].max(),b[g].max()):.2f}  sample_frames={len(g)}")
print(f"\ncream/note-card frames (bright 0.15-0.45 & low colour): ", int(((np.array([float(r['bright']) for r in rows])>0.15)).sum()))
