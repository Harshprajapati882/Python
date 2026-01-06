# Python Strings

A string in Python is a sequence of characters. It is an immutable data type, which means that once a string is created, it cannot be changed.

## Creating Strings

You can create strings using single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`).

- **Single quotes:** `'Hello, World!'`
- **Double quotes:** `"Hello, World!"`
- **Triple quotes:** Used for multi-line strings.
  ```python
  '''This is a
  multi-line string.'''
  ```

## Accessing Characters (Indexing)

You can access individual characters of a string using indexing. Python uses 0-based indexing.

- `my_string[0]` returns the first character.
- `my_string[-1]` returns the last character.

## Slicing

Slicing allows you to get a substring from a string.

- `my_string[2:5]` extracts characters from index 2 to 4.
- `my_string[:5]` extracts characters from the beginning up to index 4.
- `my_string[2:]` extracts characters from index 2 to the end.

## String Concatenation and Repetition

- **Concatenation (+):** Combines two strings.
- **Repetition (*):** Repeats a string multiple times.

## Immutability

Strings are immutable. You cannot change a character in a string. However, you can create a new string by combining parts of the old string.

## Common Functions

- `len(my_string)`: Returns the length of the string.
- `str(object)`: Converts an object to its string representation.

## String Formatting

### f-Strings (Formatted String Literals)

f-Strings provide a concise and convenient way to embed expressions inside string literals for formatting.

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```
