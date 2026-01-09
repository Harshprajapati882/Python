# Function & Function types

# Defining a simple function
def greet():
    """This function greets the user."""
    print("Hello, World!")

# Calling the function
greet()

# Function with arguments
def greet_user(name):
    """This function greets the user with the given name."""
    print(f"Hello, {name}!")

greet_user("Alice")

# Function with a return value
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b

result = add(5, 3)
print("Sum:", result)

# Required arguments
def required_args(a, b):
    print(f"a: {a}, b: {b}")

# required_args(5) # This would cause an error
required_args(5, 10)

# Keyword arguments
def keyword_args(name, age):
    print(f"Name: {name}, Age: {age}")

keyword_args(name="Bob", age=30)
keyword_args(age=25, name="Charlie")

# Default arguments
def default_args(country="Norway"):
    print(f"I am from {country}")

default_args("Sweden")
default_args()

# Variable-length arguments (*args)
def var_args(*args):
    print("Arguments passed:", args)
    for arg in args:
        print(arg)

var_args(1, 2, 3, "four")

# Variable-length keyword arguments (**kwargs)
def var_kwargs(**kwargs):
    print("Keyword arguments passed:", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

var_kwargs(first_name="John", last_name="Doe", age=40)

# Lambda function
multiply = lambda x, y: x * y
print("Multiplication:", multiply(5, 4))

# Example of using lambda with other functions like filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: (x % 2 == 0), numbers))
print("Even numbers:", even_numbers)

# Built-in functions
print("Length of numbers list:", len(numbers))
print("Type of 'Hello':", type("Hello"))

# User-defined function example
def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = 17
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


# --- Advanced Function Concepts ---

# Scope (LEGB Rule)
x = "global"

def outer_func():
    x = "enclosing"
    def inner_func():
        x = "local"
        print("Inside inner_func:", x) # local
    inner_func()
    print("Inside outer_func:", x) # enclosing

outer_func()
print("Global:", x) # global

# Closures
def outer_closure(msg):
    message = msg
    def inner_closure():
        print(message)
    return inner_closure

my_closure = outer_closure("Hello from closure!")
my_closure()


# Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()


# Generators
def my_generator(n):
    for i in range(n):
        yield i

gen = my_generator(5)
print("\nGenerator output:")
for i in gen:
    print(i)


# Type Hinting
def greet_typed(name: str) -> str:
    return "Hello, " + name

print("\n" + greet_typed("World"))


# Recursion
def factorial(n: int) -> int:
    """Calculates factorial recursively."""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("\nFactorial of 5:", factorial(5))