# This file makes the 'my_package' directory a Python package.

# This code will be executed when the package is imported.
print("Initializing 'my_package'...")

# We can also make functions from modules available at the package level
# to simplify imports for the user.
from . import string_utils
