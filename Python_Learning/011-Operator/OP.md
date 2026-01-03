**Operators And Types — Topic-wise Notes**

- **Scope:** concise notes and examples covering Python data types and all operator categories, with examples in `OP.py`.

**Basic Types**
- **Numeric:** int, float, complex — use for arithmetic and numeric computations.
- **Boolean:** bool (True / False) — used in comparisons and logical operations.
- **Text:** str — immutable sequence of Unicode characters.
- **Sequence:** list, tuple, range — ordered collections (lists mutable, tuples immutable).
- **Mapping:** dict — key/value store.
- **Set:** set, frozenset — unordered unique collections (frozenset immutable).
- **NoneType:** None — represents absence of value.
- **Type checks & conversion:** `type(obj)`, `isinstance(obj, Type)`, `int()`, `float()`, `str()`, `bool()`.

**Operator Categories**
- **Arithmetic Operators:** `+`, `-`, `*`, `/`, `//`, `%`, `**` — standard math, integer division, modulo, exponent.
- **Assignment Operators:** `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` — assign and combine operations.
- **Comparison Operators:** `==`, `!=`, `<`, `>`, `<=`, `>=` — return `bool` results.
- **Logical Operators:** `and`, `or`, `not` — boolean logic with short-circuiting.
- **Bitwise Operators:** `&`, `|`, `^`, `~`, `<<`, `>>` — operate on integers at bit level.
- **Membership Operators:** `in`, `not in` — check membership in sequences/collections.
- **Identity Operators:** `is`, `is not` — check object identity (same object in memory).
- **Ternary (Conditional) Operator:** `x if cond else y` — inline conditional expression.

**Operator Precedence (brief)**
- Highest to lowest (relevant groups): parentheses `()`, exponent `**`, unary `+ - ~`, `*, /, //, %`, `+, -`, bitwise shifts, bitwise AND/OR/XOR, comparisons, `not`, `and`, `or`, `if-else`, assignment.

**Notes & Best Practices**
- Use `//` for integer division results when you need floor division.
- Prefer `is` only for comparing to `None` and singletons, otherwise use `==` for value equality.
- Use `isinstance()` for safe type checks (supports inheritance).

**Where examples live**
- Examples demonstrating each operator category and type behavior are in `OP.py` in the same folder.

**Quick example snippets (see OP.py for full runnable file)**
- Arithmetic: `3 + 2`, `5**2`, `7 // 2`, `7 % 2`
- Comparison: `a == b`, `a != b`, chained comparisons: `1 < x <= 10`
- Logical: `a and b`, `a or b`, `not a` (short-circuits)
- Bitwise: `5 & 3`, `5 | 2`, `~5`, `1 << 3`, `8 >> 2`
- Membership: `'a' in 'cat'`, `3 in [1,2,3]`
- Identity: `a is b` (compare `id(a)`)
- Ternary: `x = 'yes' if cond else 'no'`

---

For more details and interactive experimentation, run `OP.py` with Python 3 (recommended 3.8+).
