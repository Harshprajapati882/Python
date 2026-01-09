# main_module.py

# --- 1. Basic Import ---
# We will import a module named 'my_math_functions.py'
# First, let's create that file.

# Let's assume 'my_math_functions.py' contains:
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b

import my_math_functions

result_add = my_math_functions.add(10, 5)
result_sub = my_math_functions.subtract(10, 5)

print(f"Using basic import: {result_add}, {result_sub}")


# --- 2. Using 'from...import' ---
from my_math_functions import add, subtract

result_add_from = add(20, 5)
result_sub_from = subtract(20, 5)
print(f"Using 'from...import': {result_add_from}, {result_sub_from}")


# --- 3. Importing with an alias 'as' ---
import my_math_functions as math_ops

result_add_alias = math_ops.add(30, 5)
print(f"Using alias 'as': {result_add_alias}")

from my_math_functions import add as sum_vals
result_add_alias_func = sum_vals(40,5)
print(f"Using alias 'as' for a function: {result_add_alias_func}")


# --- 4. Built-in modules ---
import math
import datetime
import os

print(f"\n--- Built-in Modules ---")
print(f"Value of PI from math module: {math.pi}")
print(f"Square root of 25: {math.sqrt(25)}")
print(f"Current date and time: {datetime.datetime.now()}")
print(f"Current working directory: {os.getcwd()}")


# --- 5. The __name__ == "__main__" block ---
# Let's look at the contents of my_math_functions.py again.
# It could be written as:

# my_math_functions.py
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# print(f"The __name__ of my_math_functions is: {__name__}")
#
# if __name__ == "__main__":
#     print("my_math_functions.py is being run directly")
#     print(add(1,1))
# else:
#     print("my_math_functions.py is being imported.")

print(f"\n--- Running vs Importing ---")
# When we run this file (main_module.py), the __name__ for this file is "__main__"
print(f"The __name__ of main_module.py is: {__name__}")
# The output from my_math_functions.py will show that its __name__ is 'my_math_functions'
# because it is being imported.


# --- 6. Packages ---
# Assuming we have a package structure like this:
# my_package/
# ↗↗
# └── string_ops.py
# 
# And string_ops.py contains:
# def reverse_string(s):
#     return s[::-1]

# You would import it like this:
from my_package import string_ops

print("\n--- Packages ---")
reversed_text = string_ops.reverse_string("hello")
print(f"Reversed string: {reversed_text}")
