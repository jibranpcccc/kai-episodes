p=r"C:\Users\jibra\Desktop\1\KAI\data\make_episodes.py"
s=open(p,encoding="utf-8").read()
a=".stat .n{{font-family:var(--sans);font-weight:800;letter-spacing:-.035em;line-height:.9}}"
b=".stat .n{{font-family:var(--sans);font-weight:800;letter-spacing:-.035em;line-height:1.04}}"
assert a in s
s=s.replace(a,b)
open(p,"w",encoding="utf-8").write(s)
print("line-height fixed")
