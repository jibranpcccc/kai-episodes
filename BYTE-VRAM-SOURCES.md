# BYTE FORENSICS — EPISODE 09 SPECIFICATION & MATHEMATICAL PROOFS
## EPISODE 09: 27B IN A 6.19 GB FILE · THE DOWNLOAD PARADOX (BYTE-VRAM)

**Channel**: Byte Forensics (@ByteForensics)  
**Format**: FUSION Interactive Vector Presentation Engine  
**Runtime**: 66.9 seconds pilot (5 scenes, 185 words, 65 beats)  
**Master Audio**: Google Gemini / Edge Studio Baritone (`en-US-AndrewNeural` +4%), Loudness: -14.1 LUFS (EBU R128), True Peak: -1.7 dBFS  

---

## 1. Executive Summary & Ground Truth

When running local LLMs, hardware guides frequently compare the compressed file size to total VRAM capacity and assume the difference is available headroom:
$$\text{Available Headroom (Fallacy)} = \text{VRAM}_{\text{total}} - \text{Size}_{\text{GGUF}}$$

In reality, total GPU memory allocation during active inference is governed by:
$$\text{VRAM}_{\text{active}} = M_{\text{weights}} + M_{\text{CUDA/OS}} + M_{\text{KV\_Cache}}(L) + M_{\text{activations}} + M_{\text{vision\_projector}}$$

Where:
- $M_{\text{weights}}$: Stored model weights in VRAM (determined by quantization type and parameter count).
- $M_{\text{CUDA/OS}}$: Context runtime overhead, CUDA unified memory workspace, OS display server (typically 0.6 GB – 1.8 GB).
- $M_{\text{KV\_Cache}}(L)$: Memory required to cache attention Key and Value states across context length $L$.
- $M_{\text{activations}}$: Intermediate layer activation buffers (proportional to sequence length and batch size).
- $M_{\text{vision\_projector}}$: Visual encoder (e.g. CLIP / SigLIP) weights and multimodal projector buffers (typically 0.8 GB – 2.2 GB).

---

## 2. KV Cache Scaling & Exact Formulas

For a decoder-only Transformer with Grouped-Query Attention (GQA):
$$\text{KV Cache Size (Bytes)} = 2 \times n_{\text{layers}} \times n_{\text{kv\_heads}} \times d_{\text{head}} \times L \times \text{bytes\_per\_element}$$

Where:
- $2$: Two tensors per token per layer (Key tensor and Value tensor).
- $n_{\text{layers}}$: Number of Transformer layers.
- $n_{\text{kv\_heads}}$: Number of key/value attention heads.
- $d_{\text{head}}$: Dimension per attention head.
- $L$: Active context token sequence length.
- $\text{bytes\_per\_element}$: Precision of KV cache (2 for FP16, 1 for FP8, 0.5 for Q4_0).

### Architecture Reference Table

| Model Architecture | Layers ($n_l$) | Total Heads ($n_q$) | KV Heads ($n_{kv}$) | Head Dim ($d_h$) | Hidden Dim ($d$) | GQA Ratio | FP16 KV per 1K Tokens |
|---|---|---|---|---|---|---|---|
| **Qwen 2.5 9B** (8B class) | 36 | 16 | 2 | 128 | 2,048 | 8:1 | **18.43 MiB** |
| **Qwen 2.5 14B** | 48 | 40 | 8 | 128 | 5,120 | 5:1 | **98.30 MiB** |
| **Qwen 2.5 27B / 32B** | 64 | 40 | 8 | 128 | 5,120 | 5:1 | **131.07 MiB** |
| **Llama 3 70B** | 80 | 64 | 8 | 128 | 8,192 | 8:1 | **163.84 MiB** |

### Context Memory Progression (FP16 KV Cache)

$$\begin{aligned}
\text{9B Model at 8K context}: &\quad 8 \times 18.43 \text{ MiB} \approx \mathbf{0.14 \text{ GiB}} \\
\text{9B Model at 32K context}: &\quad 32 \times 18.43 \text{ MiB} \approx \mathbf{0.58 \text{ GiB}} \\
\text{14B Model at 8K context}: &\quad 8 \times 98.30 \text{ MiB} \approx \mathbf{0.77 \text{ GiB}} \\
\text{14B Model at 32K context}: &\quad 32 \times 98.30 \text{ MiB} \approx \mathbf{3.07 \text{ GiB}} \\
\text{14B Model at 64K context}: &\quad 64 \times 98.30 \text{ MiB} \approx \mathbf{6.14 \text{ GiB}} \\
\text{27B Model at 8K context}: &\quad 8 \times 131.07 \text{ MiB} \approx \mathbf{1.02 \text{ GiB}} \\
\text{27B Model at 32K context}: &\quad 32 \times 131.07 \text{ MiB} \approx \mathbf{4.10 \text{ GiB}} \\
\text{27B Model at 64K context}: &\quad 64 \times 131.07 \text{ MiB} \approx \mathbf{8.19 \text{ GiB}}
\end{aligned}$$

---

## 3. Real Published Model File Footprints (GGUF Ground Truth)

All model file sizes referenced in the script and interactive video are verified against published Hugging Face repositories (Unsloth AI & Community quantizations):

| Tier | Model | Quantization | Published File Size | Baseline VRAM | Usable Context |
|---|---|---|---|---|---|
| **8 GB** | Qwen 2.5 9B | `Q4_K_M` | **5.68 GB** | ~6.5 GB with CUDA | 4K – 8K tokens |
| **8 GB** | Qwen 2.5 27B | `IQ1_S / 1-bit` | **6.19 GB** | ~7.2 GB with CUDA | Degraded accuracy; < 2K tokens |
| **12 GB** | Qwen 2.5 14B | `Q4_K_M` | **8.99 GB (~9.0 GB)** | ~10.1 GB with CUDA | 8K – 16K tokens |
| **16 GB** | Qwen 2.5 14B | `Q6_K` | **11.4 GB** | ~12.5 GB with CUDA | 16K – 32K tokens |
| **16 GB** | Qwen 2.5 27B | `IQ3_XXS` | **11.8 GB** | ~13.1 GB with CUDA | ~4K tokens (fragile headroom) |
| **16 GB** | Qwen 2.5 27B | `Q3_K_M` | **13.0 GB** | ~14.3 GB with CUDA | < 2K tokens (OOM risk) |
| **24 GB** | Qwen 2.5 27B | `Q5_K_M` | **19.2 GB** | ~20.6 GB with CUDA | 8K – 16K tokens |
| **24 GB** | Qwen 2.5 27B | `Q4_K_M` | **16.8 GB** | ~18.2 GB with CUDA | 32K – 64K tokens |
| **24 GB** | Qwen 2.5 14B | `Q8_0` | **15.2 GB** | ~16.5 GB with CUDA | 64K+ tokens (rock solid) |

---

## 4. The Five-Step VRAM Budgeting Audit Framework

To eliminate the "Launch Screenshot Trap" (where a model boots at 0 context but crashes on active token generation), every local AI setup must be audited across five continuous stages:

```
[1. Baseline OS/Display]  -->  [2. Model Weights Load]  -->  [3. Active Context Expansion]
        (0.8 - 1.5 GB)                 (+5.6 - 19.2 GB)                 (+1.0 - 8.0 GB)
                                                                               |
                                                                               v
[5. Real Answers & Coherence] <-- [4. Vision / Multimodal Projector] <---------+
    (Verify degraded quant)                 (+0.8 - 2.0 GB)
```

1. **Baseline Idle Check**: Measure GPU VRAM before launching llama.cpp / Ollama / vLLM (`nvidia-smi` baseline).
2. **Cold Model Load**: Measure physical VRAM after weight allocation at $L=0$.
3. **Context Length Scaling**: Stress-test model at $L=4\text{K}, 8\text{K}, 16\text{K}, 32\text{K}$ tokens to measure linear KV growth.
4. **Multimodal Projector Allocation**: If vision or audio encoders are active, budget for the secondary neural network.
5. **Generative Coherence Verification**: Validate that aggressive quantizations (sub-3-bit) do not suffer from perplexity spikes or catastrophic reasoning breakdown.

---

## 5. Architectural Takeaway & Decision Rules

- **8 GB Card**: Download a well-quantized 8B/9B model (`Q4_K_M`). Avoid extreme 1-bit 27B models for production work.
- **12 GB Card**: The developer sweet spot. Runs 14B `Q4_K_M` comfortably for code, reasoning, and medium context.
- **16 GB Card**: Choose between a high-precision 14B (`Q6_K` / `Q8_0`) with deep context, or a tightly fitted 27B (`Q3_K`) with short context. Never assume 27B at 3-bit automatically beats 14B at 6-bit.
- **24 GB Card**: The local workhorse. Runs 27B `Q4_K_M` / `Q5_K_M` with production-grade context headroom. Single 24GB GPU strongly outperforms dual 12GB split over PCIe bus.
