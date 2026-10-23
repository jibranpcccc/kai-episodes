import re,os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
for f in ["EPISODE.html","EPISODE-02.html","EPISODE-03.html"]:
    h=open(os.path.join(ROOT,f),encoding="utf-8").read()
    ext=[m for m in re.findall(r'(?:href|src)="([^"]+)"',h) if not m.startswith(("http","data:"))]
    print(f"{f}: {len(h)//1024} KB  external: {ext if ext else 'none'}")
    print(f"    audio: {sorted(set(re.findall(r'audio/[a-z0-9_]+\.mp3',h)))}")
    for a in sorted(set(re.findall(r'audio/[a-z0-9_]+\.mp3',h))):
        if not os.path.exists(os.path.join(ROOT,a.replace('/',os.sep))): print("    MISSING", a)
