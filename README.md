README.md
=========

Additional setup
----------------

Python environment setup
------------------------

- **Make install:** run `make install` to create a virtual environment in `.venv` and install `requirements.txt` if present. For Windows, run `make install-windows`.
- **Unix script:** `env_setup.sh` — creates `.venv` and installs requirements. Run: `bash env_setup.sh`.
- **Windows scripts:** `env_setup.bat` and `env_setup.ps1` — run the appropriate script in Command Prompt or PowerShell.
- **VS Code on Windows:** See [WINDOWS_VSCODE_SETUP.md](WINDOWS_VSCODE_SETUP.md) for step-by-step instructions to configure the interpreter and workspace settings.
# Python
Learning Python 
# Python Learning — Consolidated Notes

## Table of contents
- Introduction
- Python Basics — Overview
- OOP in Python
- Complete Syllabus
- Windows VS Code setup
- Pips & Modules
- Python Data Structures
- Comments, Escape Sequences, Print, Input, and Variables

---

## Introduction to Python

**Python** is a high-level, interpreted, general-purpose programming language known for its readable syntax and strong community. Created by Guido van Rossum and first released in 1991, Python emphasizes code readability and developer productivity, making it a great choice for beginners and professionals alike.

---

## Key features

- Readable & concise syntax — code is easy to understand and maintain
- Interpreted & cross-platform — runs on Windows, macOS, Linux
- Dynamic typing and automatic memory management
- Batteries-included standard library for many common tasks
- Vast ecosystem of third-party packages (PyPI) for web, data, ML, automation

## Where Python is used

- Web development (Django, Flask)
- Data science & machine learning (NumPy, pandas, scikit-learn, TensorFlow)
- Scripting & automation, DevOps
- Education, prototyping, and scientific computing

## Basic syntax — quick example

```python
# hello.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
```

Run the example with:

```bash
python hello.py
```

---

## Python Basics — Overview

This file summarizes core Python fundamentals and study checkpoints.

- Syntax & style: indentation, PEP8 basics
- Data types: `int`, `float`, `str`, `bool`, `None`
- Variables & naming conventions
- Operators: arithmetic, comparison, logical, membership, identity
- Control structures: `if`/`else`, `for`, `while`, `break`, `continue`
- Functions: definition, return, arguments, `*args`/`**kwargs`, lambdas
- Data structures: lists, tuples, sets, dicts — methods and use-cases
- Comprehensions: list/dict/set comprehensions and generator expressions
- Modules & packages: `import`, `from ... import`, package layout
- File I/O: reading/writing, CSV basics, `with` keyword
- Exceptions: `try`/`except`, creating custom exceptions
- Iterators & generators: iterator protocol, `yield`
- Useful stdlib modules: `os`, `sys`, `pathlib`, `datetime`, `json`, `re`, `collections`

Exercises:
- Print and format strings, f-strings
- Implement simple functions (factorial, fibonacci)
- Manipulate lists and dictionaries
- Read/write a text file and parse lines

---

## OOP in Python — Methods, Patterns, and Examples

Core concepts:
- Classes and instances
- Encapsulation (private/protected conventions)
- Inheritance (single, multiple) and MRO
- Polymorphism and duck typing
- Abstraction and interfaces (`abc`)

Important method types and special methods:
- `__init__(self, ...)` — constructor
- `__new__(cls, ...)` — instance creation
- `__repr__(self)` / `__str__(self)` — readable representations
- Comparison: `__eq__`, `__lt__`, `__le__`, etc.
- Numeric ops: `__add__`, `__sub__`, `__mul__`, ...
- Container protocol: `__len__`, `__contains__`, `__iter__`, `__getitem__`, `__setitem__`
- Context manager: `__enter__`, `__exit__`
- Callable objects: `__call__`

Decorators and attribute helpers:
- `@classmethod` — method receives class `cls`
- `@staticmethod` — no implicit first argument
- `@property` — attribute access via methods
- Descriptors for advanced attribute control

Design guidance:
- Prefer composition over inheritance for many cases
- Keep methods small and single-responsibility
- Use ABCs for clear interfaces when needed

Example usage patterns and exercises:
- Implement a `Person` / `Employee` hierarchy with properties
- Create a custom container implementing iteration and indexing
- Write a context-manager class for resource handling

---

## Python Learning - Complete Syllabus

This syllabus covers Python basics through core OOP topics and practical examples. Use it as a checklist while studying.

1. Getting Started
   - Installation, interpreters, REPL, virtual environments
   - Running scripts, shebang, basic tooling

2. Python Basics
   - Syntax, comments, indentation
   - Data types: numbers, strings, booleans, None
   - Variables and assignments
   - Operators: arithmetic, comparison, logical, bitwise

3. Control Flow
   - `if`, `elif`, `else`
   - Loops: `for`, `while`, `break`, `continue`, `else` on loops
   - Comprehensions: list, dict, set, generator

4. Functions
   - Defining functions, return values
   - Positional, keyword, default args
   - `*args`, `**kwargs`
   - Lambda, higher-order functions, closures
   - Decorators

5. Data Structures
   - Lists, tuples, sets, dictionaries
   - Common methods, slicing, iteration
   - Collections module basics (`deque`, `Counter`, `defaultdict`, `namedtuple`)

6. Modules & Packages
   - Importing, package structure, `__init__.py`
   - `pip`, `venv`, `requirements.txt`

7. File I/O
   - `open()`, reading/writing files, context managers

8. Error Handling & Testing
   - Exceptions (`try`, `except`, `finally`, `else`)
   - Creating custom exceptions
   - Unit testing with `unittest`/`pytest`

9. Iterators & Generators
   - Iterator protocol, `__iter__`, `__next__`
   - Generators with `yield`, generator expressions

10. Concurrency & Async
   - Threads vs processes
   - `asyncio` basics, `async`/`await`

11. Standard Library Highlights
   - `os`, `sys`, `pathlib`, `datetime`, `json`, `re`, `logging`, `subprocess`

12. Advanced Topics (overview)
   - Context managers, descriptors, metaclasses
   - Packaging and distribution
   - Type hints and `mypy`

13. OOP (Object-Oriented Programming)
   - Classes and instances
   - Attributes and methods
   - Encapsulation, inheritance, polymorphism, abstraction
   - Special / magic methods (dunder methods)
   - `@classmethod`, `@staticmethod`, `@property`
   - Multiple inheritance and MRO
   - Abstract Base Classes (`abc`)

14. Practical Projects & Exercises
   - CLI tools, small web scrapers, simple web app, data parsing
   - Project structure, tests, CI basics

Suggested study flow: start with sections 1–5, then 6–9, follow with OOP (13), and finish with advanced topics and projects.

---

## Windows — VS Code Python setup

1. Install Python for Windows from https://python.org and check "Add Python to PATH".
2. Install Visual Studio Code: https://code.visualstudio.com/
3. In VS Code, install the **Python** extension (ms-python.python).
4. Open this repository folder in VS Code.
5. Create the virtual environment:
   - Run `env_setup.ps1` in PowerShell or `env_setup.bat` in Command Prompt.
6. Select interpreter: press `Ctrl+Shift+P` → `Python: Select Interpreter` → choose `.venv\Scripts\python.exe`.
7. Recommended (workspace) settings: create `.vscode/settings.json` with the recommended python path and activation.
8. If using PowerShell, you may need to allow running the activation script: run PowerShell as Admin and set `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.

See `env_setup.ps1` and `env_setup.bat` for automated steps.

---

## Pips & Modules — Notes and Examples

This document covers the essential topics for working with Python packages and modules and using `pip` and virtual environments. It includes commands, concepts, and runnable examples in `Pips&Modules.py` and the example package `mypkg`.

Topics to Learn

- `pip` basics: install, uninstall, list, show, search
- Virtual environments: `venv`, `virtualenv`, `pipenv`, `poetry`
- Requirements management: `requirements.txt`, `pip freeze` and `pip install -r`
- Creating modules & packages: `.py` modules, `__init__.py`, package structure, relative vs absolute imports
- Editable installs & development workflows: `pip install -e .`, `pyproject.toml`, `setup.cfg`
- Publishing: building wheels, `twine upload` (high level)
- Dependency tools: `pipx`, `venv`, `pip-tools`, `poetry` basics
- Security & reproducibility: pinning versions, hashes, virtual env per-project

Common pip & venv Commands (examples included in original notes)

See `Pips&Modules.py` and `mypkg` in the repository for runnable examples.

---

## Python Data Structures — Notes

Built-in structures

- List (`list`): ordered, mutable sequence. Good for indexed access and ordered collections.
  - Common ops: append, extend, insert, pop, remove, slicing, iteration.
  - Complexity: indexing O(1), append amortized O(1), insert/delete O(n).

- Tuple (`tuple`): ordered, immutable sequence. Use for fixed collections and keys in dicts.
  - Common ops: indexing, unpacking, iteration.
  - Complexity: similar to `list` for read access, but immutable.

- Set (`set`) and `frozenset`: unordered collections of unique elements.
  - Common ops: add, remove, membership test, set operations (union, intersection, difference).
  - Complexity: average O(1) for membership/add/remove.

- Dictionary (`dict`): mapping of keys to values. Ordered (insertion order) since Python 3.7.
  - Common ops: get, set, pop, keys/values/items, iteration.
  - Complexity: average O(1) for lookup/insert/delete.

- String (`str`): immutable sequence of Unicode characters. Supports slicing, formatting.

- Bytes/Bytearray: immutable/mutable byte sequences for binary data.

- Range (`range`): efficient immutable sequence of integers commonly used in loops.

Collections module (specialized structures)

- `deque`: double-ended queue for fast appends/pops from both ends (O(1)).
- `defaultdict`: dict subclass that provides default values for missing keys.
- `Counter`: multiset for counting hashable items.
- `namedtuple`: lightweight tuple with named fields.
- `OrderedDict`: (mostly historical) preserves insertion order — built-in dict now does this.

Array & heap utilities: `array.array`, `heapq`, `bisect`.

Key topics to learn and exercises are included in the original notes.

---

## Comments, Escape Sequences, Print, Input, and Variables — Notes

Comments

- Single-line comment: start with `#`.
- Multi-line / docstring style: use triple quotes `""" ... """` (commonly used for docstrings).

Escape sequences

- `\n` newline
- `\t` tab
- `\\` backslash
- `\'` single quote and `\"` double quote
- Unicode escapes: `\u2764` or `\U0001F600`
- Raw strings: prefix with `r` to ignore escapes (useful for regex and Windows paths).

print function

- In Python 3 `print()` is a function with `sep`, `end`, `file`, and `flush` options.

User input

- Use `input(prompt)` to read a line of text (returns `str`). Convert types carefully and handle `ValueError` and `EOFError`.

Variables and Types

- Basic built-in types: `int`, `float`, `str`, `bool`, `NoneType`.
- Use `type()` and `isinstance()` to inspect values.

Exercises and examples are in the original `All.py` and notes.

---

*This consolidated file was generated from the repository's note files in `Python_Learning/`.*
