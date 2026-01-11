# Descriptors in Python

# A descriptor is a class that controls attribute access in another class.
# They are the mechanism behind properties, static methods, and more.

# --- Example 1: A Simple Logging Descriptor ---
print("--- 1. A Simple Descriptor ---")

class LoggingDescriptor:
    """A descriptor that logs when an attribute is get, set, or deleted."""
    
    def __get__(self, instance, owner):
        print(f"Getting value from '{instance}'...")
        # To store the actual value, we need to attach it to the instance.
        # We use a "private" name to avoid an infinite loop.
        return instance._internal_value

    def __set__(self, instance, value):
        print(f"Setting value to '{value}' in '{instance}'...")
        instance._internal_value = value

    def __delete__(self, instance):
        print(f"Deleting value from '{instance}'...")
        del instance._internal_value

class MyClass:
    # We assign an instance of the descriptor to a class attribute.
    managed_attribute = LoggingDescriptor()

    def __init__(self, initial_value):
        # The initial value is set through the descriptor's __set__ method
        self.managed_attribute = initial_value

# --- Usage ---
obj = MyClass("first value") # Setting value to 'first value'...

# Accessing the attribute calls __get__
val = obj.managed_attribute  # Getting value...
print(f"Retrieved value: {val}")

# Changing the attribute calls __set__
obj.managed_attribute = "second value" # Setting value to 'second value'...

# Deleting the attribute calls __delete__
del obj.managed_attribute # Deleting value...


# --- Example 2: A Reusable Validation Descriptor ---
print("\n--- 2. A Validation Descriptor ---")

class PositiveNumber:
    """A data descriptor that ensures a value is a positive number."""
    
    def __set_name__(self, owner, name):
        # This special method is called when the descriptor is created.
        # It allows us to know the attribute's name in the owner class.
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        # Get the value from the instance's __dict__ using the private name
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        if value <= 0:
            raise ValueError("Value must be positive.")
        # Set the value in the instance's __dict__ using the private name
        setattr(instance, self.private_name, value)

class Product:
    # We can reuse the same descriptor for multiple attributes.
    price = PositiveNumber()
    quantity = PositiveNumber()

    def __init__(self, name, price, quantity):
        self.name = name
        # These assignments will trigger the PositiveNumber.__set__ method
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

# --- Usage ---
try:
    # This works fine
    book = Product("The Hobbit", 25.50, 100)
    print(f"Total cost of {book.name}: ${book.total_cost()}")

    # This will fail the validation in the descriptor
    # book.price = -10 # Raises ValueError
    
    # This will also fail validation
    invalid_product = Product("Invalid", "free", 10) # Raises TypeError
    
except (ValueError, TypeError) as e:
    print(f"\nError creating product: {e}")

# This demonstrates how descriptors allow for reusable, encapsulated validation logic.
