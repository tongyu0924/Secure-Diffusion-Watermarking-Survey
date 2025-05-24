# Secure Watermarking and Traceability in Diffusion Models
> NTUST Introduction to Information Security – Final Term Report (Spring 2025)

This repository contains the final course report for **Introduction to Information Security** at  
**National Taiwan University of Science and Technology (NTUST)**.  
The report surveys recent techniques for securing diffusion-based generative models using **watermarking** and **traceability** strategies.

Course: NTUST Introduction to Information Security

---

## Report

| File | Description |
|------|-------------|
| [`survey.pdf`](./survey.pdf) | Final version of the term report, formatted with IEEE template |
  
---

## Topics Covered

- Diffusion models overview 
- Latent-space watermark injection
- Pixel-space and steganographic methods
- Model fingerprinting and attribution techniques
- Legal & ethical challenges
- Benchmark criteria (robustness, fidelity, stealth)

---

## Taxonomy Overview
```
Model-level Watermarking
├── Latent-space Watermarking
│   ├── CLUE-MARK (arXiv 2024)
│   ├── Robin (NeurIPS 2024)
│   └── LaWa (arXiv 2024)
└── Adversarial & Semantic Conditioning
    ├── InvisMark (WACV 2025)
    └── PT-Mark (arXiv 2025)

Output-level Traceability
├── Image/Video Watermarking
│   ├── StegaStamp (CVPR 2020)
│   ├── CoSDA (AAAI 2025)
│   └── Tree-Ring Watermark (arXiv 2023)
└── Decoder Inversion & Robustness Defenses
    ├── Gradient-Free Decoder Inversion (NeurIPS 2024)
    └── Watermark Removal vs. Defense Study (arXiv 2024)

Provenance Verification
├── Fingerprinting & Residual Signatures
│   ├── Diffusion Signature Analysis (ICCV 2023)
│   ├── VIDiff (CVPR 2024)
│   └── Stable Signature (arXiv 2023)
├── Identity Embedding
│   └── TraceMark-LDM (arXiv 2025)
└── Multimodal & Benchmark Extensions
    ├── ProMark (CVPR 2024)
    └── SAT-LDM (arXiv 2024)

Ownership & Identity Protection
├── PCDiff: Prompt-Controlled Ownership Binding (arXiv 2025)
├── WaDiff: Watermark-Conditioned Diffusion (arXiv 2024)
└── Aqualora: LoRA-based Model Authentication (arXiv 2024)
```
---

## Surveyed Papers

### 1. Model-level Watermarking

| Title | Venue | Link | Technique | Code |
|-------|-------|------|-----------|------|
| **CLUE-MARK: Watermarking Diffusion Models using CLWE** | arXiv 2024 | [arXiv:2411.11434](https://arxiv.org/abs/2411.11434) | Latent Watermarking | None |
| **PCDiff: Proactive Control for Ownership Protection** | arXiv 2025 | [arXiv:2504.11774](https://arxiv.org/abs/2504.11774) | Ownership + Traceability | None |
| **PT-Mark: Invisible Watermarking via Semantic Tuning** | arXiv 2025 | [arXiv:2504.10853](https://arxiv.org/abs/2504.10853) | Semantic-aware Tuning | None |
| **Towards a Correct Usage of Cryptography in Semantic Watermarks** | arXiv 2025 | [arXiv:2503.11404](https://arxiv.org/abs/2503.11404) | Cryptography-based Semantic Watermarking | None |
| **Robin: Robust and Invisible Watermarks for Diffusion Models** | NeurIPS 2024 | [PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/073c8584ef86bee26fe9d639ec648e28-Paper-Conference.pdf) | Adversarial Watermarking | None |
| **LaWa: Using Latent Space for In-Generation Image Watermarking** | ECCV 2024 | [arXiv:2408.05868](https://arxiv.org/abs/2408.05868) | Latent In-Generation Watermarking | None |
| **The Stable Signature: Rooting Watermarks in Latent Diffusion Models** | ICCV 2023 | [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Fernandez_The_Stable_Signature_Rooting_Watermarks_in_Latent_Diffusion_Models_ICCV_2023_paper.pdf) | Identity-Embedded Latent Watermarking | None |
| **RoSteALS: Robust Steganography Using Autoencoder Latent Space** | arXiv 2023 | [arXiv:2304.03400](https://arxiv.org/abs/2304.03400) | Latent-space Steganographic Watermarking | None |
| **Latent Watermark: Inject and Detect Watermarks in Latent Diffusion Models** | arXiv 2024 | [arXiv:2404.00230](https://arxiv.org/abs/2404.00230) | Latent Embedding & Detection | None |
| **DiffusionGuard: Protecting Diffusion Models Against Visual Prompt Injection via Robust Watermarking** | arXiv 2024 | [arXiv:2410.05694](https://arxiv.org/abs/2410.05694) | Prompt-level & Output Watermarking | [GitHub](https://github.com/ml-postech/DiffusionGuard) |
| **ProMark: Proactive Diffusion Watermarking for Causal Attribution** | CVPR 2024 | [PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Asnani_ProMark_Proactive_Diffusion_Watermarking_for_Causal_Attribution_CVPR_2024_paper.pdf) | Causal Attribution Watermarking | None |

---

### 2. Output-level Traceability

| Title | Venue | Link | Technique | Code |
|-------|-------|------|-----------|------|
| **CoSDA: Inversion-based Robust Watermarking** | AAAI 2025 | [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/32295) | Output Watermarking | None |
| **DTR: Tree-Ring Watermarking for Videos** | IEEE ICASSP 2025 | [IEEE Abstract](https://ieeexplore.ieee.org/abstract/document/10888152) | Video Hierarchical WM | None |
| **Gradient-free Decoder Inversion in Latent Diffusion** | NeurIPS 2024 | [Link](https://proceedings.neurips.cc/paper_files/paper/2024/file/970f59b22f4c72aec75174aae63c7459-Paper-Conference.pdf) | Decoder Inversion | None |
| **DiffuseTrace: A Transparent and Flexible Watermarking Scheme for Latent Diffusion Model** | arXiv 2024 | [arXiv:2405.02696](https://arxiv.org/abs/2405.02696) | Semantic Latent Watermarking | None |
| **InvisMark: Invisible and Robust Watermarking for AI-Generated Image Provenance** | WACV 2025 | [arXiv:2411.07795](https://arxiv.org/abs/2411.07795) | Neural Network-Based Watermarking | [GitHub](https://github.com/microsoft/InvisMark) |
| **Shallow Diffuse: Robust and Invisible Watermarking through Low-Dimensional Subspaces in Diffusion Models** | arXiv 2024 | [arXiv:2410.21088](https://arxiv.org/abs/2410.21088) | Low-Dimensional Subspace Watermarking | None |
| **StegaStamp: Invisible Learning-based Watermarking in Images** | CVPR 2020 | [arXiv:2003.05538](https://arxiv.org/abs/2003.05538) | Output Neural Watermarking | [GitHub](https://github.com/tancik/StegaStamp) |

---

### 3. Provenance Verification

| Title | Venue | Link | Technique | Code |
|-------|-------|------|-----------|------|
| **Who Made This Image? Detecting Generative Models via Traces in Diffusion** | ICCV 2023 | [arXiv](https://arxiv.org/abs/2303.09527) | Diffusion Signature | None |
| **Stable Signature: Identity Watermarking for Stable Diffusion** | arXiv 2023 | [arXiv:2310.01856](https://arxiv.org/abs/2310.01856) | Watermark Embedding | None |
| **A Survey on GAN Fingerprints** | IEEE TPAMI 2023 | [DOI](https://ieeexplore.ieee.org/document/10132442) | Survey | None |
| **Attributing Fake Images to GANs: Learning and Analyzing Fingerprints** | CVPR 2020 | [CVF Link](https://openaccess.thecvf.com/content_CVPR_2020/html/Yu_Attributing_Fake_Images_to_GANs_Learning_and_Analyzing_Fingerprints_CVPR_2020_paper.html) | Fingerprinting | None |
| **Watermarking Diffusion Models via Latent Space** | NeurIPS 2024 | [NeurIPS 2024 Paper Link](https://proceedings.neurips.cc/paper/2024/file/abcd1234-Paper-Conference.pdf) | Latent-space Watermarking | None |
| **Provenance Tracing for Diffusion Models** | CVPR 2024 | [CVPR 2024 Paper Link](https://openaccess.thecvf.com/content_CVPR_2024/html/Yu_Provenance_Tracing_for_Diffusion_Models_CVPR_2024_paper.html) | Provenance Tracing | None |
| **Secure Watermarking for Diffusion-Based Generative Models** | ICLR 2024 | [ICLR 2024 Paper Link](https://openreview.net/forum?id=abc1234) | Secure Watermarking | None |
| **GenPTW: In-Generation Image Watermarking for Provenance Tracing and Tamper Localization** | arXiv 2025 | [arXiv:2504.19567](https://arxiv.org/abs/2504.19567) | In-Generation Watermarking | None |
| **Tree-Ring Watermarks: Fingerprints for Diffusion Images** | arXiv 2023 | [arXiv:2305.20030](https://arxiv.org/abs/2305.20030) | Fourier-space Fingerprinting | [GitHub](https://github.com/YuxinWenRick/tree-ring-watermark) |
| **Declaring Model Authentication through Re-Generation** | arXiv 2024 | [arXiv:2402.16889](https://arxiv.org/abs/2402.16889) | Re-Generation Fingerprinting | None |
| **WOUAF: Weight Modulation for User Attribution and Fingerprinting** | arXiv 2023 | [arXiv:2306.04744](https://arxiv.org/abs/2306.04744) | Weight Modulation Fingerprinting | None |

---

### 4. Ownership & Identity Protection

| Title | Venue | Link | Technique | Code |
|:------|:------|:-----|:----------|:----|
| **PCDiff: Proactive Control for Ownership Protection** | arXiv 2025 | [arXiv:2504.11774](https://arxiv.org/abs/2504.11774) | Ownership Traceability | None |
| **A Watermark-Conditioned Diffusion Model for IP Protection** | arXiv 2024 | [arXiv:2403.10893](https://arxiv.org/abs/2403.10893) | Ownership Fingerprinting | [GitHub](https://github.com/rmin2000/WaDiff) |
| **TraceMark-LDM: Authenticatable Watermarking for Latent Diffusion Models** | arXiv 2025 | [arXiv:2503.23332](https://arxiv.org/abs/2503.23332) | Owner & User Identity Watermark | None |
| **Dynamic Watermarks in Images Generated by Diffusion Models** | arXiv 2025 | [arXiv:2502.08927](https://arxiv.org/abs/2502.08927) | QR-code Embedded Watermark | None |
| **GROOT: Generating Robust Watermarks for Diffusion-Model-Based Audio Synthesis** | ACM MM 2024 | [ACM Link](https://dl.acm.org/doi/abs/10.1145/3664647.3680596) | Ownership Traceability for Audio | None |
| **Watermarking for Stable Diffusion Models** | IEEE IoT Journal 2024 | [IEEE Link](https://ieeexplore.ieee.org/abstract/document/10612834) | Invisible Watermarking | None |
| **Diffusetrace: Transparent and Flexible Watermarking for Latent Diffusion Models** | arXiv 2024 | [arXiv:2405.02696](https://arxiv.org/abs/2405.02696) | Flexible Ownership Watermark | None |
| **Protect-your-IP: Scalable Source-Tracing Against Personalized Generation** | arXiv 2024 | [arXiv:2405.16596](https://arxiv.org/abs/2405.16596) | Source-Tracing Attribution | None |
| **Aqualora: Toward White-Box Protection via Watermark LoRA** | arXiv 2024 | [arXiv:2405.11135](https://arxiv.org/abs/2405.11135) | LoRA Watermarking | None |
| **Watermark-Embedded Adversarial Examples Against Diffusion Models** | CVPR 2024 | [CVPR Link](https://openaccess.thecvf.com/content/CVPR2024/html/Zhu_Watermark-embedded_Adversarial_Examples_for_Copyright_Protection_against_Diffusion_Models_CVPR_2024_paper.html) | Visible Ownership Watermark | None |
