import asyncio, edge_tts, subprocess, os, re
LINES=[
"A thirty billion parameter model runs faster on your twenty-four gigabyte card than a twenty-seven billion one. Same card. Bigger model. More speed. That shouldn't be possible.",
"Muse Glimmer thirty B is fourteen point seven eight gigabytes on disk. Qwen three point eight twenty-seven B is sixteen point six eight. The bigger model is the smaller file.",
"That's not magic. It's quantization. Glimmer at four-bit medium is smaller than Qwen at four-bit small. And its cache grows more slowly as you add context.",
"Here is measured VRAM at every context length. At sixty-four K, Glimmer needs seventeen gigabytes. Qwen needs twenty-two. At two hundred fifty-six K, Glimmer peaks at twenty. Qwen hits thirty-four.",
"On a three thousand ninety, Glimmer generates forty-five tokens a second. Qwen does forty. At sixty-four K, Glimmer holds forty-two. Qwen drops to thirty-four. And Qwen cannot reach one twenty-eight K on that card at all.",
"One honest caveat. Those are different quantization levels, so this is not a perfectly fair fight. And the agentic claims are not benchmarked yet. Treat them as unconfirmed.",
"So on twenty-four gigabytes, Glimmer for long context. Qwen if you need its specific behaviour. And on a five oh ninety, Glimmer still wins at eighty-three tokens a second.",
"Stop shopping by parameter count. Shop by what fits at the context you actually use.",
]
async def main():
    tot=0
    for i,t in enumerate(LINES,1):
        c=edge_tts.Communicate(t,"en-US-AndrewNeural",rate="+8%")
        buf=bytearray()
        async for ch in c.stream():
            if ch["type"]=="audio": buf+=ch["data"]
        p=f"_tmp{i}.mp3"; open(p,"wb").write(bytes(buf))
        d=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],
              capture_output=True,text=True).stdout.strip())
        os.remove(p)
        tot+=d
        print(f"  scene {i}: {d:5.2f}s   {len(t.split())} words")
    g=0.25*7; tail=0.8
    print(f"\n  speech {tot:.2f}s + 7 gaps {g:.2f}s + tail {tail}s = {tot+g+tail:.2f}s runtime")
    print(f"  words {sum(len(x.split()) for x in LINES)}  ->  {sum(len(x.split()) for x in LINES)/(tot/60):.0f} wpm")
    print(f"  average reveal budget needed: {tot/52:.2f}s  (52+ reveals for a 2s max gap)")
asyncio.run(main())
