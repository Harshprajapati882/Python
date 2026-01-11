# Python Errors and Exceptions: Code Examples

# 1. Syntax Errors
# The following line would cause a SyntaxError because of the missing colon.
# if 5 > 2
#     print("Five is greater than two!")


# 2. Exceptions (Runtime Errors)
print("--- 2. Exceptions ---")
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Some common built-in exceptions
try:
    x = "hello" + 5  # TypeError
except TypeError as e:
    print(f"Caught a TypeError: {e}")

try:
    int("abc")  # ValueError
except ValueError as e:
    print(f"Caught a ValueError: {e}")

try:
    my_list = [1, 2, 3]
    print(my_list[5])  # IndexError
except IndexError as e:
    print(f"Caught an IndexError: {e}")

try:
    my_dict = {'a': 1}
    print(my_dict['b'])  # KeyError
except KeyError as e:
    print(f"Caught a KeyError: {e}")

print("\n--- 3. Handling Exceptions: try...except ---")
try:
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    result = numerator / denominator
except (ValueError, ZeroDivisionError) as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The result is {result}")


print("\n--- 4. The `else` and `finally` Clauses ---")
file = None
try:
    file = open("non_existent_file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("The file was not found.")
else:
    print("File read successfully.")
    print(content)
finally:
    if file:
        file.close()
    print("Finished file operation. `finally` block executed.")


print("\n--- 5. Raising Exceptions ---")
def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        print("User is a minor.")
    else:
        print("User is an adult.")

try:
    process_age(-5)
except ValueError as e:
    print(f"Error processing age: {e}")

# Re-raising an exception
try:
    a = 1 / 0
except ZeroDivisionError:
    print("Logging the division by zero error...")
    # raise # Uncommenting this would re-raise the exception and stop the script


print("\n--- 6. Exception Chaining ---")
def calculate_something():
    try:
        # Simulate a low-level error
        result = 1 / 0
    except ZeroDivisionError as e:
        # Chain the original exception to a more descriptive, higher-level exception
        raise RuntimeError("Failed to perform calculation") from e

try:
    calculate_something()
except RuntimeError as e:
    print(f"Caught a runtime error: {e}")
    print(f"Original cause: {e.__cause__}")


print("\n--- 7. Nested try Blocks ---")
try:
    print("Outer try block")
    try:
        print("Inner try block")
        raise KeyError("A key error in the inner block")
    except ValueError:
        print("Inner except block (ValueError)")
    finally:
        print("Inner finally block")
except KeyError as e:
    print(f"Outer except block caught: {e}")


print("\n--- 8. User-Defined Exceptions ---")
class InsufficientFundsError(Exception):
    """Custom exception raised when an account has insufficient funds."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to withdraw {amount} with only {balance} available."
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    print(f"Error: {e}")


print("\n--- 9. Assertions ---")
# Assertions are for debugging, not for runtime error handling,
# as they can be disabled.
try:
    temperature_celsius = -10
    assert temperature_celsius >= 0, "Temperature cannot be below absolute zero (for this example)!"
except AssertionError as e:
    print(f"Assertion failed: {e}")


print("\n--- 10. Logging ---")
import logging

# Configure logging to a file
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    result = 1 / 0
except ZeroDivisionError:
    logging.error("A ZeroDivisionError occurred.", exc_info=True)
    print("Logged a ZeroDivisionError to app.log")


print("\n--- 11. Warnings ---")
import warnings

def old_function():
    warnings.warn(
        "old_function() is deprecated and will be removed in a future version.",
        DeprecationWarning,
        stacklevel=2 # Points the warning to where the function was called
    )
    print("Executing the old function...")

print("Calling a deprecated function:")
old_function()


print("\n--- 12. Debugging with pdb ---")
import pdb

def complex_calculation(a, b, c):
    x = a * b
    # Set a breakpoint. When the script runs, it will pause here.
    # pdb.set_trace()
    # In the pdb console, you can inspect variables (e.g., 'p x')
    # and continue execution ('c') or step through ('n').
    y = x + c
    return y

print("Running a function with a pdb trace (commented out).")
# result = complex_calculation(5, 10, 20)
# print(f"Result of complex_calculation: {result}")
print("PDB example is ready to be used (uncomment `pdb.set_trace()` and the call).")
