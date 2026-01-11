# Wrapper Classes (Decorator Pattern)

A wrapper class, often associated with the **Decorator** or **Proxy** design patterns, is a class that "wraps around" or contains an instance of another class. Its purpose is to add new functionality or modify the existing behavior of the wrapped object without changing its source code.

This is a powerful technique for extending the capabilities of classes, especially when you cannot (or should not) modify the original class, such as when it comes from a third-party library.

## How it Works

1.  **Composition**: The wrapper class holds an instance of the target object as an attribute. This is an example of "composition over inheritance".
2.  **Delegation**: The wrapper class implements the same interface (methods) as the wrapped object. When a method is called on the wrapper, it can add its own logic before, after, or instead of calling the corresponding method on the wrapped object. This is called **delegation**.
3.  **Attribute Access**: To make the wrapper behave exactly like the original object, you often need to forward all attribute and method lookups that aren't explicitly handled by the wrapper to the wrapped object. This can be done by implementing the special `__getattr__` method.

## Example Scenario

Imagine you have a simple `File` object that can `read()` and `write()`. You want to add logging to every read and write operation without modifying the original `File` class.

You can create a `LoggingFileWrapper` class.

1.  It will take a `File` object in its constructor and store it.
2.  It will have its own `read()` method. Inside this method, it will first print a log message and *then* call the original `file.read()` method.
3.  It will do the same for the `write()` method.

```python
class File:
    def __init__(self, filename):
        self._filename = filename
    def read(self):
        # logic to read file
        return "File content"
    def write(self, data):
        # logic to write file
        pass

class LoggingFileWrapper:
    def __init__(self, file_object):
        self._wrapped_obj = file_object

    def read(self):
        print(f"LOG: Reading from {self._wrapped_obj._filename}")
        return self._wrapped_obj.read()

    def write(self, data):
        print(f"LOG: Writing to {self._wrapped_obj._filename}")
        return self._wrapped_obj.write(data)

# Usage
real_file = File("my_data.txt")
logged_file = LoggingFileWrapper(real_file)

content = logged_file.read() # Will print a log message and then read.
```

## `__getattr__` for Transparent Wrapping

The example above only works for the `read` and `write` methods. What if the original object had other methods that we didn't explicitly define in the wrapper? Trying to call them would fail.

The `__getattr__(self, name)` method provides a solution. It's a special method that is called automatically when you try to access an attribute that doesn't exist on an object. We can use it to delegate the lookup to the wrapped object.

```python
class Wrapper:
    def __init__(self, obj):
        self._wrapped_obj = obj
    
    def __getattr__(self, name):
        # If an attribute is not found on the wrapper,
        # get it from the wrapped object instead.
        return getattr(self._wrapped_obj, name)
```
This makes the wrapper "transparent" for any attributes or methods it doesn't explicitly override.
