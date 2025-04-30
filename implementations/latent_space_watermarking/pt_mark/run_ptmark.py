from embed_ptmark import embed_watermark
from verify_ptmark import compute_ssim_score
from PIL import Image
import torch

if __name__ == "__main__":
    prompt = "A photo of a bouquet of purple irises"
    secret_key = 42
    output_path = "ptmark_watermarked.png"

    # Embed watermark
    image = embed_watermark(prompt, secret_key)
    image.save(output_path)
    print(f"Watermarked image saved at: {output_path}")

    # Evaluate with dummy reference image (just for demo)
    reference = Image.open("reference.png").resize(image.size)
    ssim = compute_ssim_score(image, reference)
    print(f"SSIM against reference: {ssim:.4f}")
