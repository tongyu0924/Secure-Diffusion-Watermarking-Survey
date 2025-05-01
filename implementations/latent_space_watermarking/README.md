# Latent-Space Watermarking

This folder contains reproducible implementations of selected latent-space watermarking methods, including:

# Latent-Space Watermarking

This folder contains implementations of selected latent-space watermarking methods, including:

- `clue_mark`: CLUE-MARK
- `robin`, `robin_core`, `robin_light`: Robin-based latent watermarking experiments (see: [ROBIN — unofficial](https://github.com/Hannah1102/ROBIN/tree/main))

---

## ▶️ Run CLUE-MARK Example
To generate a latent-watermarked image using a CLUE-MARK-inspired approach:
```bash
cd clue_mark
python run_cluemark.py
```
 
This will generate a sample image (cluemark_watermarked.png) with a latent watermark embedded using a fixed prompt and deterministic seed.
