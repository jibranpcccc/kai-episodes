import re, json
h=open(r"C:\Users\jibra\Desktop\1\KAI\BYTE-01.html",encoding="utf-8").read()
sc=[(float(a),float(b)) for a,b in re.findall(r"\{s:\s*([0-9.]+),\s*e:\s*([0-9.]+)\}",h)]
total=float(re.search(r"total: ([0-9.]+)",h).group(1))
events=[]
for i,(a,b) in enumerate(sc):
    block=re.search(r'<section class="scene" data-scene="%d">(.*?)</section>'%i,h,re.S).group(1)
    for v in re.findall(r'data-in="([0-9.]+)"',block):
        events.append(round(a+float(v),3))
events=sorted(set(events))
print(f"visual events: {len(events)}   episode: {total:.2f}s   average gap: {total/max(len(events),1):.2f}s\n")
print(f"{'gap':>6}  {'from':>6} -> {'to':>6}")
print("-"*30)
bad=0
for p,q in zip(events, events[1:]):
    g=q-p
    if g>2.0:
        bad+=1
        print(f"{g:6.2f}  {p:6.2f} -> {q:6.2f}   <-- OVER")
print(f"\ngaps over 2.0s: {bad} of {len(events)-1}")
print(f"longest gap  : {max((q-p) for p,q in zip(events,events[1:])):.2f}s")
