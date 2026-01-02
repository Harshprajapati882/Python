(#) Continue and Break in Python

This note explains `break` and `continue` statements, when to use them, common patterns, and alternatives (including switch-like constructs).

- **`break`**: Immediately exit the nearest enclosing loop. Use when you have found what you need and further iterations are unnecessary.
- **`continue`**: Skip the rest of the current loop iteration and proceed to the next iteration. Use when the current item should be ignored but the loop should continue.

When to use:
- Use `break` to stop searching early (e.g., stop when a match is found).
- Use `continue` to skip invalid or irrelevant items and keep the loop logic simple.

Common patterns and gotchas:
- **For-else**: A `for` loop can have an `else` block that runs if the loop completes normally (no `break`). Use this to distinguish "found" vs "not found" cases.
- **Nested loops**: `break` only exits the innermost loop. To break out of multiple levels, use a flag, raise an exception, or refactor into a function and `return`.
- **Avoid overuse**: Excessive `break`/`continue` can make logic harder to read. Sometimes restructuring (helper functions, filtering data first) is clearer.

Switch / Case alternatives in Python:
- Python doesn't have a C-style `switch` statement. From Python 3.10 there is `match` (structural pattern matching) which covers many switch-like uses.
- For simple value dispatch, prefer `if-elif` chains or a dictionary mapping values to callables.

Example quick references:

- For search with `break` and `for-else` — stops on first match and detects not-found.
- Use `continue` to skip processing some items (e.g., skip negatives).

See the companion `Conti&Br.py` for runnable examples and short output demonstration.

