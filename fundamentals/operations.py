import numpy as np


def elementwise_operations(a: np.ndarray, b: np.ndarray) -> dict[str, np.ndarray]:
    """Perform element-wise operations between two arrays."""
    return {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b,
        "power": a**2,
    }


def scalar_operations(arr: np.ndarray) -> dict[str, np.ndarray]:
    """Apply scalar operations to an array."""
    return {
        "multiply_by_2": arr * 2,
        "add_10": arr + 10,
    }


if __name__ == "__main__":
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])

    print("Element-wise:", elementwise_operations(a, b))
    print("Scalar:", scalar_operations(a))
