import re,os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
for f in ["EPISODE-02.html","EPISODE-03.html"]:
    h=open(os.path.join(ROOT,f),encoding="utf-8").read()
    vals=re.findall(r'data-in="([^"]*)"',h)
    bad=[v for v in vals if not re.fullmatch(r"[0-9.]+",v)]
    sfx=len(re.findall(r"\{t:[0-9.]+, ?f:'",h))
    print(f"{f:18} cues={len(vals):3d} unresolved={len(bad)} sfx={sfx} zoomcalc={'zoom:min' in h}")
    # show the first few cue times actually written
    print("   cue times:", ", ".join(vals[:8]))
