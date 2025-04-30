import torch

def apply_latent_watermark(latents, secret_key, strength=0.01):
    """
    Apply lightweight cryptographic noise into latents using a secret key.
    """
    torch.manual_seed(secret_key)
    noise = torch.randn(latents.shape, dtype=latents.dtype, device=latents.device) * strength
    return latents + noise
