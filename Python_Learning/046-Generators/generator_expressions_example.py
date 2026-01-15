"""
Python Generator Expressions - Detailed Examples

This module focuses specifically on generator expressions and their advantages
over list comprehensions, including memory efficiency and lazy evaluation.
"""

import sys
import time

# ============================================================================
# Example 1: BASIC GENERATOR EXPRESSION
# ============================================================================

print("=" * 70)
print("EXAMPLE 1: BASIC GENERATOR EXPRESSION")
print("=" * 70)

print("\nBasic generator expression: (x * 2 for x in range(5))")
gen_exp = (x * 2 for x in range(5))

print(f"Generator object: {gen_exp}")
print(f"Type: {type(gen_exp)}")

print("\nIterating through the generator:")
for value in gen_exp:
    print(f"  {value}")

print("\nComparison with list comprehension:")
list_comp = [x * 2 for x in range(5)]
print(f"List: {list_comp}")
print(f"Type: {type(list_comp)}")

# ============================================================================
# Example 2: MEMORY EFFICIENCY COMPARISON
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 2: MEMORY EFFICIENCY COMPARISON")
print("=" * 70)

# List comprehension - creates the entire list in memory
list_comp = [i for i in range(1000)]
list_size = sys.getsizeof(list_comp)
print(f"\nList comprehension (1000 items):")
print(f"  Memory: {list_size} bytes")

# Generator expression - creates an iterator, values are generated on-the-fly
gen_exp_mem = (i for i in range(1000))
gen_size = sys.getsizeof(gen_exp_mem)
print(f"\nGenerator expression (1000 items):")
print(f"  Memory: {gen_size} bytes")

savings = list_size - gen_size
print(f"\nMemory savings: {savings} bytes ({(savings/list_size)*100:.1f}%)")

# Test with larger dataset
print("\n--- Larger Dataset Comparison ---")
large_list = [i for i in range(100000)]
large_gen = (i for i in range(100000))
print(f"List (100,000 items): {sys.getsizeof(large_list)} bytes")
print(f"Generator (100,000 items): {sys.getsizeof(large_gen)} bytes")

# ============================================================================
# Example 3: LAZY EVALUATION
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 3: LAZY EVALUATION")
print("=" * 70)

print("\nDefining a function that prints when called:")

def expensive_operation(x):
    """Simulate an expensive operation."""
    print(f"  Processing {x}...")
    return x * x

print("\nCreating generator (no execution yet):")
gen_lazy = (expensive_operation(i) for i in range(5))
print(f"  Generator created: {gen_lazy}")
print("  (Notice: nothing printed - computation hasn't happened yet)")

print("\nRequesting values one by one:")
print(f"  First value: {next(gen_lazy)}")
print(f"  Second value: {next(gen_lazy)}")

print("\nRequesting remaining values in a loop:")
for val in gen_lazy:
    print(f"  Value: {val}")

# ============================================================================
# Example 4: GENERATOR EXPRESSIONS WITH FILTERING
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 4: GENERATOR EXPRESSIONS WITH FILTERING")
print("=" * 70)

# Generator expression with filter
print("\nFilter even numbers from 0-9:")
gen_even = (x for x in range(10) if x % 2 == 0)
print(f"  {list(gen_even)}")

# Generator expression with multiple conditions
print("\nNumbers between 5-15 that are divisible by 3:")
gen_filtered = (x for x in range(20) if 5 <= x <= 15 and x % 3 == 0)
print(f"  {list(gen_filtered)}")

# ============================================================================
# Example 5: GENERATOR EXPRESSIONS WITH TRANSFORMATION
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 5: GENERATOR EXPRESSIONS WITH TRANSFORMATION")
print("=" * 70)

# Simple transformation
print("\nSquare of numbers 0-5:")
gen_squares = (x ** 2 for x in range(6))
print(f"  {list(gen_squares)}")

# Transformation with filtering
print("\nSquares of even numbers only (0-10):")
gen_even_squares = (x ** 2 for x in range(11) if x % 2 == 0)
print(f"  {list(gen_even_squares)}")

# Complex transformation
print("\nConvert temperatures from Celsius to Fahrenheit:")
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit = ((c * 9/5) + 32 for c in celsius_temps)
print(f"  Celsius: {celsius_temps}")
print(f"  Fahrenheit: {list(fahrenheit)}")

# ============================================================================
# Example 6: USING GENERATORS WITH BUILT-IN FUNCTIONS
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 6: USING GENERATORS WITH BUILT-IN FUNCTIONS")
print("=" * 70)

# sum() with generator expression
print("\nSum of squares (1-10):")
total = sum(x ** 2 for x in range(1, 11))
print(f"  {total}")

# max() with generator expression
print("\nMaximum squared value (1-10):")
max_squared = max(x ** 2 for x in range(1, 11))
print(f"  {max_squared}")

# min() with generator expression
print("\nMinimum positive even number (1-20):")
min_even = min(x for x in range(1, 21) if x % 2 == 0)
print(f"  {min_even}")

# all() with generator expression
print("\nAll numbers in range are positive (1-10):")
all_positive = all(x > 0 for x in range(1, 11))
print(f"  {all_positive}")

# any() with generator expression
print("\nAny number divisible by 7 (1-10):")
any_div_7 = any(x % 7 == 0 for x in range(1, 11))
print(f"  {any_div_7}")

# ============================================================================
# Example 7: PERFORMANCE COMPARISON
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 7: PERFORMANCE COMPARISON")
print("=" * 70)

# Creation time
print("\nCreation time comparison:")

# List comprehension creation
start = time.time()
list_comp = [x ** 2 for x in range(100000)]
list_time = time.time() - start

# Generator creation
start = time.time()
gen_expr = (x ** 2 for x in range(100000))
gen_time = time.time() - start

print(f"  List creation: {list_time:.6f}s")
print(f"  Generator creation: {gen_time:.6f}s")
print(f"  Generator is {list_time/gen_time:.1f}x faster!")

# First value access
print("\nAccessing first 10 values:")

# From list
start = time.time()
list_comp = [x ** 2 for x in range(100000)]
for i in range(10):
    _ = list_comp[i]
list_time = time.time() - start

# From generator
start = time.time()
gen_expr = (x ** 2 for x in range(100000))
for i in range(10):
    _ = next(gen_expr)
gen_time = time.time() - start

print(f"  List access: {list_time:.6f}s")
print(f"  Generator access: {gen_time:.6f}s")

# ============================================================================
# Example 8: WHEN TO USE WHAT
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 8: WHEN TO USE GENERATORS VS LISTS")
print("=" * 70)

print("\nUse GENERATOR EXPRESSIONS when:")
print("  ✓ Working with large datasets")
print("  ✓ You don't need all values at once")
print("  ✓ Memory efficiency is important")
print("  ✓ Using with functions like sum(), max(), filter()")

print("\nUse LIST COMPREHENSIONS when:")
print("  ✓ You need to access elements by index")
print("  ✓ You need to iterate multiple times")
print("  ✓ The dataset is small")
print("  ✓ You need list methods like sort(), reverse(), append()")

# Practical example
print("\n--- Practical Example ---")

# GOOD: Using generator expression
large_sum = sum(x for x in range(1000000))
print(f"Sum of 0-999999 (using generator): {large_sum}")

print("\n" + "=" * 70)
print("DEMONSTRATION COMPLETE")
print("=" * 70)

