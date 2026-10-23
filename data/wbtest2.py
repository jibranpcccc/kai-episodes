import asyncio, edge_tts
TEXT="One user gets forty tokens a second. Add a second user, and each of them gets twenty two."
async def main():
    c=edge_tts.Communicate(TEXT,"en-US-AndrewNeural",rate="+8%",boundary="WordBoundary")
    ws=[]
    async for ch in c.stream():
        if ch["type"]=="WordBoundary": ws.append((ch["offset"]/1e7,ch["text"]))
    print("words:",len(ws))
    for x in ws[:8]: print(f"   {x[0]:6.3f}s  {x[1]!r}")
    print("   ...")
    for x in ws[-5:]: print(f"   {x[0]:6.3f}s  {x[1]!r}")
    # sanity: does 'second' land before 'twenty two'?
    print("\ncheck 'twenty':", [f"{t:.2f}s" for t,w in ws if w.lower().startswith("twenty")])
asyncio.run(main())
