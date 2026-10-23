import asyncio, edge_tts, collections
TEXT = "One user gets forty tokens a second."
async def main():
    try:
        c = edge_tts.Communicate(TEXT, "en-US-AndrewNeural", rate="+8%")
        types=collections.Counter()
        sample={}
        async for ch in c.stream():
            t=ch.get("type","?"); types[t]+=1
            if t not in sample: sample[t]=ch
        print("chunk types:", dict(types))
        for t,ch in sample.items():
            keys=list(ch.keys())
            print(f"  {t}: keys={keys}")
            if t!="audio": print("    sample:", {k:v for k,v in ch.items() if k!='data'})
    except Exception as e:
        print("ERR", type(e).__name__, e)
    import inspect
    print("\nCommunicate signature:", inspect.signature(edge_tts.Communicate.__init__))
asyncio.run(main())
