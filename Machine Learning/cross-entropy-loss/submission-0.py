import numpy as np
from numpy.typing import NDArray


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        
        loss = (- 1 / len(y_true)) * (np.dot(y_true, np.log(y_pred)) + np.dot(1-y_true, np.log(1-y_pred)))

        return np.round(loss, 4)

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # Element wise sum of y * log per class, take the mean 
        loss = -np.mean(np.sum(y_true * np.log(y_pred), axis=1))
        return np.round(loss,4)
        
