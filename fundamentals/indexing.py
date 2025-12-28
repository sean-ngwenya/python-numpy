import numpy as np


def basic_indexing(arr: np.ndarray) -> dict[str, np.ndarray | int]:
    """Demonstrate basic indexing and slicing on a 1D array."""
    return {
        "first_element": arr[0],
        "last_element": arr[-1],
        "slice_1_4": arr[1:4],
    }


def matrix_indexing(matrix: np.ndarray) -> dict[str, np.ndarray | int]:
    """Demonstrate indexing operations on a 2D array."""
    return {
        "element_0_0": matrix[0, 0],
        "first_row": matrix[0, :],
        "first_column": matrix[:, 0],
        "submatrix": matrix[0:2, 0:2],
    }


def boolean_indexing(arr: np.ndarray) -> dict[str, np.ndarray]:
    """Apply boolean masks to an array."""
    return {
        "greater_than_3": arr[arr > 3],
        "even_elements": arr[arr % 2 == 0],
    }


if __name__ == "__main__":
    arr = np.array([10, 20, 30, 40, 50])
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    bool_arr = np.array([1, 2, 3, 4, 5, 6])

    print("Basic indexing:", basic_indexing(arr))
    print("Matrix indexing:", matrix_indexing(matrix))
    print("Boolean indexing:", boolean_indexing(bool_arr))
