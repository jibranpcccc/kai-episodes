import glob, json, csv, os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
rows={r["id"]:r for r in csv.DictReader(open(ROOT+r"\data\videos_ranked.csv",encoding="utf-8"))}
out=[]
for f in glob.glob(ROOT+r"\videos\*.info.json"):
    d=json.load(open(f,encoding="utf-8"))
    r=rows.get(d["id"],{})
    out.append((int(r.get("rank",99)),d["id"],d.get("upload_date"),d.get("view_count"),d.get("like_count"),d.get("comment_count"),len(d.get("chapters") or []),d.get("title","")[:50]))
for o in sorted(out):
    print(f"rank{o[0]:>3} {o[1]} date={o[2]} views={o[3]:,} likes={o[4]:,} cmts={o[5]:,} ch={o[6]}  {o[7]}")
