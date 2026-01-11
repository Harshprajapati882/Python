# Interfaces in Python

The concept of an "interface" comes from statically-typed languages (like Java or C#). An interface is a contract that defines a set of methods that a class must implement. It contains no implementation itself, only the method signatures. Any class that "implements" the interface must provide the code for all of its methods.

## Python's Approach to Interfaces

Python does not have a dedicated `interface` keyword like other languages. However, the same concept can be achieved using two primary approaches:

1.  **Duck Typing (Informal Interfaces)**
2.  **Abstract Base Classes (Formal Interfaces)**

### 1. Duck Typing

This is the most common and "Pythonic" approach. It relies on the idea that the specific type of an object is less important than the methods it implements.

> "If it walks like a duck and it quacks like a duck, then it must be a duck."

In this approach, there is no formal contract. You just assume that an object will have the necessary methods, and your code will work as long as it does. This is an **informal interface**. The "contract" is simply based on the presence of the required methods and properties.

*   **Advantage**: Very flexible and simple.
*   **Disadvantage**: The contract is not explicit. Errors (like a missing method) will only be caught at runtime when the method is called.

### 2. Abstract Base Classes (ABCs)

This is Python's way of creating **formal interfaces**. As discussed in the Abstraction topic, an Abstract Base Class (ABC) can define a set of `@abstractmethod`s.

When a class inherits from an ABC, it is **required** to implement all of the abstract methods. If it doesn't, a `TypeError` will be raised when you try to instantiate the class.

This approach is more rigid than duck typing, but it provides several benefits:
*   **Explicit Contract**: The ABC clearly defines what methods are required.
*   **Early Error Checking**: It catches errors at instantiation time if a class fails to implement the required methods, rather than later at runtime.
*   **Type Hinting**: You can use the ABC as a type hint to make it clear what kind of object a function expects.
*   **`isinstance()` Checks**: You can check if an object conforms to the interface using `isinstance(my_obj, MyABC)`.

## Which Approach to Use?

*   For most simple cases in Python, **duck typing** is sufficient and preferred for its flexibility.
*   Use **Abstract Base Classes** when you want to enforce a strict contract, especially in larger applications or frameworks where you need to ensure that different components work together correctly. ABCs are perfect for defining a plugin architecture, for example, where you need to guarantee that every plugin has a specific set of methods.
