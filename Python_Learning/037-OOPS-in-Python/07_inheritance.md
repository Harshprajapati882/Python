# Inheritance in Python

Inheritance is one of the fundamental principles of Object-Oriented Programming (OOP). It allows a class (the "child" or "subclass") to inherit attributes and methods from another class (the "parent" or "superclass").

This creates an "is-a" relationship. For example, a `Dog` **is an** `Animal`.

## Key Benefits of Inheritance

*   **Code Reusability**: You can write common code once in a parent class and reuse it across multiple subclasses.
*   **Logical Structure**: It helps in organizing code in a hierarchical way that often mirrors real-world relationships, making the code easier to understand.
*   **Extensibility**: You can add new functionality to a subclass without modifying the parent class.
*   **Polymorphism**: A subclass can override methods from its parent class to provide its own specific implementation.

## Terminology

*   **Parent Class (Superclass or Base Class)**: The class being inherited from.
*   **Child Class (Subclass or Derived Class)**: The class that inherits from another class.

## Syntax

To create a subclass, you pass the parent class as an argument to the child class definition.

```python
class ParentClass:
    # ... attributes and methods

class ChildClass(ParentClass):
    # ... can use attributes and methods of ParentClass
    # ... can also have its own new attributes and methods
```

## The `super()` Function

The `super()` function is used to give access to methods and properties of a parent or sibling class. When you override a method in a subclass (like `__init__`), you often still want to call the parent's version of that method. `super()` lets you do this.

```python
class ChildClass(ParentClass):
    def __init__(self, arg1, arg2):
        # Call the __init__ of the ParentClass
        super().__init__(arg1) 
        self.new_attribute = arg2
```

## Types of Inheritance

1.  **Single Inheritance**: A subclass inherits from only one superclass. (e.g., `Class B` inherits from `Class A`)
2.  **Multiple Inheritance**: A subclass inherits from multiple superclasses. (e.g., `Class C` inherits from `Class A` and `Class B`)
3.  **Multilevel Inheritance**: A subclass inherits from a class that itself is a subclass. (e.g., `Class C` inherits from `Class B`, and `Class B` inherits from `Class A`)
4.  **Hierarchical Inheritance**: Multiple subclasses inherit from a single superclass. (e.g., `Class B` and `Class C` both inherit from `Class A`)
5.  **Hybrid Inheritance**: A combination of two or more types of inheritance.
