import torch
import torch.nn.functional as F

def apply_latent_watermark(latents, embedder, secret_key, strength=1.0):
    """
    Embed watermark into latent using the provided embedder and secret key.

    Args:
        latents (Tensor): Input latent tensor (B, C, H, W).
        embedder (nn.Module): The trained embedder model.
        secret_key (Tensor): Key tensor (B, key_dim).
        strength (float): Scaling factor for embedding strength.

    Returns:
        Tensor: Watermarked latents
    """
    with torch.no_grad():
        embedded = embedder(latents, secret_key)
        return embedded * strength + latents * (1 - strength)

def compute_ssim(img1, img2):
    """Compute Structural Similarity Index (SSIM) between two images."""
    from pytorch_msssim import ssim
    img1 = img1.unsqueeze(0) if img1.dim() == 3 else img1
    img2 = img2.unsqueeze(0) if img2.dim() == 3 else img2
    return ssim(img1, img2, data_range=1.0, size_average=True).item()
