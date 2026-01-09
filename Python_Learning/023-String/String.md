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

## Immutability and "Modifying" Strings

Strings are immutable. You cannot change a character in a string. However, you can create a new string by combining parts of the old string or by using methods that return a new string.

For example, to change a character, you can create a new string:
`new_string = "J" + my_string[1:]`

## String Formatting

### f-Strings (Formatted String Literals)

f-Strings provide a concise and convenient way to embed expressions inside string literals for formatting.

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

### `str.format()` Method

The `format()` method is a powerful and flexible way to format strings.

```python
name = "Bob"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {1} and I am {0} years old.".format(age, name)) # Using positional arguments
print("My name is {name} and I am {age} years old.".format(age=age, name=name)) # Using keyword arguments
```

### Old Style Formatting (`%` operator)

This is an older way of formatting strings, similar to `printf` in C.

```python
name = "Charlie"
age = 35
print("My name is %s and I am %d years old." % (name, age))
```

## Escape Characters

Escape characters are used to insert characters that are illegal in a string. An escape character is a backslash `\` followed by the character you want to insert.

| Escape Sequence | Description                  |
|-----------------|------------------------------|
| `\'`            | Single quote                 |
| `\"`            | Double quote                 |
| `\\`            | Backslash                    |
| `\n`            | New line                     |
| `\t`            | Tab                          |
| `\b`            | Backspace                    |


## Common String Methods

String methods perform operations on strings and return new strings. They do not modify the original string.

| Method           | Description                                                 |
|------------------|-------------------------------------------------------------|
| `upper()`        | Returns a new string in uppercase.                          |
| `lower()`        | Returns a new string in lowercase.                          |
| `strip()`        | Removes leading/trailing whitespace.                        |
| `lstrip()`       | Removes leading whitespace.                                 |
| `rstrip()`       | Removes trailing whitespace.                                |
| `replace(old, new)` | Replaces all occurrences of `old` with `new`.             |
| `split(sep)`     | Splits the string into a list of substrings at `sep`.       |
| `join(iterable)` | Joins elements of an iterable with the string as a separator. |
| `startswith(prefix)`| Returns `True` if the string starts with `prefix`.       |
| `endswith(suffix)`| Returns `True` if the string ends with `suffix`.          |
| `find(sub)`      | Returns the lowest index of `sub` or -1 if not found.       |
| `isdigit()`      | Returns `True` if all characters are digits.                |
| `isalpha()`      | Returns `True` if all characters are alphabetic.            |


## String Exercises

1.  **Reverse a String**: Write a program that takes a string and prints it in reverse.
2.  **Palindrome Check**: Write a program that checks if a string is a palindrome (reads the same forwards and backwards).
3.  **Count Vowels**: Write a program to count the number of vowels (a, e, i, o, u) in a given string.
4.  **Word Count**: Write a program to count the number of words in a sentence.
5.  **Title Case**: Write a program to convert a string into title case (the first letter of each word is capitalized).

---
