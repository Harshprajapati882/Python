# Descriptors

A descriptor is a Python object that implements a protocol consisting of three special methods: `__get__`, `__set__`, and `__delete__`. Descriptors allow you to create objects that have "managed attributes" – attributes whose access is controlled by the descriptor's methods.

They are a powerful, low-level feature that is the underlying mechanism for many of Python's most common features, including properties, static methods, class methods, and even regular methods.

## The Descriptor Protocol

A class is a descriptor if it implements any of the following methods:

*   `__get__(self, instance, owner)`:
    *   Called when you get the value of an attribute (`instance.attr`).
    *   `self`: The descriptor instance itself.
    *   `instance`: The instance of the class where the descriptor is being accessed (e.g., the `my_obj` in `my_obj.attr`). Will be `None` if accessed on the class itself (`MyClass.attr`).
    *   `owner`: The class that owns the descriptor (e.g., `MyClass`).

*   `__set__(self, instance, value)`:
    *   Called when you set the value of an attribute (`instance.attr = value`).
    *   `instance`: The instance of the owner class.
    *   `value`: The value being assigned to the attribute.

*   `__delete__(self, instance)`:
    *   Called when you delete an attribute (`del instance.attr`).
    *   `instance`: The instance of the owner class.

## Data vs. Non-Data Descriptors

*   **Data Descriptor**: A descriptor that implements `__set__` or `__delete__`. Data descriptors have the highest precedence. If a data descriptor and an instance's `__dict__` attribute have an entry with the same name, the data descriptor takes priority.
*   **Non-Data Descriptor**: A descriptor that only implements `__get__`. Non-data descriptors have lower precedence. If an instance's `__dict__` has an entry with the same name, the `__dict__` entry takes priority. (This is why you can override methods on a per-instance basis).

## How to Use a Descriptor

You create an instance of a descriptor class as a **class attribute** in another class (the "owner" class).

```python
class MyDescriptor:
    def __get__(self, instance, owner):
        print("Getting...")
        return "some value"

class MyClass:
    # 'attr' is an instance of MyDescriptor
    attr = MyDescriptor()

obj = MyClass()
val = obj.attr  # This automatically calls MyDescriptor.__get__
# Output: Getting...
print(val)      # Output: some value
```

## What are Descriptors Used For?

While you might not write descriptors directly very often, understanding them is key to understanding how Python works.

1.  **Properties**: The `@property` decorator is just an elegant way to create a data descriptor. It's the most common use case you'll encounter.
    ```python
    class MyClass:
        @property
        def my_attr(self):
            # This is the __get__ logic
            return self._my_attr
        
        @my_attr.setter
        def my_attr(self, value):
            # This is the __set__ logic
            self._my_attr = value
    ```
2.  **Validation**: Descriptors are excellent for creating reusable attribute validation logic. You can have a descriptor that, for example, ensures an attribute is always a positive integer, and then reuse that descriptor for multiple attributes in multiple classes.

3.  **Methods**: In Python, functions are non-data descriptors. When you access a method on an instance (`my_obj.my_method`), the function's `__get__` method is called. It binds the function to the instance (`my_obj`) and returns a "bound method" object, which is why `self` is passed automatically when you call it.

Descriptors are a fundamental part of Python's object model, providing a powerful and flexible way to control attribute access.
