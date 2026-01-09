"""
Number.py - Comprehensive Guide to Numbers in Python
This file demonstrates all aspects of working with numbers in Python
"""

# ============================================================================
# 1. INTEGER TYPES (int)
# ============================================================================

# Basic integers
positive_int = 42
negative_int = -17
zero = 0

# Python 3 has arbitrary precision integers (no overflow!)
very_large_int = 99999999999999999999999999999999999999
print(f"Large integer: {very_large_int}")

# Different number bases
binary = 0b1010  # Binary (base 2) = 10
octal = 0o12     # Octal (base 8) = 10
hexadecimal = 0xA # Hex (base 16) = 10
print(f"Binary {binary}, Octal {octal}, Hex {hexadecimal}")

# Converting between bases
num = 255
print(f"Binary: {bin(num)}")    # 0b11111111
print(f"Octal: {oct(num)}")     # 0o377
print(f"Hex: {hex(num)}")       # 0xff

# Underscores for readability (Python 3.6+)
million = 1_000_000
binary_readable = 0b_1111_0000
print(f"Million: {million}")

# ============================================================================
# 2. FLOATING POINT NUMBERS (float)
# ============================================================================

# Basic floats
pi = 3.14159
negative_float = -2.5
scientific = 1.5e-4  # 0.00015
large_scientific = 2.5e10  # 25000000000.0

print(f"Scientific notation: {scientific}, {large_scientific}")

# Float precision and limitations
print(f"Float precision issue: {0.1 + 0.2}")  # 0.30000000000000004
print(f"Float precision issue: {0.1 + 0.2 == 0.3}")  # False!

# Checking for infinity and NaN
infinity = float('inf')
neg_infinity = float('-inf')
not_a_number = float('nan')

import math
print(f"Is infinity? {math.isinf(infinity)}")
print(f"Is NaN? {math.isnan(not_a_number)}")
print(f"Is finite? {math.isfinite(42.5)}")

# ============================================================================
# 3. COMPLEX NUMBERS (complex)
# ============================================================================

# Creating complex numbers
z1 = 3 + 4j  # j or J for imaginary unit
z2 = complex(2, -1)  # 2 - 1j
pure_imaginary = 5j
real_only = complex(7, 0)

print(f"Complex: {z1}, {z2}")

# Accessing real and imaginary parts
print(f"Real part: {z1.real}, Imaginary part: {z1.imag}")

# Complex number operations
z3 = z1 + z2  # Addition
z4 = z1 * z2  # Multiplication
conjugate = z1.conjugate()  # Complex conjugate
magnitude = abs(z1)  # Magnitude (distance from origin)

print(f"Conjugate: {conjugate}, Magnitude: {magnitude}")

# ============================================================================
# 4. DECIMAL - HIGH PRECISION ARITHMETIC
# ============================================================================

from decimal import Decimal, getcontext

# Set precision
getcontext().prec = 50

# Decimal avoids float precision issues
d1 = Decimal('0.1')
d2 = Decimal('0.2')
print(f"Decimal precision: {d1 + d2}")  # Exactly 0.3

# Financial calculations
price = Decimal('19.99')
tax_rate = Decimal('0.08')
total = price * (1 + tax_rate)
print(f"Total with tax: ${total:.2f}")

# High precision calculations
pi_decimal = Decimal('3.1415926535897932384626433832795028841971')
print(f"High precision pi: {pi_decimal}")

# ============================================================================
# 5. FRACTIONS - RATIONAL NUMBERS
# ============================================================================

from fractions import Fraction

# Creating fractions
f1 = Fraction(3, 4)  # 3/4
f2 = Fraction(1, 2)  # 1/2
f3 = Fraction('0.5')  # From string
f4 = Fraction(0.25)  # From float

print(f"Fractions: {f1}, {f2}, {f3}, {f4}")

# Fraction arithmetic (exact)
result = f1 + f2  # 5/4
result2 = f1 * f2  # 3/8
print(f"Fraction addition: {result}, multiplication: {result2}")

# Converting to float
print(f"Fraction to float: {float(f1)}")

# ============================================================================
# 6. BASIC ARITHMETIC OPERATIONS
# ============================================================================

a, b = 17, 5

addition = a + b        # 22
subtraction = a - b     # 12
multiplication = a * b  # 85
division = a / b        # 3.4 (always returns float)
floor_division = a // b # 3 (integer division, rounds down)
modulo = a % b          # 2 (remainder)
exponentiation = a ** b # 17^5 = 1419857

print(f"Operations: +{addition}, -{subtraction}, *{multiplication}")
print(f"Division: /{division}, //{floor_division}, %{modulo}, **{exponentiation}")

# Negative floor division
print(f"-17 // 5 = {-17 // 5}")  # -4 (rounds toward negative infinity)
print(f"-17 % 5 = {-17 % 5}")    # 3

# ============================================================================
# 7. AUGMENTED ASSIGNMENT OPERATORS
# ============================================================================

x = 10
x += 5   # x = x + 5
x -= 3   # x = x - 3
x *= 2   # x = x * 2
x /= 4   # x = x / 4
x //= 2  # x = x // 2
x %= 3   # x = x % 3
x **= 2  # x = x ** 2

print(f"Final x: {x}")

# ============================================================================
# 8. COMPARISON OPERATORS
# ============================================================================

print(f"5 > 3: {5 > 3}")
print(f"5 < 3: {5 < 3}")
print(f"5 >= 5: {5 >= 5}")
print(f"5 <= 5: {5 <= 5}")
print(f"5 == 5: {5 == 5}")
print(f"5 != 3: {5 != 3}")

# Chained comparisons
print(f"1 < 5 < 10: {1 < 5 < 10}")  # True
print(f"1 < 5 > 3: {1 < 5 > 3}")    # True

# ============================================================================
# 9. BUILT-IN MATH FUNCTIONS
# ============================================================================

numbers = [1, -5, 3.7, -2.1, 10]

print(f"abs(-5) = {abs(-5)}")           # Absolute value: 5
print(f"round(3.7) = {round(3.7)}")     # Round: 4
print(f"round(3.5) = {round(3.5)}")     # Banker's rounding: 4
print(f"round(4.5) = {round(4.5)}")     # Banker's rounding: 4
print(f"round(3.14159, 2) = {round(3.14159, 2)}")  # 2 decimals: 3.14

print(f"pow(2, 3) = {pow(2, 3)}")       # 2^3 = 8
print(f"pow(2, 3, 5) = {pow(2, 3, 5)}") # (2^3) % 5 = 3

print(f"min(numbers) = {min(numbers)}") # -5
print(f"max(numbers) = {max(numbers)}") # 10
print(f"sum(numbers) = {sum(numbers)}") # 7.6

# divmod - quotient and remainder
quotient, remainder = divmod(17, 5)
print(f"divmod(17, 5) = {quotient}, {remainder}")

# ============================================================================
# 10. MATH MODULE - ADVANCED FUNCTIONS
# ============================================================================

import math

# Constants
print(f"Pi: {math.pi}")
print(f"Euler's number: {math.e}")
print(f"Tau (2*pi): {math.tau}")
print(f"Infinity: {math.inf}")

# Rounding and truncation
print(f"ceil(3.2) = {math.ceil(3.2)}")     # 4
print(f"floor(3.8) = {math.floor(3.8)}")   # 3
print(f"trunc(3.8) = {math.trunc(3.8)}")   # 3
print(f"trunc(-3.8) = {math.trunc(-3.8)}") # -3

# Power and logarithms
print(f"sqrt(16) = {math.sqrt(16)}")               # 4.0
print(f"pow(2, 10) = {math.pow(2, 10)}")           # 1024.0
print(f"exp(2) = {math.exp(2)}")                   # e^2
print(f"log(100) = {math.log(100)}")               # Natural log
print(f"log10(100) = {math.log10(100)}")           # Base 10: 2.0
print(f"log2(8) = {math.log2(8)}")                 # Base 2: 3.0
print(f"log(8, 2) = {math.log(8, 2)}")             # Custom base

# Trigonometry (radians)
angle = math.pi / 4  # 45 degrees
print(f"sin(π/4) = {math.sin(angle)}")
print(f"cos(π/4) = {math.cos(angle)}")
print(f"tan(π/4) = {math.tan(angle)}")

# Convert between degrees and radians
print(f"radians(180) = {math.radians(180)}")  # π
print(f"degrees(π) = {math.degrees(math.pi)}") # 180

# Factorial and combinations
print(f"factorial(5) = {math.factorial(5)}")  # 120
print(f"gcd(48, 18) = {math.gcd(48, 18)}")    # 6
print(f"lcm(12, 15) = {math.lcm(12, 15)}")    # 60 (Python 3.9+)

# ============================================================================
# 11. RANDOM MODULE - RANDOM NUMBERS
# ============================================================================

import random

# Random integers
print(f"Random int [1, 10]: {random.randint(1, 10)}")
print(f"Random range [0, 100, step 5]: {random.randrange(0, 100, 5)}")

# Random floats
print(f"Random float [0, 1): {random.random()}")
print(f"Random uniform [1, 10]: {random.uniform(1, 10)}")

# Random choice from sequence
colors = ['red', 'green', 'blue', 'yellow']
print(f"Random choice: {random.choice(colors)}")

# Shuffle and sample
numbers_list = list(range(1, 11))
random.shuffle(numbers_list)  # In-place shuffle
print(f"Shuffled: {numbers_list}")

sample = random.sample(range(1, 50), 6)  # 6 unique numbers
print(f"Lottery numbers: {sample}")

# ============================================================================
# 12. TYPE CONVERSION AND CHECKING
# ============================================================================

# Type checking
print(f"type(42) = {type(42)}")
print(f"type(3.14) = {type(3.14)}")
print(f"type(2+3j) = {type(2+3j)}")
print(f"isinstance(42, int) = {isinstance(42, int)}")
print(f"isinstance(3.14, (int, float)) = {isinstance(3.14, (int, float))}")

# Type conversion
str_num = "42"
float_num = 3.14
complex_num = 2 + 3j

converted_int = int(str_num)        # "42" -> 42
converted_float = float(str_num)    # "42" -> 42.0
converted_str = str(42)             # 42 -> "42"
int_from_float = int(float_num)     # 3.14 -> 3
float_from_complex = abs(complex_num) # Magnitude

print(f"Conversions: {converted_int}, {converted_float}, {int_from_float}")

# ============================================================================
# 13. NUMBER FORMATTING
# ============================================================================

value = 1234.56789

# f-strings (Python 3.6+)
print(f"Default: {value}")
print(f"2 decimals: {value:.2f}")
print(f"Width 10: {value:10.2f}")
print(f"Zero-padded: {value:010.2f}")
print(f"With commas: {value:,.2f}")
print(f"Percentage: {0.1567:.2%}")
print(f"Scientific: {value:.2e}")

# Format method
print("Value: {:.2f}".format(value))

# Padding and alignment
print(f"Left: {value:<15.2f}|")
print(f"Right: {value:>15.2f}|")
print(f"Center: {value:^15.2f}|")

# ============================================================================
# 14. BITWISE OPERATIONS (for integers)
# ============================================================================

a, b = 12, 5  # Binary: 1100, 0101

print(f"AND: {a & b}")      # 0100 = 4
print(f"OR: {a | b}")       # 1101 = 13
print(f"XOR: {a ^ b}")      # 1001 = 9
print(f"NOT: {~a}")         # Two's complement
print(f"Left shift: {a << 2}")   # 110000 = 48
print(f"Right shift: {a >> 2}")  # 0011 = 3

# Checking if number is even/odd using bitwise
print(f"12 is even: {(12 & 1) == 0}")
print(f"13 is odd: {(13 & 1) == 1}")

# ============================================================================
# 15. SPECIAL NUMERIC METHODS
# ============================================================================

# Integer division and modulo relationship
n, d = 17, 5
print(f"{n} = {d} * {n//d} + {n%d}")  # 17 = 5 * 3 + 2

# Sign function
def sign(x):
    return (x > 0) - (x < 0)

print(f"sign(5) = {sign(5)}, sign(-5) = {sign(-5)}, sign(0) = {sign(0)}")

# Clamp function
def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

print(f"clamp(15, 0, 10) = {clamp(15, 0, 10)}")

# ============================================================================
# 16. PRACTICAL EXAMPLES
# ============================================================================

# Example 1: Calculate compound interest
principal = 1000
rate = 0.05
time = 10
amount = principal * (1 + rate) ** time
print(f"Compound interest: ${amount:.2f}")

# Example 2: Temperature conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Example 3: Distance between two points
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance: {distance}")

# Example 4: Check if prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(f"17 is prime: {is_prime(17)}")
print(f"18 is prime: {is_prime(18)}")

# Example 5: Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(f"First 10 Fibonacci numbers: {list(fibonacci(10))}")

print("\n✓ Number.py demonstration complete!")
