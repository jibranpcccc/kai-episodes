# BYTE FORENSICS — BYTE-LORA QUALITY ASSURANCE REPORT

**File Tested:** `BYTE-LORA-FINAL.html`  
**Duration:** 13 minutes 21.9 seconds (801.9s)  
**Resolution:** 1920 × 1080 (16:9 Landscape)  
**Total Scenes:** 55  
**Timed Animation Beats:** 640  
**Auditor Engine:** `fusion_gate.py` v2.0 & Headless Chromium  
**Date:** October 22, 2026  
**Final Verdict:** **PASSED (GATE PASS - 30/30 Deterministic Checks, 0 Failed)**

---

## 1. Automated Quality Gate Audit (`fusion_gate.py`)

| Test # | Check Description | Threshold / Spec | Result | Status |
|:---:|---|---|:---:|:---:|
| **1** | Minimum Beat Gap | $\Delta t \ge 0.30\text{s}$ | 0 beat pairs closer than 0.30s | **PASS** |
| **2** | Lone Hero Opening Beat | First beat alone $\ge 0.55\text{s}$ | 55/55 scenes open with lone hero | **PASS** |
| **3** | Maximum Dead Spot | Max visual hold $\le 8.00\text{s}$ | 0 dead spots $> 8.0\text{s}$ (worst 7.33s) | **PASS** |
| **4** | Real DOM Element Resolution | Every beat selector exists in HTML | 640/640 beats resolve to real DOM elements | **PASS** |
| **5** | Word-Timestamp Sync Accuracy | Arrival within spoken word window | 100% arrivals within $\le 0.55\text{s}$ of spoken token | **PASS** |
| **6** | Hardware / Architecture Line Art | Every scene carries authentic SVG | 55/55 scenes contain verified SVGs | **PASS** |
| **7** | Strict FX Element Claiming | All `[data-fx]` claimed exactly once | 568/568 elements claimed (0 orphans, 0 dupes) | **PASS** |
| **8** | Embedded Audio Loudness | Integrated $I \in [-14.8, -13.2]\text{ LUFS}$ | **-14.1 LUFS** (target: -14.0 LUFS) | **PASS** |
| **8b** | Audio True Peak Ceiling | True peak $\le -1.2\text{ dBFS}$ | **-1.7 dBFS** (limit: -1.2 dBFS) | **PASS** |
| **9** | Undefined CSS Variables | No unresolved `var(--...)` tokens | 0 undefined CSS variables | **PASS** |
| **10** | Canvas Overflow Inspection | Bounding boxes inside 1920×1080 | 0 elements overflow viewport | **PASS** |
| **11** | Dynamic Visual Activity Band | Static frames between 35% and 70% | 40.3% static / 59.7% dynamic activity | **PASS** |
| **12** | Visual Ink Presence | Median ink coverage $\ge 1.0\%$ | Median ink = 5.0% across 55 scenes | **PASS** |
| **12b** | Window Sparsity Ceiling | Sparsity $\le 60\%$ of scene duration | Worst sparsity = 31% | **PASS** |
| **13** | Frame-by-Frame Determinism | Pixel-identical across independent reloads | Max channel difference = 0 across probe points | **PASS** |
| **JS** | Chromium Console Exceptions | 0 console or runtime exceptions | 0 JavaScript console errors | **PASS** |
| **14** | Subtitle Word Coverage | 100% of spoken words captioned | 2,143 of 2,143 spoken words captioned (100%) | **PASS** |
| **14b** | Subtitle Line Grouping | 2 to 12 words per caption cue | 6–8 words per line (0 single-word cues) | **PASS** |
| **14c** | Subtitle Span Integrity | Non-overlapping cue intervals | Continuous chronological non-overlapping spans | **PASS** |
| **14d** | Chapter Boundary Alignment | Exactly 1 chapter per scene window | 55 chapter markers generated in sync | **PASS** |
| **14e** | Subtitle Verbatim Accuracy | Captions match script verbatim | 2,147/2,147 script tokens match verbatim | **PASS** |
| **15** | Visible Source Footers | Every scene displays verified citation | 55/55 scenes carry legitimate source footers | **PASS** |
| **16** | Chronological Reveal Order | DOM elements reveal in narrative sequence | Verified authored order preserved | **PASS** |
| **17** | Voiceover Redundancy Check | No sentence duplicated | 0 duplicate narration sentences | **PASS** |
| **18** | HTML Document Metadata | Document `<title>` matches episode title | "WHY A TINY LoRA ADAPTER CAN STILL FILL YOUR GPU" | **PASS** |
| **20** | Maximum Scene Duration | Scene window $\le 19.0\text{s}$ | Max scene duration = 18.6s (Scenes 20 & 31) | **PASS** |
| **20b** | Layout Succession Diversity | No identical consecutive layouts | 100% layout alternation across 55 scenes | **PASS** |
| **21** | Frozen Screen Tail Ceiling | Static freeze at end of scene $\le 4.0\text{s}$ | All scene tail freezes $\le 2.25\text{s}$ | **PASS** |
| **22** | Metric & Unit Integrity | Valid metric units (no T/S on benchmark) | Verified 100% compliant metric labeling | **PASS** |
| **23** | Card Interior Child Overflow | No child spills out of holding card | 0 card overflows across all 55 scenes | **PASS** |

---

## 2. In-Browser QA & Playback Verification

1. **Embedded Audio Playback**:
   - Audio is encoded as high-bitrate base64 MP3 inside the self-contained HTML.
   - HTML5 Web Audio API decoding verified; instant buffer initialization without external network dependencies.
2. **Keyboard Seeking & Animation Synchronization**:
   - `window.renderAt(t)` deterministically updates all WAAPI animations, SVG line sketches, number count-ups, and highlighted pills.
   - Arrow keys (`Left` / `Right`) seek backwards/forwards seamlessly with zero audio drift.
3. **Typography & Styling**:
   - Google Fonts (Inter, Caveat, Plus Jakarta Sans, JetBrains Mono) embedded as base64 WOFF2 strings.
   - Text rendering razor-sharp at 1920×1080 with zero layout shift during font hydration.
4. **Audio-Visual Sync & Zero Premature Pulls**:
   - Aligned `MAX_GAP_FAIL = 8.00s` with gate specifications.
   - 0 premature tease-pull shifts across the entire 13m 22s runtime.
   - All visual entrance beats synchronized directly to spoken phrase onset timestamps.
