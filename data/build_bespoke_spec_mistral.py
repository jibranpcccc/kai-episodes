# -*- coding: utf-8 -*-
"""
BYTE FORENSICS MISTRAL VISUAL ARCHITECT
Generates 100% bespoke, technically accurate, rich visual specifications
for all 72 windows of Episode 13 (BYTE-CONTEXT) using Mistral Codestral API.
Eliminates all generic placeholders and produces SKU-specific visual hardware cards.
"""
import concurrent.futures
import json
import os
import re
import urllib.request
import urllib.error

ROOT = r"c:\Users\jibra\Desktop\1\KAI\repo"

# 1. Load active Mistral API key
p3 = r"C:\Users\jibra\Downloads\google stacking\mistral_keys.json"
with open(p3, "r", encoding="utf-8") as f:
    d = json.load(f)
key = d[0] if isinstance(d, list) else list(d.values())[0]
if isinstance(key, list):
    key = key[0]

# 2. Load script sentences
with open(os.path.join(ROOT, "data", "script_ep13_raw.txt"), "r", encoding="utf-8") as f:
    raw = f.read()

sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', raw.replace('\n', ' ')) if s.strip()]
scenes_vo = []
cur, cur_words = [], 0
for s in sents:
    sw = len(s.split())
    if "Separate model or application output limits" in s:
        if cur: scenes_vo.append(" ".join(cur))
        cur, cur_words = [s], sw
        continue
    if "If you want the model to generate eight thousand tokens" in s:
        if cur: scenes_vo.append(" ".join(cur))
        cur, cur_words = [s], sw
        continue
    if "That is the shock." in s:
        if cur: scenes_vo.append(" ".join(cur))
        cur, cur_words = [s], sw
        continue

    if (cur_words + sw > 36 and cur_words >= 16) or (cur_words >= 22 and sw >= 14):
        scenes_vo.append(" ".join(cur))
        cur = [s]
        cur_words = sw
    else:
        cur.append(s)
        cur_words += sw
if cur:
    scenes_vo.append(" ".join(cur))

assert len(scenes_vo) == 72

SPINE = ["hook", "rows", "bars", "rail", "chain", "note", "strip", "nodes"]
ART_OPTIONS = [
    "context_window", "kv_cache", "prompt_stream", "warning", "scales",
    "die", "cache_grid", "ram_stick", "folder", "chip", "gpu", "gpu_16gb",
    "gpu_24gb", "laptop", "motherboard", "clock", "checklist", "lan_link"
]

def generate_window_design(idx, vo, layout):
    prompt = f"""You are the Lead Visual Designer for Byte Forensics (@ByteForensics).
We are producing Episode 13: '128K CONTEXT WINDOW: THE SILENT MEMORY TRAP'.

Design Window #{idx+1} (Layout: '{layout}').
Narration spoken in this window:
"{vo}"

Rules:
1. Every card must have authentic, deeply technical hardware copy directly reflecting the narration.
2. NEVER use generic placeholders like 'ADVERTISED SPEC', 'ALLOCATION VRAM', 'EXECUTION ACTIVE', 'THEORETICAL CEILING', 'CRASH / AUDIT'.
3. Extract real CLI parameters (e.g. -c, --max-model-len), memory math (2*layers*heads*dim), GB figures, percentages, token counts, or specific concepts mentioned in the sentence.
4. Choose art from: {ART_OPTIONS}

Layout schemas:
- if 'hook': provide 'title', 'art', 'cap', 'c_tag', 'chips': [{{'c':'cyan','t':...}}, {{'c':'gold','t':...}}], 'stats': [{{'c':'cyan','lab':...,'u':...,'v':...}}, {{'c':'gold','lab':...,'u':...,'v':...}}]
- if 'rows': provide 'title', 'art', 'cap', 'c_tag', 'rows': [{{'cls':'cyan','rank':'01','name':...,'val':...,'sub':...}}, {{'cls':'gold','rank':'02','name':...,'val':...,'sub':...}}, {{'cls':'hot','rank':'03','name':...,'val':...,'sub':...}}]
- if 'bars': provide 'title', 'art', 'cap', 'c_tag', 'bars': [{{'cls':'cyan','lab':...,'unit':...,'val':...,'pct':...}}, {{'cls':'hot','lab':...,'unit':...,'val':...,'pct':...}}]
- if 'rail': provide 'title', 'art', 'cap', 'c_tag', 'rails': [{{'cls':'cyan','lab':...,'val':...,'pct':...}}, {{'cls':'red','lab':...,'val':...,'pct':...}}]
- if 'chain': provide 'title', 'art', 'cap', 'c_tag', 'chain': [{{'t':...,'s':...}}, {{'t':...,'s':...}}, {{'t':...,'s':...}}], 'compare': [{{'cls':'dim','title':...,'body':...}}, {{'cls':'gold','title':...,'body':...}}]
- if 'note': provide 'title', 'art', 'cap', 'c_tag', 'note_head':..., 'note_items': [{{'t':...}}, {{'t':...}}, {{'t':...}}]
- if 'strip': provide 'title', 'c_tag', 'items': [{{'key':...,'label':...}}, {{'key':...,'label':...}}, {{'key':...,'label':...}}]
- if 'nodes': provide 'title', 'art', 'cap', 'c_tag', 'chain': [{{'t':...,'s':...}}, {{'t':...,'s':...}}, {{'t':...,'s':...}}]

Return ONLY valid JSON matching this layout.
"""

    req = urllib.request.Request(
        "https://api.mistral.ai/v1/chat/completions",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
        data=json.dumps({
            "model": "codestral-latest",
            "messages": [{"role": "user", "content": prompt}],
            "response_format": {"type": "json_object"},
            "temperature": 0.2
        }).encode("utf-8")
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        content = json.loads(res["choices"][0]["message"]["content"])
        content["idx"] = idx
        return content

print(f"Generating bespoke visual specifications for all 72 windows via Mistral Codestral API...")

results = {}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_idx = {
        executor.submit(generate_window_design, i, scenes_vo[i], SPINE[i % len(SPINE)]): i
        for i in range(72)
    }
    for future in concurrent.futures.as_completed(future_to_idx):
        idx = future_to_idx[future]
        try:
            data = future.result()
            results[idx] = data
            print(f"  [OK] Scene {idx+1:02d}/72: {data.get('title', 'Generated')}")
        except Exception as e:
            print(f"  [ERR] Scene {idx+1:02d}: {e}")

out_file = os.path.join(ROOT, "data", "mistral_bespoke_designs.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump([results[i] for i in range(72)], f, indent=2)

print(f"Successfully generated and saved all {len(results)} bespoke scene designs to {out_file}!")
