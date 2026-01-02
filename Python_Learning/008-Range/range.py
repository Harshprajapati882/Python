
#!/usr/bin/env python3
"""Runnable examples for Python `range()` usage.

Run with:

	python3 Python_Learning/008-Range/range.py

This file demonstrates common patterns, memory behaviour, and typical pitfalls.
"""

import sys


def demo_basic():
	print("basic:", list(range(5)))


def demo_start_stop():
	print("start-stop:", list(range(2, 6)))


def demo_step():
	print("step:", list(range(0, 10, 2)))


def demo_negative():
	print("negative step:", list(range(5, 0, -1)))


def demo_indices_and_enumerate():
	sample = ['a', 'b', 'c', 'd']
	by_index = [sample[i] for i in range(len(sample))]
	by_enum = [(i, v) for i, v in enumerate(sample)]
	print("indices:", by_index)
	print("enumerate:", by_enum)


def demo_memory():
	# range is lightweight; list(range(...)) allocates full memory
	r = range(10_000_000)
	lst = list(range(10_000_000))
	print("range object size:", sys.getsizeof(r))
	print("list size:", sys.getsizeof(lst))
	# show small slice without converting entire range
	print("first 5 of range:", list(r[:5]))


def main():
	demo_basic()
	demo_start_stop()
	demo_step()
	demo_negative()
	demo_indices_and_enumerate()
	demo_memory()


if __name__ == "__main__":
	main()

