import asyncio, edge_tts
TEXT = "One user gets forty tokens a second. Add a second user, and each of them gets twenty two."
async def main():
    c = edge_tts.Communicate(TEXT, "en-US-AndrewNeural", rate="+8%")
    words=[]
    async for ch in c.stream():
        if ch["type"]=="WordBoundary":
            words.append((ch["offset"]/10_000_000, ch["duration"]/10_000_000, ch["text"]))
    print(f"word boundaries: {len(words)}")
    for w in words[:12]:
        print(f"   {w[0]:6.3f}s  +{w[1]:.3f}  {w[2]!r}")
    print("   ...")
    for w in words[-4:]:
        print(f"   {w[0]:6.3f}s  +{w[1]:.3f}  {w[2]!r}")
asyncio.run(main())
