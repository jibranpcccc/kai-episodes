import re,os,subprocess,json
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
for ep in ["ep02","ep03"]:
    p=os.path.join(ROOT,"episodes",ep,"index.html")
    h=open(p,encoding="utf-8").read()
    # inline script (EPISODE object) syntax
    js="\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    t=os.path.join(ROOT,"data","_c.js"); open(t,"w",encoding="utf-8").write(js)
    r=subprocess.run(["node","--check",t],capture_output=True,text=True)
    print(f"{ep}: inline JS {'PASS' if r.returncode==0 else 'FAIL'}")
    if r.returncode: print(r.stderr[:300])
    os.remove(t)
    sc=re.search(r"scenes: \[(.*?)\]",h,re.S).group(1)
    sc=[(float(a),float(b)) for a,b in re.findall(r"\{s:\s*([\d.]+),\s*e:\s*([\d.]+)\}",sc)]
    tot=float(re.search(r"total: ([\d.]+)",h).group(1))
    bad=0; ch=[]; prev=-1
    for f in range(int(tot*60)+1):
        t2=f/60; idx=0
        for i,(s,e) in enumerate(sc):
            if t2>=s: idx=i
        if idx<0 or idx>=len(sc): bad+=1
        if idx!=prev: ch.append(idx+1); prev=idx
    print(f"{ep}: total={tot}s scenes={len(sc)} bad_frames={bad} switch_order={ch}")
