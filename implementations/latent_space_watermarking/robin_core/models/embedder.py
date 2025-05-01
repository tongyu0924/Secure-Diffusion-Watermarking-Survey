import torch
import torch.nn as nn

class Embedder(nn.Module):
    def __init__(self, latent_dim=4, key_dim=128):
        super(Embedder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(latent_dim, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 32, kernel_size=3, padding=1),
            nn.ReLU(),
        )

        self.fc_key = nn.Linear(key_dim, 32)
        self.decoder = nn.Sequential(
            nn.Conv2d(32, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, latent_dim, kernel_size=3, padding=1)
        )

    def forward(self, latents, key):
        # latents: (B, C, H, W), key: (B, key_dim)
        x = self.encoder(latents)
        key_embed = self.fc_key(key).view(-1, 32, 1, 1)
        x = x + key_embed  # Add key influence
        return self.decoder(x)
