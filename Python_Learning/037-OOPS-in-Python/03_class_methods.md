# Class Methods

In Python, classes can have three types of methods:
1.  **Instance Methods**: The most common type. They take the instance (`self`) as the first argument. They can modify both object state and class state.
2.  **Class Methods**: These are bound to the class and not the object instance. They take the class (`cls`) as the first argument. They cannot modify object instance state, but they can modify class state that applies across all instances of the class.
3.  **Static Methods**: They don't take the instance (`self`) or the class (`cls`) as the first argument. They are like regular functions that are namespaced within the class. They cannot modify object or class state.

This section focuses on **Class Methods**.

## Defining a Class Method

A class method is created using the `@classmethod` decorator. The first parameter of a class method is conventionally named `cls`, which refers to the class itself.

## Key Characteristics of Class Methods

*   **Bound to the Class**: They are called on the class itself (e.g., `MyClass.class_method()`) rather than on an instance (e.g., `my_object.instance_method()`). You can also call them from an instance, but the first argument will still be the class.
*   **Access to Class State**: They can access and modify class-level attributes. This is useful for managing data that is shared among all instances of a class.
*   **Factory Methods**: A common use case for class methods is to create "factory methods". These are methods that can create instances of the class using alternative ways, for example, by parsing a string or loading data from a file. This provides more flexible ways to create objects than just using the `__init__` constructor.
