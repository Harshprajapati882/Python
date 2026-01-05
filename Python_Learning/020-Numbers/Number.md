# Python Numbers - Comprehensive Guide

## Table of Contents
1. [Number Types Overview](#number-types-overview)
2. [Integers (int)](#integers-int)
3. [Floating Point Numbers (float)](#floating-point-numbers-float)
4. [Complex Numbers (complex)](#complex-numbers-complex)
5. [Decimal - High Precision](#decimal---high-precision)
6. [Fractions - Rational Numbers](#fractions---rational-numbers)
7. [Arithmetic Operations](#arithmetic-operations)
8. [Comparison Operators](#comparison-operators)
9. [Built-in Functions](#built-in-functions)
10. [Math Module](#math-module)
11. [Random Numbers](#random-numbers)
12. [Type Conversion](#type-conversion)
13. [Number Formatting](#number-formatting)
14. [Bitwise Operations](#bitwise-operations)
15. [Best Practices](#best-practices)

---

## Number Types Overview

Python has three built-in numeric types:

| Type | Description | Example |
|------|-------------|---------|
| `int` | Integer numbers | `42`, `-17`, `0` |
| `float` | Floating point numbers | `3.14`, `-0.5`, `1.5e-4` |
| `complex` | Complex numbers | `3+4j`, `2-1j` |

Additionally, Python provides specialized numeric types:
- **Decimal**: For high-precision decimal arithmetic
- **Fraction**: For rational number arithmetic

---

## Integers (int)

### Basic Properties
- **Arbitrary precision**: No maximum limit (only limited by available memory)
- **Immutable**: Cannot be changed after creation
- **No overflow**: Unlike many other languages

### Creating Integers

```python
# Basic integers
x = 42
y = -17
zero = 0

# Very large integers (no problem!)
large = 99999999999999999999999999999999999999
```

### Different Number Bases

Python supports multiple number systems:

```python
binary = 0b1010      # Binary (base 2) = 10
octal = 0o12         # Octal (base 8) = 10
hexadecimal = 0xA    # Hexadecimal (base 16) = 10
```

### Converting Between Bases

```python
num = 255
bin(num)   # '0b11111111'
oct(num)   # '0o377'
hex(num)   # '0xff'
```

### Readability with Underscores (Python 3.6+)

```python
million = 1_000_000
billion = 1_000_000_000
binary = 0b_1111_0000_1010
```

---

## Floating Point Numbers (float)

### Basic Properties
- Implemented using **IEEE 754 double precision** (64-bit)
- Approximately **15-17 decimal digits** of precision
- Range: approximately ±10<sup>308</sup>

### Creating Floats

```python
pi = 3.14159
negative = -2.5
scientific = 1.5e-4      # 0.00015
large = 2.5e10           # 25000000000.0
```

### ⚠️ Floating Point Precision Issues

Floats cannot represent all decimal numbers exactly:

```python
0.1 + 0.2        # 0.30000000000000004 (not exactly 0.3!)
0.1 + 0.2 == 0.3 # False!
```

**Why?** Computers store numbers in binary, and some decimal fractions (like 0.1) cannot be represented exactly in binary, similar to how 1/3 cannot be represented exactly in decimal (0.333...).

**Solution**: Use `decimal.Decimal` for exact decimal arithmetic or `math.isclose()` for comparisons:

```python
import math
math.isclose(0.1 + 0.2, 0.3)  # True
```

### Special Float Values

```python
infinity = float('inf')
neg_infinity = float('-inf')
not_a_number = float('nan')

import math
math.isinf(infinity)      # True
math.isnan(not_a_number)  # True
math.isfinite(42.5)       # True
```

---

## Complex Numbers (complex)

Complex numbers have a **real** and **imaginary** part.

### Creating Complex Numbers

```python
z1 = 3 + 4j              # Using j suffix
z2 = complex(2, -1)      # Using complex() function
pure_imaginary = 5j
real_only = complex(7, 0)
```

**Note**: Use `j` or `J` for the imaginary unit (not `i`).

### Accessing Parts

```python
z = 3 + 4j
z.real  # 3.0
z.imag  # 4.0
```

### Operations

```python
z1 = 3 + 4j
z2 = 2 - 1j

z1 + z2           # Addition: (5+3j)
z1 * z2           # Multiplication: (10+5j)
z1.conjugate()    # Complex conjugate: (3-4j)
abs(z1)           # Magnitude: 5.0
```

**Magnitude formula**: |a + bj| = √(a² + b²)

---

## Decimal - High Precision

The `decimal` module provides arbitrary precision decimal arithmetic, ideal for **financial calculations** and situations where exact decimal representation is required.

### Why Use Decimal?

```python
from decimal import Decimal

# Float problem
0.1 + 0.2  # 0.30000000000000004

# Decimal solution
Decimal('0.1') + Decimal('0.2')  # Exactly 0.3
```

### Setting Precision

```python
from decimal import getcontext

getcontext().prec = 50  # Set precision to 50 digits
```

### Creating Decimals

```python
d1 = Decimal('10.5')     # From string (recommended)
d2 = Decimal(10.5)       # From float (less precise)
d3 = Decimal((0, (1, 5), -1))  # From tuple
```

**Important**: Always use strings when possible to avoid float precision issues:

```python
Decimal(0.1)    # Decimal('0.1000000000000000055511151231257827021181583404541015625')
Decimal('0.1')  # Decimal('0.1') - exactly what you want!
```

### Financial Example

```python
from decimal import Decimal

price = Decimal('19.99')
tax_rate = Decimal('0.08')
total = price * (1 + tax_rate)
print(f"${total:.2f}")  # $21.59
```

---

## Fractions - Rational Numbers

The `fractions` module provides exact rational number arithmetic.

### Creating Fractions

```python
from fractions import Fraction

f1 = Fraction(3, 4)      # 3/4
f2 = Fraction('0.5')     # 1/2
f3 = Fraction(0.25)      # 1/4
f4 = Fraction('1.5')     # 3/2
```

### Operations

```python
Fraction(1, 2) + Fraction(1, 3)  # 5/6
Fraction(2, 3) * Fraction(3, 4)  # 1/2
Fraction(1, 2) / Fraction(1, 4)  # 2
```

### Automatic Simplification

```python
Fraction(6, 8)   # Automatically becomes 3/4
Fraction(100, 10) # Automatically becomes 10
```

---

## Arithmetic Operations

### Basic Operations

| Operator | Operation | Example | Result |
|----------|-----------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division (float) | `5 / 2` | `2.5` |
| `//` | Floor division | `5 // 2` | `2` |
| `%` | Modulo (remainder) | `5 % 2` | `1` |
| `**` | Exponentiation | `5 ** 2` | `25` |

### Division Operators

```python
17 / 5   # 3.4 (true division, always returns float)
17 // 5  # 3 (floor division, rounds down to nearest integer)
17 % 5   # 2 (remainder)

# Relationship: n = (n // d) * d + (n % d)
# 17 = (17 // 5) * 5 + (17 % 5)
# 17 = 3 * 5 + 2
```

### Floor Division with Negatives

Floor division rounds toward **negative infinity**, not toward zero:

```python
17 // 5   # 3
-17 // 5  # -4 (not -3!)

17 % 5    # 2
-17 % 5   # 3 (not -2!)
```

### Augmented Assignment

```python
x = 10
x += 5   # x = x + 5  → 15
x -= 3   # x = x - 3  → 12
x *= 2   # x = x * 2  → 24
x /= 4   # x = x / 4  → 6.0
x //= 2  # x = x // 2 → 3.0
x %= 3   # x = x % 3  → 0.0
x **= 2  # x = x ** 2 → 0.0
```

---

## Comparison Operators

### Basic Comparisons

```python
5 > 3    # True (greater than)
5 < 3    # False (less than)
5 >= 5   # True (greater than or equal)
5 <= 5   # True (less than or equal)
5 == 5   # True (equal)
5 != 3   # True (not equal)
```

### Chained Comparisons

Python allows chaining multiple comparisons:

```python
1 < 5 < 10     # True (equivalent to: 1 < 5 and 5 < 10)
1 < 5 > 3      # True (equivalent to: 1 < 5 and 5 > 3)
x = 5
0 < x < 100    # True (x is between 0 and 100)
```

---

## Built-in Functions

### Essential Functions

```python
abs(-5)              # 5 (absolute value)
round(3.7)           # 4 (round to nearest integer)
round(3.14159, 2)    # 3.14 (round to 2 decimal places)
pow(2, 3)            # 8 (2^3)
pow(2, 3, 5)         # 3 ((2^3) % 5)

numbers = [1, -5, 3, -2, 10]
min(numbers)         # -5
max(numbers)         # 10
sum(numbers)         # 7
```

### Banker's Rounding

Python 3 uses "banker's rounding" (round half to even):

```python
round(0.5)   # 0 (rounds to nearest even)
round(1.5)   # 2 (rounds to nearest even)
round(2.5)   # 2 (rounds to nearest even)
round(3.5)   # 4 (rounds to nearest even)
```

### divmod()

Returns quotient and remainder as a tuple:

```python
divmod(17, 5)  # (3, 2)
# Equivalent to: (17 // 5, 17 % 5)
```

---

## Math Module

The `math` module provides advanced mathematical functions.

### Constants

```python
import math

math.pi     # 3.141592653589793
math.e      # 2.718281828459045
math.tau    # 6.283185307179586 (2 * pi)
math.inf    # Infinity
```

### Rounding Functions

```python
math.ceil(3.2)    # 4 (round up)
math.floor(3.8)   # 3 (round down)
math.trunc(3.8)   # 3 (remove decimal part)
math.trunc(-3.8)  # -3 (toward zero)
```

**Difference between floor() and trunc()**:
- `floor()` rounds toward negative infinity
- `trunc()` rounds toward zero

```python
math.floor(-3.8)  # -4
math.trunc(-3.8)  # -3
```

### Power and Roots

```python
math.sqrt(16)       # 4.0 (square root)
math.pow(2, 10)     # 1024.0 (2^10)
math.exp(2)         # 7.389... (e^2)
```

### Logarithms

```python
math.log(100)       # 4.605... (natural log, base e)
math.log10(100)     # 2.0 (base 10)
math.log2(8)        # 3.0 (base 2)
math.log(8, 2)      # 3.0 (custom base)
```

### Trigonometry

**Important**: All trig functions use **radians**, not degrees!

```python
angle = math.pi / 4  # 45 degrees

math.sin(angle)     # 0.707...
math.cos(angle)     # 0.707...
math.tan(angle)     # 1.0

# Inverse functions
math.asin(0.5)      # π/6
math.acos(0.5)      # π/3
math.atan(1)        # π/4
```

### Degree/Radian Conversion

```python
math.radians(180)       # π (3.141...)
math.degrees(math.pi)   # 180.0
```

### Number Theory

```python
math.factorial(5)    # 120 (5!)
math.gcd(48, 18)     # 6 (greatest common divisor)
math.lcm(12, 15)     # 60 (least common multiple, Python 3.9+)
```

### Hyperbolic Functions

```python
math.sinh(x)  # Hyperbolic sine
math.cosh(x)  # Hyperbolic cosine
math.tanh(x)  # Hyperbolic tangent
```

---

## Random Numbers

The `random` module generates pseudo-random numbers.

### Random Integers

```python
import random

random.randint(1, 10)        # Random integer from 1 to 10 (inclusive)
random.randrange(0, 100, 5)  # Random from 0, 5, 10, ..., 95
```

### Random Floats

```python
random.random()           # Random float from 0.0 to 1.0 (exclusive)
random.uniform(1.5, 10.5) # Random float from 1.5 to 10.5
```

### Random Choices

```python
colors = ['red', 'green', 'blue']
random.choice(colors)     # Pick one random element

random.choices(colors, k=3)  # Pick 3 elements (with replacement)
random.sample(colors, 2)     # Pick 2 unique elements (without replacement)
```

### Shuffling

```python
deck = list(range(1, 53))
random.shuffle(deck)  # Shuffle in place
```

### Setting Seed (for reproducibility)

```python
random.seed(42)  # Same seed = same sequence of random numbers
```

---

## Type Conversion

### Between Number Types

```python
int(3.9)          # 3 (truncates decimal)
int('42')         # 42
int('101', 2)     # 5 (binary to integer)
int('FF', 16)     # 255 (hex to integer)

float(42)         # 42.0
float('3.14')     # 3.14

complex(2, 3)     # (2+3j)
complex('2+3j')   # (2+3j)

str(42)           # '42'
bool(0)           # False (0 is falsy)
bool(42)          # True (non-zero is truthy)
```

### Type Checking

```python
type(42)                    # <class 'int'>
type(3.14)                  # <class 'float'>

isinstance(42, int)         # True
isinstance(3.14, float)     # True
isinstance(42, (int, float)) # True (check multiple types)
```

---

## Number Formatting

### f-strings (Python 3.6+)

```python
value = 1234.56789

f"{value}"           # '1234.56789'
f"{value:.2f}"       # '1234.57' (2 decimal places)
f"{value:10.2f}"     # '   1234.57' (width 10)
f"{value:010.2f}"    # '0001234.57' (zero-padded)
f"{value:,.2f}"      # '1,234.57' (with comma separator)
f"{0.1567:.2%}"      # '15.67%' (percentage)
f"{value:.2e}"       # '1.23e+03' (scientific notation)
```

### Alignment

```python
f"{value:<15.2f}|"  # 'Left aligned   |'
f"{value:>15.2f}|"  # '   Right aligned|'
f"{value:^15.2f}|"  # '  Centered     |'
```

### Binary, Octal, Hex

```python
num = 42
f"{num:b}"   # '101010' (binary)
f"{num:o}"   # '52' (octal)
f"{num:x}"   # '2a' (hex lowercase)
f"{num:X}"   # '2A' (hex uppercase)
f"{num:#x}"  # '0x2a' (with prefix)
```

---

## Bitwise Operations

Bitwise operations work on the **binary representation** of integers.

### Basic Operators

| Operator | Name | Example | Binary | Result |
|----------|------|---------|--------|--------|
| `&` | AND | `12 & 5` | `1100 & 0101` | `4` |
| `|` | OR | `12 | 5` | `1100 | 0101` | `13` |
| `^` | XOR | `12 ^ 5` | `1100 ^ 0101` | `9` |
| `~` | NOT | `~12` | `~1100` | `-13` |
| `<<` | Left shift | `12 << 2` | `110000` | `48` |
| `>>` | Right shift | `12 >> 2` | `0011` | `3` |

### Practical Uses

**Check if even/odd:**
```python
num & 1 == 0  # Even if True, odd if False
```

**Swap two variables without temp:**
```python
a, b = 5, 10
a ^= b
b ^= a
a ^= b
# Now a = 10, b = 5
```

**Set a bit:**
```python
num |= (1 << position)
```

**Clear a bit:**
```python
num &= ~(1 << position)
```

**Toggle a bit:**
```python
num ^= (1 << position)
```

---

## Best Practices

### 1. Choose the Right Type

- **int**: Whole numbers, counting, indexing
- **float**: Scientific calculations, measurements (where precision isn't critical)
- **Decimal**: Financial calculations, exact decimal arithmetic
- **Fraction**: Exact rational arithmetic
- **complex**: Engineering, physics calculations

### 2. Avoid Float Comparison

```python
# ❌ Bad
if 0.1 + 0.2 == 0.3:
    pass

# ✅ Good
import math
if math.isclose(0.1 + 0.2, 0.3):
    pass
```

### 3. Use Decimal for Money

```python
# ❌ Bad
price = 19.99 * 1.08  # Float precision issues

# ✅ Good
from decimal import Decimal
price = Decimal('19.99') * Decimal('1.08')
```

### 4. Use Integer Division Correctly

```python
# Want integer result? Use //
quotient = 17 // 5  # 3

# Want float result? Use /
result = 17 / 5  # 3.4
```

### 5. Handle Division by Zero

```python
# ❌ Bad
result = x / y  # Crashes if y is 0

# ✅ Good
if y != 0:
    result = x / y
else:
    result = 0  # or float('inf'), or handle appropriately
```

### 6. Use Constants from math Module

```python
# ❌ Bad
pi = 3.14

# ✅ Good
import math
pi = math.pi
```

### 7. Format Numbers for Display

```python
# ❌ Bad
print(f"Price: {price}")  # Might show too many decimals

# ✅ Good
print(f"Price: ${price:.2f}")  # Always 2 decimals
```

### 8. Use Type Hints (Python 3.5+)

```python
def calculate_area(radius: float) -> float:
    return 3.14159 * radius ** 2
```

---

## Common Pitfalls

### 1. Float Precision
```python
# Problem
0.1 + 0.1 + 0.1 == 0.3  # False!

# Solutions
# a) Use decimal
from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3')  # True

# b) Use isclose for comparisons
import math
math.isclose(0.1 + 0.1 + 0.1, 0.3)  # True
```

### 2. Integer Division in Python 2 vs 3
```python
# Python 2: 5 / 2 = 2 (integer division)
# Python 3: 5 / 2 = 2.5 (float division)

# Use // for integer division in Python 3
5 // 2  # 2
```

### 3. Mutable Default Arguments
```python
# ❌ Bad
def add_to_list(value, my_list=[]):  # Dangerous!
    my_list.append(value)
    return my_list

# ✅ Good
def add_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list
```

---

## Quick Reference Card

```python
# Creation
x = 42               # int
y = 3.14             # float
z = 2 + 3j           # complex

# Arithmetic
+ - * / // % **

# Comparison
== != < > <= >=

# Built-in
abs() round() pow() min() max() sum()

# Math module
import math
math.sqrt() math.log() math.sin() math.ceil()

# Random
import random
random.randint() random.random() random.choice()

# Type conversion
int() float() str() complex()

# Decimal & Fraction
from decimal import Decimal
from fractions import Fraction

# Formatting
f"{value:.2f}"  # 2 decimals
f"{value:,}"    # With commas
f"{value:.2%}"  # Percentage
```

---

## Resources

- **Official Python Documentation**: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
- **Decimal Module**: https://docs.python.org/3/library/decimal.html
- **Math Module**: https://docs.python.org/3/library/math.html
- **Random Module**: https://docs.python.org/3/library/random.html

---

**Happy Coding! 🐍✨**