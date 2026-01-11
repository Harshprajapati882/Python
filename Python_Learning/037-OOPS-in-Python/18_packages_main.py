# This file demonstrates how to import and use code from our custom package.

print("--- Starting main script ---")

# --- Different ways to import from a package ---

# 1. Import the entire module
print("\n1. Importing the 'string_utils' module:")
from my_package import string_utils

text = "Hello World"
reversed_text = string_utils.reverse_string(text)
vowel_count = string_utils.count_vowels(text)
print(f"Original text: '{text}'")
print(f"Reversed text: '{reversed_text}'")
print(f"Number of vowels: {vowel_count}")


# 2. Import a specific function from a module
print("\n2. Importing a specific function 'is_prime':")
from my_package.sub_package.math_utils import is_prime

number = 17
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# 3. Import from a sub-package module using an alias
print("\n3. Importing with an alias:")
from my_package.sub_package import math_utils as mu

radius = 5
circle_area = mu.area_of_circle(radius)
print(f"The area of a circle with radius {radius} is {circle_area:.2f}")


# Note that the "Initializing..." print statements from the __init__.py files
# are executed only the first time a component of the package is imported.
print("\n--- Main script finished ---")

# Expected output order:
# --- Starting main script ---
#
# 1. Importing the 'string_utils' module:
# Initializing 'my_package'...
# Original text: 'Hello World'
# Reversed text: 'dlroW olleH'
# Number of vowels: 3
#
# 2. Importing a specific function 'is_prime':
# Initializing 'sub_package'...
# 17 is a prime number.
#
# 3. Importing with an alias:
# The area of a circle with radius 5 is 78.54
#
# --- Main script finished ---
