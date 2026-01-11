# Method Overriding

Method overriding is a concept in object-oriented programming where a subclass provides a specific implementation for a method that is already defined in its superclass. When a method in a subclass has the same name, same parameters, and same return type (or a subtype) as a method in its superclass, the method in the subclass is said to override the method in the superclass.

This is a key mechanism for achieving polymorphism.

## How it Works

1.  **Inheritance is Required**: Method overriding can only occur in the context of inheritance, where there is a parent (superclass) and a child (subclass).
2.  **Matching Method Signature**: The method in the subclass must have the same "signature" (name and number/type of parameters) as the method in the parent class.
3.  **Execution**: When you call the overridden method on an object of the subclass, the version of the method defined in the subclass is executed, not the version from the superclass.

## Why Use Method Overriding?

*   **Specialized Behavior**: It allows subclasses to provide a more specific or specialized version of a method. For example, a generic `Animal` class might have a `speak()` method, but the `Dog` subclass will override it to "bark" and the `Cat` subclass will override it to "meow".
*   **Polymorphism**: It enables you to write generic code that can work with objects of the superclass, but which will behave correctly and specifically when it encounters objects of the subclass.

## Using `super()` with Overriding

Sometimes, you don't want to completely replace the parent's method, but rather extend it. You can do this by calling the parent's version of the method from within the subclass's overridden method using the `super()` function.

```python
class Parent:
    def greet(self):
        print("Hello from the Parent!")

class Child(Parent):
    def greet(self):
        # First, call the original method from the parent
        super().greet()
        # Then, add new functionality
        print("...and hello from the Child!")

child = Child()
child.greet()
# Output:
# Hello from the Parent!
# ...and hello from the Child!
```

This is very common, especially when overriding the `__init__` constructor, where you need to ensure the parent class is also properly initialized.
