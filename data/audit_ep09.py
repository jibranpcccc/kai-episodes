# -*- coding: utf-8 -*-
with open(r"C:\Users\jibra\Desktop\1\KAI\BYTE-EP09.html", "r", encoding="utf-8") as f:
    text = f.read()

import json, re

m = re.search(r"window\.FUSION = (\{.*?\});</script>", text, re.S)
if m:
    F = json.loads(m.group(1))
    print(f"Title: {F.get('title')}")
    print(f"Kicker: {F.get('kicker')}")
    print(f"Subtitle: {F.get('subtitle')}")
    print(f"Total runtime: {F.get('total')}s")
    print(f"Total beats: {len(F.get('beats', []))}")
    print(f"Total scenes: {len(F.get('scenes', []))}")
    print(f"Total spoken words: {len(F.get('words', []))}")

    # Check for ACT mentions across scenes, beats, words
    act_matches = []
    for sc in F.get('scenes', []):
        lbl = sc.get('label', '')
        if re.search(r'\bact\b', lbl, re.I):
            act_matches.append(f"Scene {sc['id']}: label '{lbl}'")
    
    # Check spoken words
    spoken_text = " ".join([w[1] for w in F.get('words', [])])
    acts_in_speech = re.findall(r'(\b\w+\s+\w+\s+act\s+\w+\s+\w+\b)', spoken_text, re.I)
    print(f"ACT mentions in scene labels: {act_matches}")
    print(f"ACT mentions in speech context: {acts_in_speech}")

    # Check window layouts
    layouts = [sc.get('label', '').split()[-1] for sc in F.get('scenes', [])]
    consec = []
    for i in range(1, len(layouts)):
        if layouts[i] == layouts[i-1]:
            consec.append((i, layouts[i]))
    print(f"Consecutive identical layouts: {consec}")
