import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        max_val = np.max(z)
        new_vals = np.exp(z - max_val)
        sum_vals = np.sum(new_vals)

        return np.round(new_vals / sum_vals, 4)
