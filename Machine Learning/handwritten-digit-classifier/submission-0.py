import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    def __init__(self):
        super().__init__()
        torch.manual_seed(0)
        
        self.linear1 = nn.Linear(784, 512)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
        self.linear2 = nn.Linear(512, 10)
        self.sigmoid = nn.Sigmoid()


    def forward(self, images: TensorType[float]) -> TensorType[float]:
        torch.manual_seed(0)
        z1 = self.linear1(images)
        h1 = self.relu(z1)
        h1 = self.dropout(h1)

        z2 = self.linear2(h1)
        h2 = self.sigmoid(z2)

        return torch.round(h2,decimals=4)

