# BYTE FORENSICS — BYTE-LORA PRODUCTION REPAIR & QUALITY UPGRADE
## CHANGELOG & DETAILED AUDIT REPORT

**Date:** October 22, 2026  
**Target Build:** `BYTE-LORA-FINAL.html`  
**Base Source:** `spec_lora_final.py` (derived from `spec_lora_full.py`)  
**Quality Gate Status:** **29 PASSED, 0 FAILED (GATE PASS)**  

---

### Executive Summary

The production file `BYTE-LORA.html` has been thoroughly audited and repaired without altering the visual identity, typography, color palette, or layout structure of the FUSION design system. All mathematical errors, obsolete citations, and disconnected explanations have been resolved. Audio narration, word-level timestamps, beat tables, on-screen text, number counters, and captions now 100% agree.

---

### Itemized Priority Breakdown

#### Priority 1 — LoRA Parameter Calculation for Qwen2.5-3B-Instruct
- **Architectural Ground Truth** (from official `Qwen/Qwen2.5-3B-Instruct` config.json):
  - Hidden Dimension ($d$): 2,048
  - Intermediate / MLP Dimension ($d_{mlp}$): 11,008
  - Hidden Layers: 36
  - Attention Heads: 16
  - KV Heads: 2 (Grouped-Query Attention with head dimension 128; KV dim = $2 \times 128 = 256$)
- **Query & Value Only (Rank 16)**:
  - `q_proj`: $2048 \times 16 + 16 \times 2048 = 65,536$
  - `v_proj`: $2048 \times 16 + 16 \times 256 = 36,864$
  - Per layer: $102,400$. Across 36 layers: **3,686,400 trainable parameters** (*Preserved*).
- **All Seven Projections (Rank 16)**:
  - `q_proj`: $2048 \times 16 + 16 \times 2048 = 65,536$
  - `k_proj`: $2048 \times 16 + 16 \times 256 = 36,864$
  - `v_proj`: $2048 \times 16 + 16 \times 256 = 36,864$
  - `o_proj`: $2048 \times 16 + 16 \times 2048 = 65,536$
  - `gate_proj`: $2048 \times 16 + 16 \times 11,008 = 208,896$
  - `up_proj`: $2048 \times 16 + 16 \times 11,008 = 208,896$
  - `down_proj`: $11,008 \times 16 + 16 \times 2048 = 208,896$
  - **Per Layer Total:** **831,488**
  - **36 Layers Total:** **29,933,568 trainable parameters** (29.93M).
- **Corrections Applied Everywhere**:
  - Replaced erroneous `25,067,520` $\to$ **`29,933,568`**.
  - Replaced erroneous `25.07M` $\to$ **`29.93M`**.
  - Replaced spoken `"twenty-five million"` $\to$ **`"twenty-nine point nine three million"`** and **`"twenty-nine million, nine hundred thirty-three thousand, five hundred sixty-eight"`**.
  - Updated all affected scenes: Scene 1 (Hook), Scene 13 (Chain), Scene 35 (Rows), and Scene 36 (Chain).

---

#### Priority 2 — Correct Adapter Memory Estimates
- **Theoretical 16 Bytes/Param Memory Footprint**:
  - FP32 Adapter Weights: 4 bytes
  - FP32 Gradients: 4 bytes
  - FP32 Adam 1st Moment: 4 bytes
  - FP32 Adam 2nd Moment: 4 bytes
  - Subtotal per parameter: **16 bytes**
  - Calculation: $29,933,568 \times 16 = 478,937,088\text{ bytes}$
  - Mebibytes: $478,937,088 / 1,048,576 = \mathbf{456.75\text{ MiB}}$.
- **Corrections Applied**:
  - Eliminated the erroneous `382.5 MiB` and the incorrect assertion `"382.5 MiB, NOT 457"`.
  - Displayed and voiced the exact figure: **`456.75 MiB`**.
  - Added explicit engineering qualifications clarifying that 456.75 MiB is the *theoretical adapter state subtotal* (weights + gradients + optimizer moments), and does NOT equal total GPU training VRAM, which must also accommodate the frozen base model, dynamic activation graphs, and CUDA workspaces.

---

#### Priority 3 — Voiceover Resynthesis & Timestamp Synchronization
- Edge-TTS regenerated affected narration windows using the authorized voice actor (`en-US-AndrewNeural`, `rate=+4%`).
- Word-level timestamps were precisely captured via Microsoft Speech Service word boundaries and adjusted for lead/tail silence via FFmpeg filters.
- Verified in `fusion_gate.py`:
  - `PASS 5: every arrival lands within 0.55s of its spoken word` (0 violations).
  - Master audio track calibrated with two-pass EBU R128 to **-14.1 LUFS** and **-1.7 dBFS true peak** (compliant with YouTube and broadcast loudness standards).

---

#### Priority 4 — Replaced Silicon Wafer Detour with Training Memory Mechanics
- **Scene 4 (~0:42)** was completely replaced:
  - *Old Content:* Generic explanation of semiconductor manufacturing (silicon wafers, dies, packages).
  - *New Content:* Highly focused, relevant technical breakdown of why LoRA training memory explodes despite tiny saved adapter weights:
    - **Frozen Base Weights:** Reside statically in VRAM.
    - **Forward Activations:** Stored dynamically at every layer to support the backward pass.
    - **Backpropagation Gradients & Optimizer States:** Live memory allocated for the trainable rank matrices.
    - **Core Insight:** Execution state, not file size, dictates hardware fit.
- Updated Scene 16 drawing from `art="wafer"` to `art="scales"` to match the GPT-3 175B evaluation metrics table.

---

#### Priority 5 — Audit of Technical Claims & Evidence Categories
- All technical citations across all 55 scenes audited and classified:
  - **MEASURED:** Direct empirical benchmarks run on specific hardware configurations.
  - **EXTERNAL BENCHMARK:** Peer-reviewed benchmarks from published papers (Hu et al. 2021, Dettmers et al. 2023).
  - **DERIVED:** Exact mathematical calculations based on published model architecture parameters (e.g. Qwen2.5-3B-Instruct config).
  - **ESTIMATED:** Qualified engineering bounds (e.g. KV-cache memory scaling, activation checkpointing tradeoffs).

---

#### Priority 6 — Replaced Incorrect Source Attribution
- **Scene 55 Source Footer**:
  - *Old Attribution:* `measured · hardware-corner.net · qwen3.8 27b · llama.cpp 153d324bc...` (completely unrelated to LoRA training).
  - *New Attribution:* `derived · Hu et al. 2021 (LoRA, arxiv 2106.09685) · Dettmers et al. 2023 (QLoRA, arxiv 2305.14314) · Qwen2.5-3B-Instruct config.json`.

---

#### Priority 7 — Visual Presentation Preservation
- Preserved the full FUSION visual system:
  - Dark cinematic obsidian canvas (`#0B0D13`).
  - Gold (`#F5D547`), cyan (`#47D5F5`), lime (`#B4E33D`), and coral red (`#FF5C5C`) accents.
  - Vector line-art SVGs that animate via WAAPI stroke-dashoffset sketching.
  - 639 synchronized animation beats across 55 scenes.
  - Zero layout repetition across consecutive scenes.

---

#### Priority 8 — Accurate English Captions
- Rebuilt `BYTE-LORA-FINAL.srt`:
  - 297 caption cues.
  - Exactly 2,145 words covering 100% of spoken narration.
  - Line-based grouping (6–8 words per cue) with standard comma millisecond formatting (`00:00:00,000`).
  - Zero single-word cues. Zero overlapping spans.

---

#### Priority 9 — Automated Quality Gate Results (`fusion_gate.py`)
```
FUSION GATE  BYTE-LORA-FINAL   runtime 802.7s   beats 639   words 2145

  PASS  1    no two beats within 0.30s
  PASS  2    every scene opens with a lone hero (>= 0.55s)
  PASS  3    no dead spot longer than 8.0s
  PASS  4    every beat resolves to a real element
  PASS  6    every window carries a drawing
  PASS  7    all 567 elements claimed exactly once
  PASS  10   nothing overflows the 1920x1080 canvas
  PASS  9    no undefined var(--x) colours
  PASS  5    every arrival lands within 0.55s of its spoken word
  PASS  11   static 40.5% / changed 59.5% (band 35-70% static)
        ink: min 0.0%  p5 2.0%  median 5.1%  max 27.9%   (55 windows)
  PASS  12   every window carries a picture (median ink >= 1.0%)
  PASS  12b  no window is mostly sparse (worst 31% of window 42)
  PASS  13   renderAt(t) is pixel-identical across two loads
  PASS  JS   no console errors
  PASS  8    embedded audio -14.1 LUFS (target -14 +/- 0.8)
  PASS  8b   true peak -1.7 dBFS (limit -1.2)
  PASS  14   captions cover all 2145 spoken words
  PASS  14b  every caption reads as a line (6-8 words)
  PASS  14c  no overlapping cues, the whole speech is captioned
  PASS  14d  chapters file has one line per window (55)
  PASS  14e  caption text is the script's own words (2149/2149)
  PASS  15   every window carries a source footer (55)
  PASS  16   every window reveals its elements in the authored order
  PASS  17   no sentence is narrated twice
  PASS  18   the document title carries the episode title
  PASS  20   no window runs longer than 19s (worst 18.6s)
  PASS  20b  no two consecutive windows share a layout
  PASS  21   no window ends on more than 4.0s of frozen screen
  PASS  22   every bar carries a unit and no score wears a T/S

Total: 29 passed, 4 warnings (long hold warnings), 0 failed
RESULT: GATE PASS
```
