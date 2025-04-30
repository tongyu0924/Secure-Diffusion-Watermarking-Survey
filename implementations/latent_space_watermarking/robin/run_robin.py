from PIL import Image
import numpy as np
import torch
from robin_watermark import add_adversarial_watermark
from robin_defense_eval import calculate_ssim

def load_image(path):
    image = Image.open(path).convert("RGB")
    return np.array(image)

def save_image(np_img, path):
    Image.fromarray(np.clip(np_img, 0, 255).astype(np.uint8)).save(path)

if __name__ == "__main__":
    image_path = "sample_input.png"
    output_path = "robin_watermarked.png"

    image = load_image(image_path)
    print("Original image loaded.")

    watermarked = add_adversarial_watermark(image, epsilon=8)
    save_image(watermarked, output_path)
    print("Adversarial watermark added and saved.")

    ssim_score = calculate_ssim(image, watermarked)
    print(f"SSIM between original and watermarked image: {ssim_score:.4f}")
