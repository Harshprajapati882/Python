# Python RegEx Examples
import re

# --- 1. Basic Matching with re.search() ---
print("--- 1. Basic Matching ---")
text = "hello world"
# Search for the pattern 'world' in the text
match = re.search(r"world", text)
if match:
    print(f"Found a match: '{match.group()}'") # .group() returns the matched string
    print(f"Match found at index: {match.start()} to {match.end()}")
else:
    print("No match found.")

# --- 2. Metacharacters ---
print("\n--- 2. Metacharacters ---")
text = "The rain in Spain falls mainly in the plain."

# `^` - Starts with
if re.search(r"^The", text):
    print("Text starts with 'The'")

# `$` - Ends with
if re.search(r"plain\.$", text):
    print("Text ends with 'plain.'")

# `.` - Any character
# Finds 'pl' followed by any character and then 'in'
matches = re.findall(r"pl.in", text)
print(f"Found '.': {matches}")

# `*` - Zero or more occurrences
# Finds 'a' followed by zero or more 'i's
matches = re.findall(r"ai*", text)
print(f"Found '*': {matches}")

# `+` - One or more occurrences
# Finds 'a' followed by one or more 'i's
matches = re.findall(r"ai+", text)
print(f"Found '+': {matches}")

# `?` - Zero or one occurrence
# Finds 'a' followed by zero or one 'i'
matches = re.findall(r"ai?", text)
print(f"Found '?': {matches}")


# `{}` - Specific number of occurrences
# Finds sequences of exactly 2 'l's
matches = re.findall(r"l{2}", text)
print(f"Found '{{}}': {matches}")

# `|` - Either or
# Finds either 'falls' or 'stays'
matches = re.findall(r"falls|stays", text)
print(f"Found '|': {matches}")

# `[]` - A set of characters
# Finds any character in the set: 'a', 'i', or 'n'
matches = re.findall(r"[ain]", text)
print(f"Found '[]': {len(matches)} occurrences of 'a', 'i', or 'n'")

# `()` - Grouping
# Find 'ain' in 'Spain' or 'plain'
matches = re.findall(r"(Sp|pl)ain", text)
print(f"Found '()': {matches}")


# --- 3. Special Sequences ---
print("\n--- 3. Special Sequences ---")
text = "My phone number is 123-456-7890. Call me!"

# `\d` - Matches digits
digits = re.findall(r"\d", text)
print(f"Digits (\\d): {digits}")

# `\D` - Matches non-digits
non_digits = re.findall(r"\D", text)
print(f"Non-Digits (\\D): {''.join(non_digits).strip()}")

# `\s` - Matches whitespace
whitespace = re.findall(r"\s", text)
print(f"Whitespace (\\s): {len(whitespace)} occurrences")

# `\w` - Matches word characters (letters, numbers, underscore)
word_chars = re.findall(r"\w", text)
print(f"Word Chars (\\w): {''.join(word_chars)}")

# `\b` - Word boundary
# Find 'Call' as a whole word
boundary_match = re.search(r"\bCall\b", text)
if boundary_match:
    print(f"Word Boundary (\\b): Found '{boundary_match.group()}'")


# --- 4. Core `re` Functions ---
print("\n--- 4. Core `re` Functions ---")

# `re.match()` - Matches only at the beginning of the string
match_obj = re.match(r"My", text)
if match_obj:
    print(f"re.match(): Found '{match_obj.group()}' at the start.")
else:
    print("re.match(): No match at the start.")

# `re.findall()` - Finds all non-overlapping matches
numbers = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print(f"re.findall(): Phone number found: {numbers}")

# `re.split()` - Splits the string by the pattern
parts = re.split(r"-", text)
print(f"re.split(): {parts}")

# `re.sub()` - Replaces matches with a string
censored_text = re.sub(r"\d", "*", text)
print(f"re.sub(): {censored_text}")

# --- 5. `re.compile()` for Efficiency ---
print("\n--- 5. `re.compile()` ---")
# Compile a pattern for repeated use
phone_pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
text1 = "My number is 555-123-4567."
text2 = "His number is 555-987-6543."

print(f"Compiled pattern on text1: {phone_pattern.findall(text1)}")
print(f"Compiled pattern on text2: {phone_pattern.findall(text2)}")


# --- 6. RegEx Flags ---
print("\n--- 6. RegEx Flags ---")
text = "Python is fun.\npython is powerful."

# `re.IGNORECASE`
matches_icase = re.findall(r"python", text, re.IGNORECASE)
print(f"re.IGNORECASE: {matches_icase}")

# `re.MULTILINE`
# The `^` normally matches only the beginning of the string.
# With MULTILINE, it matches the beginning of each line.
matches_multiline = re.findall(r"^python", text, re.MULTILINE | re.IGNORECASE)
print(f"re.MULTILINE: {matches_multiline}")

# `re.DOTALL`
# The `.` normally does not match a newline.
# With DOTALL, it does.
text_with_newline = "fun.\npython"
match_dotall = re.search(r"fun.python", text_with_newline, re.DOTALL)
if match_dotall:
    print("re.DOTALL: `.` matched a newline character.")

# --- 7. Practical Example: Email Validation ---
print("\n--- 7. Email Validation Example ---")

def is_valid_email(email):
    # A common (but not perfect) email validation pattern
    pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    return pattern.match(email)

emails = ["test@example.com", "invalid-email", "another.test@domain.co.uk", "user@.com"]
for email in emails:
    if is_valid_email(email):
        print(f"'{email}' is a valid email.")
    else:
        print(f"'{email}' is NOT a valid email.")
