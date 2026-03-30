import torch
import torch.nn as nn
from torchtyping import TensorType

class SingleHeadAttention(nn.Module):

    def __init__(self, embedding_dim: int, attention_dim: int):
        super().__init__()
        torch.manual_seed(0)
        
        self.attn_dim = attention_dim
        self.emb_dim = embedding_dim

        self.key_linear = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.query_linear = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.value_linear = nn.Linear(embedding_dim, attention_dim, bias=False)

    def forward(self, embedded: TensorType[float]) -> TensorType[float]:
        
        K = self.key_linear(embedded)
        Q = self.query_linear(embedded)
        V = self.value_linear(embedded)
        context_length = K.shape[1]

        attn_scores = (Q @ K.transpose(1,2)) / (self.attn_dim ** 0.5)
        mask = torch.tril(torch.ones(context_length, context_length)) == 0 # lower triangular mask
        attn_scores = attn_scores.masked_fill(mask, float('-inf'))

        scaled_value = nn.functional.softmax(attn_scores, dim=2) @ V
        return torch.round(scaled_value, decimals=4)
        
