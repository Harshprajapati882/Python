# Match

## What is `match` (structural pattern matching)

`match` is Python's structural pattern matching statement (introduced in Python 3.10). It allows you to compare a value against one or more patterns and destructure complex data in a clear, readable way.

## Why it was added

- To replace long `if`/`elif` chains that inspect the shape of data.
- To make data deconstruction explicit and concise (tuples, lists, dicts, dataclasses, classes).
- To make code for parsing and routing (e.g., AST visitors, message handlers) more declarative and maintainable.

## When to use `match`

- When you need to branch logic based on the *structure* of a value (not just equality). 
- When you want to unpack and bind parts of a data structure directly in the control flow.
- For parsing nested data (JSON-like structures), command dispatch, AST or protocol handling.

## Key concepts

- Patterns: literals, variable capture, sequence patterns, mapping patterns, class patterns, wildcard `_`.
- Guards: add extra conditions with `if` after a pattern.
- OR patterns: match multiple alternative patterns with `|`.
- Capture-rest: use `*rest` in sequence patterns.

## Examples

See the companion `Match.py` for runnable examples. Below are concise examples and explanations.

### 1) Literal matching

```
match value:
	case 0:
		...
	case 1:
		...
```

Use this when matching specific constant values.

### 2) Capture and wildcard

```
match point:
	case (0, y):       # captures y when x==0
		...
	case (x, y):
		...
	case _:
		...          # wildcard: matches anything
```

### 3) Sequence and rest

```
match seq:
	case [first, *rest]:
		...
```

### 4) Mapping (dict) patterns

```
match data:
	case {"type": "point", "x": x, "y": y}:
		...
```

### 5) Class patterns

If a class defines `__match_args__`, you can match and extract fields:

```
class P:
	__match_args__ = ("x", "y")
	def __init__(self, x, y):
		self.x = x
		self.y = y

match obj:
	case P(x, y):
		...
```

### 6) Guards and OR patterns

```
match value:
	case x if x > 0:
		...
	case 0 | 1 | 2:
		...
```

## Notes and best practices

- Prefer `match` when control flow depends on structure rather than single-value equality.
- Avoid overusing `match` for trivial equality checks — basic `if` may be clearer.
- Keep patterns simple and readable; complex nested patterns can be harder to maintain.

## See also

- `Match.py` for runnable examples demonstrating the patterns above.

