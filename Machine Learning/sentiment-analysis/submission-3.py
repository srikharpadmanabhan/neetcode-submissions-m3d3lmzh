import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    def __init__(self, vocabulary_size: int):
        super().__init__()
        torch.manual_seed(0)
        
        self.embedding = nn.Embedding(vocabulary_size, 16)
        self.linear = nn.Linear(16,1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x: TensorType[int]) -> TensorType[float]:
        
        embeddings = self.embedding(x)
        averaged_embeddings = torch.mean(embeddings,dim=1)
        z = self.linear(averaged_embeddings)
        h = self.sigmoid(z)

        return torch.round(h, decimals=4)