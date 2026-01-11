# Polymorphism in Python

The word "polymorphism" means "many forms". In programming, it refers to the ability of an object or function to take on multiple forms. More specifically, it means that a single interface (like a method name, an operator, or a function) can be used to refer to actions or objects of different types, and the correct action will be executed based on the object's class.

## 1. Polymorphism with Class Inheritance (Method Overriding)

This is the most common form of polymorphism. A subclass can provide its own specific implementation of a method that is already provided by its superclass.

*   **Superclass**: Defines a generic method.
*   **Subclass**: **Overrides** that method with a more specific behavior.

When you have a collection of objects from different subclasses, you can call the same method on all of them, and each object will execute its own version of the method.

```python
class Animal:
    def speak(self):
        print("An animal speaks")

class Dog(Animal):
    def speak(self):  # Method overriding
        print("A dog barks")

class Cat(Animal):
    def speak(self):  # Method overriding
        print("A cat meows")

# A single function can handle different types of objects
def make_animal_speak(animal):
    animal.speak()

make_animal_speak(Dog()) # Output: A dog barks
make_animal_speak(Cat()) # Output: A cat meows
```

## 2. Polymorphism with Duck Typing

Python is a dynamically-typed language, which leads to a concept known as "duck typing". The idea is:

> "If it walks like a duck and it quacks like a duck, then it must be a duck."

In programming terms, this means that the type of an object is less important than the methods it defines. If an object has the methods and properties that your code expects, it can be used, regardless of its actual class or what it inherits from.

This allows for a very flexible form of polymorphism that does not require inheritance.

```python
class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

# This function doesn't care if the object is a Duck or a Person.
# It only cares if the object has a 'quack' method.
def make_it_quack(obj):
    obj.quack()

make_it_quack(Duck())   # Output: Quack, quack!
make_it_quack(Person()) # Output: I'm quacking like a duck!
```

## 3. Polymorphism with Operators (Operator Overloading)

Polymorphism also applies to built-in operators. The `+` operator, for example, behaves differently depending on the type of its operands:
*   For numbers, it performs addition (`3 + 5` is `8`).
*   For strings, it performs concatenation (`"hello" + "world"` is `"helloworld"`).
*   For lists, it performs merging (`[1, 2] + [3, 4]` is `[1, 2, 3, 4]`).

You can define how operators work for your own custom classes by implementing special methods (like `__add__`, `__mul__`, etc.). This is called **operator overloading**.
