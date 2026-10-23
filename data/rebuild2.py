import re, os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; P=os.path.join(ROOT,"EPISODE.html")
h=open(P,encoding="utf-8").read()

# explicit, hand-verified cue placement (phrase onsets measured on the new audio)
S=[0.00,4.10,14.31,20.64,25.88,32.36,36.17]
ABS={
 0:[0.10,0.40,0.66,0.93,1.15,1.42,2.38],
 1:[4.20,8.41,9.84,12.02],
 2:[14.41,17.73,19.20,19.60],
 3:[20.74,22.30],                 # cap, caption   (needle is JS)
 4:[25.98,25.98,28.50,30.81],
 5:[32.46,32.50,35.16,35.45],
 6:[36.30,38.19,40.32,41.40],
}
NEW={sc:[round(a-S[sc],2) for a in vals] for sc,vals in ABS.items()}
for sc,vals in NEW.items():
    m=re.search(r'(<section class="scene" data-scene="%d">.*?</section>)'%sc,h,re.S)
    blk=m.group(1); it=iter(vals)
    assert len(re.findall(r'data-in="[0-9.]+"',blk))==len(vals), sc
    nb=re.sub(r'data-in="[0-9.]+"',lambda _:'data-in="%s"'%next(it),blk,count=len(vals))
    h=h.replace(blk,nb)

JS={'segw':4.31,'segk':5.74,'ctx':7.92,'pour':19.20-14.31,'ndl':23.75-20.64}
for k,v in JS.items():
    h=re.sub(r"rel>=[0-9.]+( && !fired\.has\('%s'\))"%k, lambda m:"rel>=%.2f"%v+m.group(1), h)
h=re.sub(r"if\(i===0 && rel>=[0-9.]+\)", "if(i===0 && rel>=2.38)", h)

W=[20.355,35.885]
h=re.sub(r"const WIPES = \[[0-9., ]+\];", f"const WIPES = [{W[0]:.3f}, {W[1]:.3f}];", h)

sfx=[(8.41,'tick'),(9.84,'tick'),(14.41,'tick'),(17.73,'tick'),(18.87,'tick'),
     (W[0],'whoosh'),
     (25.98,'thud'),(28.50,'tick'),(30.81,'tick'),
     (32.50,'tick'),(35.16,'tick'),
     (W[1],'whoosh'),(40.32,'thud')]
h=re.sub(r"const SFX = \[.*?\];",
         "const SFX = [\n"+"\n".join(f"  {{t:{t:6.3f}, f:'{k}'}}," for t,k in sfx)+"\n];", h, flags=re.S)

open(P,"w",encoding="utf-8").write(h)
print("explicit cue map written")
for sc in sorted(NEW): print(f"  scene{sc+1}: {NEW[sc]}")
