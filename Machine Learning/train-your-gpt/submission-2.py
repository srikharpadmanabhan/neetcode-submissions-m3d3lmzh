import torch
import torch.nn as nn
import torch.nn.functional as F

# The GPT model is provided for you. It returns raw logits (not probabilities).
# You only need to implement the training loop below.

class Solution:
    def train(self, model: nn.Module, data: torch.Tensor, epochs: int, context_length: int, batch_size: int, lr: float) -> float:
        
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
        for epoch in range(epochs):
            torch.manual_seed(epoch)
            rand_indices = torch.randint(low=0, high=len(data)-context_length, size=(batch_size,))
            X = torch.stack([data[index:index+context_length] for index in rand_indices])
            y = torch.stack([data[index + 1:index + 1 + context_length] for index in rand_indices])

            logits = model(X)
            B, T, C = logits.shape
            logits_flat = logits.reshape((B*T,C))
            targets_flat = y.reshape((B*T))
            loss = F.cross_entropy(logits_flat, targets_flat)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        
        return round(loss.item(), 4)
