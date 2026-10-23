import re, os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
p=os.path.join(ROOT,"EPISODE.html")
h=open(p,encoding="utf-8").read()
orig=h

# ---------- 1. per-scene data-in values, in document order ----------
NEW={1:[0.20,4.53,6.50,8.44],     # weights @8.88s, KV @10.85s, context @12.79s
     2:[0.15,2.53,5.05,5.45],     # +6GB tape @18.6s, RAM box @21.1s, caption @21.5s
     4:[0.10,0.35,1.55,3.35],
     5:[0.10,0.35,3.68,4.05],     # bandwidth bar @40.66s, tape @41.03s
     6:[0.20,2.83,5.16,7.23]}     # line2 @45.6s, tape @47.93s, watermark @50.0s
for n,vals in NEW.items():
    m=re.search(r'(<section class="scene" data-scene="%d">.*?</section>)'%n, h, re.S)
    blk=m.group(1)
    found=re.findall(r'data-in="[0-9.]+"', blk)
    assert len(found)==len(vals), (n,len(found),len(vals))
    it=iter(vals)
    nb=re.sub(r'data-in="[0-9.]+"', lambda _: 'data-in="%s"'%next(it), blk, count=len(vals))
    h=h.replace(blk,nb)

# ---------- 2. in-scene trigger thresholds ----------
js=[("if(rel>=0.90 && !fired.has('segw'))","if(rel>=4.53 && !fired.has('segw'))"),
    ("if(rel>=5.00 && !fired.has('segk'))","if(rel>=6.50 && !fired.has('segk'))"),
    ("if(rel>=7.60 && !fired.has('ctx'))","if(rel>=8.44 && !fired.has('ctx'))"),
    ("if(rel>=2.40 && !fired.has('pour'))","if(rel>=4.60 && !fired.has('pour'))"),
    ("if(rel>=0.80 && !fired.has('ndl'))","if(rel>=3.18 && !fired.has('ndl'))")]
for a,b in js:
    assert a in h, a
    h=h.replace(a,b)

# ---------- 3. wipes must reach full cover exactly on the cut ----------
# cut1 23.74 - 0.285 = 23.455 ; cut2 42.77 - 0.285 = 42.485
h=h.replace("const WIPES = [23.30, 42.30];","const WIPES = [23.455, 42.485];")
assert "23.455" in h

# ---------- 4. rebuild the SFX cue list on speech onsets ----------
old=re.search(r"const SFX = \[.*?\];", h, re.S).group(0)
new="""const SFX = [
  {t: 8.88,   f:'tick'},
  {t:10.85,   f:'tick'},
  {t:16.25,   f:'tick'},
  {t:18.60,   f:'tick'},
  {t:20.70,   f:'tick'},
  {t:23.455,  f:'whoosh'},
  {t:30.28,   f:'thud'},
  {t:31.45,   f:'tick'},
  {t:33.35,   f:'tick'},
  {t:37.20,   f:'tick'},
  {t:40.70,   f:'tick'},
  {t:42.485,  f:'whoosh'},
  {t:47.95,   f:'thud'}
];"""
h=h.replace(old,new)

open(p,"w",encoding="utf-8").write(h)
print("patched:", len(orig),"->",len(h),"bytes")
print("data-in rewrites:", sum(len(v) for v in NEW.values()))
