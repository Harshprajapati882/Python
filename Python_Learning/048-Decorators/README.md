# Python Decorators - Function Decorators

## 📚 Overview

This section covers **Python Decorators**, a powerful feature that allows you to modify or enhance functions without changing their source code. Decorators are a fundamental concept in Python for writing clean, reusable, and maintainable code.

## 📁 Files in This Directory

- **Decorators.md** - Comprehensive notes and theory on decorators
- **Decorators.py** - 15 practical code examples with detailed comments
- **README.md** - This file

## 🎯 Topics Covered

### 1. **Basic Function Decorators**
   - Understanding decorator pattern
   - Simple decorator structure
   - Using @decorator syntax

### 2. **Decorators with Arguments**
   - Handling *args and **kwargs
   - Making decorators flexible
   - Supporting any function signature

### 3. **Function Metadata Preservation**
   - Using @functools.wraps
   - Preserving __name__ and __doc__
   - Importance for debugging

### 4. **Decorators with Parameters**
   - Creating decorators that accept parameters
   - Multi-level nesting
   - Practical examples like @repeat and @retry

### 5. **Chaining Decorators**
   - Applying multiple decorators
   - Execution order (bottom-to-top)
   - Combining decorator effects

### 6. **Practical Use Cases**
   - **Logging Decorator** - Track function calls
   - **Timing Decorator** - Measure performance
   - **Validation Decorator** - Check arguments
   - **Caching Decorator** - Memoization
   - **Authorization Decorator** - Permission checks
   - **Retry Decorator** - Handle failures

## 🔑 Key Concepts

### First-Class Functions
```python
# Functions can be assigned to variables
my_func = some_function

# Functions can be passed as arguments
run_function(some_function)

# Functions can be returned
return some_function
```

### Higher-Order Functions
Functions that take other functions as arguments or return functions.

### Closures
Inner functions with access to variables from outer scope.

## 💡 Basic Decorator Pattern

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Code BEFORE function
        result = func(*args, **kwargs)
        # Code AFTER function
        return result
    return wrapper

@decorator
def my_function():
    pass
```

## 📊 Decorator with Parameters Pattern

```python
def decorator_with_params(param1, param2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Use param1, param2 here
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_params("value1", "value2")
def my_function():
    pass
```

## 🎨 Common Use Cases

| Use Case | Example | Purpose |
|----------|---------|---------|
| **Logging** | Track all function calls | Debugging & monitoring |
| **Timing** | Measure execution time | Performance analysis |
| **Caching** | Store results | Optimization |
| **Validation** | Check inputs | Error prevention |
| **Authorization** | Check permissions | Security |
| **Retry** | Retry on failure | Reliability |
| **Rate Limiting** | Control frequency | Resource management |

## ✅ Best Practices

1. **Always use @wraps** from functools to preserve metadata
2. **Use *args, **kwargs** for maximum flexibility
3. **Keep logic simple** - decorators should be focused
4. **Document well** - include docstrings
5. **Remember order** - decorators applied bottom-to-top when chained
6. **Test thoroughly** - decorators affect function behavior

## ⚡ Quick Reference

### Simple Decorator
```python
@wraps(func)
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
```

### Decorator with Parameters
```python
def my_decorator(param):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Chaining Decorators
```python
@decorator2
@decorator1
def function():
    pass
# Order: decorator1 applied first, then decorator2
```

## 🚀 Running the Examples

```bash
# Navigate to the directory
cd Python_Learning/048-Decorators/

# Run the code examples
python Decorators.py
```

## 📖 Example Output

The code demonstrates 15 practical examples:
1. Basic decorator
2. Decorator without @ syntax
3. Decorator with positional arguments
4. Decorator with keyword arguments
5. Metadata preservation comparison
6. Logging decorator
7. Timing decorator
8. Decorator with parameters (@repeat)
9. Retry decorator
10. Chaining decorators (different orders)
11. Validation decorator
12. Caching/Memoization decorator
13. Authorization decorator
14. Summary and best practices

## 🎓 Learning Path

1. Start with **Decorators.md** for theory
2. Review code examples 1-2 for basic understanding
3. Study examples 3-6 for practical techniques
4. Explore examples 7-15 for real-world applications
5. Try writing your own decorators

## 💡 Tips

- Decorators are applied when function is **defined**, not when called
- Use a debugger to trace decorator execution order
- Consider using existing decorators from libraries (e.g., `functools`)
- Decorators work with functions, methods, and classes

## 🔗 Related Topics

- Functions
- Closures
- Lambda Functions
- Higher-Order Functions
- functools module

## ❓ Questions to Ask Yourself

1. What does `@wraps` do and why is it important?
2. How do decorators with parameters work?
3. What is the execution order when decorators are chained?
4. How can decorators be used for logging, timing, and caching?
5. What are the advantages of using decorators?

---

**Last Updated**: January 2026  
**Python Version**: 3.7+
