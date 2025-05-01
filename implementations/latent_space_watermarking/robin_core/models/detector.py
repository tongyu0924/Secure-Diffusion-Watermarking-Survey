import torch
import torch.nn as nn

class Detector(nn.Module):
    def __init__(self, input_channels=4):
        super(Detector, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(input_channels, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1, 1)),

            nn.Flatten(),
            nn.Linear(64, 2)  # Binary classification (no watermark vs watermark)
        )

    def forward(self, x):
        return self.model(x)
