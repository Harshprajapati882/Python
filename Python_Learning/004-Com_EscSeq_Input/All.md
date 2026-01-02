
# Comments, Escape Sequences, Print, Input, and Variables — Notes

## Comments
- Single-line comment: start with `#`.
- Multi-line / docstring style: use triple quotes `""" ... """` (commonly used for docstrings).

Examples:
```
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
```
print("Line1\nLine2")
print(r"C:\temp\new")
```

## `print` statement / function
- In Python 3 `print()` is a function with useful parameters:
  - `sep` (separator between values), default `' '`.
  - `end` (what to print at the end), default `'\n'`.
  - `file` (where to write), default `sys.stdout`.
  - `flush` (force flush), default `False`.

Examples:
```
print('a', 'b', sep='-', end='\n')
print(f"Value: {x}")  # f-strings (Python 3.6+)
```

## User input
- Use `input(prompt)` to read a line of text from the user (returns `str`).
- When converting to other types, handle exceptions (`ValueError`).
- For non-interactive scripts, handle `EOFError` or provide defaults.

Example pattern:
```
try:
	value = input('Enter number: ')
	n = int(value)
except EOFError:
	# non-interactive environment - provide default
	n = 0
except ValueError:
	print('Please type an integer')
```

## Variables and Types
- Basic built-in types: `int`, `float`, `str`, `bool`, `NoneType`.
- Collections: `list`, `tuple`, `dict`, `set`.
- Binary: `bytes`, `bytearray`, `memoryview`.
- Other: `complex`, functions, classes, modules.
- Check type: `type(x)`; check instance: `isinstance(x, int)`.

### Type conversion
- `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `dict()`, `set()`

## Exercises
1. Write a small script that asks the user for two numbers and prints their sum (handle invalid input).
2. Demonstrate escape sequences and raw strings with file paths and regex patterns.
3. Print several values with a custom separator and without a trailing newline.

## Further reading
- Official Python tutorial — Input and Output, and Data types sections.

