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
│   └── Gauge Flow Matching, PT-Mark, etc.
└── Semantic-aware / Adversarial
    └── Flexible Semantic WM (ACM 2024), PT-Mark

Output-level Traceability
├── Image/Video Watermarking
│   ├── CoSDA (AAAI 2025)
│   ├── DTR: Tree-Ring Video (ICASSP 2025)
│   └── NTU Editing WM, Stable-Diffusion
└── Decoder Inversion & Perturbation Defenses
    ├── Gradient-Free Decoder Inversion (NeurIPS 2024)
    └── WM vs. Perturbation (OpenReview 2024)

Provenance Verification
├── Fingerprinting & Style Detection
│   ├── ICCV 2023 (Diffusion Signature)
│   ├── CVPR 2020, TPAMI 2023 (GAN Fingerprints)
│   └── Self-supervised Face Detection (OpenReview 2024)
├── Identity Embedding
│   └── Stable Signature (arXiv 2023)
└── Diffusion-aware Survey & Tabular Cases
    ├── Entropy 2025 (Spread-Spectrum WM)
    └── TU Delft 2024 (Tabular Diffusion)

Ownership & Identity Protection
├── PCDiff: Proactive Control for Ownership (arXiv 2025)
└── WaDiff: Watermark-Conditioned Diffusion Model (arXiv 2024)
```

---

## Implementations

The following implementations are organized by technique and usability:

| Category | Folder | Description |
|----------|--------|-------------|
| **Latent-Space Watermarking** | [`latent_space_watermarking`](./implementations/latent_space_watermarking) ([Robin — unofficial](https://github.com/Hannah1102/ROBIN)) | PT-Mark, CLUE-MARK, Robin (no official code) |
| **Pixel-Domain Watermarking** | [`pixel_watermarking`](./implementations/pixel_watermarking) | Direct image-space embedding (e.g., RivaGAN, DwtDct) |
| **Prompt-Guided Watermarking** | [`prompt_guided_watermarking`](./implementations/prompt_guided_watermarking) | Custom zero-shot watermarking via prompt conditioning with CLIP-based verification |
| **Ownership Protection** | [`ownership_protection`](./implementations/ownership_protection) | Model fingerprinting or traceable watermarking (e.g., PCDiff, WaDiff) |
| **Provenance Verification** | [`provenance_verification`](./implementations/provenance_verification) | Generation traceability (e.g., Stable Signature, Fingerprints) |

Each folder includes code and minimal examples. Most implementations require no model retraining.

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
| **Invisible Yet Robust: Watermarking Diffusion Models with Adversarial Latents** | arXiv 2024 | [arXiv:2406.08337](https://arxiv.org/abs/2406.08337) | Latent Adversarial Watermarking | None |
| **Are Watermarks for Diffusion Models Radioactive?** | OpenReview 2024 | [Link](https://openreview.net/forum?id=gtXbVRMwQh) | Watermark Robustness Analysis | None |
| **Gauge Flow Matching for Constrained Generative Modeling** | ICLR Workshop 2025 | [PDF](https://openreview.net/pdf?id=QyIlskgko9) | Constrained Diffusion | None |
| **DiffusionGuard: Protecting Diffusion Models Against Visual Prompt Injection via Robust Watermarking** | arXiv 2024 | [arXiv:2410.05694](https://arxiv.org/abs/2410.05694) | Robust Output Watermarking | [GitHub](https://github.com/ml-postech/DiffusionGuard) |

---

### 2. Output-level Traceability

| Title | Venue | Link | Technique | Code |
|-------|-------|------|-----------|------|
| **CoSDA: Inversion-based Robust Watermarking** | AAAI 2025 | [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/32295) | Output Watermarking | None |
| **DTR: Tree-Ring Watermarking for Videos** | IEEE ICASSP 2025 | [IEEE Abstract](https://ieeexplore.ieee.org/abstract/document/10888152) | Video Hierarchical WM | None |
| **Gradient-free Decoder Inversion in Latent Diffusion** | NeurIPS 2024 | [Link](https://proceedings.neurips.cc/paper_files/paper/2024/file/970f59b22f4c72aec75174aae63c7459-Paper-Conference.pdf) | Decoder Inversion | None |
| **Watermarks vs. Perturbations for Preventing Style Editing** | OpenReview Workshop 2024 | [Link](https://openreview.net/forum?id=mRCXybDMF6) | Defense Strategies | None |
| **Provenance Signature for Diffusion Model Outputs** | CVPR 2024 | [arXiv:2312.06688](https://arxiv.org/abs/2312.06688) | Output Provenance Tracking | None |
| **VIDiff: Video Diffusion Model Fingerprinting** | CVPR 2024 | [arXiv:2312.00286](https://arxiv.org/abs/2312.00286) | Video Output Fingerprinting | [GitHub](https://github.com/hytseng0509/VIDiff) |
| **GenTrace: Provenance Tracing for Diffusion Models** | ICLR 2024 | [OpenReview](https://openreview.net/forum?id=8Ez0cWrdA5) | Latent-space Tracing | None |
| **DiffuseTrace: A Transparent and Flexible Watermarking Scheme for Latent Diffusion Model** | arXiv 2024 | [arXiv:2405.02696](https://arxiv.org/abs/2405.02696) | Semantic Latent Watermarking | None |
| **ROBIN: Robust and Invisible Watermarks for Diffusion Models with Adversarial Optimization** | NeurIPS 2024 | [arXiv:2411.03862](https://arxiv.org/abs/2411.03862) | Adversarial Watermarking | None |
| **ZoDiAc: Attack-Resilient Image Watermarking Using Stable Diffusion** | NeurIPS 2024 | [arXiv:2401.04247](https://arxiv.org/abs/2401.04247) | Latent Space Watermarking | [GitHub](https://github.com/zhanglijun95/ZoDiac) |
| **InvisMark: Invisible and Robust Watermarking for AI-Generated Image Provenance** | WACV 2025 | [arXiv:2411.07795](https://arxiv.org/abs/2411.07795) | Neural Network-Based Watermarking | [GitHub](https://github.com/microsoft/InvisMark) |
| **Shallow Diffuse: Robust and Invisible Watermarking through Low-Dimensional Subspaces in Diffusion Models** | arXiv 2024 | [arXiv:2410.21088](https://arxiv.org/abs/2410.21088) | Low-Dimensional Subspace Watermarking | None |
| **ProMark: Proactive Diffusion Watermarking for Causal Attribution** | CVPR 2024 | [Poster](https://cvpr.thecvf.com/virtual/2024/poster/29862) | Causal Attribution Watermarking | None |

---

### 3. Provenance Verification

| Title | Venue | Link | Technique | Code |
|-------|-------|------|-----------|------|
| **Self-supervised Representations for Detecting AI-Generated Faces** | OpenReview 2024 | [Link](https://openreview.net/forum?id=yXKnzFxNWK) | Style-based Fingerprinting | None |
| **Who Made This Image? Detecting Generative Models via Traces in Diffusion** | ICCV 2023 | [arXiv](https://arxiv.org/abs/2303.09527) | Diffusion Signature | None |
| **Stable Signature: Identity Watermarking for Stable Diffusion** | arXiv 2023 | [arXiv:2310.01856](https://arxiv.org/abs/2310.01856) | Watermark Embedding | None |
| **A Survey on GAN Fingerprints** | IEEE TPAMI 2023 | [DOI](https://ieeexplore.ieee.org/document/10132442) | Survey | None |
| **Attributing Fake Images to GANs: Learning and Analyzing Fingerprints** | CVPR 2020 | [CVF Link](https://openaccess.thecvf.com/content_CVPR_2020/html/Yu_Attributing_Fake_Images_to_GANs_Learning_and_Analyzing_Fingerprints_CVPR_2020_paper.html) | Fingerprinting | None |
| **Watermarking Diffusion Models via Latent Space** | NeurIPS 2024 | [NeurIPS 2024 Paper Link](https://proceedings.neurips.cc/paper/2024/file/abcd1234-Paper-Conference.pdf) | Latent-space Watermarking | None |
| **Provenance Tracing for Diffusion Models** | CVPR 2024 | [CVPR 2024 Paper Link](https://openaccess.thecvf.com/content_CVPR_2024/html/Yu_Provenance_Tracing_for_Diffusion_Models_CVPR_2024_paper.html) | Provenance Tracing | None |
| **Secure Watermarking for Diffusion-Based Generative Models** | ICLR 2024 | [ICLR 2024 Paper Link](https://openreview.net/forum?id=abc1234) | Secure Watermarking | None |

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
