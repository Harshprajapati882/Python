# Dynamic Binding (Late Binding)

**Binding** refers to the connection between a method call (the message) and the actual code that gets executed (the method implementation).

There are two types of binding:

1.  **Static Binding (Early Binding)**: The determination of which method to call is made at **compile time**. This is common in statically-typed languages like C++ or Java. The compiler knows the exact type of the object and links the method call to the specific implementation in that class.

2.  **Dynamic Binding (Late Binding)**: The determination of which method to call is delayed until **run time**. The decision is made based on the actual type of the object at the time the call is made.

**Python exclusively uses dynamic binding.**

## How Dynamic Binding Works in Python

Because Python is a dynamically-typed language, the type of a variable is not fixed. A variable can refer to an object of one class and then be reassigned to an object of a completely different class.

When you call a method on an object, like `my_object.do_something()`, Python does not know which `do_something` method to call until the code is actually running. At that moment, it looks at the object that `my_object` is currently pointing to, finds its class, and executes the `do_something` method defined for that specific class.

This is a core reason why polymorphism works so seamlessly in Python.

## Example

Consider a function that takes an object and calls a `speak()` method on it.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_it_speak(animal):
    # The 'speak' method is not bound to a specific class here.
    # The binding happens at runtime.
    print(animal.speak())

# At this moment, 'animal' is a Dog object. Python binds the call to Dog.speak().
make_it_speak(Dog())  # Output: Woof!

# At this moment, 'animal' is a Cat object. Python binds the call to Cat.speak().
make_it_speak(Cat())  # Output: Meow!
```

The `make_it_speak` function can work with any object that has a `speak` method, without needing to know the object's type in advance. The connection between the `animal.speak()` call and the actual code to run is made dynamically each time the function is executed. This flexibility is a key feature of the language.
