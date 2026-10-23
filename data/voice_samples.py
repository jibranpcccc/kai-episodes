import asyncio, edge_tts, os, subprocess
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
OUT=os.path.join(ROOT,"voice_samples"); os.makedirs(OUT,exist_ok=True)

TEXT=("Everyone buying a GPU for local AI is measuring the wrong number. "
      "Twenty-four gigabytes of VRAM doesn't run a twenty-four gigabyte model. "
      "The weights are only half.")

VOICES=[
 ("andrew","en-US-AndrewNeural","US male","warm, conversational"),
 ("brian","en-US-BrianNeural","US male","energetic, casual"),
 ("christopher","en-US-ChristopherNeural","US male","deep, authoritative"),
 ("guy","en-US-GuyNeural","US male","punchy, news"),
 ("steffan","en-US-SteffanNeural","US male","documentary, mature"),
 ("ryan","en-GB-RyanNeural","UK male","warm British"),
 ("ava","en-US-AvaNeural","US female","expressive, modern"),
 ("aria","en-US-AriaNeural","US female","crisp, news"),
]

async def gen():
    for slug,voice,_,_ in VOICES:
        p=os.path.join(OUT,slug+".mp3")
        try:
            await edge_tts.Communicate(TEXT, voice, rate="+0%").save(p)
            print(f"  ok  {slug:<12} {voice}")
        except Exception as e:
            print(f"  FAIL {slug}: {type(e).__name__} {e}")
asyncio.run(gen())

print("\n--- durations ---")
for slug,voice,_,_ in VOICES:
    p=os.path.join(OUT,slug+".mp3")
    if not os.path.exists(p): continue
    d=subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],
                     capture_output=True,text=True).stdout.strip()
    print(f"  {slug:<12} {float(d):5.2f}s  {os.path.getsize(p)/1024:5.0f} KB")
