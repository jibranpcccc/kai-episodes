import csv, json, datetime, statistics as st, re

rows=list(csv.DictReader(open(r"C:\Users\jibra\Desktop\1\KAI\data\videos_all.csv",encoding="utf-8")))
dates={}
for line in open(r"C:\Users\jibra\Desktop\1\KAI\data\dates.tsv",encoding="utf-8"):
    p=line.rstrip("\n").split("\t")
    if len(p)>=4: dates[p[0]]=p[3]
now=datetime.datetime(2026,10,19,tzinfo=datetime.timezone.utc)
for r in rows:
    d=dates.get(r["id"],"")
    r["up"]=f"{d[:4]}-{d[4:6]}-{d[6:]}" if len(d)==8 else ""
    if r["up"]:
        dt=datetime.datetime.strptime(r["up"],"%Y-%m-%d").replace(tzinfo=datetime.timezone.utc)
        r["age"]=max((now-dt).days,0)
        r["vpd"]=round(int(r["views"])/max(r["age"],1),0)
    else:
        r["age"]=""; r["vpd"]=""
rows.sort(key=lambda r:int(r["views"]),reverse=True)
for i,r in enumerate(rows,1): r["rank"]=i

with open(r"C:\Users\jibra\Desktop\1\KAI\data\videos_ranked.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=["rank","id","title","views","vpd","age","up","duration_s","url"],extrasaction="ignore");w.writeheader();w.writerows(rows)

print("="*104); print("TOP 20 BY VIEWS"); print("="*104)
print(f"{'#':>3} {'views':>8} {'v/day':>7} {'age':>4} {'dur':>7} {'upload':>10}  title")
for r in rows[:20]:
    print(f"{r['rank']:>3} {int(r['views']):>8,} {int(float(r['vpd'])):>7,} {r['age']:>4} {r['duration_s']:>7} {r['up']:>10}  {r['title'][:58]}")

print(); print("="*104); print("TOP 15 BY VELOCITY (views/day)"); print("="*104)
for r in sorted(rows,key=lambda r:float(r["vpd"] or 0),reverse=True)[:15]:
    print(f"{int(float(r['vpd'])):>7,}/d {int(r['views']):>8,} views  age={r['age']:>3}d  {r['up']}  {r['title'][:56]}")

vd=[float(r["vpd"]) for r in rows if r["vpd"]]
print(f"\nvelocity: median={st.median(vd):,.0f}/d  p90={sorted(vd)[int(len(vd)*0.9)]:,.0f}/d  max={max(vd):,.0f}/d")
print("span:", min(r["up"] for r in rows if r["up"]), "->", max(r["up"] for r in rows if r["up"]))
top10=rows[:10]
print("top10 upload span:", min(r['up'] for r in top10 if r['up']), "->", max(r['up'] for r in top10 if r['up']))
print("top10 ages:", sorted(int(r['age']) for r in top10 if r['age']!=""))

