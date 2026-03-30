import torch
from torchtyping import TensorType
from typing import Tuple

class Solution:
    def create_batches(self, data: TensorType[int], context_length: int, batch_size: int) -> Tuple[TensorType[int], TensorType[int]]:
        
        torch.manual_seed(0)
        
        start = 0
        end = len(data) - context_length



        
        rand_indices = torch.randint(low=start, high=end, size=(batch_size,))

        X = torch.stack([data[index: index + context_length] for index in rand_indices])
        y = torch.stack([data[index + 1: index + 1 + context_length] for index in rand_indices])

        return X, y
        