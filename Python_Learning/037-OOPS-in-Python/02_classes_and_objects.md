# Classes and Objects

In object-oriented programming, a **class** is a blueprint for creating objects. It defines a set of attributes that will characterize any object that is an instance of the class, and a set of methods or functions that can be performed by such objects.

An **object** is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created. Creating an object is also called "instantiating a class".

## Key Concepts

*   **Class**: A template or blueprint for creating objects.
    *   It defines properties (attributes) and behaviors (methods).
    *   Example: A `Car` class can define that all cars have a `color` and a `model`, and that they can `start()` and `stop()`.

*   **Object**: A specific instance of a class.
    *   It has its own state (values for its attributes).
    *   Example: `my_red_car` could be an object of the `Car` class with `color = "red"`. `my_blue_car` could be another object with `color = "blue"`.

*   **`__init__` method**: This is a special method in Python classes. It is a constructor that is automatically called when you create a new instance (object) of a class. It is used to initialize the object's attributes.

*   **`self`**: The `self` parameter is a reference to the current instance of the class and is used to access variables that belong to the class. It does not have to be named `self`, but it is a strong convention in Python. It is the first argument of every method in a class.
