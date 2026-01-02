#!/usr/bin/env python3
"""Runnable examples for Pips & Modules chapter.

Demonstrates importing the local package `mypkg` and using its API.
"""

from mypkg import add, mul


def demo_local_package():
    a, b = 7, 5
    print(f"add({a}, {b}) ->", add(a, b))
    print(f"mul({a}, {b}) ->", mul(a, b))


if __name__ == "__main__":
    demo_local_package()
