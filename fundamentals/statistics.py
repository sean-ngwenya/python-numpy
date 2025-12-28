import numpy as np


def descriptive_statistics(data: np.ndarray) -> dict[str, float]:
    """Compute common descriptive statistics."""
    return {
        "sum": float(np.sum(data)),
        "mean": float(np.mean(data)),
        "median": float(np.median(data)),
        "std_dev": float(np.std(data)),
        "variance": float(np.var(data)),
        "min": float(np.min(data)),
        "max": float(np.max(data)),
        "range": float(np.ptp(data)),
    }


def cumulative_and_dot(
    data: np.ndarray, v1: np.ndarray, v2: np.ndarray
) -> dict[str, np.ndarray | int]:
    """Demonstrate cumulative sum and dot product."""
    return {
        "cumulative_sum": np.cumsum(data),
        "dot_product": np.dot(v1, v2),
    }


def reshape_example(arr: np.ndarray, shape: tuple[int, int]) -> np.ndarray:
    """Reshape an array to a new shape."""
    return arr.reshape(shape)


if __name__ == "__main__":
    data = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    arr = np.arange(12)

    print("Stats:", descriptive_statistics(data))
    print("Extras:", cumulative_and_dot(data, v1, v2))
    print("Reshaped:\n", reshape_example(arr, (3, 4)))
