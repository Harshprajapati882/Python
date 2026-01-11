# Access Modifiers in Python

Access modifiers are keywords that set the accessibility (visibility) of classes, methods, and other members. In many object-oriented languages like Java or C++, `public`, `private`, and `protected` are used to control access.

Python does not have explicit keywords for access modifiers. Instead, it relies on a convention using underscores (`_`) in attribute names to indicate their intended visibility. This is a form of "gentleman's agreement" among developers.

## 1. Public Members

*   **Convention**: No leading underscore.
*   **Accessibility**: Public members can be accessed from anywhere, both inside and outside the class. This is the default behavior.

    ```python
    class MyClass:
        def __init__(self):
            self.public_var = "I am public"
    ```

## 2. Protected Members

*   **Convention**: Single leading underscore (e.g., `_protected_var`).
*   **Accessibility**: This is a hint to other programmers that the attribute or method is intended for internal use within the class and its subclasses. However, Python does *not* enforce this. You can still access protected members from outside the class.

    ```python
    class MyClass:
        def __init__(self):
            self._protected_var = "I am protected"
    ```
    The single underscore tells other developers: "Don't touch this unless you are a subclass."

## 3. Private Members

*   **Convention**: Double leading underscore (e.g., `__private_var`).
*   **Accessibility**: This triggers a mechanism called **name mangling**. Python internally changes the name of the attribute to `_ClassName__attributeName`. This makes it much harder to access from outside the class, effectively making it private.
*   **Why use it?**: Name mangling is primarily intended to avoid accidental name clashes with attributes in subclasses. It's not for strict security, but to prevent overriding by mistake.

    ```python
    class MyClass:
        def __init__(self):
            self.__private_var = "I am private"
    
    obj = MyClass()
    # print(obj.__private_var)  # This will raise an AttributeError
    # You can still access it if you know the mangled name:
    # print(obj._MyClass__private_var) 
    ```

## Getters and Setters

To provide controlled access to "private" or "protected" attributes, we can use getter and setter methods. This is a key part of encapsulation.

*   **Getter**: A method to get the value of an attribute.
*   **Setter**: A method to set the value of an attribute, often with some validation logic.

Python also provides the `@property` decorator as a more "Pythonic" way to manage getters and setters, making them feel like regular attribute access.
