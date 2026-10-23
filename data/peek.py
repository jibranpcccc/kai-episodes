import json, sys
p = r"C:\Users\jibra\Desktop\1\KAI\data\channel_raw.json"
d = json.load(open(p, encoding="utf-8"))
print("channel      :", d.get("channel") or d.get("uploader") or d.get("title"))
print("channel_id   :", d.get("channel_id") or d.get("id"))
print("followers    :", d.get("channel_follower_count"))
print("description  :", (d.get("description") or "")[:600].replace("\n"," | "))
print("total entries:", len(d.get("entries") or []))
ents = d.get("entries") or []
keys = set()
for e in ents[:3]: keys |= set(e.keys())
print("entry keys   :", sorted(keys))
