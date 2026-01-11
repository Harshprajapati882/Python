# Duck Typing

Duck typing is a concept in programming related to dynamic typing. The name comes from the "duck test":

> "If it walks like a duck and it quacks like a duck, then it must be a duck."

In the context of Python, this means that the **type of an object is less important than the methods and properties it possesses**. If an object has the necessary methods and attributes to perform a certain operation, then it can be used in that operation, regardless of its actual class or what it inherits from.

This is a form of polymorphism that is not based on inheritance. It's an "informal interface" that relies on behavior rather than on a declared type.

## How it Works

Instead of checking an object's type with `isinstance()`, code that uses duck typing simply assumes the object has the methods it needs and calls them.

```python
class Duck:
    def fly(self):
        print("Duck flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

class Fish:
    def swim(self):
        print("Fish swimming")

def make_it_fly(flying_object):
    # This function doesn't care if the object is a Duck or an Airplane.
    # It only cares that it has a .fly() method.
    flying_object.fly()

duck = Duck()
plane = Airplane()
fish = Fish()

make_it_fly(duck)   # Works, output: "Duck flying"
make_it_fly(plane)  # Works, output: "Airplane flying"
# make_it_fly(fish) # This would raise an AttributeError because a Fish object has no .fly() method.
```
The `make_it_fly` function operates on any object that "quacks" like a flying object (i.e., has a `fly` method).

## Duck Typing vs. Static Typing

This is a major difference from statically-typed languages (like Java or C#). In those languages, you would typically define a formal `IFlyable` interface and make sure both `Duck` and `Airplane` implement it.

```java
// Java example
public interface IFlyable {
    void fly();
}

public void makeItFly(IFlyable flyingObject) {
    flyingObject.fly();
}
```

In Python, you can achieve this same level of formality using Abstract Base Classes (ABCs), but the default and most "Pythonic" approach is often to rely on duck typing for its simplicity and flexibility.

## EAFP: "Easier to Ask for Forgiveness than Permission"

Duck typing is closely related to a common coding style in Python known as EAFP: **E**asier to **A**sk for **F**orgiveness than **P**ermission.

This style assumes an object has the necessary methods and wraps the call in a `try...except` block to handle cases where it doesn't.

```python
def make_it_fly_safely(any_object):
    try:
        any_object.fly()
    except AttributeError:
        print(f"This object of type {type(any_object).__name__} can't fly.")

make_it_fly_safely(duck)  # Works
make_it_fly_safely(plane) # Works
make_it_fly_safely(fish)  # Fails gracefully
```
This is often considered more Pythonic than the LBYL ("Look Before You Leap") approach, which would involve checking `hasattr(obj, 'fly')` before calling the method.
