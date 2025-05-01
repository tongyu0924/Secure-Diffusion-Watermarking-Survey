import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from models.detector import Detector
from utils.evaluation import evaluate_detector


def generate_fake_dataset(embedder, batch_size=64, latent_shape=(4, 32, 32), key_dim=128):
    """Generate fake latents with and without watermark for training."""
    X, Y = [], []
    for _ in range(batch_size):
        latent = torch.randn(latent_shape)
        key = torch.randn(key_dim)
        X.append(latent)
        Y.append(0)  # no watermark

        watermarked = embedder(latent.unsqueeze(0), key.unsqueeze(0)).squeeze(0)
        X.append(watermarked)
        Y.append(1)  # has watermark

    X = torch.stack(X)
    Y = torch.tensor(Y).long()
    return TensorDataset(X, Y)


def train():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    from models.embedder import Embedder  # Used to generate training data
    embedder = Embedder(latent_dim=4, key_dim=128).to(device)
    embedder.load_state_dict(torch.load("checkpoints/embedder.pth", map_location=device))
    embedder.eval()

    dataset = generate_fake_dataset(embedder, batch_size=256)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    model = Detector(input_channels=4).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-4)

    for epoch in range(5):
        total_loss = 0.0
        model.train()
        for x_batch, y_batch in dataloader:
            x_batch, y_batch = x_batch.to(device), y_batch.to(device)
            optimizer.zero_grad()
            logits = model(x_batch)
            loss = criterion(logits, y_batch)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        print(f"Epoch {epoch+1}: Loss = {total_loss / len(dataloader):.4f}")
        torch.save(model.state_dict(), "checkpoints/detector.pth")
        evaluate_detector(model, dataloader, device)


if __name__ == "__main__":
    train()
