import numpy as np
from numpy.typing import NDArray


class Solution:
    def forward(self, x: NDArray[np.float64], gamma: NDArray[np.float64], beta: NDArray[np.float64]) -> NDArray[np.float64]:
        epsilon = 1e-5
        mean = np.mean(x)
        variance = np.var(x)

        result = ((x - mean) / (np.sqrt(variance + epsilon))) * gamma + beta
        return np.round(result,5)
