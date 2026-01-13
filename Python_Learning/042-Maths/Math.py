"""
This file provides a comprehensive overview of the Python `math` module.
It covers a wide range of mathematical functions and constants available in the module.
"""

import math

# Number-Theoretic and Representation Functions
print("--- Number-Theoretic and Representation Functions ---")

# math.ceil(x): Returns the smallest integer greater than or equal to x.
x = 1.4
print(f"ceil({x}) = {math.ceil(x)}")  # Output: 2

# math.floor(x): Returns the largest integer less than or equal to x.
x = 1.9
print(f"floor({x}) = {math.floor(x)}")  # Output: 1

# math.fabs(x): Returns the absolute value of x.
x = -10
print(f"fabs({x}) = {math.fabs(x)}")  # Output: 10.0

# math.factorial(x): Returns the factorial of x.
x = 5
print(f"factorial({x}) = {math.factorial(x)}")  # Output: 120

# math.gcd(a, b): Returns the greatest common divisor of a and b.
a, b = 48, 18
print(f"gcd({a}, {b}) = {math.gcd(a, b)}")  # Output: 6

# math.fmod(x, y): Returns the remainder of x/y.
x, y = 20, 3
print(f"fmod({x}, {y}) = {math.fmod(x, y)}")  # Output: 2.0

# math.trunc(x): Returns the truncated integer value of x.
x = 2.77
print(f"trunc({x}) = {math.trunc(x)}")  # Output: 2

# math.isfinite(x): Returns True if x is finite.
print(f"isfinite(5) = {math.isfinite(5)}")  # Output: True
print(f"isfinite(inf) = {math.isfinite(math.inf)}")  # Output: False

# math.isinf(x): Returns True if x is infinity.
print(f"isinf(5) = {math.isinf(5)}")  # Output: False
print(f"isinf(inf) = {math.isinf(math.inf)}")  # Output: True

# math.isnan(x): Returns True if x is Not a Number.
print(f"isnan(5) = {math.isnan(5)}")  # Output: False
print(f"isnan(nan) = {math.isnan(math.nan)}")  # Output: True

print("\n--- Power and Logarithmic Functions ---")

# math.exp(x): Returns e**x.
x = 2
print(f"exp({x}) = {math.exp(x)}")

# math.log(x[, base]): Returns the logarithm of x to the given base.
# If the base is not specified, returns the natural logarithm of x.
x = 100
print(f"log({x}) = {math.log(x)}")
print(f"log({x}, 10) = {math.log(x, 10)}")

# math.log10(x): Returns the base-10 logarithm of x.
x = 100
print(f"log10({x}) = {math.log10(x)}")

# math.pow(x, y): Returns x raised to the power y.
x, y = 2, 3
print(f"pow({x}, {y}) = {math.pow(x, y)}")  # Output: 8.0

# math.sqrt(x): Returns the square root of x.
x = 16
print(f"sqrt({x}) = {math.sqrt(x)}")  # Output: 4.0

print("\n--- Trigonometric Functions ---")

# The argument is in radians for these functions.
angle_rad = math.pi / 4  # 45 degrees

# math.sin(x): Returns the sine of x.
print(f"sin({angle_rad:.2f} rad) = {math.sin(angle_rad):.2f}")

# math.cos(x): Returns the cosine of x.
print(f"cos({angle_rad:.2f} rad) = {math.cos(angle_rad):.2f}")

# math.tan(x): Returns the tangent of x.
print(f"tan({angle_rad:.2f} rad) = {math.tan(angle_rad):.2f}")

# Inverse trigonometric functions
# math.asin(x): Returns the arc sine of x.
x = 0.5
print(f"asin({x}) = {math.asin(x):.2f} rad")

# math.acos(x): Returns the arc cosine of x.
x = 0.5
print(f"acos({x}) = {math.acos(x):.2f} rad")

# math.atan(x): Returns the arc tangent of x.
x = 1
print(f"atan({x}) = {math.atan(x):.2f} rad")

print("\n--- Angular Conversion ---")

# math.degrees(x): Converts angle x from radians to degrees.
rad = math.pi / 2
print(f"{rad:.2f} radians = {math.degrees(rad):.0f} degrees")

# math.radians(x): Converts angle x from degrees to radians.
deg = 180
print(f"{deg} degrees = {math.radians(deg):.2f} radians")

print("\n--- Hyperbolic Functions ---")

# math.sinh(x): Returns the hyperbolic sine of x.
x = 1
print(f"sinh({x}) = {math.sinh(x):.2f}")

# math.cosh(x): Returns the hyperbolic cosine of x.
x = 1
print(f"cosh({x}) = {math.cosh(x):.2f}")

# math.tanh(x): Returns the hyperbolic tangent of x.
x = 1
print(f"tanh({x}) = {math.tanh(x):.2f}")

print("\n--- Special Functions ---")

# math.erf(x): Returns the error function at x.
x = 1
print(f"erf({x}) = {math.erf(x):.2f}")

# math.gamma(x): Returns the Gamma function at x.
x = 6
print(f"gamma({x}) = {math.gamma(x)}")  # (x-1)! = 5! = 120

print("\n--- Mathematical Constants ---")

# math.pi: The mathematical constant pi.
print(f"pi = {math.pi}")

# math.e: The mathematical constant e.
print(f"e = {math.e}")

# math.tau: The mathematical constant tau (2 * pi).
print(f"tau = {math.tau}")

# math.inf: A floating-point positive infinity.
print(f"inf = {math.inf}")

# math.nan: A floating-point "not a number" value.
print(f"nan = {math.nan}")
