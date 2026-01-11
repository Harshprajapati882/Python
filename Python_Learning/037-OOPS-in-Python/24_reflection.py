# Reflection (Introspection) in Python

class User:
    """A simple class representing a user."""
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self._session_token = "ABC-123"

    def greet(self):
        """A method to greet the user."""
        print(f"Hello, my name is {self.name}!")

    def _private_method(self):
        print("This is a private method.")


# --- Create an instance to inspect ---
user_obj = User("Alice", 101)


# --- 1. Using type() and isinstance() ---
print("--- 1. Basic Type Inspection ---")
print(f"The type of user_obj is: {type(user_obj)}")
print(f"Is user_obj an instance of User? {isinstance(user_obj, User)}")
print(f"Is user_obj an instance of object? {isinstance(user_obj, object)}")


# --- 2. Using dir() to see all members ---
print("\n--- 2. Directory of the object (dir()) ---")
# dir() lists all attributes and methods of the object
print(dir(user_obj))


# --- 3. Using hasattr(), getattr(), setattr(), delattr() ---
print("\n--- 3. Manipulating attributes by name ---")

# Check for an attribute
print(f"Does the object have a 'name' attribute? {hasattr(user_obj, 'name')}")
print(f"Does the object have an 'email' attribute? {hasattr(user_obj, 'email')}")

# Get an attribute's value
user_name = getattr(user_obj, 'name')
print(f"Username retrieved via getattr(): {user_name}")

# Try to get a non-existent attribute with a default value
user_email = getattr(user_obj, 'email', 'not_provided@example.com')
print(f"User email retrieved via getattr(): {user_email}")

# Set a new attribute
setattr(user_obj, 'email', 'alice@example.com')
print(f"Newly set email attribute: {user_obj.email}")

# Delete an attribute
delattr(user_obj, 'email')
print(f"Does the object have an 'email' attribute after deletion? {hasattr(user_obj, 'email')}")


# --- 4. Using __dict__ to see the state ---
print("\n--- 4. Inspecting the object's __dict__ ---")
# __dict__ shows the instance's state (its writable attributes)
print(user_obj.__dict__)
# You can modify it directly (though this is often not recommended)
user_obj.__dict__['is_admin'] = True
print(f"Is the user an admin? {user_obj.is_admin}")


# --- A practical example: A generic object inspector ---
print("\n--- 5. A Practical Reflection Example ---")

def inspect_object(obj):
    """
    A function that uses reflection to print details about any object.
    """
    print(f"\nInspecting object of type: {type(obj).__name__}")
    for attr_name in dir(obj):
        # Ignore special "dunder" methods to keep the output clean
        if attr_name.startswith('__'):
            continue
            
        print(f"  - Attribute: {attr_name}")
        
        # Get the actual attribute object from the instance
        attr_value = getattr(obj, attr_name)
        
        # Check if the attribute is a method (i.e., callable)
        if callable(attr_value):
            print("    -> Type: Method")
            # You could even call it, but be careful!
            # if attr_name == 'greet':
            #     attr_value()
        else:
            print(f"    -> Type: Variable, Value: '{attr_value}'")

# Use our generic inspector function on our User object
inspect_object(user_obj)
