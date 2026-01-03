"""Tuple examples and quick assertions.

Run this file to see example outputs and to verify behaviors via assertions.
"""

from collections import namedtuple


def examples():
    # Creation
    t1 = (1, 2, 3)
    t2 = 4, 5, 6  # implicit tuple
    empty = ()
    single = (42,)

    # Indexing and slicing
    assert t1[0] == 1
    assert t1[1:3] == (2, 3)

    # Immutability -> cannot assign: uncommenting below raises TypeError
    # t1[0] = 100

    # Concatenation and repetition produce new tuples
    t3 = t1 + t2
    assert t3 == (1, 2, 3, 4, 5, 6)
    assert t1 * 2 == (1, 2, 3, 1, 2, 3)

    # Methods
    t = (1, 2, 2, 3)
    assert t.count(2) == 2
    assert t.index(3) == 3

    # Packing / unpacking
    a, b, c = t1
    assert (a, b, c) == (1, 2, 3)

    x, *rest = t3
    assert x == 1
    assert rest == [2, 3, 4, 5, 6] or rest == (2, 3, 4, 5, 6)

    # Single-element nuance
    not_a_tuple = (1)
    assert type(not_a_tuple) is int
    assert type(single) is tuple

    # Use as dict key (immutable)
    d = {}
    key = ("user", 1)
    d[key] = "value"
    assert d[("user", 1)] == "value"

    # Nested tuples
    nested = ((1, 2), (3, 4))
    assert nested[1][0] == 3

    # Convert between list and tuple
    li = [1, 2, 3]
    t_from_list = tuple(li)
    assert type(t_from_list) is tuple
    assert list(t_from_list) == li

    # namedtuple example - readable, tuple-like record
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(2, 3)
    assert p.x == 2 and p.y == 3
    assert isinstance(p, tuple)

    # Swap using tuple unpacking
    a, b = 10, 20
    a, b = b, a
    assert (a, b) == (20, 10)

    print("All tuple examples passed.")


if __name__ == "__main__":
    examples()
