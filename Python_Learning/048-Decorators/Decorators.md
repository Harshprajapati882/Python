# Python Decorators

## What is a Decorator?

A decorator is a function that **modifies or enhances another function or class without permanently changing its source code**. It's a function that takes another function as input, adds some functionality to it, and returns the modified function.

Decorators use the concept of **"wrapping"** - they wrap a function with additional code that runs before and/or after the original function.

---

## Key Concepts

### 1. **First-Class Functions**
In Python, functions are first-class objects, meaning:
- Functions can be assigned to variables
- Functions can be passed as arguments to other functions
- Functions can be returned from other functions

### 2. **Higher-Order Functions**
A function that takes another function as an argument or returns a function is called a higher-order function.

### 3. **Closures**
A closure is a function that has access to variables from its enclosing scope, even after the outer function has finished executing.

---

## Function Decorators

### Basic Syntax

```python
@decorator_name
def function():
    pass
```

This is equivalent to:
```python
def function():
    pass
function = decorator_name(function)
```

### Simple Function Decorator

A basic decorator is a function that:
1. Takes a function as an argument
2. Defines a wrapper function inside
3. Returns the wrapper function

**Structure:**
```python
def decorator(func):
    def wrapper():
        # Code before function
        func()
        # Code after function
    return wrapper
```

---

## Topics Covered

### 1. Basic Decorator
- Creating a simple decorator
- Understanding the decorator pattern
- Using the @decorator syntax

### 2. Decorators with Arguments
- Passing arguments to the decorated function
- Using *args and **kwargs
- Preserving function metadata with @wraps

### 3. Decorators with Parameters
- Creating decorators that accept parameters
- Multiple levels of nesting
- Examples: repeat decorator, timing decorator

### 4. Chaining Decorators
- Applying multiple decorators to one function
- Order of execution
- Combining decorator effects

### 5. Function Metadata Preservation
- Using @functools.wraps
- Why it matters for debugging and documentation
- Preserving __name__ and __doc__

### 6. Practical Use Cases
- Logging decorator
- Timing/Performance decorator
- Authentication decorator
- Caching/Memoization decorator
- Validation decorator

---

## Basic Function Decorator Flow

```
1. Define decorator function
2. Define wrapper function inside
3. Wrapper accepts same arguments as original function
4. Return wrapper function
5. Use @decorator above function definition
```

---

## Common Decorator Patterns

### Pattern 1: Simple Wrapper
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Before execution
        result = func(*args, **kwargs)
        # After execution
        return result
    return wrapper
```

### Pattern 2: Decorator with Parameters
```python
def decorator(param):
    def decorator_wrapper(func):
        def wrapper(*args, **kwargs):
            # Use param here
            return func(*args, **kwargs)
        return wrapper
    return decorator_wrapper
```

### Pattern 3: With Metadata Preservation
```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## Advantages of Decorators

1. **Code Reusability** - Apply same functionality to multiple functions
2. **Clean Code** - Separates concerns and keeps code DRY
3. **Maintainability** - Easy to add/remove functionality
4. **Readability** - Clear intent with @decorator syntax
5. **Modularity** - Decorator logic is independent from business logic
6. **Chainable** - Can apply multiple decorators

---

## When to Use Decorators

- **Logging** - Log function calls and results
- **Authentication** - Check if user is authenticated
- **Caching** - Store function results to avoid recomputation
- **Timing** - Measure execution time
- **Validation** - Validate input arguments
- **Rate Limiting** - Control function call frequency
- **Error Handling** - Catch and handle exceptions
- **Memoization** - Cache expensive computations

---

## Important Notes

1. Decorators are applied from **bottom to top** when chaining
2. The `@wraps` decorator from functools preserves metadata
3. Decorators can be applied to functions, methods, and classes
4. Arguments are captured in closures
5. Order matters when multiple decorators are applied

