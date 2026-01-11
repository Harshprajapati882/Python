# Abstraction

Abstraction is one of the core principles of object-oriented programming. Its main goal is to **hide complexity while exposing only the essential features** of an object or system.

Think of a real-world example: a car.
*   **Essential Features (The Interface)**: You, as the driver, interact with a simple interface: a steering wheel, pedals, and a gear stick.
*   **Hidden Complexity**: You don't need to know how the engine works, how the fuel is injected, how the transmission shifts gears, or how the electrical system operates. All that complexity is hidden (abstracted away).

In programming, abstraction works the same way. It allows us to create complex systems by building on top of simpler, well-defined interfaces without needing to understand the intricate details of their implementation.

## How to Achieve Abstraction in Python

In Python, abstraction is typically achieved using **Abstract Base Classes (ABCs)**.

An abstract base class is a class that is meant to be inherited from, but not instantiated on its own. It defines a common interface (a set of methods and properties) that all its subclasses must implement.

Python's `abc` module provides the tools to create ABCs.

### Key Components of the `abc` Module

*   **`ABC`**: A helper class that you inherit from to create an abstract base class.
*   **`@abstractmethod`**: A decorator used to define an abstract method. An abstract method has a declaration but no implementation.

## Rules for Abstract Base Classes

1.  **Cannot Be Instantiated**: You cannot create a direct object of an abstract class.
    ```python
    from abc import ABC, abstractmethod

    class MyAbstractClass(ABC):
        @abstractmethod
        def my_method(self):
            pass

    # my_obj = MyAbstractClass() # This will raise a TypeError
    ```

2.  **Subclasses Must Implement Abstract Methods**: Any regular (non-abstract) subclass that inherits from an ABC *must* provide an implementation for all of its parent's abstract methods. If it fails to do so, it also becomes an abstract class, and you won't be able to instantiate it.

This mechanism ensures that any object claiming to be a certain "type" (by inheriting from the ABC) will definitely have the required methods, providing a guaranteed, consistent interface. This makes the system more predictable and easier to work with.
