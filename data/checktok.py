import re,os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
for f in ["EPISODE.html","EPISODE-02.html","EPISODE-03.html"]:
    h=open(os.path.join(ROOT,f),encoding="utf-8").read()
    vals=re.findall(r'data-in="([^"]*)"',h)
    bad=[v for v in vals if not re.fullmatch(r"[0-9.]+",v)]
    print(f"{f:18} cues={len(vals):3d}  unresolved={len(bad):3d}  {'OK' if not bad else 'BROKEN: '+str(bad[:3])}")
