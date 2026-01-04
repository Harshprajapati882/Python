# Basic Python Syntax — Notes

This file summarizes basic Python syntax elements: comments, escape sequences, and variables.

## Comments
- Single-line comment: start with `#`.
- Multi-line / docstring style: use triple quotes `""" ... """` (commonly used for docstrings).

Examples:
```python
# This is a comment
"""This is a
multi-line string often used as a docstring."""
```

## Escape sequences
- `\n` newline
- `\t` tab
- `\\` backslash
- `\'` single quote and `\"` double quote
- Unicode escapes: `\u2764` or `\U0001F600`
- Raw strings: prefix with `r` to ignore escapes (useful for regex and Windows paths).

Examples:
```python
print("Line1\nLine2")
print(r"C:\temp\new")
```

## Variables and Types
- Basic built-in types: `int`, `float`, `str`, `bool`, `NoneType`.
- Collections: `list`, `tuple`, `dict`, `set`.
- Binary: `bytes`, `bytearray`, `memoryview`.
- Other: `complex`, functions, classes, modules.
- Check type: `type(x)`; check instance: `isinstance(x, int)`.

## Type Casting (Type Conversion)

Type casting is converting a value from one data type to another. In Python this can be done implicitly by the interpreter or explicitly by the programmer using built-in constructors (for example `int()`, `float()`, `str()`, `list()`).

**Implicit vs Explicit**

- **Implicit:** Python automatically converts between compatible types (for example `int` to `float` during arithmetic).
- **Explicit:** You call conversion functions like `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, `dict()`, `bytes()`, `bytearray()`, `complex()`.

**Common Conversions**

- **Number conversions:** `int()`, `float()`, `complex()` — convert between integer, floating-point, and complex numbers. Watch out for truncation when converting `float` to `int`.
- **Text and bytes:** `str()` and `bytes()` / `bytearray()` — encoding matters when converting from `str` to `bytes` (`encode()` / `decode()` or `bytes(s, encoding)`).
- **Boolean:** `bool()` — empty containers/zero/`None` are `False`, most other values are `True`.
- **Collections:** `list()`, `tuple()`, `set()`, `dict()` — convert between iterable container types. Converting to `dict()` requires key/value pairs or another mapping.

**Built-in Conversion Functions**

- `int(x, base=10)` — from numbers or numeric strings. `int('12.9')` raises `ValueError`.
- `float(x)` — from numeric strings or numbers.
- `str(x)` — universal text representation.
- `bool(x)` — truthiness conversion.
- `list(iterable)`, `tuple(iterable)`, `set(iterable)` — collection conversions.
- `dict(mapping_or_iterable)` — from mapping or pairs of two-item iterables.
- `bytes(s, encoding)` / `bytearray(s, encoding)` — convert text to raw bytes.
- `complex(real, imag=0)` or `complex(str)` — construct complex numbers.

**Pitfalls & Notes**

- Converting a `float` to `int` truncates toward zero (precision is lost).
- Passing non-numeric strings to `int()` or `float()` raises `ValueError`.
- `bool('False')` is `True` because non-empty strings are truthy.
- Converting between collections may change ordering (sets) or remove duplicates.
- `bytes()` from a `str` requires specifying encoding or using `encode()`.

## Exercises
1. Demonstrate escape sequences and raw strings with file paths and regex patterns.
2. Demonstrate type casting with different data types and handle potential errors.

## Further reading
- Official Python tutorial — Data types sections.