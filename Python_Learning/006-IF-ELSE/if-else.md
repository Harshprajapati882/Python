**If / Else (Python)**

Overview:
- **If statement:** run code when a condition is true.
- **If-else:** choose between two branches.
- **If-Elif-Else:** chain multiple mutually exclusive conditions.
- **Nested ifs:** conditionals inside other conditionals.
- **Ternary (conditional expression):** single-line `a if cond else b`.
- **Guard clause / early return:** return early from a function instead of nesting.
- **Short-circuit booleans:** use `and` / `or` to combine conditions concisely.

Examples (conceptual):
- `if cond:` — run when `cond` truthy.
- `if cond:\n    ...\nelse:\n    ...`
- `if a:\n    ...\nelif b:\n    ...\nelse:\n    ...`
- `x = a if cond else b`  (ternary)

When to use each:
- **Simple `if`**: only one condition to check and action is optional. Use when the check is cheap and clear.
- **`if-else`**: when you need an either/or result (exactly two mutually exclusive paths).
- **`if-elif-else`**: when you have several mutually exclusive, ordered conditions. Use sparingly — prefer a dispatch table when you have many cases.
- **Nested `if`**: use when an inner decision only makes sense after an outer decision. Avoid deep nesting — refactor to functions or guard clauses.
- **Ternary expression**: for short, readable expressions that fit on one line (assignments or small returns). Avoid for complex logic.
- **Guard clause / early return**: often clearer than nesting; use at start of function to handle edge cases.
- **Short-circuit logic (`and` / `or`)**: great for concise combined conditions, but be careful with side effects when using function calls.

When not to use / alternatives:
- **Too many `elif` branches**: don't use long chains of `elif` for dozens of cases — use a dictionary dispatch (mapping keys to functions or values) or `match` (Python 3.10+).
- **Deep nesting**: avoid; use guard clauses or split into helper functions.
- **Complex boolean expressions**: consider splitting into named boolean variables (for readability) or encapsulate logic in a function with a descriptive name.
- **Using `if` to select behavior across many values**: use a dictionary dispatch or `match` instead of many `elif` clauses.

Alternatives and when to prefer them:
- **Dictionary dispatch**: prefer when cases are keyed by simple values (strings, enums, ints). Faster and more maintainable than many `elif`.
- **`match` / pattern matching**: prefer when matching complex data shapes (tuples, dicts, classes) — clearer than nested `if`.
- **Exceptions**: use exceptions for exceptional error handling, not for normal control flow.
- **Polymorphism / OOP**: prefer object-oriented dispatch when behavior depends on object type; use subclassing or strategy pattern to avoid conditional logic spread across code.

Style tips:
- Keep conditions simple and readable; extract complex expressions into well-named variables.
- Prefer explicit comparisons (`if x == 0`) over relying on truthiness when the meaning matters.
- Comment intent, not mechanics — explain WHY a branch exists when it's not obvious.

See `if-else.py` for runnable patterns and quick tests.

