# Dynamic Typing in Python

# In Python, a variable is just a name pointing to an object.
# The type is associated with the object, not the name.

# 1. A variable can hold values of different types at different times.
print("--- 1. Reassigning variable types ---")
my_var = 100
print(f"The variable holds: {my_var}, which is of type: {type(my_var)}")

my_var = "Hello, Python!"
print(f"The variable now holds: '{my_var}', which is of type: {type(my_var)}")

my_var = ["a", "b", "c"]
print(f"The variable now holds: {my_var}, which is of type: {type(my_var)}")


# 2. Function parameters are also dynamically typed.
print("\n--- 2. Dynamic typing in function calls ---")
def process_data(data):
    """
    This function's behavior depends on the type of 'data' it receives at runtime.
    """
    if isinstance(data, str):
        print(f"Processing a string: {data.upper()}")
    elif isinstance(data, list):
        print(f"Processing a list. Length: {len(data)}. Items: {data}")
    elif isinstance(data, int):
        print(f"Processing an integer. Double the value is: {data * 2}")
    else:
        print(f"Cannot process data of type: {type(data)}")

process_data("some text")
process_data([10, 20, 30])
process_data(42)
process_data((1, 2)) # Will go to the else block

# This flexibility is powerful but can lead to runtime errors if not handled.
# For example, what if we expected a list and tried to call a list-specific method?

def get_first_item(items):
    # This will crash if 'items' is not a sequence (like a list or string)
    try:
        print(f"The first item is: {items[0]}")
    except TypeError as e:
        print(f"Error: {e}. The object does not support indexing.")
    except IndexError:
        print("Error: The sequence is empty.")

print("\n--- 3. Potential runtime errors from dynamic typing ---")
get_first_item(["apple", "banana"])
get_first_item("orange")
get_first_item([])
get_first_item(123) # This will cause a TypeError

# 4. Python is STRONGLY typed, not weakly typed.
print("\n--- 4. Python is Strongly Typed ---")
# You cannot perform operations between incompatible types without explicit conversion.
a = 5
b = "10"

try:
    result = a + b
except TypeError as e:
    print(f"Could not add {a} and '{b}'. Error: {e}")

# You must explicitly convert the types.
result1 = a + int(b)
print(f"Result after explicit conversion (int): {result1}")

result2 = str(a) + b
print(f"Result after explicit conversion (str): {result2}")
