"""Final pass: two closing scenes per episode, reaching ~1,250 words / 7+ min."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, "data", "specs")

LAST = {}

LAST["byte-03"] = [
 {"type": "rows", "head": "the buying decision",
  "vo": "So here is the decision, stated plainly. If long context is the reason you are buying, buy the model with the smaller cache before you buy a bigger card. If you already own the card, choose the model that fits its window and plan the rest of your workflow around that limit. And if you genuinely need two hundred fifty-six K on a single card, the answer is a model that was designed to be efficient, not a card that was designed to be fast.",
  "items": [["Long context first", "pick the efficient model", "good"],
            ["Card already owned", "fit the model to the window", "good"],
            ["256K on one card", "efficiency, not speed", "dim"]],
  "cues": {"h": "the decision", "0": "smaller cache", "1": "already own the card", "2": "two hundred fifty-six K"}},

 {"type": "caveat", "head": "three myths this kills",
  "vo": "Three myths die here. More parameters does not mean more memory, because the file is quantized and the cache is not. A bigger number on the box does not mean a better experience, because the box does not know your context length. And a faster card does not fix a capacity problem, because twenty-four gigabytes is twenty-four gigabytes whether it is fast or slow.",
  "items": ["Parameters equal memory", "Box numbers equal experience",
            "Speed fixes capacity"],
  "tape": "all three are false",
  "cues": {"h": "Three myths", "0": "More parameters", "1": "bigger number on the box", "2": "faster card", "t": "all three"}},
]

LAST["byte-04"] = [
 {"type": "rows", "head": "if you are buying today",
  "vo": "If you are buying today, the order of operations is this. Decide the context length you actually need. Find the model that fits that context on the memory you can afford. Then, and only then, buy the fastest card with that much memory. Doing it in the other order is how people end up with two cards, half the speed, and a model that still does not fit the way they wanted.",
  "items": [["1. Pick the context", "the length you really use", "good"],
            ["2. Find the model", "that fits that context", "good"],
            ["3. Buy the card", "fastest with that memory", "good"]],
  "cues": {"h": "If you are buying today", "0": "the context length", "1": "Find the model", "2": "buy the fastest card"}},

 {"type": "caveat", "head": "the honest bottom line",
  "vo": "The bottom line is uncomfortable for the two-card route. In every measurement in front of us, one card with twenty-four gigabytes beat two cards with thirty-two, on generation, on prefill, and on simplicity. The only cases where two cards win are the ones where you already own one, or where your workload is a queue of small requests rather than one long conversation. Measure your own workload before you decide which of those you are.",
  "items": ["One card won on both metrics", "Two cards win only on ownership or queue workloads"],
  "tape": "measure your workload",
  "cues": {"h": "The bottom line", "0": "beat two cards", "1": "queue of small requests", "t": "Measure your own"}},
]

LAST["byte-05"] = [
 {"type": "rows", "head": "when unified actually wins",
  "vo": "Unified memory wins in three specific situations. The model does not fit on any consumer card. You need it to run on a laptop or on battery. Or you need it quiet, because a workstation that sounds like a hairdryer is not usable in a room with other people. None of those are speed arguments, and all of them are legitimate. Buy it for those reasons and you will be happy.",
  "items": [["Model does not fit", "only door", "good"],
            ["Laptop or battery", "only option", "good"],
            ["Silence", "genuine requirement", "good"]],
  "cues": {"h": "three specific situations", "0": "does not fit", "1": "on a laptop", "2": "quiet"}},

 {"type": "caveat", "head": "the number that decides it",
  "vo": "If you take one number from this video, take the ratio. Forty-five point three tokens a second on a discrete card against twelve point seven six on the small unified box, for the same model at the same context. That is three and a half times. If that gap does not matter to your workload, buy the quiet machine. If it does, buy the card, and stop paying for memory you are not using.",
  "items": ["Discrete card 45.3 t/s", "GB10 12.76 t/s", "Same model, same context"],
  "tape": "three and a half times",
  "cues": {"h": "If you take one number", "0": "forty-five point three", "1": "twelve point seven six", "t": "three and a half times"}},
]

LAST["byte-06"] = [
 {"type": "rows", "head": "what to do if you already run 3.8",
  "vo": "If you already run three point eight, do not panic and do not downgrade blindly. Measure your own context length first. If you live under sixteen K, the regression barely touches you, because the two models are within a few percent there. If you work at sixty-four K or beyond, it is worth benchmarking three point six on your actual tasks, because the speed difference is large enough to change how the tool feels.",
  "items": [["Under 16K", "barely affects you", "good"],
            ["64K and beyond", "benchmark both", "hot"],
            ["Do not downgrade blind", "quality may still win", "dim"]],
  "cues": {"h": "If you already run three point eight", "0": "under sixteen K", "1": "sixty-four K", "2": "downgrade blindly"}},

 {"type": "caveat", "head": "the bottom line",
  "vo": "The bottom line: a newer version number is not a performance guarantee, and a model release note will never tell you that long context got slower. The only defence is measurement on your own machine, at your own context length, with your own prompts. That is ten minutes of work, and it is the difference between choosing a model and being sold one.",
  "items": ["Version numbers are not performance", "Measure at your context, on your machine"],
  "tape": "measure, then choose",
  "cues": {"h": "The bottom line", "0": "not a performance guarantee", "1": "your own machine", "t": "measure, then choose"}},
]

LAST["byte-07"] = [
 {"type": "rows", "head": "caching in practice",
  "vo": "In practice, prompt caching is the single highest leverage setting for long context work. If your tool supports it, keep the stable part of the prompt first and the changing part last, because a cache hit requires the prefix to match exactly. Move one word at the top and you pay the full prefill again. That one habit turns a three minute wait into a two second one.",
  "items": [["Stable prefix first", "so the cache hits", "good"],
            ["Changing content last", "so the prefix still matches", "good"],
            ["Edit the top", "and you pay full price again", "hot"]],
  "cues": {"h": "prompt caching", "0": "stable part of the prompt", "1": "changing part last", "2": "full prefill again"}},

 {"type": "caveat", "head": "the bottom line",
  "vo": "The bottom line is that prefill is the half of performance nobody publishes, and it is the half you feel first. Every time you paste a document, you are watching a benchmark run in real time. Learn what your machine does at your prompt length, and the hardware conversation gets a lot shorter, because you will already know the answer before anyone posts a table.",
  "items": ["Prefill is the invisible half", "Time to first token is what you feel"],
  "tape": "the half nobody publishes",
  "cues": {"h": "The bottom line", "0": "nobody publishes", "1": "feel first", "t": "nobody publishes"}},
]

for key, extra in LAST.items():
    path = os.path.join(SPECS, key + ".json")
    ep = json.load(open(path, encoding="utf-8"))
    scenes = ep["scenes"]
    close = scenes.pop()
    scenes.extend(extra)
    scenes.append(close)
    ep["scenes"] = scenes
    json.dump(ep, open(path, "w", encoding="utf-8"), indent=1)
    words = sum(len(s["vo"].split()) for s in scenes)
    print(f"{key.upper()}: {len(scenes)} scenes, {words} words (~{words/175:.1f} min)")
