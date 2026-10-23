import re
h=open(r"C:\Users\jibra\Desktop\1\KAI\BYTE-02.html",encoding="utf-8").read()
sc=[(float(a),float(b)) for a,b in re.findall(r"\{s:\s*([0-9.]+),\s*e:\s*([0-9.]+)\}",h)]
for i,(a,b) in enumerate(sc,1): print(f"  scene {i:2}: {a:6.1f} -> {b:6.1f}  ({b-a:4.1f}s)")
print("total", max(b for _,b in sc))
