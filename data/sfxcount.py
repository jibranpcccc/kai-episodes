import re,os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
h=open(os.path.join(ROOT,"EPISODE.html"),encoding="utf-8").read()
blk=re.search(r"const SFX = \[(.*?)\];",h,re.S).group(1)
items=re.findall(r"\{t:\s*([0-9.]+),\s*f:'(\w+)'\}",blk)
print("SFX cues:",len(items))
for t,k in items: print(f"   {float(t):6.2f}  {k}")
w=[float(x) for x in re.search(r"const WIPES = \[([0-9., ]+)\]",h).group(1).split(",")]
print("\nwipe cues present?", all(abs(float(t)-a)<0.01 for t,k in items for a in w if k=='whoosh') )
print("whooshes at:",[round(float(t),3) for t,k in items if k=='whoosh'], " wipes:",w)
