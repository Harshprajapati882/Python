# Reflection in Python

**Reflection** (or **introspection**) is the ability of a program to examine, and in some cases modify, its own structure and behavior at runtime.

In simpler terms, it means that code can get information about other code. For example, an object can be asked for its type, its attributes, and its methods.

Python's dynamic nature makes it exceptionally good at reflection. Many built-in functions and special attributes are provided for this purpose.

## Key Reflection Functions and Attributes

### 1. `type()` and `isinstance()`
These functions are the most basic form of reflection.

*   `type(obj)`: Returns the type (class) of an object.
*   `isinstance(obj, class)`: Checks if an object is an instance of a particular class or any of its subclasses.

### 2. `dir()`
The `dir(obj)` function returns a list of all the attributes and methods of an object (including special methods like `__init__`, `__str__`, etc.). It's a powerful tool for exploring what an object can do.

### 3. `hasattr()`, `getattr()`, `setattr()`, and `delattr()`
These functions allow you to manipulate an object's attributes using their string names. This is a core feature of reflection.

*   `hasattr(obj, 'name')`: Checks if an object has an attribute with the given name (string).
*   `getattr(obj, 'name')`: Gets the value of an attribute from an object. It's equivalent to `obj.name`, but the name is a string. You can provide a default value to be returned if the attribute doesn't exist.
*   `setattr(obj, 'name', value)`: Sets the value of an attribute on an object. It's equivalent to `obj.name = value`.
*   `delattr(obj, 'name')`: Deletes an attribute from an object.

### 4. `__dict__`
The `__dict__` attribute of an object is a dictionary that stores the object's writable attributes. You can directly view and manipulate this dictionary, which provides another powerful way to inspect and modify an object's state at runtime.

### 5. `callable()`
The `callable(obj)` function returns `True` if the object can be "called" (like a function or a method), and `False` otherwise.

## Why is Reflection Useful?

*   **Frameworks and Plugins**: Frameworks like Django or Flask use reflection extensively to discover models, views, and routes defined by the user. A plugin system can use reflection to inspect a plugin file and find the classes or functions it needs to integrate.
*   **Serialization/Deserialization**: Libraries that convert objects to/from formats like JSON or XML (e.g., `jsonpickle`) use reflection. They inspect the object's attributes to figure out what data needs to be saved and then use reflection again to reconstruct the object from the saved data.
*   **Debugging and Testing**: Reflection allows you to write generic testing code that can inspect the state of an object, or to build powerful debugging tools that can explore the program's live state.
*   **Writing Generic Code**: You can write functions that operate on objects without knowing their specific types in advance. For example, a function that prints all the public attributes of any given object.
