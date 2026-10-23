import glob, os, re, collections
D=r"C:\Users\jibra\Desktop\1\KAI\kai_txt"
def text(p):
    out=[];seen=set()
    for line in open(p,encoding="utf-8",errors="ignore"):
        line=line.strip()
        if not line or line.startswith(("WEBVTT","Kind:","Language:","NOTE")) or "-->" in line: continue
        line=re.sub(r"<[^>]+>","",line).strip()
        if not line or line in seen: continue
        seen.add(line); out.append(line)
    return " ".join(out)
files=sorted(glob.glob(os.path.join(D,"*.en.vtt")))
allt=" ".join(text(p) for p in files)
words=allt.split()
print("corpus:", len(words), "words\n")

print("--- OPENINGS (first 45 words of each) ---")
for p in files[:3]:
    t=text(p)
    print(" •", " ".join(t.split()[:45]), "\n")

print("--- style signals per 1000 words ---")
low=allt.lower()
for pat,label in [(r"\byou\b","you"),(r"\byour\b","your"),(r"\?", "questions"),
                  (r"\bhere'?s\b","here's"),(r"\bbut\b","but"),
                  (r"\bso\b","so"),(r"\bactually\b","actually"),
                  (r"\bnobody\b","nobody"),(r"\bmost people\b","most people"),
                  (r"\bthe problem\b","the problem"),(r"\bthat'?s\b","that's"),
                  (r"\bwe\b","we"),(r"\bi\b","I")]:
    n=len(re.findall(pat,low))
    print(f"  {label:14} {n:5d}   ({n/len(words)*1000:5.1f} per 1k)")

print("\n--- top 3-word openers of sentences (transition style) ---")
sents=[s.strip() for s in re.split(r"(?<=[.!?])\s+", allt) if s.strip()]
c=collections.Counter(" ".join(s.split()[:2]).lower().strip(",.") for s in sents)
for k,v in c.most_common(18):
    print(f"  {v:4d}  {k}")
