import torch
import torch.nn.functional as F

def mse_loss(output, target):
    """Standard MSE loss for reconstruction."""
    return F.mse_loss(output, target)

def contrastive_loss(latent_clean, latent_watermarked, margin=1.0):
    """
    Simple contrastive loss: encourage separation between clean and watermarked latents.
    """
    diff = latent_clean - latent_watermarked
    distance = torch.norm(diff, dim=1)
    return torch.mean(torch.clamp(margin - distance, min=0.0))
