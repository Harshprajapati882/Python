# `__str__` and `__repr__`

`__str__` and `__repr__` are special methods, often called "dunder" (double underscore) methods, that you can define in your Python classes to control how your objects are converted to strings.

While they both produce strings, they have different intended purposes and audiences.

## `__str__`

*   **Purpose**: To return an **"informal"** or "user-friendly" string representation of an object.
*   **Audience**: The end-user of your program.
*   **Goal**: Readability. The output should be easy to understand.
*   **How it's called**:
    *   By the `str()` built-in function: `str(my_object)`
    *   By the `print()` function.
    *   By string formatting (f-strings or `.format()`).

If you define `__str__`, printing your object will produce a clean, readable output.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(10, 20)
print(p)  # Output: (10, 20)
```

## `__repr__`

*   **Purpose**: To return an **"official"** or "developer-friendly" string representation of an object.
*   **Audience**: The developer (for debugging, logging, etc.).
*   **Goal**: To be unambiguous and, if possible, to be a valid Python expression that could be used to recreate the object with the same state. A common convention is to format the string like a constructor call (e.g., `ClassName(arg1=value1, ...)`).
*   **How it's called**:
    *   By the `repr()` built-in function: `repr(my_object)`
    *   When you type the object's name into an interactive Python console and press Enter.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(10, 20)
print(repr(p))  # Output: Point(x=10, y=20)
# In a console, just typing 'p' would also show this output.
```

## How They Interact

1.  If you call `print()` or `str()` on an object, Python looks for a `__str__` method.
2.  If a `__str__` method is **not found**, Python will fall back and use the `__repr__` method instead.
3.  If neither is found, it uses the default representation, which looks something like `<__main__.ClassName object at 0x...>`.

## Best Practice

*   **Always implement `__repr__`**: Every class you write should have an unambiguous `__repr__` for the sake of the developer (you!). It makes debugging much easier. A good `__repr__` is invaluable.
*   **Implement `__str__` if you need a "pretty" output**: Only implement `__str__` if you want to provide a separate, user-friendly display format for your object. If your `__repr__` is already readable enough for users, you might not need a separate `__str__`.

A common pattern is to have `__repr__` be the definitive, developer-focused representation and then have `__str__` simply call `__repr__` if you don't need a different user format. However, it's often more useful to have them serve their distinct purposes.
