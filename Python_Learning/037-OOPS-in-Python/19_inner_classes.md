# Inner Classes (Nested Classes)

An inner class, or nested class, is a class defined inside another class. This is a way to group classes that are logically related, creating a more organized and encapsulated structure.

```python
class OuterClass:
    # Outer class attributes and methods

    class InnerClass:
        # Inner class attributes and methods
        pass
```

## Why Use Inner Classes?

1.  **Encapsulation and Scoping**: If a class is only ever used by one other class, it makes sense to define it inside that class. This hides the inner class from the global scope, avoiding clutter and making it clear that the inner class is a helper or detail of the outer class. The relationship becomes more explicit.

2.  **Logical Grouping**: It provides a way to structure code where one class is conceptually a component of another. For example, a `Car` class might have an `Engine` inner class, because an `Engine` is an integral part of a `Car` and might not need to be exposed as a standalone class.

3.  **Access to Outer Class Data**: While the inner class does not automatically have access to the outer class's instance data (like `self`), it's common to pass an instance of the outer class to the inner class's constructor. This allows the inner object to interact with the state of its containing object.

## How to Use Inner Classes

You typically instantiate the outer class first, and then you can create instances of the inner class. The inner class is accessed as an attribute of the outer class.

```python
class Car:
    def __init__(self, make):
        self.make = make
        # The Car object can create its own Engine object
        self.engine = self.Engine("V8")

    def start(self):
        print(f"Starting the {self.make}...")
        self.engine.start()

    class Engine:
        def __init__(self, type):
            self.type = type

        def start(self):
            print(f"Starting the {self.type} engine.")

# Create an instance of the outer class
my_car = Car("Ford")
my_car.start()

# You can also create an instance of the inner class separately,
# though this is less common.
engine_instance = Car.Engine("V6")
engine_instance.start()
```

In this example, the `Engine` is tightly coupled with the `Car`. Defining it as an inner class makes this relationship clear and keeps the `Engine` class out of the global namespace where it might not be relevant.
