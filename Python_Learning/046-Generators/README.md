# Python Generators - Complete Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Basic Concepts](#basic-concepts)
3. [Generator Functions](#generator-functions)
4. [Generator Expressions](#generator-expressions)
5. [Advanced Features](#advanced-features)
6. [Practical Examples](#practical-examples)
7. [Performance Considerations](#performance-considerations)
8. [Common Pitfalls](#common-pitfalls)

## Introduction

Generators are a powerful feature in Python that allow you to create iterators efficiently. They are particularly useful when dealing with large datasets or infinite sequences because they generate values on-the-fly instead of storing them all in memory.

### Key Benefits
- **Memory Efficient**: Only stores one value in memory at a time
- **Lazy Evaluation**: Values are computed only when needed
- **Clean Syntax**: Simple and readable code
- **Composable**: Easy to chain generators together

## Basic Concepts

### What is a Generator?

A generator is a special type of iterator that produces values using the `yield` keyword. Instead of returning a single value and exiting (like a regular function), a generator can yield multiple values, pausing its execution between yields.

```python
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
```

### How Generators Work

1. **Creation**: When you call a generator function, it returns a generator object without executing the function body
2. **Iteration**: Each call to `next()` resumes execution from where it left off
3. **Pause**: Execution pauses at the `yield` statement
4. **Resume**: Execution continues from the next line after the `yield` when `next()` is called again
5. **Termination**: When the function ends or a `return` is encountered, `StopIteration` is raised

## Generator Functions

### Syntax

```python
def generator_name():
    # Setup code
    yield value1
    # More code
    yield value2
    # More code
    return  # Optional
```

### Example: Countdown Generator

```python
def countdown(n):
    """Generate numbers from n down to 1."""
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # Output: 5, 4, 3, 2, 1
```

### Example: Fibonacci Sequence

```python
def fibonacci(limit):
    """Generate Fibonacci numbers up to limit."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(100):
    print(num)  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
```

## Generator Expressions

### Syntax

Generator expressions are similar to list comprehensions but use parentheses `()` instead of square brackets `[]`.

```python
# List comprehension
list_comp = [x * x for x in range(5)]

# Generator expression
gen_expr = (x * x for x in range(5))
```

### Advantages

1. **Memory Efficient**
   ```python
   # Creates a list of 1 million items in memory
   list_comp = [x for x in range(1000000)]
   
   # Creates a generator that yields one value at a time
   gen_expr = (x for x in range(1000000))
   ```

2. **Lazy Evaluation**
   ```python
   def expensive_operation(x):
       print(f"Computing {x}")
       return x ** 2
   
   # No computation happens yet
   gen = (expensive_operation(x) for x in range(5))
   
   # Computation only happens when we iterate
   print(next(gen))  # Only "Computing 0" is printed
   ```

3. **Use with Built-in Functions**
   ```python
   # Memory efficient sum without creating a list
   total = sum(x * x for x in range(1000000))
   
   # Find the max efficiently
   max_val = max(x for x in data if x > 0)
   ```

## Advanced Features

### The `send()` Method

The `send()` method allows you to send a value back into the generator:

```python
def echo():
    """Receive and echo values."""
    while True:
        value = yield
        print(f"Received: {value}")

gen = echo()
next(gen)  # Prime the generator
gen.send("Hello")  # Output: Received: Hello
gen.send("World")  # Output: Received: World
```

### Exception Handling

```python
def generator_with_try():
    """Handle exceptions in a generator."""
    try:
        yield 1
        yield 2
        yield 3
    except ValueError:
        print("ValueError caught!")
        yield "Error handled"
    finally:
        print("Cleanup code")

gen = generator_with_try()
print(next(gen))      # Output: 1
print(gen.throw(ValueError))  # Throws ValueError
gen.close()           # Stops the generator
```

### The `throw()` Method

```python
def my_generator():
    try:
        yield 1
        yield 2
    except ValueError as e:
        print(f"Caught: {e}")

gen = my_generator()
print(next(gen))           # Output: 1
print(gen.throw(ValueError, "Error message"))
```

### The `close()` Method

```python
def my_generator():
    try:
        yield 1
        yield 2
    finally:
        print("Generator is being closed")

gen = my_generator()
print(next(gen))  # Output: 1
gen.close()       # Calls finally block
```

## Practical Examples

### 1. Reading Large Files

```python
def read_large_file(filepath, chunk_size=1024):
    """Read a large file efficiently."""
    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Usage
for chunk in read_large_file('huge_file.bin'):
    process_chunk(chunk)
```

### 2. Infinite Sequences

```python
def infinite_counter(start=0):
    """Generate infinite sequence of numbers."""
    while True:
        yield start
        start += 1

# Usage - take first 5
from itertools import islice
numbers = list(islice(infinite_counter(), 5))  # [0, 1, 2, 3, 4]
```

### 3. Generator Pipelines

```python
def source():
    """Generate data."""
    for i in range(1, 11):
        yield i

def transform(iterable):
    """Transform data."""
    for value in iterable:
        yield value * 2

def filter_data(iterable):
    """Filter data."""
    for value in iterable:
        if value % 4 == 0:
            yield value

# Chain generators together
result = list(filter_data(transform(source())))
print(result)  # [4, 8, 12, 16, 20]
```

### 4. Parsing CSV

```python
import csv

def parse_csv(filepath):
    """Parse CSV file efficiently."""
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

# Usage
for record in parse_csv('data.csv'):
    print(record)
```

## Performance Considerations

### Memory Usage Comparison

```python
import sys

# List comprehension
list_comp = [x**2 for x in range(100000)]
print(f"List size: {sys.getsizeof(list_comp)} bytes")

# Generator expression
gen_expr = (x**2 for x in range(100000))
print(f"Generator size: {sys.getsizeof(gen_expr)} bytes")
# Generator is much smaller!
```

### When to Use Generators

✅ **Use generators when:**
- Working with large datasets
- You don't need all values at once
- Processing infinite sequences
- Streaming data
- Building data pipelines

❌ **Don't use generators when:**
- You need random access to elements
- You need to iterate multiple times
- The dataset is small enough to fit in memory
- You need to use len() on the collection

### When to Use Lists

✅ **Use lists when:**
- You need to access elements by index
- You need to iterate multiple times
- The dataset is small
- You need built-in methods like sort(), reverse()

## Common Pitfalls

### 1. Exhausted Generators

```python
gen = (x for x in range(3))
list(gen)  # [0, 1, 2]
list(gen)  # [] - Generator is exhausted!
```

**Solution**: Create a new generator if you need to iterate again.

### 2. Single Pass Iteration

```python
gen = (x for x in range(3))
for x in gen:
    print(x)
for x in gen:  # Won't print anything - generator exhausted
    print(x)
```

**Solution**: Use generator functions to create new generators when needed.

### 3. Not Priming with `send()`

```python
def echo():
    while True:
        value = yield
        print(value)

gen = echo()
gen.send("Hello")  # Error! Must call next() first to reach yield
```

**Solution**: Always call `next()` before using `send()`.

### 4. Forgetting Generator Returns a Value

```python
def my_gen():
    yield 1
    return "Done"

gen = my_gen()
print(next(gen))  # 1
try:
    next(gen)
except StopIteration as e:
    print(e.value)  # "Done"
```

## Summary Table

| Feature | Generator | List |
|---------|-----------|------|
| Memory | O(1) - one value | O(n) - all values |
| Speed | Fast creation | Slower creation |
| Access | Sequential only | Random access |
| Reusable | Single use | Multiple uses |
| Best for | Large data | Small data |
| Syntax | `yield` | `[]` |

## Files in This Module

- **Generators.md**: Detailed documentation
- **Generators.py**: Basic examples and demonstrations
- **generator_expressions_example.py**: Generator expression examples
- **main.py**: Complete runnable examples with all concepts
- **README.md**: This file

## Running Examples

```bash
# Run all examples
python main.py

# Run individual files
python Generators.py
python generator_expressions_example.py
```

---

**Remember**: Generators are a key tool in Python for writing efficient, elegant code. Use them wisely!
