# Python String Methods Examples

# Case Conversion
my_string = "Hello, World! This is Python."
print(f"Original: '{my_string}'")
print(f"upper(): '{my_string.upper()}'")
print(f"lower(): '{my_string.lower()}'")
print(f"capitalize(): '{my_string.capitalize()}'")
print(f"title(): '{my_string.title()}'")
print(f"swapcase(): '{my_string.swapcase()}'")
print("-" * 20)

# Whitespace Removal
ws_string = "   Some whitespace   "
print(f"Original: '{ws_string}'")
print(f"strip(): '{ws_string.strip()}'")
print(f"lstrip(): '{ws_string.lstrip()}'")
print(f"rstrip(): '{ws_string.rstrip()}'")
print("-" * 20)

# Searching and Finding
sentence = "The quick brown fox jumps over the lazy dog."
print(f"Original: '{sentence}'")
print(f"find('fox'): {sentence.find('fox')}")
print(f"find('cat'): {sentence.find('cat')}") # Not found
print(f"rfind('the'): {sentence.rfind('the')}")
print(f"count('the'): {sentence.lower().count('the')}")
print(f"startswith('The'): {sentence.startswith('The')}")
print(f"endswith('dog.'): {sentence.endswith('dog.')}")
try:
    sentence.index('cat')
except ValueError as e:
    print(f"index('cat') raised a ValueError: {e}")
print("-" * 20)


# Splitting and Joining
csv = "apple,banana,cherry"
fruits = csv.split(',')
print(f"split(','): {fruits}")

words = "this is a sentence"
word_list = words.split()
print(f"split(): {word_list}")

delimiter = " "
joined_string = delimiter.join(word_list)
print(f"join(): '{joined_string}'")
print("-" * 20)


# Character Type Checking
print(f"'Python'.isalpha(): {'Python'.isalpha()}")
print(f"'Python3'.isalpha(): {'Python3'.isalpha()}")
print(f"'12345'.isdigit(): {'12345'.isdigit()}")
print(f"'Python3'.isalnum(): {'Python3'.isalnum()}")
print(f"'   '.isspace(): {'   '.isspace()}")
print(f"'UPPER'.isupper(): {'UPPER'.isupper()}")
print(f"'lower'.islower(): {'lower'.islower()}")
print(f"'Title Case'.istitle(): {'Title Case'.istitle()}")
print("-" * 20)


# Replacement
text = "I like apples, apples are my favorite fruit."
new_text = text.replace("apples", "oranges")
print(f"Original: '{text}'")
print(f"replace('apples', 'oranges'): '{new_text}'")

# Replace with a limit
limited_replace = text.replace("apples", "bananas", 1)
print(f"replace with limit 1: '{limited_replace}'")
print("-" * 20)
