import numpy as np


def create_1d_array() -> np.ndarray:
    """Create a basic 1D NumPy array."""
    return np.array([1, 2, 3, 4, 5])


def create_2d_array() -> np.ndarray:
    """Create a 2D NumPy array (matrix)."""
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def create_special_arrays() -> dict[str, np.ndarray]:
    """Create common special NumPy arrays."""
    return {
        "zeros": np.zeros((3, 3)),
        "ones": np.ones((2, 4)),
        "identity": np.eye(3),
        "random": np.random.rand(3, 3),
    }


def create_sequences() -> dict[str, np.ndarray]:
    """Create NumPy sequences using arange and linspace."""
    return {
        "arange": np.arange(0, 10, 2),
        "linspace": np.linspace(0, 1, 5),
    }


if __name__ == "__main__":
    arr1 = create_1d_array()
    print("1D Array:", arr1)
    print("Shape:", arr1.shape, "Dtype:", arr1.dtype)

    matrix = create_2d_array()
    print("\n2D Array:\n", matrix)
    print("Shape:", matrix.shape, "Dimensions:", matrix.ndim)

    special = create_special_arrays()
    for name, array in special.items():
        print(f"\n{name.capitalize()}:\n{array}")

    sequences = create_sequences()
    for name, array in sequences.items():
        print(f"\n{name}:\n{array}")
