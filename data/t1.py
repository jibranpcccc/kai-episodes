import asyncio, edge_tts
async def m():
    try:
        await edge_tts.Communicate("Testing one two three.","en-US-AndrewNeural").save(r"C:\Users\jibra\Desktop\1\KAI\voice_samples\_test.mp3")
        print("SUCCESS")
    except Exception as e:
        print("FAIL:", type(e).__name__, str(e)[:120])
asyncio.run(m())
