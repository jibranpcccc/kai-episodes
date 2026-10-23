# BYTE FORENSICS — BYTE-LORA TECHNICAL SOURCES & MATHEMATICAL PROOFS

## 1. Primary Model Architecture Specification

- **Target Model:** `Qwen/Qwen2.5-3B-Instruct`
- **Official Hugging Face Configuration:** [https://huggingface.co/Qwen/Qwen2.5-3B-Instruct/blob/main/config.json](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct/blob/main/config.json)
- **Key Architectural Constants:**
  - Hidden Size ($d$): `2,048`
  - Intermediate / MLP Size ($d_{mlp}$): `11,008`
  - Number of Hidden Layers ($L$): `36`
  - Number of Attention Query Heads: `16`
  - Number of Key/Value Heads ($n_{kv}$): `2` (Grouped-Query Attention)
  - Head Dimension ($d_k$): `128`
  - Attention Key/Value Dimension: $2 \times 128 = \mathbf{256}$
  - Attention Query / Output Dimension: $16 \times 128 = \mathbf{2,048}$

---

## 2. Mathematical Derivations

### A. LoRA Rank-16 Trainable Parameter Counts

Under Low-Rank Adaptation (LoRA), an original weight matrix $W \in \mathbb{R}^{d_{in} \times d_{out}}$ is adapted via low-rank decomposition:
$$\Delta W = B \cdot A$$
where $A \in \mathbb{R}^{r \times d_{in}}$ and $B \in \mathbb{R}^{d_{out} \times r}$.  
Trainable parameters per adapted linear projection:
$$P = r \times d_{in} + d_{out} \times r = r \times (d_{in} + d_{out})$$

For rank $r = 16$:

#### 1. Attention Projections
- **Query Projection (`q_proj`)**:
  - $d_{in} = 2,048, \quad d_{out} = 2,048$
  - Parameters $= 16 \times (2,048 + 2,048) = 16 \times 4,096 = \mathbf{65,536}$
- **Key Projection (`k_proj`)**:
  - $d_{in} = 2,048, \quad d_{out} = 256$
  - Parameters $= 16 \times (2,048 + 256) = 16 \times 2,304 = \mathbf{36,864}$
- **Value Projection (`v_proj`)**:
  - $d_{in} = 2,048, \quad d_{out} = 256$
  - Parameters $= 16 \times (2,048 + 256) = 16 \times 2,304 = \mathbf{36,864}$
- **Output Projection (`o_proj`)**:
  - $d_{in} = 2,048, \quad d_{out} = 2,048$
  - Parameters $= 16 \times (2,048 + 2,048) = 16 \times 4,096 = \mathbf{65,536}$

#### 2. MLP / Feed-Forward Projections
- **Gate Projection (`gate_proj`)**:
  - $d_{in} = 2,048, \quad d_{out} = 11,008$
  - Parameters $= 16 \times (2,048 + 11,008) = 16 \times 13,056 = \mathbf{208,896}$
- **Up Projection (`up_proj`)**:
  - $d_{in} = 2,048, \quad d_{out} = 11,008$
  - Parameters $= 16 \times (2,048 + 11,008) = 16 \times 13,056 = \mathbf{208,896}$
- **Down Projection (`down_proj`)**:
  - $d_{in} = 11,008, \quad d_{out} = 2,048$
  - Parameters $= 16 \times (11,008 + 2,048) = 16 \times 13,056 = \mathbf{208,896}$

#### Layer Totals & Full-Model Sums
- **Case 1: Query & Value Only ($q\_proj + v\_proj$)**:
  - Per layer: $65,536 + 36,864 = \mathbf{102,400}$
  - Across 36 layers: $102,400 \times 36 = \mathbf{3,686,400}$ trainable parameters (~3.69M).
- **Case 2: All Seven Projections Targeted ($q + k + v + o + gate + up + down$)**:
  - Attention per layer: $65,536 + 36,864 + 36,864 + 65,536 = 204,800$
  - MLP per layer: $208,896 + 208,896 + 208,896 = 626,688$
  - Total per layer: $204,800 + 626,688 = \mathbf{831,488}$
  - Across 36 layers: $831,488 \times 36 = \mathbf{29,933,568}$ trainable parameters (~29.93M).

*(Proof that the previous value of 25,067,520 was derived under an erroneous MLP dimension or missing gate/up projection factors).*

---

### B. Adapter State Memory Subtotal

Assuming full-precision (FP32) training for adapter arrays:
1. Adapter Weights: $4\text{ bytes/parameter}$
2. Adapter Gradients: $4\text{ bytes/parameter}$
3. First Adam Moment buffer: $4\text{ bytes/parameter}$
4. Second Adam Moment buffer: $4\text{ bytes/parameter}$

Total theoretical memory per trainable parameter:
$$\text{Bytes per parameter} = 4 + 4 + 4 + 4 = 16\text{ bytes}$$

For all 7 projections ($29,933,568\text{ parameters}$):
$$\text{Total Bytes} = 29,933,568 \times 16 = 478,937,088\text{ bytes}$$
$$\text{Mebibytes (MiB)} = \frac{478,937,088}{1,048,576} = \mathbf{456.75\text{ MiB}}$$

*(Proof that 456.75 MiB is the exact theoretical adapter subtotal for these four arrays, correcting the old incorrect "382.5 MiB, NOT 457" assertion).*

---

## 3. Evidence Categories & Literature References

| Evidence Class | Description | Source / Reference in Episode |
|---|---|---|
| **DERIVED** | Mathematical calculations based on explicit architectural parameters | Qwen2.5-3B config.json: 3,686,400 (Q/V), 29,933,568 (All 7), 456.75 MiB adapter subtotal, KV-cache formulas ($2 \times 36 \times 2 \times 128 \times L \times 2\text{ bytes}$). |
| **EXTERNAL BENCHMARK** | Peer-reviewed empirical results published in seminal research | **Hu et al. 2021 (LoRA)**: GPT-3 175B WikiSQL (73.8 FT vs 73.4 LoRA) and MNLI (89.5 FT vs 91.7 LoRA).<br>**Dettmers et al. 2023 (QLoRA)**: LLaMA 7B Alpaca tuning, NF4 + double quantization scoring, 65B model on 48GB GPU. |
| **MEASURED** | Direct empirical measurements conducted under documented hardware & OS testbeds | Training run power measurement via wall wattmeter (250W average system draw across 1 hour = 0.25 kWh), VRAM allocation monitoring under PyTorch CUDA memory allocator. |
| **ESTIMATED** | Qualified engineering rules of thumb & architectural bounds | Activation memory scaling under forward pass without checkpointing, CUDA workspace overhead (500–1000 MiB), gradient accumulation memory buffers. |

---

## 4. Key Citations

1. **Hu, Edward J., et al. (2021)**:  
   *LoRA: Low-Rank Adaptation of Large Language Models*.  
   arXiv:2106.09685 [cs.CL]. [https://arxiv.org/abs/2106.09685](https://arxiv.org/abs/2106.09685)
2. **Dettmers, Tim, et al. (2023)**:  
   *QLoRA: Efficient Finetuning of Quantized LLMs*.  
   arXiv:2305.14314 [cs.LG]. [https://arxiv.org/abs/2305.14314](https://arxiv.org/abs/2305.14314)
3. **Qwen Team (2024)**:  
   *Qwen2.5: A Party of Foundation Models*.  
   [https://github.com/QwenLM/Qwen2.5](https://github.com/QwenLM/Qwen2.5) & [https://huggingface.co/Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)
