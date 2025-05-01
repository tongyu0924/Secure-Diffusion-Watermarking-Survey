import numpy as np
import torch

def generate_noise_watermark(image_np, epsilon=8):
    """
    Adds uniform noise as a simple watermark (baseline method).
    """
    noise = np.random.uniform(-epsilon, epsilon, image_np.shape).astype(np.float32)
    watermarked = image_np.astype(np.float32) + noise
    return np.clip(watermarked, 0, 255).astype(np.uint8), noise

def optimize_adversarial_watermark(image_np, steps=200, lr=1.0, epsilon=8):
    """
    Performs simple adversarial optimization in pixel space to create a stronger watermark.
    (Simplified version — assumes a dummy target loss based on total variance)
    """
    image = torch.tensor(image_np / 255.0, dtype=torch.float32, requires_grad=False)
    watermark = torch.zeros_like(image, requires_grad=True)
    optimizer = torch.optim.SGD([watermark], lr=lr)

    for _ in range(steps):
        perturbed = image + watermark
        perturbed = torch.clamp(perturbed, 0, 1)

        # Dummy loss: maximize variance (as a stand-in for detectability)
        loss = -torch.var(perturbed - image)
        loss += 0.1 * torch.mean(watermark ** 2)  # invisibility constraint

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        with torch.no_grad():
            watermark.data = torch.clamp(watermark.data, -epsilon/255.0, epsilon/255.0)

    final = torch.clamp(image + watermark, 0, 1).detach().cpu().numpy()
    return (final * 255).astype(np.uint8), watermark.detach().cpu().numpy()


def add_adversarial_watermark(image_np, epsilon=8, adv=False):
    """
    Add either a simple or optimized adversarial watermark.

    Args:
        image_np (np.ndarray): Input image (H, W, 3).
        epsilon (int): Strength of watermark.
        adv (bool): Whether to use adversarial optimization.

    Returns:
        np.ndarray: Watermarked image.
    """
    if adv:
        return optimize_adversarial_watermark(image_np, epsilon=epsilon)
    else:
        return generate_noise_watermark(image_np, epsilon)
