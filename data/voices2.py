import asyncio, edge_tts, re
async def main():
    vs = await edge_tts.list_voices()
    keep=[v for v in vs if v["Locale"] in ("en-US","en-GB","en-AU","en-IE")]
    print(f"total voices {len(vs)} · english {len(keep)}\n")
    for v in sorted(keep, key=lambda x:(x["Locale"], x["ShortName"])):
        name=v["ShortName"].replace("Neural","")
        tag=""
        if "Multilingual" in v["ShortName"]: tag=" [multilingual]"
        print(f'  {v["Locale"]}  {name:<28} {v["Gender"]:<6}{tag}')
asyncio.run(main())
