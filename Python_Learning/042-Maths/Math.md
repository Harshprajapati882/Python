# Math Module in Python

The `math` module is a standard module in Python that provides access to mathematical functions defined by the C standard. These functions are useful for a wide range of mathematical operations, from basic arithmetic to more complex trigonometric, logarithmic, and special functions.

## Importing the `math` module

To use the functions and constants in the `math` module, you first need to import it:

```python
import math
```

## Major Categories of Functions

### 1. Number-Theoretic and Representation Functions

These functions are used for basic number operations and representation.

- `math.ceil(x)`: Returns the smallest integer greater than or equal to `x`.
- `math.floor(x)`: Returns the largest integer less than or equal to `x`.
- `math.fabs(x)`: Returns the absolute value of `x`.
- `math.factorial(x)`: Returns the factorial of a non-negative integer `x`.
- `math.gcd(a, b)`: Returns the greatest common divisor of integers `a` and `b`.
- `math.fmod(x, y)`: Returns the remainder of `x/y` as specified by the C library.
- `math.trunc(x)`: Returns the integer part of `x`.
- `math.isfinite(x)`, `math.isinf(x)`, `math.isnan(x)`: Check if a number is finite, infinity, or NaN (Not a Number).

### 2. Power and Logarithmic Functions

These functions are used for exponentiation and logarithmic calculations.

- `math.exp(x)`: Returns `e` raised to the power `x`.
- `math.log(x[, base])`: Returns the logarithm of `x` to the given `base`. If the base is not specified, it computes the natural logarithm (base `e`).
- `math.log10(x)`: Returns the base-10 logarithm of `x`.
- `math.pow(x, y)`: Returns `x` raised to the power `y`.
- `math.sqrt(x)`: Returns the square root of `x`.

### 3. Trigonometric Functions

These functions perform trigonometric calculations. The input for `sin`, `cos`, and `tan` is in **radians**.

- `math.sin(x)`: Returns the sine of `x`.
- `math.cos(x)`: Returns the cosine of `x`.
- `math.tan(x)`: Returns the tangent of `x`.
- `math.asin(x)`, `math.acos(x)`, `math.atan(x)`: Inverse trigonometric functions.

### 4. Angular Conversion

These functions are used to convert between radians and degrees.

- `math.degrees(x)`: Converts angle `x` from radians to degrees.
- `math.radians(x)`: Converts angle `x` from degrees to radians.

### 5. Hyperbolic Functions

These functions are analogs of the ordinary trigonometric functions.

- `math.sinh(x)`: Returns the hyperbolic sine of `x`.
- `math.cosh(x)`: Returns the hyperbolic cosine of `x`.
- `math.tanh(x)`: Returns the hyperbolic tangent of `x`.

### 6. Special Functions

The `math` module also includes some special mathematical functions.

- `math.erf(x)`: The error function.
- `math.gamma(x)`: The Gamma function.

### 7. Mathematical Constants

The module provides some important mathematical constants.

- `math.pi`: The mathematical constant π (pi).
- `math.e`: The mathematical constant e.
- `math.tau`: The mathematical constant τ (tau), equal to `2 * pi`.
- `math.inf`: A floating-point representation of positive infinity.
- `math.nan`: A floating-point representation of "Not a Number".

For a complete list of all available functions and constants, you can refer to the official Python documentation for the `math` module.
