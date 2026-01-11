# Multiple Inheritance

Multiple inheritance is a feature of some object-oriented programming languages in which a class can inherit attributes and methods from more than one parent class. This allows a class to combine the features of several existing classes.

## Syntax

You list the parent classes in the class definition, separated by commas.

```python
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
```
The `Child` class will now have access to all the public and protected members of both `Parent1` and `Parent2`.

## The "Diamond Problem" and Method Resolution Order (MRO)

A potential issue with multiple inheritance is the "diamond problem". This occurs when a class inherits from two parent classes that both inherit from the same grandparent class.

```
      A
     / \
    B   C
     \ /
      D
```
If there is a method in `A` that is overridden by both `B` and `C`, which version should `D` inherit?

Python solves this using the **Method Resolution Order (MRO)**. The MRO defines the order in which base classes are searched when looking for a method. Python uses a C3 linearization algorithm to determine the MRO, which ensures a consistent and predictable order.

You can inspect the MRO of a class using the `__mro__` attribute or the `mro()` method.

```python
print(D.__mro__)
# or
print(D.mro())
```

The MRO follows a "depth-first, then left-to-right" logic, but in a way that avoids inheriting from the same class multiple times if possible. The order will be: `D -> B -> C -> A -> object`.

## Best Practices and Mixins

While powerful, multiple inheritance can make code complex and hard to understand if overused. A common and recommended pattern for using multiple inheritance is with **"mixin" classes**.

*   **Mixin**: A mixin is a class that provides a specific, self-contained piece of functionality, but is not meant to be instantiated on its own. It's designed to be "mixed in" with other classes to add its behavior.
*   **Example**: A `LoggingMixin` could provide logging capabilities to any class that inherits from it, without that class needing to be a specific "type" of logger.

This approach often leads to cleaner and more maintainable designs than inheriting from multiple, large, stateful classes.

```