# Operator Overloading

Operator overloading is a form of polymorphism that allows you to define how Python's built-in operators (like `+`, `-`, `*`, `==`, `<`, `>`) behave with instances of your own custom classes.

By implementing special "dunder" (double underscore) methods, you can make your objects work with these operators in an intuitive and readable way.

For example, instead of writing `vector1.add(vector2)`, you can overload the `+` operator to write `vector1 + vector2`, which is much cleaner.

## Common Operator Overloading Methods

### Arithmetic Operators
*   `__add__(self, other)`: Addition (`+`)
*   `__sub__(self, other)`: Subtraction (`-`)
*   `__mul__(self, other)`: Multiplication (`*`)
*   `__truediv__(self, other)`: Division (`/`)
*   `__floordiv__(self, other)`: Floor Division (`//`)
*   `__pow__(self, other)`: Exponentiation (`**`)

### Comparison Operators
*   `__eq__(self, other)`: Equal to (`==`)
*   `__ne__(self, other)`: Not equal to (`!=`)
*   `__lt__(self, other)`: Less than (`<`)
*   `__gt__(self, other)`: Greater than (`>`)
*   `__le__(self, other)`: Less than or equal to (`<=`)
*   `__ge__(self, other)`: Greater than or equal to (`>=`)

### Other Useful Operators
*   `__len__(self)`: Length (`len(obj)`)
*   `__str__(self)`: String conversion (`str(obj)`)
*   `__repr__(self)`: Representation (`repr(obj)`)
*   `__getitem__(self, key)`: Accessing items by index (`obj[key]`)
*   `__setitem__(self, key, value)`: Setting items by index (`obj[key] = value`)

## Example: Creating a `Vector` Class

Imagine a 2D vector class that represents a point `(x, y)`. We want to be able to add two vectors together.

```python
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Check if the 'other' object is also a Vector2D
        if not isinstance(other, Vector2D):
            return NotImplemented
        # Return a *new* Vector2D object that is the sum of the two.
        return Vector2D(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

v1 = Vector2D(2, 4)
v2 = Vector2D(1, 5)

# Because we defined __add__, we can use the '+' operator
result = v1 + v2

print(result)  # Output: Vector2D(3, 9)
```

## `NotImplemented`

In the example above, `NotImplemented` is a special constant. By returning it, you are telling the Python interpreter that your method does not know how to handle the operation with the given `other` object.

This gives the `other` object a chance to handle the operation. If `v1 + my_object` is called and `v1.__add__(my_object)` returns `NotImplemented`, Python will then try to call `my_object.__radd__(v1)` (the "reflected" addition). If that also fails, a `TypeError` is raised. This makes operator overloading more flexible and robust.
