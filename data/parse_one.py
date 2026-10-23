import json
d=json.load(open(r"C:\Users\jibra\Desktop\1\KAI\data\one.json",encoding="utf-8"))
for k in ["id","title","upload_date","timestamp","view_count","like_count","comment_count","duration","channel_follower_count","categories","language","age_limit"]:
    print(f"{k:22}: {d.get(k)}")
print("tags              :", (d.get("tags") or [])[:20])
print("chapters          :", len(d.get("chapters") or []))
for c in (d.get("chapters") or [])[:14]:
    print(f"   {c['start_time']:7.0f}s  {c['title']}")
print("desc[:900]        :")
print((d.get("description") or "")[:900])
fmts=[f for f in d.get("formats",[]) if f.get("vcodec") not in (None,"none")]
print("\nvideo formats avail (h, fps, tbr, codec):")
seen=set()
for f in sorted(fmts,key=lambda x:-(x.get("height") or 0)):
    key=(f.get("height"),f.get("fps"),f.get("vcodec"))
    if key in seen: continue
    seen.add(key)
    print(f"   {f.get('height')}p{f.get('fps')} {f.get('ext')} {f.get('vcodec')} tbr={f.get('tbr')} filesize~{(f.get('filesize') or f.get('filesize_approx') or 0)/1e6:.0f}MB")
