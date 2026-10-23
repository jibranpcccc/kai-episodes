import asyncio, edge_tts, subprocess, os, re
txt=open("BYTE-02-SCRIPT.md",encoding="utf-8").read()
# pull the blockquoted VO under each chapter heading
chunks=re.split(r"### CH (\d+) —", txt)[1:]
pairs=[]
for i in range(0,len(chunks),2):
    num=chunks[i]; body=chunks[i+1]
    lines=[l[1:].strip() for l in body.split("\n") if l.startswith(">")]
    vo=" ".join(l for l in lines if l)
    if vo: pairs.append((int(num), vo))
print(f"chapters with VO: {len(pairs)}")
async def main():
    tot=0; words=0
    for num,vo in pairs:
        c=edge_tts.Communicate(vo,"en-US-AndrewNeural",rate="+8%")
        buf=bytearray()
        async for ch in c.stream():
            if ch["type"]=="audio": buf+=ch["data"]
        p=f"_m{num}.mp3"; open(p,"wb").write(bytes(buf))
        d=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],
              capture_output=True,text=True).stdout.strip())
        os.remove(p); tot+=d; words+=len(vo.split())
        print(f"  CH{num:>2}: {d:6.2f}s  {len(vo.split()):4d} words")
    gaps=0.30*(len(pairs)-1); tail=1.0; total=tot+gaps+tail
    print(f"\n  speech {tot:.1f}s + gaps {gaps:.1f}s + tail {tail}s")
    print(f"  RUNTIME {total:.1f}s = {total/60:.2f} min   ({'PASS' if total>=420 else 'FAIL'} vs 7:00)")
    print(f"  words {words}  wpm {words/(tot/60):.0f}")
    need=total/1.6
    print(f"  reveals needed (<=2s rule, ~1.6s cadence): {int(need)}")
asyncio.run(main())
