# Python Strings Examples

print("--- Creating Strings ---")
single_quoted = 'Hello, World!'
double_quoted = "Hello, Python!"
triple_quoted = """This is a
multi-line string."""

print(single_quoted)
print(double_quoted)
print(triple_quoted)

print("\n--- String Indexing ---")
my_string = "Python"
print(f"First character: {my_string[0]}")
print(f"Last character: {my_string[-1]}")

print("\n--- String Slicing ---")
print(f"Slice [2:5]: {my_string[2:5]}")
print(f"Slice [:5]: {my_string[:5]}")
print(f"Slice [2:]: {my_string[2:]}")
print(f"Reverse a string: {my_string[::-1]}")


print("\n--- String Concatenation ---")
str1 = "Hello"
str2 = "World"
result = str1 + ", " + str2
print(f"Concatenation: {result}")

print("\n--- String Repetition ---")
repeated_string = "Ha" * 3
print(f"Repetition: {repeated_string}")

print("\n--- Immutability and 'Modifying' Strings ---")
try:
    my_string[0] = 'J'
except TypeError as e:
    print(f"Error when trying to change a string: {e}")

# Create a new string
new_string = "J" + my_string[1:]
print(f"New string: {new_string}")


print("\n--- Common Functions ---")
print(f"Length of my_string: {len(my_string)}")
num = 123
num_str = str(num)
print(f"String representation of {num} is '{num_str}'")

print("\n--- String Formatting ---")
# f-Strings
name = "Alice"
age = 30
print(f"f-String: My name is {name} and I am {age} years old.")

# str.format()
name = "Bob"
age = 25
print("str.format(): My name is {} and I am {} years old.".format(name, age))
print("str.format(): My name is {1} and I am {0} years old.".format(age, name))
print("str.format(): My name is {name} and I am {age} years old.".format(age=age, name=name))

# Old Style Formatting (%)
name = "Charlie"
age = 35
print("Old Style (%): My name is %s and I am %d years old." % (name, age))


print("\n--- Escape Characters ---")
print('It\'s a beautiful day.')
print("He said, \"Hello!\"")
print("This is a backslash: \\")
print("Line 1\nLine 2")
print("Column 1\tColumn 2")


print("\n--- Common String Methods ---")
text = "   Hello World!   "
print(f"Original: '{text}'")
print(f"upper(): {text.upper()}")
print(f"lower(): {text.lower()}")
print(f"strip(): '{text.strip()}'")
print(f"lstrip(): '{text.lstrip()}'")
print(f"rstrip(): '{text.rstrip()}'")
print(f"replace('l', 'X'): {text.replace('l', 'X')}")
print(f"split(' '): {text.split()}")
words = ['Python', 'is', 'fun']
print(f"join(): {'-'.join(words)}")
print(f"startswith('   Hello'): {text.startswith('   Hello')}")
print(f"endswith('World!   '): {text.endswith('World!   ')}")
print(f"find('World'): {text.find('World')}")
print(f"isdigit(): {'123'.isdigit()}")
print(f"isalpha(): {'Python'.isalpha()}")


print("\n--- String Exercises ---")

# 1. Reverse a String
string_to_reverse = "Hello Python"
reversed_string = string_to_reverse[::-1]
print(f"1. Reversed '{string_to_reverse}': '{reversed_string}'")

# 2. Palindrome Check
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

test_palindrome = "A man a plan a canal Panama"
print(f"2. Is '{test_palindrome}' a palindrome? {is_palindrome(test_palindrome)}")
test_not_palindrome = "Hello"
print(f"   Is '{test_not_palindrome}' a palindrome? {is_palindrome(test_not_palindrome)}")

# 3. Count Vowels
def count_vowels(s):
    count = 0
    vowels = "aeiou"
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
    
text_for_vowels = "This is a sample sentence."
print(f"3. Vowel count in '{text_for_vowels}': {count_vowels(text_for_vowels)}")

# 4. Word Count
sentence = "This is a sample sentence with several words."
word_count = len(sentence.split())
print(f"4. Word count in '{sentence}': {word_count}")

# 5. Title Case
text_to_title = "hello world of python"
print(f"5. Title case of '{text_to_title}': {text_to_title.title()}")
