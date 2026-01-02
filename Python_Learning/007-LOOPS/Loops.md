
# Loops in Python

This file summarizes loop types, common topics, controls, and examples. See `Loops.py` for runnable examples.

1) What is a loop?
- A loop repeats a block of code while a condition holds or over items in a sequence.

2) Loop types
- `for` loop: iterate over any iterable (list, tuple, dict, string, range, generator).
- `while` loop: repeat while a condition is True.

3) Key topics
- Iterables and iterators: `for` works with any iterable; use `iter()` and `next()` for manual iteration.
- `range()` for numeric sequences.
- `enumerate()` to get index + value.
- `zip()` to iterate multiple iterables in parallel.
- Loop controls: `break` (exit loop), `continue` (skip to next iteration), `pass` (no-op).
- `for`/`while` + `else`: `else` runs if loop completes without `break`.
- Nested loops: a loop inside another loop.
- Comprehensions: compact way to build lists/sets/dicts using loops.

4) Common patterns
- Summing or searching: use `for` with accumulator or `while` for condition-based loops.
- Iterating dicts: `for k, v in d.items()`.
- Safe removal during iteration: avoid modifying a list while iterating; use list comprehension or iterate over a copy.

5) Examples (in `Loops.py`)
- Basic `for` over list and `range()`.
- `for` with `enumerate`, `zip`, and dicts.
- `while` loop and `break`/`continue`.
- Nested loops and `for`/`else` behavior.
- List comprehension equivalents.

6) Tips and gotchas
- Infinite loops: ensure `while` loops change state that can end the loop.
- Off-by-one: `range(n)` goes 0..n-1.
- Using `break` prevents the loop `else` block from running.

7) Exercises
- Write a function that returns the first duplicate in a list using loops.
- Use a `while` loop to implement a simple number guessing game.
- Convert nested loops into a comprehension when possible.

For runnable code and output, open [Loops.py](Loops.py).

