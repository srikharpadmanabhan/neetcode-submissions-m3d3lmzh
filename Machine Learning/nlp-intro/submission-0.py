import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        
        combined_sentences = positive + negative
        unique_words = sorted({word for sentence in combined_sentences for word in sentence.split()})
        
        encoding_map = {word: idx + 1 for idx, word in enumerate(unique_words)}
        encoded_sentences = [torch.tensor([encoding_map[word] for word in sentence.split()]) for sentence in combined_sentences]

        padded = torch.nn.utils.rnn.pad_sequence(encoded_sentences, padding_value=0, batch_first=True)

        return padded