
**Range in Python**

- **Purpose:** `range()` generates an immutable sequence of integers. It's commonly used for looping a specific number of times or generating index sequences.

**Syntax:**

- `range(stop)` — generates 0, 1, 2, ..., stop-1
- `range(start, stop)` — generates start, start+1, ..., stop-1
- `range(start, stop, step)` — generates values from start to stop-1 stepping by step

**Parameters:**

- `start` (optional): integer where sequence starts (default 0)
- `stop` (required): integer where sequence ends (exclusive)
- `step` (optional): integer step (can be negative)

**Key properties:**

- `range()` returns a range object (an iterable), not a list — it's memory efficient.
- The `stop` value is exclusive: it is not included in the generated sequence.
- `step` may be negative to generate a descending sequence.

**Common uses & examples:**

- Looping a fixed number of times:

	for i in range(5):
			# i -> 0,1,2,3,4

- Specifying a start:

	for i in range(2, 6):
			# i -> 2,3,4,5

- Using a step:

	for i in range(0, 10, 2):
			# i -> 0,2,4,6,8

- Descending sequences (negative step):

	for i in range(5, 0, -1):
			# i -> 5,4,3,2,1

**Working with indices:**

- Iterate over indices of a sequence:

	for i in range(len(my_list)):
			process(my_list[i])

- Prefer `enumerate()` when you need both index and value:

	for i, val in enumerate(my_list):
			process(i, val)

**Performance / memory:**

- `range()` is lazy and stores only start/stop/step; converting to `list(range(...))` allocates memory for all values.

	import sys
	sys.getsizeof(range(1000000))      # small
	sys.getsizeof(list(range(1000000))) # much larger

**Pitfalls:**

- Off-by-one errors: remember `stop` is exclusive.
- Using a step of 0 raises `ValueError`.

**Compatibility:**

- In Python 3, `range()` behaves like the old Python 2 `xrange()` (i.e., returns an iterable). Python 2 `range()` returned a list.

**See examples:** runnable examples are provided in [Python_Learning/008-Range/range.py](Python_Learning/008-Range/range.py).

**Short checklist:**

- Use `range(stop)` for simple counts.
- Use `range(start, stop)` to offset the beginning.
- Use `range(start, stop, step)` for steps or reversing.
