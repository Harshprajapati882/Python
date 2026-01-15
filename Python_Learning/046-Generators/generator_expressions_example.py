# Python Generator Expressions Examples

# Example 1: Basic generator expression
print("Example 1: Basic generator expression")
gen_exp = (x * 2 for x in range(5))

print("Generator object:", gen_exp)

print("Iterating through the generator:")
for value in gen_exp:
    print(value)

print("-" * 20)

# Example 2: Memory efficiency of generator expressions vs. list comprehensions
import sys

print("Example 2: Memory Efficiency")
# List comprehension - creates the entire list in memory
list_comp = [i for i in range(1000)]
print("Memory size of list comprehension:", sys.getsizeof(list_comp), "bytes")

# Generator expression - creates an iterator, values are generated on-the-fly
gen_exp_mem = (i for i in range(1000))
print("Memory size of generator expression:", sys.getsizeof(gen_exp_mem), "bytes")

print("-" * 20)

# Example 3: Lazy evaluation
print("Example 3: Lazy Evaluation")

def my_func(x):
    print(f"Processing {x}")
    return x * x

gen_lazy = (my_func(i) for i in range(5))

print("Generator created, but not yet iterated.")

print("First iteration:")
print("Result:", next(gen_lazy))

print("Second iteration:")
print("Result:", next(gen_lazy))

print("Remaining iterations:")
for val in gen_lazy:
    print("Result:", val)

print("-" * 20)


# Example 4: Cleaner code
print("Example 4: Cleaner Code")

# Using a generator function
def square_numbers(nums):
    for i in nums:
        yield (i*i)

# Using a generator expression - more concise
sum_of_squares_gen_exp = sum(x*x for x in range(10)) 

print("Sum of squares (using generator expression):", sum_of_squares_gen_exp)

# Equivalent using a for loop
sum_of_squares_loop = 0
for x in range(10):
    sum_of_squares_loop += x*x

print("Sum of squares (using a for loop):", sum_of_squares_loop)

print("-" * 20)

