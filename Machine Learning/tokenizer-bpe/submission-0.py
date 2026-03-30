from typing import List

class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        tokens = list(corpus)
        merges = []

        for merge in range(num_merges):
            pair_counts = {}
            for i in range(len(tokens) - 1):
                pair = (tokens[i], tokens[i + 1])
                if pair in pair_counts:
                    pair_counts[pair] += 1
                else:
                    pair_counts[pair] = 1

            if not pair_counts:
                break

            max_freq = max(pair_counts.values())
            best_pair = None
            for pair, count in pair_counts.items():
                if count == max_freq:
                    if best_pair is None or pair < best_pair:
                        best_pair = pair

            a, b = best_pair
            merges.append([a, b])

            new_tokens = []
            i = 0
            while i < len(tokens):
                if i < len(tokens) - 1 and tokens[i] == a and tokens[i + 1] == b:
                    new_tokens.append(a + b)
                    i += 2 
                else:
                    new_tokens.append(tokens[i])
                    i += 1

            tokens = new_tokens

        return merges