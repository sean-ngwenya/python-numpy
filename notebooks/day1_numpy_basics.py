"""
Day 1: NumPy Basics
Applying Linear Algebra knowledge to Python
"""

import numpy as np

print("=" * 70)
print(" NUMPY: LINEAR ALGEBRA IN PYTHON")
print("=" * 70)

# ============================================================================
# 1. CREATING ARRAYS (20 min)
# ============================================================================
print("\n1. CREATING NUMPY ARRAYS")
print("-" * 70)

# From lists
arr1 = np.array([1, 2, 3, 4, 5])
print(f"1D Array: {arr1}")
print(f"Shape: {arr1.shape}, Dtype: {arr1.dtype}")

# 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D Array (Matrix):\n{matrix}")
print(f"Shape: {matrix.shape}, Dimensions: {matrix.ndim}")

# Special arrays
zeros = np.zeros((3, 3))
print(f"\nZeros matrix:\n{zeros}")

ones = np.ones((2, 4))
print(f"\nOnes matrix:\n{ones}")

identity = np.eye(3)
print(f"\nIdentity matrix:\n{identity}")

random_matrix = np.random.rand(3, 3)
print(f"\nRandom matrix:\n{random_matrix}")

# Range
sequence = np.arange(0, 10, 2)  # start, stop, step
print(f"\nSequence: {sequence}")

linspace = np.linspace(0, 1, 5)  # start, stop, num_points
print(f"Linspace: {linspace}")

# ============================================================================
# 2. ARRAY INDEXING & SLICING (15 min)
# ============================================================================
print("\n2. INDEXING & SLICING")
print("-" * 70)

arr = np.array([10, 20, 30, 40, 50])
print(f"Array: {arr}")
print(f"First element: {arr[0]}")
print(f"Last element: {arr[-1]}")
print(f"Slice [1:4]: {arr[1:4]}")

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nMatrix:\n{matrix}")
print(f"Element [0, 0]: {matrix[0, 0]}")
print(f"First row: {matrix[0, :]}")
print(f"First column: {matrix[:, 0]}")
print(f"Submatrix [0:2, 0:2]:\n{matrix[0:2, 0:2]}")

# Boolean indexing
arr = np.array([1, 2, 3, 4, 5, 6])
print(f"\nArray: {arr}")
print(f"Elements > 3: {arr[arr > 3]}")
print(f"Even elements: {arr[arr % 2 == 0]}")

# ============================================================================
# 3. ARRAY OPERATIONS (20 min)
# ============================================================================
print("\n3. ARRAY OPERATIONS")
print("-" * 70)

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}  (element-wise)")
print(f"a / b = {a / b}")
print(f"a ** 2 = {a**2}")

# Scalar operations
print(f"\na * 2 = {a * 2}")
print(f"a + 10 = {a + 10}")

# Matrix operations (YOU KNOW THIS FROM LINEAR ALGEBRA!)
print("\n4. MATRIX OPERATIONS (Linear Algebra!)")
print("-" * 70)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"Matrix A:\n{A}")
print(f"\nMatrix B:\n{B}")

# Matrix multiplication (@ operator)
print(f"\nA @ B (Matrix multiplication):\n{A @ B}")

# Element-wise multiplication
print(f"\nA * B (Element-wise):\n{A * B}")

# Transpose
print(f"\nA.T (Transpose):\n{A.T}")

# Determinant (requires linalg)
det_A = np.linalg.det(A)
print(f"\nDeterminant of A: {det_A:.2f}")

# Inverse (if exists)
try:
    inv_A = np.linalg.inv(A)
    print(f"\nInverse of A:\n{inv_A}")
    print(f"\nA @ inv(A) (should be identity):\n{A @ inv_A}")
except:
    print("\nMatrix is not invertible")

# ============================================================================
# 4. SOLVING LINEAR SYSTEMS (15 min - YOU KNOW THIS!)
# ============================================================================
print("\n5. SOLVING LINEAR SYSTEMS")
print("-" * 70)

# Solve Ax = b
# Example: 2x + 3y = 8
#          3x + 4y = 11

A = np.array([[2, 3], [3, 4]])
b = np.array([8, 11])

print(f"System of equations:")
print(f"2x + 3y = 8")
print(f"3x + 4y = 11")
print(f"\nMatrix form Ax = b")
print(f"A =\n{A}")
print(f"b = {b}")

x = np.linalg.solve(A, b)
print(f"\nSolution: x = {x}")
print(f"Verification: A @ x = {A @ x}")

# ============================================================================
# 5. USEFUL NUMPY FUNCTIONS (20 min)
# ============================================================================
print("\n6. USEFUL FUNCTIONS")
print("-" * 70)

data = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
print(f"Data: {data}")

print(f"\nSum: {np.sum(data)}")
print(f"Mean: {np.mean(data)}")
print(f"Median: {np.median(data)}")
print(f"Std Dev: {np.std(data):.2f}")
print(f"Variance: {np.var(data):.2f}")
print(f"Min: {np.min(data)}")
print(f"Max: {np.max(data)}")
print(f"Range: {np.ptp(data)}")  # peak-to-peak

# Cumulative sum
print(f"\nCumulative sum: {np.cumsum(data)}")

# Dot product
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(f"\nv1 = {v1}")
print(f"v2 = {v2}")
print(f"Dot product: {np.dot(v1, v2)}")

# Reshape
arr = np.arange(12)
print(f"\nOriginal: {arr}")
reshaped = arr.reshape(3, 4)
print(f"Reshaped (3x4):\n{reshaped}")

print("\n" + "=" * 70)
print(" ✅ NUMPY BASICS COMPLETE!")
print("=" * 70)
