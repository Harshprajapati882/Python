# Static Methods

A static method is a method that belongs to a class rather than an instance of the class. It is defined using the `@staticmethod` decorator and does not receive any implicit first argument, like `self` for instance methods or `cls` for class methods.

## Key Characteristics of Static Methods

*   **No Access to Instance or Class State**: Static methods cannot access or modify the object's state (`self`) or the class's state (`cls`). They are self-contained and work independently.

*   **Organizational Utility**: They are primarily used to group utility functions that have a logical connection to the class, but do not depend on the class or instance state. This helps in organizing the code and keeping related functions together within the class namespace.

*   **Called on the Class or Instance**: A static method can be called on the class itself (e.g., `MyClass.static_method()`) or on an instance of the class (e.g., `my_object.static_method()`). In either case, it behaves just like a regular function.

## When to Use a Static Method

You should use a static method when you have a function that is related to the class, but does not need to access any class or instance data. For example, a helper or utility function that performs a calculation based only on its input parameters.

## Instance vs. Class vs. Static Methods: A Summary

| Method Type       | Decorator        | First Argument     | Access to `self` (Instance)? | Access to `cls` (Class)? |
|-------------------|------------------|--------------------|------------------------------|--------------------------|
| **Instance Method** | (none)           | `self`             | Yes                          | Yes (`self.__class__`)   |
| **Class Method**    | `@classmethod`   | `cls`              | No                           | Yes                      |
| **Static Method**   | `@staticmethod` | (none)             | No                           | No                       |
