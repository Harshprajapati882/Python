# Input and Output — Notes

This file summarizes Python's basic input and output operations.

## `print` statement / function
- In Python 3 `print()` is a function with useful parameters:
  - `sep` (separator between values), default `' '`.
  - `end` (what to print at the end), default `"\n"`.
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

## Exercises
1. Write a small script that asks the user for two numbers and prints their sum (handle invalid input).
2. Print several values with a custom separator and without a trailing newline.

## Further reading
- Official Python tutorial — Input and Output.

