# Anonymous or Dynamic Classes in Python

# Python doesn't have a literal "anonymous class" syntax like Java.
# However, the type() constructor can be used to create classes on the fly.

# --- Example 1: Creating a simple class dynamically ---
print("--- 1. Simple Dynamic Class ---")

# Define the methods and attributes we want our class to have
def constructor(self, name):
    self.name = name

def display(self):
    print(f"Object name is: {self.name}")

# Use type() to build the class
# type(ClassName, base_classes, attributes_and_methods_dict)
SimpleDynamicClass = type(
    "SimpleDynamicClass",  # The name of the class
    (),                    # A tuple of parent classes (none in this case)
    {
        "__init__": constructor,
        "display": display,
        "default_message": "This is a dynamic class."
    }
)

# Now, we can instantiate the class we just created
obj1 = SimpleDynamicClass("MyObject1")

# And use its methods and attributes
obj1.display()
print(obj1.default_message)


# --- Example 2: Creating a one-off object for a specific task ---
print("\n--- 2. Creating a one-off event handler ---")

def process_events(event_handler):
    """
    A function that expects an object with 'on_success' and 'on_failure' methods.
    """
    print("\nProcessing started...")
    try:
        # Simulate an operation that might fail
        import random
        if random.random() > 0.5:
            raise ValueError("Random failure!")
        
        # If it succeeds, call the on_success method
        result = "Data processed successfully."
        event_handler.on_success(result)
    except ValueError as e:
        # If it fails, call the on_failure method
        event_handler.on_failure(str(e))

# We need an event handler, but maybe only for this one call.
# Let's create one dynamically.

# Define the methods for our handler
def handle_success(self, result):
    print(f"SUCCESS HANDLER: Operation completed with result: '{result}'")

def handle_failure(self, error_message):
    print(f"FAILURE HANDLER: Operation failed with error: '{error_message}'")

# Create the class and instantiate it in one go
my_handler = type(
    "MyEventHandler",
    (),
    {
        "on_success": handle_success,
        "on_failure": handle_failure
    }
)() # The final () instantiates the class immediately

# Pass the dynamically created handler to our function
process_events(my_handler)
process_events(my_handler)
