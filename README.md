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

Secure Watermarking in Diffusion Models
├── 1. Model-level Watermarking
│   ├── 🔹 Latent-space Watermarking
│   │   ├── CLUE-MARK (arXiv 2024)
│   │   ├── Robin (NeurIPS 2024)
│   │   └── Gauge Flow Matching, PT-Mark, etc.
│   └── 🔸 Semantic-aware / Adversarial
│       └── Flexible Semantic WM (ACM 2024), PT-Mark

├── 2. Output-level Traceability
│   ├── 📷 Image/Video Watermarking
│   │   ├── CoSDA (AAAI 2025)
│   │   ├── DTR: Tree-Ring Video (ICASSP 2025)
│   │   └── NTU Editing WM, Stable-Diffusion
│   └── 🔒 Decoder Inversion & Perturbation Defenses
│       ├── Gradient-Free Decoder Inversion (NeurIPS 2024)
│       └── WM vs. Perturbation (OpenReview 2024)

├── 3. Provenance Verification
│   ├── 🧬 Fingerprinting & Style Detection
│   │   ├── ICCV 2023 (Diffusion Signature)
│   │   ├── CVPR 2020, TPAMI 2023 (GAN Fingerprints)
│   │   └── Self-supervised Face Detection (OpenReview 2024)
│   ├── 🎯 Identity Embedding
│   │   └── Stable Signature (arXiv 2023)
│   └── 📊 Diffusion-aware Survey & Tabular Cases
│       ├── Entropy 2025 (Spread-Spectrum WM)
│       └── TU Delft 2024 (Tabular Diffusion)

---

## Surveyed Papers

### 1. Model-level Watermarking
| Title | Venue | Link | Technique | Notes |
|-------|-------|------|-----------|-------|
| **CLUE-MARK: Watermarking Diffusion Models using CLWE** | arXiv 2024 | [arXiv:2411.11434](https://arxiv.org/abs/2411.11434) | Latent Watermarking | Multi-key support, no model modification |
| **PCDiff: Proactive Control for Ownership Protection** | arXiv 2025 | [arXiv:2504.11774](https://arxiv.org/abs/2504.11774) | Ownership + Traceability | Proactive access control framework |
| **PT-Mark: Invisible Watermarking via Semantic Tuning** | arXiv 2025 | [arXiv:2504.10853](https://arxiv.org/abs/2504.10853) | Semantic-aware Tuning | Preserves watermark through denoising |
| **Flexible Semantic Watermarking** | ACM 2024 | [DOI:10.1145/3696409.3700282](https://dl.acm.org/doi/abs/10.1145/3696409.3700282) | Diffusion Sampling | Robust to semantic editing |
| **Robin: Robust and Invisible Watermarks for Diffusion Models** | NeurIPS 2024 | [Link](https://proceedings.neurips.cc/paper_files/paper/2024/file/073c8584ef86bee26fe9d639ec648e28-Paper-Conference.pdf) | Adversarial Watermarking | Embeds adversarially-optimized imperceptible watermarks |
| **Are Watermarks for Diffusion Models Radioactive?** | OpenReview Workshop 2024 | [Link](https://openreview.net/forum?id=gtXbVRMwQh) | Watermark Training | Evaluates persistent effects of training on watermarked data |
| **Gauge Flow Matching for Constrained Generative Modeling** | ICLR Workshop 2025 | [Link](https://openreview.net/pdf?id=QyIlskgko9) | Constrained Diffusion | Enables watermark-aware constrained generation |

---

### 2. Output-level Traceability
| Title | Venue | Link | Technique | Notes |
|-------|-------|------|-----------|-------|
| **CoSDA: Inversion-based Robust Watermarking** | AAAI 2025 | [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/32295) | Output Watermarking | Evaluates bit-level accuracy |
| **DTR: Tree-Ring Watermarking for Videos** | IEEE ICASSP 2025 | [IEEE Abstract](https://ieeexplore.ieee.org/abstract/document/10888152) | Video Hierarchical WM | Adapts to temporal structure |
| **Stable-Diffusion Image Editing Watermarks** | NTU DR 2025 | [NTU Repository](https://dr.ntu.edu.sg/handle/10356/182920) | Imperceptible WM | Designed for editing pipelines |
| **Gradient-free Decoder Inversion in Latent Diffusion** | NeurIPS 2024 | [Link](https://proceedings.neurips.cc/paper_files/paper/2024/file/970f59b22f4c72aec75174aae63c7459-Paper-Conference.pdf) | Decoder Inversion | Discusses inversion risks & detection |
| **Watermarks vs. Perturbations for Preventing Style Editing** | OpenReview Workshop 2024 | [Link](https://openreview.net/forum?id=mRCXybDMF6) | Defense Strategies | Compares watermark vs. perturbation noise |

---

### 3. Provenance Verification
| Title | Venue | Link | Technique | Notes |
|-------|-------|------|-----------|-------|
| **Spread Spectrum WM via Latent Diffusion** | Entropy 2025 | [MDPI](https://www.mdpi.com/1099-4300/27/4/428) | Spread-Spectrum | Coupled with diffusion noise |
| **Ripple Watermarking for Tabular Diffusion** | TU Delft 2024 | [PDF](https://repository.tudelft.nl/file/File_5998cfdf-a2d2-42d3-a9e5-906ca767ce1c) | Latent Tabular | Focused on tabular generative models |
| **Review: Latent Diffusion Models for WM** | Electronics 2024 | [MDPI](https://www.mdpi.com/2079-9292/14/1/25) | Survey | Summary of latent WM strategies |
| **Self-supervised Representations for Detecting AI-Generated Faces** | OpenReview 2024 | [Link](https://openreview.net/forum?id=yXKnzFxNWK) | Style-based Fingerprinting | Indirect traceability via face embeddings |
| **Who Made This Image? Detecting Generative Models via Traces in Diffusion** | ICCV 2023 | [arXiv](https://arxiv.org/abs/2303.09527) | Diffusion Signature | Detects model-specific trace in diffusion outputs |
| **Stable Signature: Identity Watermarking for Stable Diffusion** | arXiv 2023 | [arXiv:2310.01856](https://arxiv.org/abs/2310.01856) | Watermark Embedding | Embeds signer identity into Stable Diffusion |
| **A Survey on GAN Fingerprints** | IEEE TPAMI 2023 | [DOI](https://ieeexplore.ieee.org/document/10132442) | Survey | Covers fingerprinting methods for generative models |
| **Attributing Fake Images to GANs: Learning and Analyzing Fingerprints** | CVPR 2020 | [CVF Link](https://openaccess.thecvf.com/content_CVPR_2020/html/Yu_Attributing_Fake_Images_to_GANs_Learning_and_Analyzing_Fingerprints_CVPR_2020_paper.html) | Fingerprinting | Classic CVPR GAN fingerprinting work |


