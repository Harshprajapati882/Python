# Python Modules

A module in Python is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended.

## Why Use Modules?

- **Reusability:** Write code once and reuse it across multiple files.
- **Organization:** Break down large programs into smaller, manageable, and organized files.
- **Namespace:** Avoids naming conflicts by creating a separate namespace for your code.

## Creating a Module

To create a module, you just save the code you want in a file with a `.py` extension.

For example, let's create a file named `my_module.py` with a function:

```python
# my_module.py
def greet(name):
  """This function greets the person passed in as a parameter"""
  print(f"Hello, {name}!")
```

## Using a Module

You can use the `import` statement to use a module in another Python file.

### `import` statement

```python
# main.py
import my_module

my_module.greet("Alice")
```

When the interpreter encounters an `import` statement, it imports the module if it is present in the search path.

### `from...import` statement

You can import specific names from a module into the current namespace.

```python
# main.py
from my_module import greet

greet("Bob")
```

### `from...import *`

This imports all names (except those starting with an underscore `_`) from a module.

> **Note:** Using `from...import *` is generally discouraged as it can lead to code that is harder to read and can cause naming conflicts.

```python
# main.py
from my_module import *

greet("Charlie")
```

## Built-in Modules

Python comes with a standard library of modules. Some of the most commonly used ones are:

- `math`: for mathematical functions
- `datetime`: for working with dates and times
- `os`: for interacting with the operating system
- `sys`: for system-specific parameters and functions
- `json`: for working with JSON data

```python
import math

print(math.pi)
print(math.sqrt(16))
```

## The `__name__` attribute

Every module in Python has a special attribute called `__name__`. The value of `__name__` is set to `'__main__'` when you run your script directly. When you import a module, its `__name__` is set to its file name.

This is useful for writing code that should only run when the file is executed directly, not when it's imported.

```python
# my_module.py
def greet(name):
  print(f"Hello, {name}!")

if __name__ == "__main__":
  # This code will only run when my_module.py is executed directly
  print("This module is being run directly.")
  greet("World")
```

## Packages

Packages are a way of structuring Python's module namespace by using "dotted module names". A package is a directory of Python modules containing an additional `__init__.py` file (which can be empty). The `__init__.py` file tells Python that the directory should be treated as a package.

Example structure:

```
my_package/
├── __init__.py
├── module1.py
└── module2.py
```

You can then import modules from the package like this:

```python
import my_package.module1
from my_package.module2 import my_function
```
