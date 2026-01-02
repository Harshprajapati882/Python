# OOP in Python — Methods, Patterns, and Examples

Core concepts:
- Classes and instances
- Encapsulation (private/protected conventions)
- Inheritance (single, multiple) and MRO
- Polymorphism and duck typing
- Abstraction and interfaces (`abc`)

Important method types and special methods:
- `__init__(self, ...)` — constructor
- `__new__(cls, ...)` — instance creation
- `__repr__(self)` / `__str__(self)` — readable representations
- Comparison: `__eq__`, `__lt__`, `__le__`, etc.
- Numeric ops: `__add__`, `__sub__`, `__mul__`, ...
- Container protocol: `__len__`, `__contains__`, `__iter__`, `__getitem__`, `__setitem__`
- Context manager: `__enter__`, `__exit__`
- Callable objects: `__call__`

Decorators and attribute helpers:
- `@classmethod` — method receives class `cls`
- `@staticmethod` — no implicit first argument
- `@property` — attribute access via methods
- Descriptors for advanced attribute control

Design guidance:
- Prefer composition over inheritance for many cases
- Keep methods small and single-responsibility
- Use ABCs for clear interfaces when needed

Example usage patterns and exercises:
- Implement a `Person` / `Employee` hierarchy with properties
- Create a custom container implementing iteration and indexing
- Write a context-manager class for resource handling

See example scripts in `Python_Learning/examples/` for runnable demonstrations.
