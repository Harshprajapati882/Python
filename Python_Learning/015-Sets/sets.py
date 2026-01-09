#!/usr/bin/env python3
"""Set examples and demonstrations for Python learners.

Run this file to see common set operations and behaviors.
"""

def examples():
	# Creation
	a = set([1, 2, 3])
	b = {3, 4, 5}
	print("a:", a)
	print("b:", b)

	# Removing duplicates from a list
	lst = [1, 2, 2, 3, 3, 3]
	deduped = set(lst)
	print("deduped from list:", deduped)

	# Membership
	print("2 in deduped:", 2 in deduped)
	print("10 in deduped:", 10 in deduped)

	# Add / discard / remove
	deduped.add(4)
	print("after add(4):", deduped)
	deduped.discard(99)  # safe if not present
	try:
		deduped.remove(99)
	except KeyError:
		print("remove(99) raised KeyError (expected)")

	# pop (removes an arbitrary element)
	popped = deduped.pop()
	print("popped element:", popped)

	# Loop sets
	print("Looping through a set:")
	for item in a:
		print(item)

	# Join sets
	c = a.union(b)
	print("a.union(b):", c)
	d = set(a)
	d.update(b)
	print("a after update(b):", d)

	# Copy sets
	a_copy_method = a.copy()
	a_copy_constructor = set(a)
	print("a_copy_method:", a_copy_method)
	print("a_copy_constructor:", a_copy_constructor)

	# Set algebra
	print("union a|b:", a | b)
	print("intersection a&b:", a & b)
	print("difference a-b:", a - b)
	print("symmetric_difference a^b:", a ^ b)

	# In-place operators
	a_copy = set(a)
	a_copy |= b
	print("a after |= b:", a_copy)

	# Subset / superset
	print("{1,2}.issubset(a):", {1, 2}.issubset(a))
	print("b.isdisjoint(a):", b.isdisjoint(a))

	# frozenset (immutable)
	f = frozenset([1, 2, 3])
	print("frozenset f:", f)

	# Unhashable elements (lists) raise TypeError
	try:
		bad = set([[1, 2]])
	except TypeError as e:
		print("TypeError for unhashable element (list):", e)

	# Set comprehensions
	squares = {x * x for x in range(6)}
	print("squares using set comprehension:", squares)


if __name__ == "__main__":
	examples()
