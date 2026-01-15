"""
Python Generators Examples - Comprehensive Guide

This module contains examples demonstrating various aspects of Python generators.
Topics covered:
- Simple generator functions
- Generator expressions
- yield vs return
- Exception handling
- send() method
- Async generators
- Practical examples
"""

# ============================================================================
# 1. SIMPLE GENERATOR FUNCTION
# ============================================================================

def simple_generator():
    """A simple generator function that yields three numbers."""
    print("Starting generator...")
    yield 1
    yield 2
    yield 3
    print("...Generator finished.")


print("=" * 70)
print("1. SIMPLE GENERATOR FUNCTION")
print("=" * 70)

# To use the generator, you first create a generator object
gen_obj = simple_generator()
print("Created generator object:", gen_obj)

# You can iterate over it using a for loop
print("\nIterating with a for loop:")
for value in simple_generator():
    print(f"  Value: {value}")

# Or by using next()
gen_obj = simple_generator()
print("\nIterating with next():")
print(f"  First: {next(gen_obj)}")
print(f"  Second: {next(gen_obj)}")
print(f"  Third: {next(gen_obj)}")

# The next line would raise a StopIteration exception because the generator is exhausted
# print(next(gen_obj))

# Better practice: use try-except to handle StopIteration
gen_obj = simple_generator()
print("\nIterating until StopIteration:")
try:
    while True:
        print(f"  Next value: {next(gen_obj)}")
except StopIteration:
    print("  Generator exhausted!")


# ============================================================================
# 2. GENERATOR EXPRESSIONS
# ============================================================================

print("\n" + "=" * 70)
print("2. GENERATOR EXPRESSIONS")
print("=" * 70)

# List comprehension - creates entire list in memory
list_comp = [i * i for i in range(5)]
print(f"List comprehension: {list_comp}")
print(f"Type: {type(list_comp)}")

# Generator expression - creates iterator, values on-demand
gen_exp = (i * i for i in range(5))
print(f"\nGenerator expression object: {gen_exp}")
print(f"Type: {type(gen_exp)}")

print("\nValues from generator expression:")
for value in gen_exp:
    print(f"  {value}")

# Generator expression with filtering
print("\nGenerator expression with filtering:")
gen_filtered = (x for x in range(10) if x % 2 == 0)
print(f"Even numbers: {list(gen_filtered)}")

# Generator expression with transformation
print("\nGenerator expression with transformation:")
gen_transform = (x ** 2 for x in range(5) if x > 1)
print(f"Squares of numbers > 1: {list(gen_transform)}")


# ============================================================================
# 3. YIELD VS RETURN
# ============================================================================

print("\n" + "=" * 70)
print("3. YIELD VS RETURN")
print("=" * 70)

def yield_example():
    """Demonstrates yield and return in a generator."""
    yield "first value"
    yield "second value"
    return "return value"


y_gen = yield_example()
print(f"First next(): {next(y_gen)}")
print(f"Second next(): {next(y_gen)}")

try:
    next(y_gen)
except StopIteration as e:
    print(f"StopIteration raised with value: {e.value}")

print("\nKey difference:")
print("  - yield: Pauses execution, saves state, returns value")
print("  - return: Terminates generator, value becomes StopIteration.value")


# ============================================================================
# 4. EXCEPTION HANDLING IN GENERATORS
# ============================================================================

print("\n" + "=" * 70)
print("4. EXCEPTION HANDLING IN GENERATORS")
print("=" * 70)

def generator_with_exception():
    """A generator that handles exceptions."""
    print("  Generator started")
    try:
        print("  About to yield 10")
        yield 10
        print("  About to yield 20")
        yield 20
        print("  About to yield 30")
        yield 30
    except ValueError as e:
        print(f"  Caught ValueError: {e}")
        yield "Handled error"
    finally:
        print("  Generator is closing (finally block)")


print("\n--- Using throw() to inject exceptions ---")
gwe = generator_with_exception()
print(f"First next(): {next(gwe)}")

print("\nThrowing ValueError into generator...")
try:
    print(f"Value after throw: {gwe.throw(ValueError, 'Error message')}")
except StopIteration:
    print("Generator stopped after throw")

print("\n--- Using close() to stop generator ---")
gwe2 = generator_with_exception()
print(f"First next(): {next(gwe2)}")
print("Closing generator...")
gwe2.close()
print("Generator closed")


# ============================================================================
# 5. SEND() METHOD - TWO-WAY COMMUNICATION
# ============================================================================

print("\n" + "=" * 70)
print("5. SEND() METHOD - TWO-WAY COMMUNICATION")
print("=" * 70)

def counter_generator():
    """A generator that can receive values using send()."""
    count = 0
    while count < 20:
        # The yield expression receives value from send()
        received = yield count
        if received is not None:
            print(f"  Received from send(): {received}")
            count = received
        else:
            count += 1


print("\nUsing send() to communicate with generator:")
cg = counter_generator()
print(f"next() to start: {next(cg)}")
print(f"next() again: {next(cg)}")
try:
    print(f"send(10): {cg.send(10)}")
    print(f"next(): {next(cg)}")
    print(f"next(): {next(cg)}")
except StopIteration:
    print("  Generator exhausted")


# ============================================================================
# 6. PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 70)
print("6. PRACTICAL EXAMPLES")
print("=" * 70)

# Example 1: Fibonacci Generator
print("\n--- Example 1: Fibonacci Sequence ---")

def fibonacci(limit):
    """Generate Fibonacci numbers up to limit."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


print("Fibonacci numbers up to 1000:")
print(f"  {list(fibonacci(1000))}")

# Example 2: Range-like Generator
print("\n--- Example 2: Custom Range Generator ---")

def my_range(start, end, step=1):
    """A generator that behaves like range()."""
    current = start
    while current < end:
        yield current
        current += step


print("my_range(0, 10, 2):")
print(f"  {list(my_range(0, 10, 2))}")

# Example 3: File-like Reading (simulated)
print("\n--- Example 3: Reading Lines from File (Simulated) ---")

def read_lines(lines):
    """Simulate reading lines from a file."""
    for line in lines:
        yield line.strip()


sample_lines = ["Hello World", "  Python Generators  ", "Are Awesome!"]
print("Reading lines:")
for i, line in enumerate(read_lines(sample_lines), 1):
    print(f"  Line {i}: {line}")

# Example 4: Infinite Sequence Generator
print("\n--- Example 4: Infinite Sequence Generator ---")

def infinite_sequence():
    """Generate infinite sequence of numbers."""
    num = 0
    while True:
        yield num
        num += 1


# Take first 5 values from infinite sequence
from itertools import islice
print("First 5 numbers from infinite_sequence():")
print(f"  {list(islice(infinite_sequence(), 5))}")

# Example 5: Generator Pipeline
print("\n--- Example 5: Generator Pipeline ---")

def numbers():
    """Generate numbers 1-10."""
    for i in range(1, 11):
        yield i


def squares(iterable):
    """Transform each number to its square."""
    for x in iterable:
        yield x * x


def filter_large(iterable, threshold=50):
    """Filter values larger than threshold."""
    for x in iterable:
        if x > threshold:
            yield x


print("Pipeline: numbers -> squares -> filter > 50:")
result = list(filter_large(squares(numbers())))
print(f"  {result}")

# ============================================================================
# 7. ASYNC GENERATORS
# ============================================================================

import asyncio

print("\n" + "=" * 70)
print("7. ASYNC GENERATORS")
print("=" * 70)

async def async_generator():
    """An asynchronous generator that yields values with delay."""
    print("  Async generator started")
    for i in range(3):
        print(f"  Waiting before yielding {i*i}...")
        await asyncio.sleep(0.5)
        yield i * i
    print("  Async generator finished")

async def run_async_gen():
    print("\nIterating over async generator:")
    async for value in async_generator():
        print(f"  Value: {value}")

# Running the async example
if __name__ == "__main__":
    asyncio.run(run_async_gen())
