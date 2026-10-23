import asyncio, edge_tts, subprocess, os, re, time
txt=open("BYTE-02-SCRIPT.md",encoding="utf-8").read()
chunks=re.split(r"### CH (\d+) —", txt)[1:]
pairs=[]
for i in range(0,len(chunks),2):
    num=int(chunks[i]); body=chunks[i+1]
    vo=" ".join(l[1:].strip() for l in body.split("\n") if l.startswith(">") and l.strip()!=">")
    if vo: pairs.append((num, vo))
want={8:44, 9:41, 10:15}   # fallbacks only if network fails
async def one(num, vo):
    for attempt in range(4):
        try:
            c=edge_tts.Communicate(vo,"en-US-AndrewNeural",rate="+8%")
            buf=bytearray()
            async for ch in c.stream():
                if ch["type"]=="audio": buf+=ch["data"]
            p=f"_m{num}.mp3"; open(p,"wb").write(bytes(buf))
            d=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],
                  capture_output=True,text=True).stdout.strip())
            os.remove(p); return d, len(vo.split()), True
        except Exception:
            time.sleep(2)
    return want[num], len(vo.split()), False
async def main():
    base={1:51.84,2:38.14,3:53.74,4:42.86,5:59.69,6:73.42,7:32.88}
    words={1:167,2:115,3:156,4:110,5:192,6:213,7:135}
    for num,vo in pairs:
        if num<8: continue
        d,w,ok = await one(num,vo)
        base[num]=d; words[num]=w
        print(f"  CH{num:>2}: {d:6.2f}s  {w:4d} words  {'measured' if ok else 'ESTIMATED (network)'}")
    speech=sum(base.values()); total=speech+0.30*9+1.0
    print(f"\n  speech {speech:.1f}s + 9 gaps 2.7s + tail 1.0s")
    print(f"  TOTAL {total:.1f}s = {total//60}:{total%60:04.1f}   {'PASS' if total>=420 else 'FAIL'} (need 7:00)")
    print(f"  words {sum(words.values())}   wpm {sum(words.values())/(speech/60):.0f}")
asyncio.run(main())
