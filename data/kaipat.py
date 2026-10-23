import glob, os, re, json, statistics as st
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

rows=[]
for p in sorted(glob.glob(os.path.join(D,"*.en.vtt"))):
    vid=os.path.basename(p).split(".")[0]
    info=os.path.join(r"C:\Users\jibra\Desktop\1\KAI\videos",vid+".info.json")
    d=json.load(open(info,encoding="utf-8")) if os.path.exists(info) else {}
    dur=d.get("duration") or 0
    t=text(p); w=len(t.split())
    sents=[s for s in re.split(r"(?<=[.!?])\s+", t) if len(s.split())>2]
    nums=len(re.findall(r"\b\d[\d,\.]*\b", t))
    rows.append(dict(vid=vid, title=(d.get("title") or "")[:40], dur=dur, words=w,
                     wpm=w/(dur/60) if dur else 0,
                     avg_sent=st.mean([len(s.split()) for s in sents]) if sents else 0,
                     nums_per_min=nums/(dur/60) if dur else 0,
                     chapters=len(d.get("chapters") or [])))
print(f"{'video':12} {'dur':>6} {'words':>6} {'wpm':>5} {'avgsent':>8} {'num/min':>8} {'chapters':>8}")
for r in rows:
    print(f"{r['vid']:12} {r['dur']//60:>3}:{r['dur']%60:02d} {r['words']:>6} {r['wpm']:>5.0f} {r['avg_sent']:>8.1f} {r['nums_per_min']:>8.1f} {r['chapters']:>8}")
print()
print("MEDIANS: wpm %.0f | avg sentence %.1f words | numbers/min %.1f | chapters %d"
      % (st.median([r['wpm'] for r in rows]), st.median([r['avg_sent'] for r in rows]),
         st.median([r['nums_per_min'] for r in rows]), st.median([r['chapters'] for r in rows])))
print("chapter length: %.1f s" % (st.median([r['dur']/max(r['chapters'],1) for r in rows])))
