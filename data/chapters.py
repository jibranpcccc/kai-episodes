import json, glob, os, re, csv
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
files=glob.glob(ROOT+r"\videos\*.info.json")
print(f"info.json files: {len(files)}\n")
for f in sorted(files):
    d=json.load(open(f,encoding="utf-8"))
    v=d.get("view_count") or 0; lk=d.get("like_count") or 0; cm=d.get("comment_count") or 0
    print("="*96)
    print(f"{d['id']}  {d['title']}")
    print(f"  views={v:,}  likes={lk:,} ({lk/max(v,1)*100:.2f}%)  comments={cm:,} ({cm/max(v,1)*1000:.2f}/1k)  dur={d['duration']}s  date={d.get('upload_date')}")
    ch=d.get("chapters") or []
    print(f"  chapters={len(ch)}  desc_len={len(d.get('description') or '')}  tags={len(d.get('tags') or [])}")
    for c in ch:
        m,s=divmod(int(c['start_time']),60)
        print(f"     {m:>2}:{s:02d}  {c['title']}")
