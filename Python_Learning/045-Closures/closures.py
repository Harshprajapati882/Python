# Python Closures Examples

# 1. Simple Nested Function
def outer_function(text):
    """
    This is the outer function.
    """
    def inner_function():
        """
        This is the nested inner function.
        It has access to the 'text' variable from the outer scope.
        """
        print(text)

    inner_function()

print("--- Example 1: Simple Nested Function ---")
outer_function("Hello, World!")


# 2. Creating and Using a Closure
def greeter(name):
    """
    Outer function that creates a closure.
    """
    # This is the enclosing scope variable
    greeting = f"Hello, {name}!"

    def greet():
        """
        Inner function (the closure).
        It 'closes over' the 'greeting' variable.
        """
        print(greeting)

    return greet  # Return the inner function

print("\n--- Example 2: Creating and Using a Closure ---")
greet_john = greeter("John")
greet_jane = greeter("Jane")

# Even though the 'greeter' function has finished executing,
# the returned 'greet' functions (now named greet_john and greet_jane)
# still remember the 'greeting' variable from when they were created.
greet_john()
greet_jane()


# 3. Closure for State Retention (A Counter)
def counter():
    """
    A closure that acts as a stateful counter.
    """
    count = 0  # Enclosing scope variable

    def increment():
        """
        The closure that increments and prints the count.
        """
        nonlocal count  # Use nonlocal to modify the parent's 'count'
        count += 1
        print(f"Count is: {count}")

    return increment

print("\n--- Example 3: Closure for State Retention (Counter) ---")
my_counter1 = counter()
my_counter1()
my_counter1()
my_counter1()

# Each call to counter() creates a new, independent closure and state.
my_counter2 = counter()
my_counter2() # Starts from 1 again


# 4. Another State Retention Example (Adder Factory)
def adder_factory(x):
    """
    A factory for creating adder functions.
    """
    def adder(y):
        """
        The closure that adds y to the remembered x.
        """
        return x + y
    return adder

print("\n--- Example 4: Adder Factory ---")
add_5 = adder_factory(5)
add_10 = adder_factory(10)

print(f"Result of add_5(10): {add_5(10)}")  # Output: 15
print(f"Result of add_10(10): {add_10(10)}") # Output: 20
print(f"Result of add_5(3): {add_5(3)}")    # Output: 8
