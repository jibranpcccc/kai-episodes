import asyncio, edge_tts, json, re
import importlib.util
spec=importlib.util.spec_from_file_location("bfb", r"C:\Users\jibra\Desktop\1\KAI\data\bf_build.py")
# don't execute the build; just read the SCENES from the file text
src=open(r"C:\Users\jibra\Desktop\1\KAI\data\bf_build.py",encoding="utf-8").read()
vos=re.findall(r'dict\(vo="([^"]+)"', src)
print(f"scenes: {len(vos)}\n")
async def main():
    out=[]
    for i,t in enumerate(vos,1):
        c=edge_tts.Communicate(t,"en-US-AndrewNeural",rate="+8%",boundary="WordBoundary")
        ws=[]
        async for ch in c.stream():
            if ch["type"]=="WordBoundary": ws.append((round(ch["offset"]/1e7,2), ch["text"]))
        out.append(ws)
        print(f"--- scene {i}  ({ws[-1][0]:.1f}s)" if ws else f"--- scene {i}")
        line=[]
        for t2,w in ws:
            line.append(f"{t2}:{w}")
        print("  " + "  ".join(line))
        print()
    json.dump(out, open(r"C:\Users\jibra\Desktop\1\KAI\byte\words.json","w"))
asyncio.run(main())
