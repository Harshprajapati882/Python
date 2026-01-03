**Tuples — Notes & Examples**
- **Definition:** Tuples are ordered, immutable sequences in Python. They can contain heterogeneous items (different types).
- **Literal syntax:** Use parentheses () or comma-separated values. For a single-item tuple include a trailing comma: `(1,)`.
- **Common operations:** indexing, slicing, iteration, length (`len()`), membership (`in`).
- **Immutability:** You cannot change items in-place. You can, however, create new tuples from existing ones (concatenation, repetition).
- **Useful methods:** `tuple.count(value)` and `tuple.index(value)`.
- **Packing/Unpacking:** Assign multiple values at once: `a, b = (1, 2)`. Use starred expression for variable-length unpacking: `a, *rest = t`.
- **Use cases:** Fixed collections, function returns, dictionary keys (hashable), small records (or use `namedtuple` / `dataclass`).
- **Performance:** Tuples are slightly more memory- and time-efficient than lists for immutable sequences.
**Quick Reference**
- Create: `t = (1, 2, 3)` or `t = 1, 2, 3`
- Single-item: `t = (1,)`
- Empty tuple: `t = ()`
- Index: `t[0]`, slice: `t[1:3]`
- Convert between list/tuple: `list(t)`, `tuple(list_of_items)`
**Examples**
See the example file: [Tuple.py](Python_Learning/013-Tuples/Tuple.py)
**Examples explained**
- Single-element tuple needs a trailing comma, otherwise it's just parentheses around the value.
- Unpacking allows easy swapping: `a, b = b, a` (tuple packing/unpacking under the hood).
- Using tuples as dictionary keys requires immutability and hashability of the contents.
- `namedtuple` from `collections` provides field names and readable reprs for tuple-like records.
If you want more interactive examples, run the examples in [Tuple.py](Python_Learning/013-Tuples/Tuple.py).
