import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution:
    def generate(self, model, new_chars: int, context: TensorType[int], context_length: int, int_to_char: dict) -> str:

        generator = torch.manual_seed(0)
        initial_state = generator.get_state()
        res = []
        for i in range(new_chars):

            if context.shape[1] > context_length:
                context = context[:, -context_length:]
            
            logits = model(context)
            final_logits = logits[:, -1, :]
            probs = nn.functional.softmax(final_logits, dim=-1)
            next_token = torch.multinomial(probs, 1, generator=generator)
            
            context = torch.cat((context, next_token), dim=-1)
            res.append(int_to_char[next_token.item()])

            generator.set_state(initial_state)
        
        return ''.join(res)
