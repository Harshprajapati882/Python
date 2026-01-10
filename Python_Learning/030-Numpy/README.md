# NumPy

NumPy (Numerical Python) is a fundamental package for numerical computation in Python. It provides a powerful N-dimensional array object, sophisticated (broadcasting) functions, tools for integrating C/C++ and Fortran code, and useful linear algebra, Fourier transform, and random number capabilities.

## Core Features

### The NumPy ndarray
The core of NumPy is the `ndarray` (N-dimensional array) object. This is a fast and memory-efficient multidimensional array that provides vectorized arithmetic operations.

- **Homogeneous:** All elements of an `ndarray` must be of the same data type.
- **Fixed Size:** The size of an `ndarray` is fixed at creation.

### Universal Functions (ufuncs)
NumPy provides a large collection of "universal functions" (or `ufunc`s) that operate on `ndarray`s in an element-by-element fashion. These are much faster than iterating over the array in Python. Examples include `np.add`, `np.subtract`, `np.sin`, `np.cos`, etc.

### Broadcasting
Broadcasting is a powerful mechanism that allows NumPy to work with arrays of different shapes when performing arithmetic operations. It provides a means of vectorizing array operations so that looping occurs in C instead of Python.

### Linear Algebra
NumPy's `linalg` module provides a wide range of linear algebra operations, such as matrix inversion, determinant calculation, and solving systems of linear equations.

## Installation

To install NumPy, you can use pip:
```bash
pip install numpy
```

## Common Use Cases

- **Data Science & Machine Learning:** NumPy is the foundation for many data science libraries, including Pandas and Scikit-learn.
- **Scientific Computing:** Used extensively in various scientific and engineering fields for simulations and data analysis.
- **Image Processing:** Images can be represented as NumPy arrays, making it easy to perform operations on them.
