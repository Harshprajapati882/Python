# Python String Methods

Python strings have a rich set of built-in methods to perform common operations. Here are some of the most frequently used ones.

## Case Conversion

- `upper()`: Converts the string to uppercase.
- `lower()`: Converts the string to lowercase.
- `capitalize()`: Converts the first character to uppercase and the rest to lowercase.
- `title()`: Converts the first character of each word to uppercase.
- `swapcase()`: Swaps the case of all characters in the string.

## Whitespace Removal

- `strip()`: Removes leading and trailing whitespace.
- `lstrip()`: Removes leading whitespace.
- `rstrip()`: Removes trailing whitespace.

## Searching and Finding

- `find(substring)`: Returns the lowest index of the substring. Returns -1 if not found.
- `rfind(substring)`: Returns the highest index of the substring. Returns -1 if not found.
- `index(substring)`: Same as `find()`, but raises a `ValueError` if not found.
- `rindex(substring)`: Same as `rfind()`, but raises a `ValueError` if not found.
- `count(substring)`: Returns the number of non-overlapping occurrences of the substring.
- `startswith(prefix)`: Returns `True` if the string starts with the given prefix.
- `endswith(suffix)`: Returns `True` if the string ends with the given suffix.

## Splitting and Joining

- `split(separator)`: Splits the string into a list of substrings based on the separator. If no separator is specified, it splits by whitespace.
- `rsplit(separator)`: Splits the string from the right.
- `join(iterable)`: Joins the elements of an iterable into a single string, with the string as the separator.

## Character Type Checking

- `isalpha()`: Returns `True` if all characters are alphabetic.
- `isdigit()`: Returns `True` if all characters are digits.
- `isalnum()`: Returns `True` if all characters are alphanumeric.
- `isspace()`: Returns `True` if all characters are whitespace.
- `isupper()`: Returns `True` if all characters are uppercase.
- `islower()`: Returns `True` if all characters are lowercase.
- `istitle()`: Returns `True` if the string is in title case.

## Replacement

- `replace(old, new)`: Replaces all occurrences of the `old` substring with the `new` substring.
