"""
Implement matrix normalization without loops
"""

import numpy as np


def normalize_matrix(matrix):
    """Normalize the matrix so that each element is between 0 and 1."""
    min_val = np.min(matrix)
    max_val = np.max(matrix)
    normalized = (matrix - min_val) / (max_val - min_val)
    return normalized


if __name__ == "__main__":
    # Example usage
    mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    normalized_mat = normalize_matrix(mat)
    print("Original Matrix:\n", mat)
    print("Normalized Matrix:\n", normalized_mat)
