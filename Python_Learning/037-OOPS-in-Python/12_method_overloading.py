# Simulating Method Overloading in Python

# Python does not support traditional method overloading.
# If you define a method twice, the last definition wins.
class Test:
    def my_func(self, a):
        print("One argument")
    def my_func(self, a, b):
        print("Two arguments")

# test = Test()
# test.my_func(1)  # This would raise a TypeError because the first my_func is gone.


# --- Pattern 1: Using Default Arguments ---
print("--- 1. Using Default Arguments ---")
class Messenger:
    def send_message(self, recipient, message, sender="System"):
        """
        Sends a message. The sender is optional.
        """
        print(f"To: {recipient}, From: {sender} - Message: '{message}'")

m = Messenger()
# Call with 2 arguments (sender will be the default)
m.send_message("Alice", "Hello there!")
# Output: To: Alice, From: System - Message: 'Hello there!'

# Call with 3 arguments (providing a specific sender)
m.send_message("Bob", "Hi Bob!", sender="Charlie")
# Output: To: Bob, From: Charlie - Message: 'Hi Bob!'


# --- Pattern 2: Using Variable-Length Arguments (*args) ---
print("\n--- 2. Using *args ---")
class ShapeDrawer:
    def draw(self, *args):
        """
        Draws a shape. Behavior changes based on the number of arguments.
        - 1 arg: A point
        - 2 args: A line
        - 3 args: A triangle
        """
        num_args = len(args)
        if num_args == 1:
            print(f"Drawing a point at coordinates: {args[0]}")
        elif num_args == 2:
            print(f"Drawing a line from {args[0]} to {args[1]}")
        elif num_args == 3:
            print(f"Drawing a triangle with vertices at {args}")
        else:
            print("Cannot draw the shape with the given arguments.")

drawer = ShapeDrawer()
drawer.draw((10, 20))
drawer.draw((10, 20), (50, 60))
drawer.draw((10, 20), (50, 60), (30, 0))


# --- Pattern 3: Using singledispatch for type-based overloading ---
print("\n--- 3. Using functools.singledispatch ---")
from functools import singledispatch

class DataExporter:
    @singledispatch
    def export(self, data):
        """Default method for unknown data types."""
        raise TypeError(f"No export function available for type {type(data)}")

    @export.register(str)
    def _(self, data):
        """This version is called when the data is a string."""
        print(f"Exporting string: '{data}' to a text file.")

    @export.register(list)
    def _(self, data):
        """This version is called when the data is a list."""
        print(f"Exporting list: {data} to a CSV file.")
        
    @export.register(dict)
    def _(self, data):
        """This version is called when the data is a dictionary."""
        print(f"Exporting dictionary: {data} to a JSON file.")

exporter = DataExporter()
exporter.export("This is a sample sentence.")
exporter.export([1, "apple", 3.14, True])
exporter.export({"user": "John", "id": 101})
# exporter.export((1, 2, 3)) # This would raise the TypeError from the default method
