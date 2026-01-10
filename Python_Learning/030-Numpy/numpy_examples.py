import numpy as np

# 1. Creating NumPy Arrays
print("1. Creating NumPy Arrays")

# From a Python list
a = np.array([1, 2, 3, 4, 5])
print(f"Array from list: {a}")
print(f"Shape of array 'a': {a.shape}")
print(f"Data type of array 'a': {a.dtype}")

# 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D Array:\n{b}")
print(f"Shape of array 'b': {b.shape}")

# Creating arrays with initial placeholders
zeros_array = np.zeros((2, 3))
print(f"\nArray of zeros:\n{zeros_array}")

ones_array = np.ones((3, 2))
print(f"\nArray of ones:\n{ones_array}")

# Array of a constant
full_array = np.full((2, 4), 7)
print(f"\nArray filled with 7:\n{full_array}")

# Identity matrix
identity_matrix = np.eye(3)
print(f"\nIdentity matrix:\n{identity_matrix}")

# Array with a range of values
range_array = np.arange(10, 20, 2)
print(f"\nArray with a range of values: {range_array}")

# Array with linearly spaced values
linspace_array = np.linspace(0, 1, 5)
print(f"\nLinearly spaced array: {linspace_array}")

# Array with random values
random_array = np.random.random((2, 2))
print(f"\nRandom array:\n{random_array}")


# 2. Array Indexing and Slicing
print("\n2. Array Indexing and Slicing")
arr = np.array([10, 20, 30, 40, 50, 60])

# Get a single element
print(f"Element at index 2: {arr[2]}")

# Slicing
print(f"Elements from index 1 to 4: {arr[1:5]}")

# Slicing in 2D
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nOriginal Matrix:\n{matrix}")

# Get a row
print(f"Second row: {matrix[1]}")

# Get a column (this is more advanced slicing)
print(f"Third column: {matrix[:, 2]}")

# Submatrix
print(f"Submatrix (2x2 top-left):\n{matrix[:2, :2]}")


# 3. Basic Math Operations (Element-wise)
print("\n3. Basic Math Operations")
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

# Element-wise sum
print(f"Sum of x and y:\n{x + y}")
print(f"Sum using np.add:\n{np.add(x, y)}")

# Element-wise difference
print(f"\nDifference of x and y:\n{x - y}")

# Element-wise product
print(f"\nProduct of x and y:\n{x * y}")

# Element-wise division
print(f"\nDivision of x and y:\n{x / y}")

# Element-wise square root
print(f"\nSquare root of x:\n{np.sqrt(x)}")


# 4. Broadcasting
print("\n4. Broadcasting")
# We can perform operations between a smaller and a larger array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 0, 1])

# Add the vector to each row of the matrix
broadcasted = matrix + vector
print(f"Matrix after broadcasting a vector:\n{broadcasted}")


# 5. Aggregate Functions
print("\n5. Aggregate Functions")
arr = np.array([1, 2, 3, 4, 5, 6])

print(f"Sum of all elements: {arr.sum()}")
print(f"Minimum element: {arr.min()}")
print(f"Maximum element: {arr.max()}")
print(f"Mean of elements: {arr.mean()}")
print(f"Standard deviation: {arr.std()}")


# 6. Linear Algebra
print("\n6. Linear Algebra")
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Matrix multiplication (dot product)
print(f"Dot product of a and b:\n{a.dot(b)}")
print(f"Dot product using @ operator:\n{a @ b}")

# Transpose of a matrix
print(f"\nTranspose of a:\n{a.T}")

# Inverse of a matrix
try:
    print(f"\nInverse of a:\n{np.linalg.inv(a)}")
except np.linalg.LinAlgError as e:
    print(f"\nCould not compute inverse: {e}")

# Determinant of a matrix
print(f"\nDeterminant of a: {np.linalg.det(a)}")
