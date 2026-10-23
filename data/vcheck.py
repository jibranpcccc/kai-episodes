import re,os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
h=open(os.path.join(ROOT,"VOICES.html"),encoding="utf-8").read()
slugs=re.findall(r'\{slug:"([a-z]+)"',h)
print("voices in page:",len(slugs))
bad=[s for s in slugs if not os.path.exists(os.path.join(ROOT,"voice_samples",s+".mp3"))]
print("missing audio:", bad if bad else "none")
