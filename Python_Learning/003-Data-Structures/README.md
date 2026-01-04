 
# Python Data Structures — Notes

This file summarizes Python's built-in data structures, common operations, performance characteristics, and recommended topics to learn.

## Built-in structures
- List (`list`): ordered, mutable sequence. Good for indexed access and ordered collections.
	- Common ops: append, extend, insert, pop, remove, slicing, iteration.
	- Complexity: indexing O(1), append amortized O(1), insert/delete O(n).

- Tuple (`tuple`): ordered, immutable sequence. Use for fixed collections and keys in dicts.
	- Common ops: indexing, unpacking, iteration.
	- Complexity: similar to `list` for read access, but immutable.

- Set (`set`) and `frozenset`: unordered collections of unique elements.
	- Common ops: add, remove, membership test, set operations (union, intersection, difference).
	- Complexity: average O(1) for membership/add/remove.

- Dictionary (`dict`): mapping of keys to values. Ordered (insertion order) since Python 3.7.
	- Common ops: get, set, pop, keys/values/items, iteration.
	- Complexity: average O(1) for lookup/insert/delete.

- String (`str`): immutable sequence of Unicode characters. Supports slicing, formatting.

- Bytes/Bytearray: immutable/mutable byte sequences for binary data.

- Range (`range`): efficient immutable sequence of integers commonly used in loops.

## Collections module (specialized structures)
- `deque`: double-ended queue for fast appends/pops from both ends (O(1)).
- `defaultdict`: dict subclass that provides default values for missing keys.
- `Counter`: multiset for counting hashable items.
- `namedtuple`: lightweight tuple with named fields.
- `OrderedDict`: (mostly historical) preserves insertion order — built-in dict now does this.

## Array & binary-heap utilities
- `array.array`: compact arrays of basic C types (homogeneous data) useful for memory efficiency.
- `heapq`: heap functions for priority queues (min-heap by default).
- `bisect`: helpers for binary-search insertions into sorted lists.

## Key topics to learn
- Mutability vs immutability and when to use each.
- Time and space complexity for common operations.
- Iteration patterns and comprehensions.
- Choosing the right container for the job (order, uniqueness, fast lookups, memory).
- Using `collections` and `itertools` for efficient building blocks.

## Exercises
1. Implement frequency counting with `dict` and `Counter` and compare code clarity.
2. Use `bisect` to maintain a sorted list of timestamps.
3. Implement a simple priority queue using `heapq`.
4. Compare `list` vs `deque` for queue workloads (many pops from left).

## Further reading
- Official Python docs: Data structures section.
- `collections` and `itertools` docs.
