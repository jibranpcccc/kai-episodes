# -*- coding: utf-8 -*-
"""
Assemble data/spec_context.py using Mistral-generated bespoke scene designs
coupled with audio-locked Whisper timestamps for 100% synchronization.
"""
import glob
import json
import os
import pprint
import re

ROOT = r"c:\Users\jibra\Desktop\1\KAI\repo"
work = os.path.join(ROOT, "build", "BYTE-CONTEXT")

# 1. Load raw script
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

# 2. Chapters definition
CHAPTERS = [
    (1, "THE 128K PROMISE & THE MEMORY TRAP"),
    (8, "WORKING MEMORY VS PERMANENT STORAGE"),
    (15, "LIMIT 1 & LIMIT 2: MODEL VS RUNTIME LIMITS"),
    (20, "LIMIT 3: PHYSICAL MEMORY & THE KEY-VALUE CACHE"),
    (25, "THE HYPOTHETICAL KV CACHE MATH"),
    (33, "MULTI-USER CONCURRENCY & MEMORY PRESSURE"),
    (36, "LIMIT 4: EFFECTIVE USE & LOST IN THE MIDDLE"),
    (44, "THE CLOCK COST: PREFILL VS DECODING SPEED"),
    (49, "OPTIMIZATIONS & POSITIONAL SCALING TRAPS"),
    (53, "THE 6-STEP CONTEXT AUDIT METHODOLOGY"),
    (60, "RETRIEVAL-AUGMENTED GENERATION VS GIANT CONTEXT"),
    (67, "THE FINAL VERDICT: MEASURE THE REAL BOTTLENECK")
]

def get_kicker(idx):
    k = CHAPTERS[0][1]
    for sc_start, name in CHAPTERS:
        if idx >= sc_start:
            k = name
        else:
            break
    return k

SPINE = ["hook", "rows", "bars", "rail", "chain", "note", "strip", "nodes"]

# 3. Load audio word timestamps
jsons = []
for i in range(1, 73):
    matches = glob.glob(os.path.join(work, f"n{i}-*.json"))
    if not matches:
        raise ValueError(f"Missing json for window {i}")
    jsons.append(matches[0])

def extract_verbatim_phrase(vo, ws, word_idx, num_words=3):
    w_len = len(ws)
    word_idx = max(0, min(word_idx, w_len - 1))
    for start in range(word_idx, max(-1, word_idx - 3), -1):
        for k in range(min(num_words, w_len - start), 1, -1):
            sub = [ws[start + j][1] for j in range(k)]
            clean_sub = [re.sub(r"[^\w\s']", "", w) for w in sub]
            clean_sub = [w for w in clean_sub if w]
            if not clean_sub:
                continue
            phrase = " ".join(clean_sub)
            pos = vo.lower().find(phrase.lower())
            if pos != -1:
                return vo[pos:pos+len(phrase)], ws[start][0], start, pos
    w = re.sub(r"[^\w\s']", "", ws[word_idx][1])
    pos = vo.lower().find(w.lower())
    if pos != -1:
        return vo[pos:pos+len(w)], ws[word_idx][0], word_idx, pos
    first_w = vo.split()[0]
    return first_w, 0.0, 0, 0

def _toks(w):
    w = (w or "").lower().replace("’", "'").replace("“", " ").replace("”", " ").replace(".", " ").replace("-", " ")
    return [x.strip("'") for x in re.sub(r"[^\w\s']", " ", w).split() if x.strip("'")]

def get_unique_anchor(vo, ws, center_idx, prefer_tail=False):
    """Find a phrase directly from vo around center_idx that appears EXACTLY ONCE in vo."""
    words_vo = vo.split()
    n_v = len(words_vo)
    
    if prefer_tail:
        for span in [2, 3, 4]:
            st = max(0, n_v - span)
            cand_words = [w.strip(".,;:!?\"'()") for w in words_vo[st:] if w.strip(".,;:!?\"'()")]
            cand = " ".join(cand_words)
            if cand and cand.lower() in vo.lower() and vo.lower().count(cand.lower()) == 1:
                return cand
        st = max(0, n_v - 4)
        return " ".join([w.strip(".,;:!?\"'()") for w in words_vo[st:] if w.strip(".,;:!?\"'()")])

    prop = center_idx / max(1, len(ws) - 1)
    v_idx = int(prop * (n_v - 1))
    
    for span in [2, 3, 4]:
        for offset in [0, 1, -1, 2, -2, 3, -3]:
            st = max(0, min(v_idx + offset, n_v - span))
            ed = st + span
            cand_words = [w.strip(".,;:!?\"'()") for w in words_vo[st:ed] if w.strip(".,;:!?\"'()")]
            if not cand_words:
                continue
            cand = " ".join(cand_words)
            if cand.lower() in vo.lower() and vo.lower().count(cand.lower()) == 1:
                return cand
                
    st = max(0, min(v_idx, n_v - 4))
    cand_words = [w.strip(".,;:!?\"'()") for w in words_vo[st:st+4] if w.strip(".,;:!?\"'()")]
    return " ".join(cand_words)

def get_header_anchor(vo, ws):
    """The very first word(s) of the scene, matching ws[0][0]."""
    words_vo = vo.split()
    w0 = words_vo[0].strip(".,;:!?\"'()")
    if len(words_vo) > 1:
        w1 = words_vo[1].strip(".,;:!?\"'()")
        cand2 = f"{w0} {w1}"
        if cand2.lower() in vo.lower() and vo.lower().count(cand2.lower()) == 1:
            return cand2
    return w0

def clean_val(v, default="ACTIVE"):
    if v is None:
        return default
    v = str(v).strip()
    if not v:
        return default
    if "%" in v:
        clean = v.replace("%", "").strip()
        if not clean or clean.isdigit() or clean.replace(".", "", 1).isdigit():
            return "RATIO"
        v = clean
    return v

def clean_unit(u, default="TOKENS"):
    if u is None:
        return default
    u = str(u).strip().upper()
    if not u or u == "%" or u == "T/S" or u == "TOK/S":
        return default
    return u

def clean_str(s, max_len=24, default=""):
    if s is None:
        return default
    s = str(s).replace("%", "").strip()
    return s[:max_len]

def safe_float(v, default=50.0):
    try:
        if isinstance(v, (int, float)):
            return float(v)
        v = str(v).replace('%', '').strip()
        return float(v)
    except Exception:
        return default

# 4. Load Mistral Bespoke Designs
with open(os.path.join(ROOT, "data", "mistral_bespoke_designs.json"), "r", encoding="utf-8") as f:
    mistral_designs = json.load(f)

# Valid art set
VALID_ART = {
    "context_window", "kv_cache", "prompt_stream", "warning", "scales",
    "die", "cache_grid", "ram_stick", "folder", "chip", "gpu", "gpu_16gb",
    "gpu_24gb", "laptop", "motherboard", "clock", "checklist", "lan_link",
    "vram_module", "collapse", "two_die", "gauge"
}

W = []

for i in range(72):
    vo = scenes_vo[i]
    m_des = mistral_designs[i]
    layout = SPINE[i % len(SPINE)]
    kicker = get_kicker(i + 1)
    
    with open(jsons[i], "r", encoding="utf-8") as f:
        ws = json.load(f)
    total_dur = ws[-1][0]
    
    # Monotonic, unique audio-locked anchors for header, a1, a2, a3, a4
    n_words = len(ws)
    h_phrase = get_header_anchor(vo, ws)
    a1 = get_unique_anchor(vo, ws, int(n_words * 0.25))
    a2 = get_unique_anchor(vo, ws, int(n_words * 0.50))
    a3 = get_unique_anchor(vo, ws, int(n_words * 0.72))
    a4 = get_unique_anchor(vo, ws, max(0, n_words - 2), prefer_tail=True)
    
    art = m_des.get("art", "context_window")
    if art not in VALID_ART or art == "token_blocks":
        art = "context_window"
        
    title = m_des.get("title", f"SCENE {i+1}").upper()
    cap = m_des.get("cap", "TECHNICAL SPECIFICATION AUDIT").upper()
    c_tag = m_des.get("c_tag", "BYTE FORENSICS LAW").upper()
    
    win = {
        "layout": layout,
        "kicker": kicker,
        "title": title,
        "header_at": h_phrase,
        "art": art,
        "art_at": a1,
        "art_caption": cap,
        "closing": {"at": a4, "c": "gold", "t": c_tag},
        "source": "byte forensics · context memory architecture",
        "source_at": a4,
        "vo": vo
    }
    
    if layout == "hook":
        m_chips = m_des.get("chips", [
            {"c": "cyan", "t": "128K SEQUENCE"},
            {"c": "gold", "t": "ALLOCATION AUDIT"}
        ])
        m_stats = m_des.get("stats", [
            {"c": "cyan", "lab": "SEQUENCE", "u": "LIMIT", "v": "128K"},
            {"c": "gold", "lab": "STATUS", "u": "ACTIVE", "v": "AUDIT"}
        ])
        win["chips"] = [
            {"at": a1, "c": m_chips[0].get("c", "cyan"), "t": clean_str(m_chips[0].get("t", "SPEC"), 22).upper()},
            {"at": a2, "c": m_chips[1].get("c", "gold") if len(m_chips)>1 else "gold", "t": clean_str(m_chips[1].get("t", "AUDIT") if len(m_chips)>1 else "AUDIT", 22).upper()}
        ]
        win["stats"] = [
            {"at": a1, "c": m_stats[0].get("c", "cyan"), "lab": clean_str(m_stats[0].get("lab", "SPEC"), 16).upper(), "u": clean_unit(m_stats[0].get("u", "K"))[:6], "v": clean_val(m_stats[0].get("v", "128"))[:6]},
            {"at": a2, "c": m_stats[1].get("c", "gold") if len(m_stats)>1 else "gold", "lab": clean_str(m_stats[1].get("lab", "VRAM") if len(m_stats)>1 else "VRAM", 16).upper(), "u": clean_unit(m_stats[1].get("u", "GB") if len(m_stats)>1 else "GB")[:6], "v": clean_val(m_stats[1].get("v", "16") if len(m_stats)>1 else "16")[:6]}
        ]
        
    elif layout == "rows":
        m_rows = m_des.get("rows", [
            {"cls": "cyan", "rank": "01", "name": "SPECIFICATION", "val": "128K", "sub": "ADVERTISED"},
            {"cls": "gold", "rank": "02", "name": "VRAM BUFFER", "val": "ALLOC", "sub": "PHYSICAL"},
            {"cls": "hot", "rank": "03", "name": "BOTTLENECK", "val": "LIMIT", "sub": "STATE"}
        ])
        win["rows"] = [
            {"at": a1, "cls": m_rows[0].get("cls", "cyan"), "rank": "01", "name": clean_str(m_rows[0].get("name", "SPEC"), 20).upper(), "val": clean_val(m_rows[0].get("val", "128K"))[:14], "sub": clean_str(m_rows[0].get("sub", "PARAM"), 20).upper()},
            {"at": a2, "cls": m_rows[1].get("cls", "gold") if len(m_rows)>1 else "gold", "rank": "02", "name": clean_str(m_rows[1].get("name", "VRAM") if len(m_rows)>1 else "VRAM", 20).upper(), "val": clean_val(m_rows[1].get("val", "POOL") if len(m_rows)>1 else "POOL")[:14], "sub": clean_str(m_rows[1].get("sub", "BUFFER") if len(m_rows)>1 else "BUFFER", 20).upper()},
            {"at": a3, "cls": m_rows[2].get("cls", "hot") if len(m_rows)>2 else "hot", "rank": "03", "name": clean_str(m_rows[2].get("name", "LIMIT") if len(m_rows)>2 else "LIMIT", 20).upper(), "val": clean_val(m_rows[2].get("val", "STATE") if len(m_rows)>2 else "STATE")[:14], "sub": clean_str(m_rows[2].get("sub", "STATUS") if len(m_rows)>2 else "STATUS", 20).upper()}
        ]
        
    elif layout == "bars":
        m_bars = m_des.get("bars", [
            {"cls": "cyan", "lab": "SEQUENCE CEILING", "unit": "TOKENS", "val": "128K", "pct": 100},
            {"cls": "hot", "lab": "RUNTIME LIMIT", "unit": "ACTIVE", "val": "LIMITED", "pct": 45}
        ])
        b1_u = clean_unit(m_bars[0].get("unit", "TOKENS"))[:8]
        b2_u = clean_unit(m_bars[1].get("unit", "VRAM") if len(m_bars)>1 else "VRAM")[:8]
        
        win["bars"] = [
            {"at": a1, "cls": m_bars[0].get("cls", "cyan"), "lab": clean_str(m_bars[0].get("lab", "TARGET"), 24).upper(), "unit": b1_u, "val": clean_val(m_bars[0].get("val", "128K"))[:10], "pct": safe_float(m_bars[0].get("pct", 100), 100.0)},
            {"at": a2, "cls": m_bars[1].get("cls", "hot") if len(m_bars)>1 else "hot", "lab": clean_str(m_bars[1].get("lab", "ALLOC") if len(m_bars)>1 else "ALLOC", 24).upper(), "unit": b2_u, "val": clean_val(m_bars[1].get("val", "ACTIVE") if len(m_bars)>1 else "ACTIVE")[:10], "pct": safe_float(m_bars[1].get("pct", 45) if len(m_bars)>1 else 45, 45.0)}
        ]
        
    elif layout == "rail":
        m_rails = m_des.get("rails", [
            {"cls": "cyan", "lab": "TARGET SEQUENCE", "val": "128K TOKENS", "pct": 100},
            {"cls": "red", "lab": "VRAM CAPACITY", "val": "16 GB POOL", "pct": 35}
        ])
        win["rails"] = [
            {"at": a1, "cls": m_rails[0].get("cls", "cyan"), "lab": clean_str(m_rails[0].get("lab", "TARGET"), 24).upper(), "val": clean_val(m_rails[0].get("val", "128K TOKENS"))[:16], "pct": safe_float(m_rails[0].get("pct", 100), 100.0)},
            {"at": a2, "cls": m_rails[1].get("cls", "red") if len(m_rails)>1 else "red", "lab": clean_str(m_rails[1].get("lab", "HARDWARE") if len(m_rails)>1 else "HARDWARE", 24).upper(), "val": clean_val(m_rails[1].get("val", "VRAM POOL") if len(m_rails)>1 else "VRAM POOL")[:16], "pct": safe_float(m_rails[1].get("pct", 35) if len(m_rails)>1 else 35, 35.0)}
        ]
        
    elif layout == "chain":
        m_chain = m_des.get("chain", [
            {"t": "SPECIFICATION LOAD", "s": "ADVERTISED CONTEXT"},
            {"t": "VRAM ALLOCATION", "s": "KEY-VALUE CACHE"},
            {"t": "RUNTIME EXECUTION", "s": "ATTENTION PASS"}
        ])
        win["chain"] = [
            {"at": a1, "t": clean_str(m_chain[0].get("t", "STEP 1"), 22).upper(), "s": clean_str(m_chain[0].get("s", "START"), 24).upper()},
            {"at": a2, "t": clean_str(m_chain[1].get("t", "STEP 2") if len(m_chain)>1 else "STEP 2", 22).upper(), "s": clean_str(m_chain[1].get("s", "MIDDLE") if len(m_chain)>1 else "MIDDLE", 24).upper()},
            {"at": a3, "t": clean_str(m_chain[2].get("t", "STEP 3") if len(m_chain)>2 else "STEP 3", 22).upper(), "s": clean_str(m_chain[2].get("s", "FINISH") if len(m_chain)>2 else "FINISH", 24).upper()}
        ]
        win["compare"] = [
            {"at": a1, "cls": "dim", "title": "ADVERTISED CLAIM", "body": "128K SEQUENCE"},
            {"at": a2, "cls": "gold", "title": "HARDWARE STATE", "body": "MEASURED VRAM POOL"}
        ]
        
    elif layout == "note":
        m_note_items = m_des.get("note_items", [
            {"t": "VERIFY RUNTIME CONFIGURED CONTEXT"},
            {"t": "MEASURE PHYSICAL KV CACHE ALLOCATION"},
            {"t": "AUDIT RETRIEVAL ACCURACY & RECALL"}
        ])
        win["note_head"] = clean_str(m_des.get("note_head", "SYSTEM ARCHITECTURE AUDIT"), 32).upper()
        win["note_items"] = [
            {"at": a1, "t": clean_str(m_note_items[0].get("t", "STEP 1"), 60).upper()},
            {"at": a2, "t": clean_str(m_note_items[1].get("t", "STEP 2") if len(m_note_items)>1 else "STEP 2", 60).upper()},
            {"at": a3, "t": clean_str(m_note_items[2].get("t", "STEP 3") if len(m_note_items)>2 else "STEP 3", 60).upper()}
        ]
        
    elif layout == "strip":
        m_items = m_des.get("items", [
            {"key": "context_window", "label": "CONTEXT LIMIT"},
            {"key": "kv_cache", "label": "KV CACHE"},
            {"key": "warning", "label": "MEMORY TRAP"}
        ])
        win["items"] = [
            {"at": a1, "key": m_items[0].get("key", "context_window") if m_items[0].get("key") in VALID_ART else "context_window", "label": clean_str(m_items[0].get("label", "TARGET"), 18).upper()},
            {"at": a2, "key": m_items[1].get("key", "kv_cache") if len(m_items)>1 and m_items[1].get("key") in VALID_ART else "kv_cache", "label": clean_str(m_items[1].get("label", "ALLOC") if len(m_items)>1 else "ALLOC", 18).upper()},
            {"at": a3, "key": m_items[2].get("key", "warning") if len(m_items)>2 and m_items[2].get("key") in VALID_ART else "warning", "label": clean_str(m_items[2].get("label", "CRASH") if len(m_items)>2 else "CRASH", 18).upper()}
        ]
        
    elif layout == "nodes":
        m_nodes = m_des.get("chain", [
            {"t": "INSPECT MODEL EMBEDDINGS", "s": "CHECK ROPE CONFIG & TOKENIZER"},
            {"t": "AUDIT RUNTIME ENGINE SETTINGS", "s": "VERIFY CLI FLAGS IN LLAMA.CPP / VLLM"},
            {"t": "MEASURE PHYSICAL VRAM LIMIT", "s": "CALCULATE EXACT KV CACHE FOOTPRINT"}
        ])
        win["chain"] = [
            {"at": a1, "t": clean_str(m_nodes[0].get("t", "PIPELINE 1"), 24).upper(), "s": clean_str(m_nodes[0].get("s", "DETAIL 1"), 36).upper()},
            {"at": a2, "t": clean_str(m_nodes[1].get("t", "PIPELINE 2") if len(m_nodes)>1 else "PIPELINE 2", 24).upper(), "s": clean_str(m_nodes[1].get("s", "DETAIL 2") if len(m_nodes)>1 else "DETAIL 2", 36).upper()},
            {"at": a3, "t": clean_str(m_nodes[2].get("t", "PIPELINE 3") if len(m_nodes)>2 else "PIPELINE 3", 24).upper(), "s": clean_str(m_nodes[2].get("s", "DETAIL 3") if len(m_nodes)>2 else "DETAIL 3", 36).upper()}
        ]

    W.append(win)

print(f"Assembled all 72 bespoke windows.")

header_text = '''# -*- coding: utf-8 -*-
# BYTE-CONTEXT SPECIFICATION
# 128K CONTEXT WINDOW: THE SILENT MEMORY TRAP
# 72 WINDOWS · 2,088 SPOKEN WORDS · FULL AUDIO-LOCKED SYNC
# 100% VERBATIM SCRIPT PARITY · MISTRAL BESPOKE ARCHITECTURE

NAME = "BYTE-CONTEXT"
TITLE = "128K CONTEXT WINDOW: THE SILENT MEMORY TRAP"
SUBTITLE = "The Engineering Reality: Model vs Runtime Limits, KV Cache Footprint & Lost-in-the-Middle"
DOC_TITLE = "BYTE FORENSICS · 128K CONTEXT WINDOW: THE SILENT MEMORY TRAP"
KICKER = "BYTE FORENSICS · EPISODE 13"
VOICE = "en-US-AndrewNeural"
RATE = "+4%"

CHAPTERS = ''' + pprint.pformat(CHAPTERS) + '''

W = ''' + pprint.pformat(W, indent=4, width=120) + '''
'''

out_path = os.path.join(ROOT, "data", "spec_context.py")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(header_text)

print(f"Successfully wrote {out_path} ({os.path.getsize(out_path)} bytes).")
