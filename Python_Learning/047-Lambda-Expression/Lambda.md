# Lambda Expressions in Python

## Table of Contents
1. [Introduction](#introduction)
2. [Syntax](#syntax)
3. [Parameters](#parameters)
4. [Expressions](#expressions)
5. [Inline Usage](#inline-usage)
6. [Conciseness Benefits](#conciseness-benefits)
7. [Functional Programming](#functional-programming)
8. [Use Cases](#use-cases)
9. [Best Practices](#best-practices)

---

## Introduction

**Lambda** is a small anonymous function in Python that can take any number of arguments but can only have a single expression.

- **Anonymous**: No name required
- **Lightweight**: Single expression only
- **Concise**: More compact than regular functions
- **Functional**: Works perfectly with functional programming paradigms

### Key Characteristics
- Returns the result of the expression automatically
- Used for short, throwaway functions
- Popular with `map()`, `filter()`, and `sorted()`
- Cannot contain multiple statements

---

## Syntax

### Basic Syntax
```python
lambda arguments: expression
```

### Components
- **`lambda`** keyword: Defines an anonymous function
- **`arguments`**: Comma-separated list of parameters (optional)
- **`:`** colon: Separates parameters from expression
- **`expression`**: Single expression that gets evaluated and returned

### Examples
```python
# No arguments
lambda: 42

# Single argument
lambda x: x * 2

# Multiple arguments
lambda x, y: x + y

# Complex expression (still single line)
lambda x: x ** 2 if x > 0 else -x
```

---

## Parameters

### No Parameters
```python
# Lambda with no parameters
func = lambda: "Hello"
print(func())  # Output: Hello
```

### Single Parameter
```python
# Lambda with one parameter
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

### Multiple Parameters
```python
# Lambda with multiple parameters
add = lambda x, y: x + y
print(add(3, 7))  # Output: 10

multiply = lambda a, b, c: a * b * c
print(multiply(2, 3, 4))  # Output: 24
```

### Default Parameters
```python
# Lambda with default parameter values
greet = lambda name="Friend": f"Hello, {name}!"
print(greet())  # Output: Hello, Friend!
print(greet("Alice"))  # Output: Hello, Alice!
```

### Variable-Length Arguments
```python
# Using *args
sum_all = lambda *args: sum(args)
print(sum_all(1, 2, 3, 4, 5))  # Output: 15

# Using **kwargs
describe = lambda **kwargs: " ".join(f"{k}={v}" for k, v in kwargs.items())
print(describe(name="Alice", age=30, city="NYC"))
# Output: name=Alice age=30 city=NYC
```

---

## Expressions

### Arithmetic Expressions
```python
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y
power = lambda x, y: x ** y

print(add(10, 5))       # Output: 15
print(power(2, 8))      # Output: 256
```

### Conditional Expressions (Ternary)
```python
# if-else in lambda
max_value = lambda x, y: x if x > y else y
print(max_value(10, 20))  # Output: 20

# Multiple conditions
grade = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade(85))  # Output: B
```

### String Expressions
```python
# String manipulation
uppercase = lambda s: s.upper()
print(uppercase("hello"))  # Output: HELLO

# String formatting
format_name = lambda first, last: f"{first.capitalize()} {last.upper()}"
print(format_name("john", "doe"))  # Output: John DOE
```

### List/Collection Expressions
```python
# List operations
first_element = lambda lst: lst[0]
sum_list = lambda lst: sum(lst)
list_length = lambda lst: len(lst)

numbers = [1, 2, 3, 4, 5]
print(first_element(numbers))  # Output: 1
print(sum_list(numbers))       # Output: 15
print(list_length(numbers))    # Output: 5
```

### Boolean Expressions
```python
# Boolean logic
is_positive = lambda x: x > 0
is_even = lambda x: x % 2 == 0
both_true = lambda x, y: x and y

print(is_positive(5))     # Output: True
print(is_even(4))         # Output: True
print(both_true(True, False))  # Output: False
```

---

## Inline Usage

### With `map()`
```python
# Apply function to each element
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Convert strings to integers
strings = ["1", "2", "3", "4"]
integers = list(map(lambda x: int(x), strings))
print(integers)  # Output: [1, 2, 3, 4]
```

### With `filter()`
```python
# Filter elements based on condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]

# Filter strings
words = ["apple", "ant", "ball", "bat", "cat"]
words_with_a = list(filter(lambda w: 'a' in w.lower(), words))
print(words_with_a)  # Output: ['apple', 'ant', 'bat', 'cat']
```

### With `sorted()` / `sorted(key=)`
```python
# Sort by key using lambda
students = [("Alice", 85), ("Bob", 75), ("Charlie", 90)]
sorted_by_score = sorted(students, key=lambda x: x[1])
print(sorted_by_score)
# Output: [('Bob', 75), ('Alice', 85), ('Charlie', 90)]

# Sort strings by length
words = ["python", "is", "awesome", "code"]
sorted_by_length = sorted(words, key=lambda w: len(w))
print(sorted_by_length)
# Output: ['is', 'code', 'python', 'awesome']

# Sort dictionary by value
items = {"c": 3, "a": 1, "b": 2}
sorted_items = sorted(items.items(), key=lambda x: x[1])
print(sorted_items)  # Output: [('a', 1), ('b', 2), ('c', 3)]
```

### With `reduce()` (from functools)
```python
from functools import reduce

# Calculate product
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Concatenate strings
words = ["Hello", " ", "World"]
result = reduce(lambda x, y: x + y, words)
print(result)  # Output: Hello World
```

### With `min()` / `max()`
```python
# Find item with minimum/maximum value
students = [("Alice", 85), ("Bob", 75), ("Charlie", 90)]
top_student = max(students, key=lambda x: x[1])
print(top_student)  # Output: ('Charlie', 90)

bottom_student = min(students, key=lambda x: x[1])
print(bottom_student)  # Output: ('Bob', 75)
```

### With `enumerate()`
```python
# Custom enumeration starting from 1
items = ["apple", "banana", "cherry"]
for i, item in map(lambda x: (x[0] + 1, x[1]), enumerate(items)):
    print(f"{i}. {item}")
# Output:
# 1. apple
# 2. banana
# 3. cherry
```

---

## Conciseness Benefits

### Compare: Lambda vs Def Function

#### Regular Function
```python
def square(x):
    return x ** 2

result = square(5)
```

#### Lambda Function
```python
square = lambda x: x ** 2
result = square(5)
```

**Benefits of Lambda:**
- ✅ One line of code
- ✅ No need for separate function definition
- ✅ More readable when used inline with `map()`, `filter()`, etc.
- ✅ Better for throwaway/temporary functions

### Real-world Example: Data Processing
```python
# Without lambda - verbose
def filter_adults(person):
    return person["age"] >= 18

def get_name(person):
    return person["name"]

people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 16}]
adults = list(filter(filter_adults, people))
names = list(map(get_name, adults))

# With lambda - concise
adults = list(filter(lambda p: p["age"] >= 18, people))
names = list(map(lambda p: p["name"], adults))
```

---

## Functional Programming

### Core Concepts

#### 1. Map: Transform Data
```python
# Transform each element
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]
```

#### 2. Filter: Select Data
```python
# Keep only elements meeting condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]
```

#### 3. Reduce: Aggregate Data
```python
from functools import reduce

# Combine all elements into single value
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15
```

#### 4. Compose: Chain Operations
```python
# Composition with lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers, square them, sum them
result = sum(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # Output: 120
# Calculation: (2² + 4² + 6² + 8² + 10²) = 4 + 16 + 36 + 64 + 100 = 220
```

#### 5. Function as Parameter
```python
# Higher-order functions
def apply_operation(x, y, operation):
    return operation(x, y)

result1 = apply_operation(5, 3, lambda a, b: a + b)
result2 = apply_operation(5, 3, lambda a, b: a * b)

print(result1)  # Output: 8
print(result2)  # Output: 15
```

### Functional Programming Patterns

#### Pattern 1: Pipeline Processing
```python
# Process data through multiple lambda functions
data = [1, 2, 3, 4, 5]

# Pipeline: multiply by 2 → filter even → sum
pipeline = lambda lst: sum(filter(
    lambda x: x % 2 == 0,
    map(lambda x: x * 2, lst)
))

print(pipeline(data))  # Output: 30
# (1*2=2, 2*2=4, 3*2=6, 4*2=8, 5*2=10)
# Filter evens: 2, 4, 6, 8, 10 (all even)
# Sum: 30
```

#### Pattern 2: Currying (Partial Application)
```python
# Create specialized functions using lambda
multiply_by_2 = lambda x: x * 2
multiply_by_5 = lambda x: x * 5
add_10 = lambda x: x + 10

print(multiply_by_2(5))  # Output: 10
print(multiply_by_5(3))  # Output: 15
print(add_10(20))        # Output: 30
```

#### Pattern 3: Function Factory
```python
# Lambda factory that returns functions
def multiplier_factory(factor):
    return lambda x: x * factor

times_2 = multiplier_factory(2)
times_5 = multiplier_factory(5)

print(times_2(10))  # Output: 20
print(times_5(10))  # Output: 50
```

---

## Use Cases

### 1. Sorting Complex Objects
```python
employees = [
    {"name": "Alice", "salary": 50000, "dept": "IT"},
    {"name": "Bob", "salary": 60000, "dept": "HR"},
    {"name": "Charlie", "salary": 55000, "dept": "IT"},
]

# Sort by salary
by_salary = sorted(employees, key=lambda e: e["salary"])

# Sort by department, then name
by_dept_name = sorted(employees, key=lambda e: (e["dept"], e["name"]))
```

### 2. Data Transformation
```python
prices = [10.50, 20.75, 15.30]

# Apply 10% discount
discounted = list(map(lambda p: p * 0.9, prices))
print(discounted)  # Output: [9.45, 18.675, 13.77]
```

### 3. Conditional Logic
```python
# Validate data
is_valid_email = lambda email: "@" in email and "." in email
emails = ["user@example.com", "invalid.email", "test@domain.co.uk"]
valid = list(filter(is_valid_email, emails))
print(valid)  # Output: ['user@example.com', 'test@domain.co.uk']
```

### 4. Quick Callbacks
```python
# Event handling with lambda
def process_list(items, callback):
    return [callback(item) for item in items]

# Use lambda as callback
result = process_list([1, 2, 3], lambda x: x ** 2)
print(result)  # Output: [1, 4, 9]
```

### 5. Dictionary Operations
```python
data = {"a": 1, "b": 2, "c": 3}

# Double all values
doubled = {k: map_func(v) for k, v in data.items()}
# Using lambda in comprehension with map (indirectly)

# Get max key by value
max_key = max(data.keys(), key=lambda k: data[k])
print(max_key)  # Output: c
```

---

## Best Practices

### ✅ DO:
```python
# Use lambda for simple, one-line operations
squared = list(map(lambda x: x ** 2, [1, 2, 3, 4]))

# Use lambda for callbacks
sorted_data = sorted(data, key=lambda x: x["age"])

# Use lambda with built-in functions
filtered = list(filter(lambda x: x > 5, numbers))
```

### ❌ DON'T:
```python
# Don't use lambda for complex logic
# BAD
bad = lambda x: x ** 2 if x > 0 else (-x) ** 2 if x < 0 else 0

# GOOD - Use regular function instead
def complex_logic(x):
    if x > 0:
        return x ** 2
    elif x < 0:
        return (-x) ** 2
    else:
        return 0

# Don't use lambda if you need to reuse it many times
# Use a regular function instead for clarity

# Don't abuse lambda - keep it simple
# BAD: Multiple nested lambdas
func = lambda x: list(map(lambda y: filter(lambda z: z > y, [1, 2, 3]), x))

# GOOD: Use regular functions or comprehensions
```

### Guidelines
1. **Use lambdas for simple operations only**
2. **Keep lambdas to one line**
3. **Use lambdas with `map()`, `filter()`, `sorted()` and similar**
4. **Use regular functions for complex logic**
5. **Prioritize readability over brevity**
6. **Use descriptive variable names when assigning lambdas**

---

## Summary

| Aspect | Lambda | Regular Function |
|--------|--------|------------------|
| Declaration | `lambda args: expr` | `def name(args): return expr` |
| Parameters | Yes | Yes |
| Multiple statements | No | Yes |
| Naming | Anonymous | Named |
| Return | Implicit | Explicit |
| Use cases | Simple, throwaway | Complex, reusable |
| Readability | High for simple ops | Better for complex logic |

Lambda expressions are powerful tools for functional programming in Python, making code more concise and expressive when used appropriately!
