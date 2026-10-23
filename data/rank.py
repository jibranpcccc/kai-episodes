import json, csv, datetime, statistics as st

p = r"C:\Users\jibra\Desktop\1\KAI\data\channel_raw.json"
outdir = r"C:\Users\jibra\Desktop\1\KAI\data"
d = json.load(open(p, encoding="utf-8"))
ents = [e for e in (d.get("entries") or []) if e.get("id")]

def fmt_dur(s):
    if not s: return "?"
    s=int(s); h,r = divmod(s,3600); m,sec = divmod(r,60)
    return f"{h}:{m:02d}:{sec:02d}" if h else f"{m}:{sec:02d}"

rows=[]
for e in ents:
    ts = e.get("timestamp")
    dt = datetime.datetime.fromtimestamp(ts, datetime.timezone.utc) if ts else None
    v = e.get("view_count") or 0
    dur = e.get("duration") or 0
    age_days = ((datetime.datetime.now(datetime.timezone.utc) - dt).days if dt else None)
    rows.append(dict(id=e["id"], title=e.get("title",""), views=v, duration=dur,
                     duration_s=fmt_dur(dur), upload_utc=dt.strftime("%Y-%m-%d") if dt else "",
                     age_days=age_days,
                     views_per_day=round(v/age_days,1) if age_days and age_days>0 else None,
                     url=f"https://www.youtube.com/watch?v={e['id']}"))

rows.sort(key=lambda r: r["views"], reverse=True)
for i,r in enumerate(rows,1): r["rank_views"]=i

with open(outdir+r"\videos_all.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=["rank_views","id","title","views","duration","duration_s","upload_utc","age_days","views_per_day","url"])
    w.writeheader(); w.writerows(rows)

tot=sum(r["views"] for r in rows)
durs=[r["duration"] for r in rows if r["duration"]]
print(f"videos={len(rows)}  total_views={tot:,}  median_views={int(st.median([r['views'] for r in rows])):,}")
print(f"duration: median={fmt_dur(st.median(durs))} mean={fmt_dur(int(st.mean(durs)))} min={fmt_dur(min(durs))} max={fmt_dur(max(durs))}")
print()
print(f"{'#':>3} {'views':>10} {'v/d':>7} {'dur':>7} {'up':>10}  title")
print("-"*115)
for r in rows[:25]:
    print(f"{r['rank_views']:>3} {r['views']:>10,} {str(r['views_per_day']):>7} {r['duration_s']:>7} {r['upload_utc']:>10}  {r['title'][:62]}")
