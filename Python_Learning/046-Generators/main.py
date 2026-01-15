"""
Main entry point for Generators module examples.
This file demonstrates all key concepts related to Python generators.
"""

import sys
from Generators import (
    simple_generator,
    yield_example,
    generator_with_exception,
    counter_generator
)


def separator(title=""):
    """Print a formatted separator."""
    if title:
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}\n")
    else:
        print("-" * 60)


def main():
    """Main function to demonstrate generator concepts."""
    
    # 1. Basic Generator Functions
    separator("1. BASIC GENERATOR FUNCTIONS")
    print("Simple generator yields: 1, 2, 3")
    for value in simple_generator():
        print(f"  Value: {value}")
    
    # 2. Generator Expressions
    separator("2. GENERATOR EXPRESSIONS")
    print("Generator expression: (x*x for x in range(5))")
    gen_squares = (x * x for x in range(5))
    for value in gen_squares:
        print(f"  Value: {value}")
    
    # 3. Memory Efficiency Comparison
    separator("3. MEMORY EFFICIENCY COMPARISON")
    list_comp = [i for i in range(10000)]
    gen_expr = (i for i in range(10000))
    print(f"List comprehension memory: {sys.getsizeof(list_comp)} bytes")
    print(f"Generator expression memory: {sys.getsizeof(gen_expr)} bytes")
    print(f"Memory savings: {sys.getsizeof(list_comp) - sys.getsizeof(gen_expr)} bytes")
    
    # 4. Lazy Evaluation
    separator("4. LAZY EVALUATION")
    print("Creating generator (no execution yet)...")
    def expensive_op(x):
        print(f"  Computing for {x}...")
        return x ** 2
    
    lazy_gen = (expensive_op(i) for i in range(3))
    print("Generator created. Now requesting values one by one:")
    print(f"  First value: {next(lazy_gen)}")
    print(f"  Second value: {next(lazy_gen)}")
    
    # 5. yield vs return
    separator("5. yield vs return")
    print("In a generator, yield pauses and return stops:")
    y_gen = yield_example()
    print(f"  First next(): {next(y_gen)}")
    try:
        next(y_gen)
    except StopIteration as e:
        print(f"  StopIteration value: {e.value}")
    
    # 6. Exception Handling in Generators
    separator("6. EXCEPTION HANDLING IN GENERATORS")
    print("Generator with exception handling:")
    gwe = generator_with_exception()
    print(f"  First value: {next(gwe)}")
    print("  Throwing ValueError into generator...")
    try:
        print(f"  Result after throw: {gwe.throw(ValueError)}")
    except StopIteration:
        print("  Generator stopped.")
    
    # 7. send() method
    separator("7. send() METHOD")
    print("Using send() to communicate with generator:")
    cg = counter_generator()
    print(f"  Initial: {next(cg)}")
    print(f"  Increment: {next(cg)}")
    print(f"  send(100): {cg.send(100)}")
    print(f"  Increment: {next(cg)}")
    
    # 8. Practical Examples
    separator("8. PRACTICAL EXAMPLES")
    
    # Example: Reading large files line by line
    print("Example: Reading lines from generator (simulated)")
    def read_large_file(filepath):
        """Simulate reading a large file efficiently."""
        for i in range(5):
            yield f"Line {i+1}: Sample data"
    
    for line in read_large_file("dummy.txt"):
        print(f"  {line}")
    
    # Example: Fibonacci sequence
    print("\nExample: Fibonacci sequence generator")
    def fibonacci(n):
        """Generate Fibonacci sequence up to n terms."""
        a, b = 0, 1
        count = 0
        while count < n:
            yield a
            a, b = b, a + b
            count += 1
    
    print("  First 7 Fibonacci numbers:", list(fibonacci(7)))
    
    # 9. Generator Pipelines
    separator("9. GENERATOR PIPELINES")
    print("Chaining generators for data processing:")
    
    def source():
        """Generate numbers 1-5."""
        for i in range(1, 6):
            yield i
    
    def transform(iterable):
        """Transform each number by multiplying by 2."""
        for x in iterable:
            yield x * 2
    
    def filter_even(iterable):
        """Filter to keep only even results."""
        for x in iterable:
            if x % 4 == 0:
                yield x
    
    result = list(filter_even(transform(source())))
    print(f"  Pipeline result: {result}")
    
    # 10. Generator Performance
    separator("10. GENERATOR PERFORMANCE")
    import time
    
    # Using list
    start = time.time()
    squares_list = [x**2 for x in range(100000)]
    list_time = time.time() - start
    
    # Using generator
    start = time.time()
    squares_gen = (x**2 for x in range(100000))
    sum(squares_gen)
    gen_time = time.time() - start
    
    print(f"List comprehension time: {list_time:.6f}s")
    print(f"Generator expression time: {gen_time:.6f}s")
    
    separator("DEMONSTRATION COMPLETE")


if __name__ == "__main__":
    main()
