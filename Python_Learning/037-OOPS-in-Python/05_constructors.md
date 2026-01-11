# Constructors in Python

In object-oriented programming, a constructor is a special method used to initialize a newly created object. In Python, the constructor method is named `__init__`.

The `__init__` method is automatically called when you create an instance (object) of a class. Its primary purpose is to set up the initial state of the object by assigning values to its properties (attributes).

## Key Characteristics of the `__init__` Constructor

*   **Automatic Invocation**: You don't call `__init__` directly. It gets called automatically when you instantiate a class, like `my_object = MyClass(arg1, arg2)`.

*   **First Argument `self`**: The first parameter of `__init__` must always be `self`. This parameter is a reference to the newly created object, allowing you to attach attributes to it.

*   **Initializing Attributes**: Inside `__init__`, you define and initialize the instance attributes for the object. These attributes hold the state of the object.

## Types of Constructors

While Python only has one constructor method, `__init__`, we can think of its usage in a few different ways based on the parameters it accepts.

1.  **Default Constructor**: If a class does not define an `__init__` method, Python provides a default one that does nothing. It allows you to create an instance of the class, but the object will have no instance attributes upon creation.

2.  **Parameterized Constructor**: This is the most common type. The `__init__` method accepts arguments in addition to `self`. These arguments are used to initialize the instance attributes with specific values when the object is created.

## Destructors

The counterpart to a constructor is a destructor, which is called when an object is about to be destroyed or garbage collected. In Python, the destructor method is `__del__`.

*   **`__del__(self)`**: This method is called when an object's reference count drops to zero.
*   **Use with Caution**: It's important to be careful with `__del__`. The exact timing of when it's called is not guaranteed. It's generally better to use explicit `close()` methods or context managers (`with` statement) for cleaning up resources like files or network connections.
