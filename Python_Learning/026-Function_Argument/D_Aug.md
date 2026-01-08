# Function Arguments in Python

This document covers various aspects of function arguments in Python, including different types of arguments, scope, and other related concepts.

## 1. Function Arguments

Function arguments are the values passed to a function when it is called. These arguments are used within the function to perform its operations.

## 2. Positional Arguments

Positional arguments are the most common type of arguments. They are passed to a function in a specific order, and their values are assigned to the function's parameters based on their position.

```python
def greet(name, message):
    print(f"Hello {name}, {message}")

greet("Alice", "How are you?")
```

## 3. Keyword Arguments

Keyword arguments are passed to a function by specifying the parameter name followed by the value. This allows you to pass arguments in any order.

```python
def greet(name, message):
    print(f"Hello {name}, {message}")

greet(message="How are you?", name="Bob")
```

## 4. Default Arguments

Default arguments are parameters that have a default value assigned to them in the function definition. If a value is not provided for a default argument when the function is called, the default value is used.

```python
def greet(name, message="Good morning!"):
    print(f"Hello {name}, {message}")

greet("Charlie")
greet("David", "Good evening!")
```

## 5. Positional-Only Arguments

Positional-only arguments can only be passed by position, not by keyword. They are defined by placing a `/` after the positional-only parameters in the function definition.

```python
def user_info(name, age, /):
    print(f"Name: {name}, Age: {age}")

user_info("Eve", 30)
# This would raise a TypeError:
# user_info(name="Eve", age=30)
```

## 6. Keyword-Only Arguments

Keyword-only arguments can only be passed by keyword, not by position. They are defined by placing a `*` before the keyword-only parameters in the function definition.

```python
def user_info(*, name, age):
    print(f"Name: {name}, Age: {age}")

user_info(name="Frank", age=25)
# This would raise a TypeError:
# user_info("Frank", 25)
```

You can combine positional-only, regular, and keyword-only arguments:

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
   Positional-only  Positional or keyword  Keyword-only
```

## 7. Arbitrary Arguments

### Arbitrary Positional Arguments (`*args`)

If you don't know in advance how many positional arguments will be passed to your function, you can use `*args`. This collects all the extra positional arguments into a tuple.

```python
def sum_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_all(1, 2, 3, 4))
```

### Arbitrary Keyword Arguments (`**kwargs`)

If you don't know in advance how many keyword arguments will be passed to your function, you can use `**kwargs`. This collects all the extra keyword arguments into a dictionary.

```python
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Grace", city="New York", occupation="Developer")
```

## 8. Packing and Unpacking

### Packing

Packing is the process of collecting multiple values into a single variable. This is what happens with `*args` and `**kwargs`.

### Unpacking

Unpacking is the process of extracting values from a sequence (like a list or tuple) or a dictionary and passing them as separate arguments to a function.

- **Unpacking a list or tuple with `*`**:
```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))
```

- **Unpacking a dictionary with `**`**:
```python
def greet(name, message):
    print(f"Hello {name}, {message}")

details = {"name": "Heidi", "message": "Good to see you."}
greet(**details)
```

## 9. Variable Scope

Variable scope determines the accessibility of a variable.

- **Local Scope**: A variable created inside a function belongs to the local scope of that function and can only be used inside that function.
- **Global Scope**: A variable created in the main body of the Python code is a global variable and belongs to the global scope. Global variables are available from within any scope, global and local.
- **`global` keyword**: If you need to modify a global variable from within a function, you must use the `global` keyword.
- **`nonlocal` keyword**: Used in nested functions to refer to a variable in the nearest enclosing (but non-global) scope.

## 10. Function Annotations

Function annotations are a way of associating arbitrary metadata with function parameters and return values. They are stored in the `__annotations__` attribute of the function.

```python
def greet(name: str, message: str = "Hi") -> str:
    return f"{message}, {name}!"
```
Annotations don't enforce type checking; they are for documentation or for use by libraries and tools.

## 11. Built-in Functions

Python has a number of functions that are always available, called built-in functions. Examples include `print()`, `len()`, `sum()`, `max()`, `min()`, `type()`, `int()`, `str()`, etc. You can use these functions without importing any module.
