# Data Classes

Introduced in Python 3.7, the `dataclasses` module provides a decorator that automatically generates special methods for classes that are primarily used to store data.

Before data classes, if you wanted to create a class to hold some data, you would typically write a lot of boilerplate code:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
```
This is a lot of code for a simple `Point` class. You have to manually implement the initializer (`__init__`), a nice string representation (`__repr__`), and a way to compare objects (`__eq__`).

## The `@dataclass` Decorator

The `@dataclass` decorator simplifies this process immensely. It inspects the class's type annotations and automatically generates the boilerplate methods for you.

Here is the same `Point` class written as a data class:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```
That's it! This short definition is roughly equivalent to the much longer manual version above.

## What Does `@dataclass` Generate?

By default, the `@dataclass` decorator adds the following methods to your class:

*   **`__init__(self, ...)`**: An initializer that takes arguments for all the defined fields and assigns them to the instance.
*   **`__repr__(self)`**: A representation method that creates a nice string showing the class name and its fields (e.g., `Point(x=1, y=2)`). This is extremely useful for debugging.
*   **`__eq__(self, other)`**: An equality method that allows you to compare two instances of the class. They are equal if all their fields are equal.
*   **`__lt__(self, other)`, `__le__`, `__gt__`, `__ge__`**: By default, these are not generated. However, if you set `order=True` in the decorator (`@dataclass(order=True)`), it will generate these comparison methods, allowing you to sort objects of the class. The comparison is done field by field, from top to bottom.
*   **`__hash__`**: If appropriate, a hash method is generated, allowing you to use instances of the class as keys in a dictionary or store them in a set. This depends on the `eq` and `frozen` parameters.

## Customizing Data Classes

The `@dataclass` decorator has several optional parameters to customize its behavior:

*   `init=True`: Controls whether the `__init__` method is generated.
*   `repr=True`: Controls whether the `__repr__` method is generated.
*   `eq=True`: Controls whether the `__eq__` method is generated.
*   `order=False`: If `True`, generates `__lt__`, `__le__`, `__gt__`, `__ge__`.
*   `frozen=False`: If `True`, makes instances of the class immutable. Assigning to a field after creation will raise a `FrozenInstanceError`. This is useful for creating constant data objects.

Data classes are a fantastic modern Python feature that reduces boilerplate and makes code for storing data cleaner, safer, and easier to write.
