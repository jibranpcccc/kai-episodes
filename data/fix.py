p=r"C:\Users\jibra\Desktop\1\KAI\EPISODE.html"
s=open(p,encoding="utf-8").read()
rep=[
 # S1 breathing room
 (".cmp-col{display:flex;flex-direction:column;align-items:center;gap:20px;position:relative}",
  ".cmp-col{display:flex;flex-direction:column;align-items:center;gap:28px;position:relative}"),
 # S2 labels: push below the bar, split widths
 (".bar-lab{display:flex;justify-content:space-between;width:980px;margin-top:-24px}",
  ".bar-lab{display:flex;justify-content:space-between;width:980px;margin-top:18px}"),
 (".bar-lab div{display:flex;flex-direction:column;gap:6px}",
  ".bar-lab div{display:flex;flex-direction:column;gap:6px;width:48%}\n  .bar-lab div:last-child{align-items:flex-end;text-align:right}"),
 # S3 chip out of the clip zone
 (".spill-chip{position:absolute;right:-52px;top:10px}",
  ".spill-chip{position:absolute;right:-14px;top:-62px}"),
 # S4 pivot the needle on the true arc centre (260,260), length = radius
 ("#needle{position:absolute;left:50%;top:0;width:5px;height:230px;background:#F6F6F4;border-radius:3px;",
  "#needle{position:absolute;left:50%;top:60px;width:5px;height:200px;background:#F6F6F4;border-radius:3px;"),
 (".ghub{position:absolute;left:50%;top:230px;",
  ".ghub{position:absolute;left:50%;top:260px;"),
 # S6 value column must not wrap
 (".hval{width:110px;text-align:right;",
  ".hval{width:150px;white-space:nowrap;text-align:right;"),
 # S2 shorter right-hand label
 ('<span class="n az">KV cache</span><span class="u">10 GB &middot; grows with context</span>',
  '<span class="n az">KV cache</span><span class="u">10 GB &middot; variable</span>'),
]
for a,b in rep:
    if a not in s: print("NOT FOUND:", a[:60])
    s=s.replace(a,b)
open(p,"w",encoding="utf-8").write(s)
print("patched")
