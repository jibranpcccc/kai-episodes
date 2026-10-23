import csv, json
rows=list(csv.DictReader(open(r"C:\Users\jibra\Desktop\1\KAI\data\videos_ranked.csv",encoding="utf-8")))
rows.sort(key=lambda r:int(r["rank"]))
pick=[r for r in rows if int(r["rank"])<=10]
extra=[r for r in rows if r["id"]=="6tihP50zlcE"]   # 512GB sequel, 1 day old, 85k/d
seen=set(); out=[]
for r in pick+extra:
    if r["id"] not in seen:
        seen.add(r["id"]); out.append(r)
open(r"C:\Users\jibra\Desktop\1\KAI\data\ids.txt","w",encoding="utf-8").write("\n".join(r["id"] for r in out))
print("download set:",len(out))
tot=0
for r in out:
    m,s=divmod(int(r["duration_s"].split(":")[-1]) if ":" in r["duration_s"] else 0,60)
    print(f"  {r['id']}  rank={r['rank']:>2}  {int(r['views']):>8,} views  {r['duration_s']:>7}  {r['title'][:52]}")
print("total runtime:", sum(int(r["duration_s"].split(":")[0])*60+int(r["duration_s"].split(":")[1]) for r in out)//60, "min")
