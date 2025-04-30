import numpy as np

def add_adversarial_watermark(image_np, epsilon=8):
    """
    Add a simple adversarial-style watermark using uniform noise.
    
    Args:
        image_np (np.ndarray): Original image as NumPy array (H, W, 3).
        epsilon (int): Perturbation strength.

    Returns:
        np.ndarray: Watermarked image.
    """
    noise = np.random.uniform(-epsilon, epsilon, image_np.shape).astype(np.float32)
    watermarked = image_np.astype(np.float32) + noise
    return np.clip(watermarked, 0, 255).astype(np.uint8)
