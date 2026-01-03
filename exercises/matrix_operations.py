"""
Create a 1000×1000 matrix of random values and:
    Compute row-wise mean
    Compute column-wise standard deviation
"""

import numpy as np


def create_random_matrix(rows=1000, cols=1000):
    """Create a matrix of given dimensions filled with random values."""
    return np.random.randint(0, 1000, size=(rows, cols))


def compute_row_mean(matrix):
    """Compute the mean of each row in the matrix."""
    return np.mean(matrix, axis=1)


def compute_column_std(matrix):
    """Compute the standard deviation of each column in the matrix."""
    return np.std(matrix, axis=0)


if __name__ == "__main__":
    matrix = create_random_matrix()
    row_means = compute_row_mean(matrix)
    column_stds = compute_column_std(matrix)

    print("Row-wise means:", row_means)
    print("Column-wise standard deviations:", column_stds)
