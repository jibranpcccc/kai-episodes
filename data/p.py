import re, os
P=r"C:\Users\jibra\Desktop\1\KAI\EPISODE.html"
h=open(P,encoding="utf-8").read()
h=re.sub(r"rel>=[0-9.]+( && !fired\.has\('pour'\))", lambda m:"rel>=4.56"+m.group(1), h)
open(P,"w",encoding="utf-8").write(h)
print("pour -> 18.87s")
