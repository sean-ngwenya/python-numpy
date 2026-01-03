"""
Write a function that:

    Takes any matrix
    Returns determinant, rank, eigenvalues (if square)
"""

import numpy as np


def matrix_properties(matrix):
    """Compute determinant, rank, and eigenvalues of the given matrix."""
    properties = {}

    # Calculate rank
    properties["rank"] = np.linalg.matrix_rank(matrix)

    # Check if the matrix is square for determinant and eigenvalues
    if matrix.shape[0] == matrix.shape[1]:
        properties["determinant"] = np.linalg.det(matrix)
        properties["eigenvalues"] = np.linalg.eigvals(matrix)
    else:
        properties["determinant"] = None
        properties["eigenvalues"] = None

    return properties


if __name__ == "__main__":
    # Example usage
    mat_square = np.array([[4, 2], [3, 1]])
    mat_rect = np.array([[1, 2, 3], [4, 5, 6]])

    print("Square Matrix Properties:")
    props_square = matrix_properties(mat_square)
    print(
        f"\n Determinant: {props_square['determinant']}, Rank: {props_square['rank']}, Eigenvalues: {props_square['eigenvalues']}"
    )

    print("\nRectangular Matrix Properties:")
    props_rect = matrix_properties(mat_rect)
    print(
        f"\n Determinant: {props_rect['determinant']}, Rank: {props_rect['rank']}, Eigenvalues: {props_rect['eigenvalues']}"
    )
