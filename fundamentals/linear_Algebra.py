import numpy as np


def matrix_operations(A: np.ndarray, B: np.ndarray) -> dict[str, np.ndarray]:
    """Perform core matrix operations."""
    return {
        "matrix_multiply": A @ B,
        "elementwise_multiply": A * B,
        "transpose": A.T,
    }


def matrix_properties(A: np.ndarray) -> dict[str, float | np.ndarray | None]:
    """Return determinant and inverse of a matrix if invertible."""
    det = np.linalg.det(A)
    inv = np.linalg.inv(A) if det != 0 else None

    return {
        "determinant": det,
        "inverse": inv,
    }


def solve_linear_system(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Solve Ax = b."""
    return np.linalg.solve(A, b)


if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("Matrix ops:", matrix_operations(A, B))
    print("Properties:", matrix_properties(A))

    A_sys = np.array([[2, 3], [3, 4]])
    b_sys = np.array([8, 11])
    x = solve_linear_system(A_sys, b_sys)

    print("Solution:", x)
    print("Verification:", A_sys @ x)
