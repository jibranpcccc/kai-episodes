import re, io
p=r"C:\Users\jibra\Desktop\1\KAI\core\kai.css"
s=open(p,encoding="utf-8").read()
s=s.replace("height:86px;padding:0 30px;border:var(--stroke) solid var(--white);","height:84px;padding:0 30px;border:var(--stroke) solid var(--white);")
open(p,"w",encoding="utf-8").write(s)
p2=r"C:\Users\jibra\Desktop\1\KAI\core\proof-slide.html"
s2=open(p2,encoding="utf-8").read()
s2=s2.replace(".table{position:absolute;left:806px;top:325px;width:999px;display:flex;flex-direction:column;gap:30px}",
              ".table{position:absolute;left:806px;top:346px;width:999px;display:flex;flex-direction:column;gap:22px}")
open(p2,"w",encoding="utf-8").write(s2)
print("patched row height=84, gap=22, table top=346")
