# Multilevel Inheritance

Multilevel inheritance is a type of inheritance in object-oriented programming where a class inherits from a parent class, which in turn inherits from another parent class. This creates a "chain" of inheritance.

## Structure

The structure looks like this:

*   **Class A** (Grandparent)
    *   **Class B** inherits from **Class A** (Parent)
        *   **Class C** inherits from **Class B** (Child)

In this scenario:
*   `Class B` is a subclass of `Class A`.
*   `Class C` is a subclass of `Class B`.
*   Therefore, `Class C` inherits all the public and protected members of both `Class B` and `Class A`.

## How it Works

When you create an object of the child class (`Class C`), it has access to its own members, plus all the members of its parent (`Class B`) and its grandparent (`Class A`).

When a method is called on an object of `Class C`, Python's Method Resolution Order (MRO) will search for the method in the following order:
1.  `Class C`
2.  `Class B`
3.  `Class A`
4.  `object` (the base class for all classes in Python)

The first occurrence of the method found in this chain is the one that gets executed.

## Example

Consider a hierarchy of electronic devices:

1.  `Device` (Grandparent class): has a `power_on()` method.
2.  `Computer` (Parent class): inherits from `Device` and adds a `run_os()` method.
3.  `Laptop` (Child class): inherits from `Computer` and adds a `charge_battery()` method.

An object of the `Laptop` class will be able to `power_on()`, `run_os()`, and `charge_battery()`. It inherits functionality from each level of the hierarchy.

This is a very natural way to model "is-a" relationships that have multiple levels of specialization. A `Laptop` is a `Computer`, and a `Computer` is a `Device`.
