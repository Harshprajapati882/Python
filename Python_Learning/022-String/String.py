# Python Strings Examples

# Creating Strings
single_quoted = 'Hello, World!'
double_quoted = "Hello, Python!"
triple_quoted = """This is a
multi-line string."""

print(single_quoted)
print(double_quoted)
print(triple_quoted)

# String Indexing
my_string = "Python"
print(f"First character: {my_string[0]}")
print(f"Last character: {my_string[-1]}")

# String Slicing
print(f"Slice [2:5]: {my_string[2:5]}")
print(f"Slice [:5]: {my_string[:5]}")
print(f"Slice [2:]: {my_string[2:]}")

# String Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + ", " + str2
print(f"Concatenation: {result}")

# String Repetition
repeated_string = "Ha" * 3
print(f"Repetition: {repeated_string}")

# Immutability
try:
    my_string[0] = 'J'
except TypeError as e:
    print(f"Error when trying to change a string: {e}")

# Create a new string
new_string = "J" + my_string[1:]
print(f"New string: {new_string}")


# Common Functions
print(f"Length of my_string: {len(my_string)}")
num = 123
num_str = str(num)
print(f"String representation of {num} is '{num_str}'")


# f-Strings
name = "Bob"
age = 25
print(f"My name is {name} and I am {age} years old.")
