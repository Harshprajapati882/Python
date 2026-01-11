# Encapsulation

Encapsulation is one of the fundamental principles of object-oriented programming. It refers to the **bundling of data (attributes) and the methods that operate on that data into a single unit, called a class.**

A key part of encapsulation is **information hiding**: the practice of restricting direct access to some of an object's components. This means that an object should not have its internal state directly manipulated from the outside. Instead, access should be controlled through a well-defined public interface of methods.

## Why Use Encapsulation?

1.  **Data Integrity**: By controlling access to attributes through methods (like setters), you can add validation logic to ensure that the object's state remains valid. For example, you can prevent an `age` attribute from being set to a negative number.

2.  **Flexibility and Maintainability**: It decouples the internal implementation of a class from the code that uses it. You can change how the class works internally (e.g., change the name of an attribute, modify the internal logic) without breaking the external code, as long as the public interface (the methods) remains the same.

3.  **Simplicity**: It hides the internal complexity of an object from the user. Users of the class only need to know about its public methods, not how it works inside. This is a form of abstraction.

## How to Implement Encapsulation in Python

Python doesn't have strict `private` or `protected` keywords like other languages (e.g., Java, C++). Instead, it relies on naming conventions:

*   **Protected Attributes (`_single_underscore`)**: A convention indicating that an attribute is for internal use within the class and its subclasses. It's a "gentleman's agreement" and does not prevent external access.
*   **Private Attributes (`__double_underscore`)**: A convention that triggers "name mangling", making it much harder to access the attribute from outside the class. This is primarily to avoid naming conflicts in subclasses.

The primary mechanism for encapsulation in Python is to:
1.  Make your attributes "non-public" (using `_` or `__`).
2.  Provide public methods to access and modify these attributes. These methods are often called **getters** and **setters**.

A more "Pythonic" way to implement getters and setters is by using the `@property` decorator, which allows you to treat a method like a public attribute while still having the logic of a getter and setter.
