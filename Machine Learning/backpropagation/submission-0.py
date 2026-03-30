import numpy as np
from numpy.typing import NDArray
from typing import Tuple


class Solution:
    def backward(self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, y_true: float) -> Tuple[NDArray[np.float64], float]:
        
        z = x @ w + b
        z_sigmoid = 1 / (1 + np.exp(-z))

        error_term = z_sigmoid - y_true
        deriv = z_sigmoid * (1 - z_sigmoid)
        gradient = error_term * deriv

        dl_dw, dl_db = np.round(gradient * x, 5), np.round(gradient, 5)


        return dl_dw, dl_db
