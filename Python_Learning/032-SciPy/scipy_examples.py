import numpy as np
from scipy import integrate, linalg, optimize, stats, interpolate
from scipy.fftpack import fft
import matplotlib.pyplot as plt

# Note: Many SciPy functions are best understood with visualizations.
# This script will save plots to a 'temp_plots' directory.
# We will create this directory first.
import os
if not os.path.exists('temp_plots'):
    os.makedirs('temp_plots')

print("1. Integration with SciPy")
# We want to integrate a function, e.g., f(x) = x^2 from 0 to 1.
# The exact result is 1/3.
f = lambda x: x**2
result, error = integrate.quad(f, 0, 1)
print(f"Integral of x^2 from 0 to 1: {result}")
print(f"Estimated error: {error}")


print("\n2. Linear Algebra with SciPy")
# SciPy's linalg is an extension of NumPy's linalg.
# It has more advanced functions.
A = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])

# Determinant
det = linalg.det(A)
print(f"Determinant of A: {det}")

# Inverse
inv_A = linalg.inv(A)
print(f"\nInverse of A:\n{inv_A}")

# Check if inverse is correct (A . A_inv should be identity matrix)
identity = A @ inv_A
print(f"\nProduct of A and its inverse (should be close to identity):\n{np.round(identity)}")

# Solving a system of linear equations: Ax = b
b = np.array([10, 8, 3])
x = linalg.solve(A, b)
print(f"\nSolution to linear system Ax=b: {x}")
# Check: A.dot(x) - b should be close to zero
print(f"Verification (A.dot(x) - b): {A.dot(x) - b}")


print("\n3. Optimization with SciPy")
# Find the minimum of a function (e.g., f(x) = x^2 + 2x + 1)
def my_func(x):
    return x**2 + 2*x + 1

# We need an initial guess
initial_guess = 0
# The function `minimize` returns an object with details about the optimization
min_result = optimize.minimize(my_func, initial_guess)
print(f"Minimum found at x = {min_result.x[0]}")
print(f"Function value at minimum = {min_result.fun}")


print("\n4. Statistics with SciPy")
# Create some random data from a normal distribution
data = stats.norm.rvs(loc=5, scale=2, size=100) # loc=mean, scale=std dev

# Descriptive statistics
mean, var, skew, kurt = stats.norm.stats(moments='mvsk')
print(f"For a standard normal distribution:")
print(f"  Mean: {mean}, Variance: {var}, Skewness: {skew}, Kurtosis: {kurt}")

# Perform a t-test to see if the mean of our data is significantly different from a value
# Let's test against a mean of 5.1
t_statistic, p_value = stats.ttest_1samp(data, 5.1)
print(f"\nT-test results for our data against a mean of 5.1:")
print(f"  T-statistic: {t_statistic}")
print(f"  P-value: {p_value}")
if p_value < 0.05:
    print("  The mean is significantly different from 5.1 (p < 0.05)")
else:
    print("  The mean is NOT significantly different from 5.1 (p >= 0.05)")


print("\n5. Interpolation with SciPy")
# Interpolation is estimating a value between two known values.
x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)

# Create an interpolation function
f_interp = interpolate.interp1d(x, y, kind='cubic')

# Now we can use f_interp to find values at new points
x_new = np.linspace(0, 10, num=41, endpoint=True)
y_new = f_interp(x_new)

# Plotting the results
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Original data')
plt.plot(x_new, y_new, '-', label='Cubic interpolation')
plt.title('SciPy Interpolation Example')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plot_path = 'temp_plots/interpolation_example.png'
plt.savefig(plot_path)
plt.close() # Close the plot to free up memory
print(f"Interpolation plot saved to: {plot_path}")


print("\n6. Fourier Transforms with SciPy (FFT)")
# Number of sample points
N = 600
# Sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
# A signal with two frequencies (50 Hz and 80 Hz)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

# Plotting the signal and its FFT
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.title('FFT of the Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plot_path_fft = 'temp_plots/fft_example.png'
plt.savefig(plot_path_fft)
plt.close()
print(f"FFT plot saved to: {plot_path_fft}")
