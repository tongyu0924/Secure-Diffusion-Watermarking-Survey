# robin_core/train_embedder.py
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
from models.embedder import Embedder
from utils.losses import compute_losses
from utils.watermark_utils import decode_with_vae, get_latents
from diffusers import StableDiffusionPipeline
import os

# Load Stable Diffusion (only for encoder/decoder)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16 if device.type == "cuda" else torch.float32
).to(device)
vae = pipe.vae.eval()
tokenizer = pipe.tokenizer
text_encoder = pipe.text_encoder

# Dataset (e.g. CIFAR-10 resized to 512x512 for demo)
transform = transforms.Compose([
    transforms.Resize((512, 512)),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])
dataset = datasets.FakeData(size=1000, transform=transform)
data_loader = DataLoader(dataset, batch_size=8, shuffle=True)

# Model
embedder = Embedder(latent_dim=4, key_dim=128).to(device)
optimizer = optim.Adam(embedder.parameters(), lr=1e-4)

# Training loop
for epoch in range(10):
    embedder.train()
    total_loss = 0
    for images, _ in data_loader:
        images = images.to(device)
        latents = get_latents(vae, images)

        # Fake watermark key (random noise)
        w_key = torch.randn(images.size(0), 128).to(device)
        watermarked_latents = embedder(latents, w_key)

        decoded = decode_with_vae(vae, watermarked_latents)
        loss = compute_losses(images, decoded, watermarked_latents, latents)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    print(f"Epoch {epoch+1}: Loss = {total_loss/len(data_loader):.4f}")

# Save model
os.makedirs("checkpoints", exist_ok=True)
torch.save(embedder.state_dict(), "checkpoints/embedder.pth")
