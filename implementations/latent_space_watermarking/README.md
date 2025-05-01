# Latent-Space Watermarking

This folder contains reproducible implementations of selected latent-space watermarking methods, including:

- clue_mark: CLUE-MARK (no-training latent editing)
- pt_mark: PT-MARK-style semantic injection (placeholder)
- robin, robin_core, robin_light: Robin-related latent watermarking experiments (unofficial)

---

## ▶️ Run CLUE-MARK Example
To generate a latent-watermarked image using a CLUE-MARK-inspired approach:
```bash
cd clue_mark
python run_cluemark.py
```
 
This will generate a sample image (cluemark_watermarked.png) with a latent watermark embedded using a fixed prompt and deterministic seed.
