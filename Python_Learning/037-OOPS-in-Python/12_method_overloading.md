# Method Overloading

Method overloading is the ability to define multiple methods with the same name but with different parameters (either a different number of parameters or different types of parameters) within the same class. The correct method to call is determined at compile time based on the arguments provided.

## Method Overloading in Python: The Reality

**Python does not support traditional method overloading in the same way that statically-typed languages like Java or C++ do.**

In Python, if you define two methods with the same name, the second definition will simply overwrite the first one. The interpreter only recognizes the last-defined version of the method.

```python
class MyClass:
    def my_method(self, x):
        print(f"Method with one argument: {x}")

    def my_method(self, x, y):
        print(f"Method with two arguments: {x}, {y}")

obj = MyClass()
# obj.my_method(10)      # This will cause a TypeError!
# TypeError: my_method() missing 1 required positional argument: 'y'

obj.my_method(10, 20)  # This works fine.
# Output: Method with two arguments: 10, 20
```
As you can see, only the second `my_method` definition is active.

## How to Achieve Overloading-like Behavior in Python

While Python doesn't have built-in method overloading, you can achieve similar functionality using a few common patterns.

### 1. Using Default Arguments

The most straightforward way is to define a single method with default values for its optional parameters. This allows the method to be called with a variable number of arguments.

```python
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))       # 5
print(calc.add(2, 3, 5))    # 10
```

### 2. Using Variable-Length Argument Lists (`*args` and `**kwargs`)

You can define a single method that can accept any number of positional or keyword arguments. Inside the method, you can inspect the number and type of arguments and change the behavior accordingly.

```python
class Greeter:
    def greet(self, *args):
        if len(args) == 1:
            print(f"Hello, {args[0]}!")
        elif len(args) == 2:
            print(f"Hello, {args[0]} and {args[1]}!")
        else:
            print("Hello, everyone!")

g = Greeter()
g.greet("Alice")
g.greet("Alice", "Bob")
g.greet("Alice", "Bob", "Charlie")
```

### 3. Using `functools.singledispatch`

For cases where you want to vary the behavior based on the **type** of the first argument, the `@singledispatch` decorator from the `functools` module is a powerful and elegant solution. It allows you to register different "versions" of a function for different types.

This is a more advanced technique but provides a very clean way to implement type-based overloading.
