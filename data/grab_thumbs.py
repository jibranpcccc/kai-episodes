import json, os, urllib.request, concurrent.futures as cf
d=json.load(open(r"C:\Users\jibra\Desktop\1\KAI\data\channel_raw.json",encoding="utf-8"))
out=r"C:\Users\jibra\Desktop\1\KAI\thumbs"
os.makedirs(out,exist_ok=True)
def best(thumbs):
    if not thumbs: return None
    return sorted(thumbs,key=lambda t:(t.get("width") or 0))[-1]["url"]
jobs=[(e["id"],best(e.get("thumbnails"))) for e in d["entries"] if e.get("id")]
jobs=[(i,u) for i,u in jobs if u and not os.path.exists(os.path.join(out,i+".jpg"))]
def get(j):
    vid,url=j
    try:
        req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
        b=urllib.request.urlopen(req,timeout=30).read()
        open(os.path.join(out,vid+".jpg"),"wb").write(b)
        return (vid,len(b))
    except Exception as ex:
        return (vid,f"ERR {ex}")
with cf.ThreadPoolExecutor(max_workers=8) as ex:
    res=list(ex.map(get,jobs))
ok=[r for r in res if isinstance(r[1],int)]
print(f"thumbs downloaded: {len(ok)}  failed: {len(res)-len(ok)}")
print(f"avg size: {sum(r[1] for r in ok)/max(len(ok),1)/1024:.0f} KB")
