from skimage.metrics import structural_similarity as ssim
import numpy as np

def calculate_ssim(img1, img2):
    """
    Compute SSIM (Structural Similarity Index) between two RGB images.
    
    Args:
        img1 (np.ndarray): Original image.
        img2 (np.ndarray): Perturbed image.
    
    Returns:
        float: Average SSIM over RGB channels.
    """
    img1 = img1.astype(np.float32)
    img2 = img2.astype(np.float32)

    total_ssim = 0
    for i in range(3):  # R, G, B channels
        ssim_val = ssim(img1[:, :, i], img2[:, :, i], data_range=255)
        total_ssim += ssim_val
    return total_ssim / 3
