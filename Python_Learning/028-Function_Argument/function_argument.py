# Python Function Arguments Examples

# 1. Positional Arguments
print("--- 1. Positional Arguments ---")
def greet_positional(name, message):
    """This function greets the user with a message."""
    print(f"Hello {name}, {message}")

greet_positional("Alice", "How are you?")


# 2. Keyword Arguments
print("\n--- 2. Keyword Arguments ---")
def greet_keyword(name, message):
    """This function greets the user, allowing for keyword arguments."""
    print(f"Hello {name}, {message}")

greet_keyword(message="Good morning!", name="Bob")


# 3. Default Arguments
print("\n--- 3. Default Arguments ---")
def greet_default(name, message="Good morning!"):
    """This function has a default value for the message argument."""
    print(f"Hello {name}, {message}")

greet_default("Charlie")
greet_default("David", "Hope you have a great day!")


# 4. Positional-Only Arguments
print("\n--- 4. Positional-Only Arguments ---")
def user_info_positional_only(name, age, /):
    """This function only accepts positional arguments."""
    print(f"Name: {name}, Age: {age}")

user_info_positional_only("Eve", 30)
try:
    user_info_positional_only(name="Eve", age=30)
except TypeError as e:
    print(f"Caught expected error: {e}")


# 5. Keyword-Only Arguments
print("\n--- 5. Keyword-Only Arguments ---")
def user_info_keyword_only(*, name, age):
    """This function only accepts keyword arguments."""
    print(f"Name: {name}, Age: {age}")

user_info_keyword_only(name="Frank", age=25)
try:
    user_info_keyword_only("Frank", 25)
except TypeError as e:
    print(f"Caught expected error: {e}")


# 6. Combination of Argument Types
print("\n--- 6. Combination of Argument Types ---")
def combined_args(pos_only, /, standard, *, kwd_only):
    """A function with positional-only, standard, and keyword-only arguments."""
    print(f"Positional-only: {pos_only}")
    print(f"Standard: {standard}")
    print(f"Keyword-only: {kwd_only}")

combined_args(1, 2, kwd_only=3)
combined_args(1, standard=2, kwd_only=3)


# 7. Arbitrary Arguments
print("\n--- 7. Arbitrary Arguments ---")
# Arbitrary Positional Arguments (*args)
def sum_all(*numbers):
    """This function sums all the numbers passed as arguments."""
    return sum(numbers)

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")

# Arbitrary Keyword Arguments (**kwargs)
def display_info(**info):
    """This function displays information passed as keyword arguments."""
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Grace", city="New York")


# 8. Packing and Unpacking
print("\n--- 8. Packing and Unpacking ---")
# Packing is implicit in *args and **kwargs definitions above.

# Unpacking a list/tuple with *
def multiply(a, b, c):
    """This function multiplies three numbers."""
    return a * b * c

numbers_to_multiply = [2, 3, 4]
print(f"Product of {numbers_to_multiply}: {multiply(*numbers_to_multiply)}")

# Unpacking a dictionary with **
def greet_details(name, message):
    """This function greets based on a dictionary of details."""
    print(f"Hello {name}, {message}")

greeting_details = {"name": "Heidi", "message": "Good to see you."}
greet_details(**greeting_details)


# 9. Variable Scope
print("\n--- 9. Variable Scope ---")
global_var = "I am global"

def scope_test():
    local_var = "I am local"
    print(global_var)  # Accessing global variable
    print(local_var)

scope_test()
# print(local_var)  # This would cause a NameError

def modify_global():
    global global_var
    global_var = "I am a modified global"

modify_global()
print(global_var)

def outer_function():
    nonlocal_var = "I am nonlocal"
    def inner_function():
        nonlocal nonlocal_var
        nonlocal_var = "I am a modified nonlocal"
        print(nonlocal_var)
    inner_function()
    print(nonlocal_var)

outer_function()


# 10. Function Annotations
print("\n--- 10. Function Annotations ---")
def annotated_greeting(name: str, message: str = "Hi") -> str:
    """A function with type annotations."""
    return f"{message}, {name}!"

print(annotated_greeting("Ivy"))
print(f"Annotations: {annotated_greeting.__annotations__}")


# 11. Built-in Functions
print("\n--- 11. Built-in Functions ---")
numbers = [1, 5, 2, 8, 3]
print(f"Numbers: {numbers}")
print(f"Length of numbers: {len(numbers)}")
print(f"Sum of numbers: {sum(numbers)}")
print(f"Max of numbers: {max(numbers)}")
print(f"Min of numbers: {min(numbers)}")
print(f"Type of numbers: {type(numbers)}")
converted_to_string = str(numbers)
print(f"Numbers converted to string: {converted_to_string}")
