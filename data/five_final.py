import json, os
SPECS=r"C:\Users\jibra\Desktop\1\KAI\data\specs"
FINAL={
"byte-03": {"type":"rows","head":"the one sentence version",
 "vo":"If you only remember one sentence, remember this one. On a twenty-four gigabyte card, the model with the smaller cache turns two hundred fifty-six K of context from impossible into ordinary, and no amount of card speed changes that arithmetic. Glimmer fits its whole window in twenty gigabytes. Qwen three point eight needs thirty-four for the same window, and thirty-four does not fit on twenty-four, and it will not fit tomorrow either.",
 "items":[["Glimmer 30B","256K in 20 GB","good"],["Qwen 3.8","256K needs 34 GB","hot"],
          ["Your card","24 GB, fixed","dim"]],
 "cues":{"h":"one sentence","0":"Glimmer fits","1":"thirty-four","2":"fixed"}},
"byte-04": {"type":"rows","head":"the one sentence version",
 "vo":"One sentence. Two sixteen gigabyte cards give you thirty-two gigabytes of capacity and roughly half the tokens per second of a single twenty-four gigabyte card, at every context length the benchmark tested, on both generation and prefill. If you already own one of those sixteen gigabyte cards, the second one is the cheapest capacity you will ever buy. If you own neither, buy the single card and stop shopping for slots.",
 "items":[["2 cards","32 GB, ~half speed","hot"],["1 card","24 GB, full speed","good"],
          ["Already own one","the second is cheap","dim"]],
 "cues":{"h":"One sentence","0":"thirty-two gigabytes","1":"twenty-four gigabyte","2":"the second one"}},
"byte-05": {"type":"rows","head":"the one sentence version",
 "vo":"One sentence. Unified memory buys you capacity and silence, and it charges you in tokens per second, roughly three and a half times the price of a discrete card at four K and even more at long context. Buy it when the model does not fit anywhere else, or when it has to live on a laptop. Do not buy it expecting speed, because the entire design is a trade away from speed.",
 "items":[["Buys","capacity, silence","good"],["Charges","tokens per second","hot"],
          ["Buy it when","nothing else fits","dim"]],
 "cues":{"h":"One sentence","0":"capacity and silence","1":"three and a half times","2":"nothing else fits"}},
"byte-06": {"type":"rows","head":"the one sentence version",
 "vo":"One sentence. At sixty-four K context on the same card, the previous generation model generates two point four times more tokens per second than the newer one, and it prefills two point six times faster, while the two are within one percent of each other at four K. That is not a rounding error and it is not a bad review. It is a measured regression that only shows up when you test at the context length that matters.",
 "items":[["At 4K","within 1 percent","good"],["At 64K","2.4x slower","hot"],
          ["At 128K","2.4x slower","hot"]],
 "cues":{"h":"One sentence","0":"within one percent","1":"two point four times","2":"two point six times"}},
"byte-07": {"type":"rows","head":"the one sentence version",
 "vo":"One sentence. Prefill decides how long you stare at the cursor, generation decides how fast the words arrive, and almost every comparison you have ever read only measures the second one. At a hundred thousand tokens the same card can take twenty-two seconds or two hundred and seventeen depending on the model, and that gap is the entire difference between a tool you use and a tool you stop opening.",
 "items":[["Prefill","the wait you feel first","hot"],["Generation","the speed you notice second","good"],
          ["100K prompt","22 s or 217 s","dim"]],
 "cues":{"h":"One sentence","0":"the cursor","1":"the words arrive","2":"twenty-two seconds"}},
}
for key,scene in FINAL.items():
    p=os.path.join(SPECS,key+".json")
    ep=json.load(open(p,encoding="utf-8"))
    sc=ep["scenes"]; close=sc.pop(); sc.append(scene); sc.append(close); ep["scenes"]=sc
    json.dump(ep,open(p,"w",encoding="utf-8"),indent=1)
    w=sum(len(s["vo"].split()) for s in sc)
    print(f"{key.upper()}: {len(sc)} scenes, {w} words (~{w/175:.1f} min)")
