"""Small math utilities with usage examples.

Provided functions:
- add(a, b)
- mul(a, b)
- sub(a, b)
- div(a, b)
- power(a, b)
- factorial(n)
- mean(seq)

Examples (run as a script):
    $ python -m mypkg.math_ops

This module is intentionally tiny and dependency-free for learning.
"""

from typing import Iterable


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def sub(a, b):
    return a - b


def div(a, b):
    """Divide `a` by `b`. Raises ZeroDivisionError on zero denominator."""
    return a / b


def power(a, b):
    return a ** b


def factorial(n: int) -> int:
    """Return n! for n >= 0. Raises ValueError for negative n."""
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def mean(seq: Iterable[float]) -> float:
    """Return arithmetic mean of `seq`. Raises ValueError for empty sequence."""
    seq = list(seq)
    if not seq:
        raise ValueError("mean() requires at least one value")
    return sum(seq) / len(seq)


__all__ = [
    "add",
    "mul",
    "sub",
    "div",
    "power",
    "factorial",
    "mean",
]


def _demo():
    print("Examples from mypkg.math_ops:\n")
    print("add(2, 3)", add(2, 3))
    print("mul(4, 5)", mul(4, 5))
    print("sub(5, 2)", sub(5, 2))
    print("div(6, 2)", div(6, 2))
    print("power(2, 8)", power(2, 8))
    print("factorial(5)", factorial(5))
    print("mean([1,2,3,4])", mean([1, 2, 3, 4]))


if __name__ == "__main__":
    _demo()
