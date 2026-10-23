import re
h=open(r"C:\Users\jibra\Desktop\1\KAI\BYTE-03.html",encoding="utf-8").read()
sc=[(float(a),float(b)) for a,b in re.findall(r"\{s:\s*([0-9.]+),\s*e:\s*([0-9.]+)\}",h)]
secs=re.findall(r'<section class="scene[^"]*" data-scene="\d+">(.*?)</section>',h,re.S)
real=[];ticks=[]
for i,s2 in enumerate(secs):
    rail=re.search(r'<div class="rail">(.*?)</div>', s2, re.S)
    body=s2 if not rail else s2.replace(rail.group(0),"")
    for v in re.findall(r'data-in="([0-9.]+)"', body): real.append(sc[i][0]+float(v))
    if rail:
        for v in re.findall(r'data-in="([0-9.]+)"', rail.group(1)): ticks.append(sc[i][0]+float(v))
real=sorted(set(real)); allv=sorted(set(real+ticks))
def rep(n,a):
    g=[q-p for p,q in zip(a,a[1:])]
    print(f"{n:22} events {len(a):4}  max {max(g):5.2f}s  median {sorted(g)[len(g)//2]:4.2f}s  over2s {sum(1 for x in g if x>2)}")
rep("meaningful reveals", real); rep("with rail ticks", allv)
