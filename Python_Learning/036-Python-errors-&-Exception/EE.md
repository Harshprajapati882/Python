# Python Errors and Exceptions

This guide covers the essentials of handling errors and exceptions in Python.

---

## 1. Introduction to Errors

In Python, there are two main kinds of errors: syntax errors and exceptions.

### a. Syntax Errors

Also known as parsing errors, these are the most common kind of complaint you get while you are still learning Python. A syntax error occurs when the parser detects an incorrect statement.

**Example:**
```python
# Missing a colon
if a > b
    print("a is greater")
```

### b. Exceptions

Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called **exceptions** and are not unconditionally fatal.

**Example:**
```python
print(10 / 0)  # Raises a ZeroDivisionError
```

---

## 2. Built-in Exceptions

Python has a number of built-in exceptions that are raised when the interpreter encounters an error. Some common ones include:

- **`Exception`**: The root class for all built-in, non-system-exiting exceptions.
- **`SyntaxError`**: Raised by the parser when a syntax error is encountered.
- **`TypeError`**: Raised when an operation or function is applied to an object of inappropriate type.
- **`ValueError`**: Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
- **`IndexError`**: Raised when a sequence subscript is out of range.
- **`KeyError`**: Raised when a mapping (dictionary) key is not found.
- **`FileNotFoundError`**: Raised when a file or directory is requested but doesn’t exist.
- **`ZeroDivisionError`**: Raised when the second argument of a division or modulo operation is zero.
- **`AttributeError`**: Raised when an attribute reference or assignment fails.
- **`ImportError`**: Raised when the `import` statement has trouble trying to load a module.

---

## 3. Handling Exceptions: `try...except`

The `try` and `except` block in Python is used to catch and handle exceptions.

```python
try:
    # Code that might raise an exception
    x = 1 / 0
except ZeroDivisionError:
    # Code to execute if the specific exception occurs
    print("You can't divide by zero!")
```

- **Handling Multiple Exceptions**: You can handle multiple exceptions with a single `except` block.
  ```python
  try:
      # Some code
  except (TypeError, ValueError) as e:
      print(f"Caught a TypeError or ValueError: {e}")
  ```
- **Generic Exception Handler**: It's possible to catch any exception. This is generally discouraged unless you have a good reason.
  ```python
  try:
      # Some code
  except Exception as e:
      print(f"An unexpected error occurred: {e}")
  ```

---

## 4. The `else` and `finally` Clauses

### a. `try...except...else`

The `else` block is executed if the `try` clause does not raise an exception.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"Division successful, result is {result}")
```

### b. `try...finally`

The `finally` block is always executed before leaving the `try` statement, whether an exception has occurred or not. It's useful for cleanup actions, like closing a file.

```python
try:
    f = open("my_file.txt", "w")
    f.write("Hello")
finally:
    print("Closing file...")
    f.close()
```

---

## 5. Raising Exceptions

The `raise` statement allows the programmer to force a specified exception to occur.

```python
x = -1
if x < 0:
    raise ValueError("Number cannot be negative")
```

You can also re-raise an exception within an `except` block.

```python
try:
    # Some operation
except Exception as e:
    print("Logging the error...")
    raise # Re-raises the last exception
```

---

## 6. Exception Chaining

Exception chaining (`raise new_exception from original_exception`) is used to indicate that one exception was caused by another.

```python
def my_function():
    try:
        # Risky operation
    except SomeError as e:
        raise MyCustomError("Something went wrong in my_function") from e
```
This preserves the original stack trace.

---

## 7. Nested `try` Blocks

You can have `try...except` blocks inside other `try` blocks. If an exception occurs in the inner `try`, the inner `except` is checked first. If it doesn't handle it, the outer `except` blocks are checked.

---

## 8. User-Defined Exceptions

You can create your own exception classes by inheriting from the base `Exception` class. This is useful for creating more specific and descriptive errors in your application.

```python
class MyCustomError(Exception):
    """A custom exception for my application."""
    pass

try:
    raise MyCustomError("This is a custom error message.")
except MyCustomError as e:
    print(e)
```

---

## 9. Assertions

The `assert` statement is a debugging aid that tests a condition. If the condition is false, it raises an `AssertionError` with an optional message.

```python
age = 15
assert age >= 18, "User must be 18 or older"
```
**Note**: Assertions can be globally disabled with the `-O` and `-OO` command-line switches, so they are not a substitute for robust error handling.

---

## 10. Logging

The `logging` module provides a flexible framework for emitting log messages from Python programs. It's the standard way to log errors and other information.

```python
import logging

logging.basicConfig(level=logging.ERROR, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("Exception occurred", exc_info=True)
```
This logs the error to `app.log` with a full stack trace.

---

## 11. Warnings

The `warnings` module is used to issue warning messages. Warnings are typically issued in situations where it is useful to alert the user of some condition in a program, where that condition doesn't warrant raising an exception and terminating the program.

```python
import warnings

def deprecated_function():
    warnings.warn("This function is deprecated and will be removed in a future version.", DeprecationWarning)
    # ... function logic ...

deprecated_function()
```

---

## 12. Debugging with `pdb`

The Python Debugger (`pdb`) is an interactive debugger for Python programs. It allows you to set breakpoints, step through code, inspect variables, and more.

You can set a breakpoint in your code like this:
```python
import pdb

def my_function(x, y):
    result = x + y
    pdb.set_trace() # Execution will pause here
    return result

my_function(2, 3)
```

When you run this script, you'll be dropped into the `pdb` interactive console, where you can use commands like `n` (next line), `c` (continue), `p <variable>` (print variable), etc.
