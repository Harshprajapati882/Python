# Regular Expressions (RegEx) in Python

Regular Expressions (or RegEx) are a powerful tool for matching patterns in text. In Python, the `re` module provides an interface to the regular expression engine.

---

## 1. Introduction to Regular Expressions

A Regular Expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. They are widely used for input validation, parsing, and web scraping.

---

## 2. The `re` Module

Python's `re` module provides full support for Perl-like regular expressions. To use it, you first need to import it:

```python
import re
```

---

## 3. Basic Patterns & Metacharacters

Metacharacters are characters with a special meaning:

| Metacharacter | Description                                          | Example         |
| :------------ | :--------------------------------------------------- | :-------------- |
| `.`           | Matches any character except a newline.              | `a.b` matches `acb` |
| `^`           | Matches the start of the string.                     | `^hello`        |
| `$`           | Matches the end of the string.                       | `world$`        |
| `*`           | Matches zero or more repetitions of the preceding character. | `a*`            |
| `+`           | Matches one or more repetitions of the preceding character.  | `a+`            |
| `?`           | Matches zero or one repetition of the preceding character.   | `a?`            |
| `[]`          | Defines a character set.                             | `[abc]`         |
| `[a-z]`       | Matches any lowercase letter.                        |                 |
| `[^abc]`      | Matches any character except a, b, or c.             |                 |
| `|`           | `OR` operator. Matches either of two patterns.       | `a|b`           |
| `()`          | Groups sub-patterns.                                 | `(a|b)c`        |
| `\`           | Escapes special characters.                          | `\.` matches `.`  |
| `{m}`         | Matches exactly `m` repetitions.                     | `a{2}`          |
| `{m,n}`       | Matches from `m` to `n` repetitions.                 | `a{2,4}`        |


---

## 4. Special Sequences

Special sequences are `\` followed by one of the characters below, and they have a special meaning:

| Sequence | Description                                     |
| :------- | :---------------------------------------------- |
| `\d`     | Matches any decimal digit; equivalent to `[0-9]`. |
| `\D`     | Matches any non-digit character.                |
| `\s`     | Matches any whitespace character.               |
| `\S`     | Matches any non-whitespace character.           |
| `\w`     | Matches any alphanumeric character (`[a-zA-Z0-9_]`). |
| `\W`     | Matches any non-alphanumeric character.         |
| `\b`     | Matches a word boundary.                        |
| `\A`     | Matches the beginning of the string.            |
| `\Z`     | Matches the end of the string.                  |

---

## 5. Core `re` Functions

The `re` module offers a set of functions to work with regular expressions.

### `re.match(pattern, string)`
Matches the pattern only at the **beginning** of the string.

### `re.search(pattern, string)`
Scans through the string, looking for the **first** location where the pattern produces a match.

### `re.findall(pattern, string)`
Finds **all** substrings where the pattern matches and returns them as a list of strings.

### `re.split(pattern, string)`
Splits the string by the occurrences of the pattern.

### `re.sub(pattern, repl, string)`
Replaces one or many matches with a string or the result of a function.

### `re.compile(pattern)`
Compiles a regular expression pattern into a regular expression object, which can be used for matching using its `match()`, `search()`, and other methods. This is efficient if you are using the same expression multiple times.

---

## 6. The Match Object

The `search()` and `match()` functions return a `Match` object when a match is found. This object contains information about the match.

| Method      | Description                                       |
| :---------- | :------------------------------------------------ |
| `group()`   | Returns the part of the string where the match was found. |
| `span()`    | Returns a tuple containing the start and end positions of the match. |
| `start()`   | Returns the starting position of the match.      |
| `end()`     | Returns the ending position of the match.        |

---

## 7. RegEx Flags

Flags (or modifiers) can change the behavior of the regular expression engine.

| Flag             | Short | Description                                                   |
| :--------------- | :---- | :------------------------------------------------------------ |
| `re.IGNORECASE`  | `re.I`| Makes the pattern case-insensitive.                           |
| `re.MULTILINE`   | `re.M`| `^` and `$` match the start/end of each line, not just the string. |
| `re.DOTALL`      | `re.S`| Makes `.` match any character, including newlines.            |

---

## 8. Common Use Cases & Examples

### Example 1: Email Validation
A common (though simplified) pattern to validate an email address.

**Pattern:** `r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"`

### Example 2: Extracting Phone Numbers
Find all phone numbers in a standard US format from a text.

**Pattern:** `r"\d{3}-\d{3}-\d{4}"`

### Example 3: Web Scraping - Finding Links
Extract all `<a>` tag `href` attributes from an HTML string.

**Pattern:** `r'href="([^"]*)"'`
