from PIL import Image
import numpy as np
import torch
import os
from robin_watermark import add_adversarial_watermark
from robin_defense_eval import calculate_ssim, calculate_psnr

def load_image(path):
    """Load an image and convert to RGB NumPy array."""
    image = Image.open(path).convert("RGB")
    return np.array(image)

def save_image(np_img, path):
    """Save a NumPy array as an image."""
    Image.fromarray(np.clip(np_img, 0, 255).astype(np.uint8)).save(path)

if __name__ == "__main__":
    image_path = "sample_input.png"
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "robin_watermarked.png")
    mask_path = os.path.join(output_dir, "robin_watermark_mask.png")

    # Load the original image
    image = load_image(image_path)
    print("Original image loaded.")

    # === Choose watermarking mode ===
    ADV = True         # Set True for adversarial optimization
    EPSILON = 8        # Perturbation strength

    # Apply adversarial or random watermark
    watermarked, wm_mask = add_adversarial_watermark(image, epsilon=EPSILON, adv=ADV)
    save_image(watermarked, output_path)
    print("Watermarked image saved to:", output_path)

    # Visualize and save the watermark noise (difference image)
    diff_visual = np.clip((wm_mask * 255 + 127), 0, 255).astype(np.uint8)
    save_image(diff_visual, mask_path)
    print("Watermark mask saved to:", mask_path)

    # Evaluate similarity between original and watermarked images
    ssim = calculate_ssim(image, watermarked)
    psnr = calculate_psnr(image, watermarked)
    print(f"SSIM: {ssim:.4f}")
    print(f"PSNR: {psnr:.2f} dB")
