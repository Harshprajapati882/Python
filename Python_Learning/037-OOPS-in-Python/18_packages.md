# Packages in Python

As you write more code, you'll want to organize it to avoid having one massive, unmanageable file. In Python, you can organize code using **modules** and **packages**.

## Modules

A **module** is simply a single Python file (`.py`) containing functions, classes, and variables. You can use the code from one module in another file by using the `import` statement.

```python
# file: my_module.py
def greet():
    print("Hello!")

# file: main.py
import my_module
my_module.greet()
```

## Packages

A **package** is a way of organizing related modules into a directory hierarchy. It's essentially a directory that contains a special file called `__init__.py`, along with other modules and potentially other sub-packages.

The `__init__.py` file can be empty, but its presence tells Python that the directory should be treated as a package. This allows you to use dot notation to import modules from the package.

### Example Package Structure

```
my_project/
|-- main.py
|-- my_app/
|   |-- __init__.py
|   |-- formatters.py
|   |-- utils.py
|   |--- ui/
|   |   |-- __init__.py
|   |   |-- buttons.py
|   |   |-- windows.py
```

In this structure:
*   `my_app` is a package.
*   `ui` is a sub-package of `my_app`.
*   `formatters.py`, `utils.py`, `buttons.py`, and `windows.py` are modules.

### Importing from Packages

You can import modules, classes, or functions from packages using dot notation.

```python
# In main.py

# Import the entire module
import my_app.formatters
my_app.formatters.some_function()

# Import a specific function from a module
from my_app.utils import another_function
another_function()

# Import from a sub-package
from my_app.ui.buttons import Button
my_button = Button()
```

## The `__init__.py` File

The `__init__.py` file has two main purposes:

1.  **Package Marker**: It marks the directory as a Python package.
2.  **Package Initialization**: The code in `__init__.py` is executed when the package or a module within it is imported. This can be useful for:
    *   Running initialization code for the package.
    *   Making it easier to import from the package by using the `__all__` variable or by importing sub-modules into the package's namespace.

For example, in `my_app/__init__.py` you could write:

```python
# my_app/__init__.py
from .formatters import some_function

print("my_app package is being initialized!")
```
Now, from `main.py`, you could import `some_function` directly from `my_app`:

```python
# main.py
from my_app import some_function
some_function()
```
This can make the import paths cleaner for the users of your package.
