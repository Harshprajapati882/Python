**Overview**

Type casting is converting a value from one data type to another. In Python this can be done implicitly by the interpreter or explicitly by the programmer using built-in constructors (for example `int()`, `float()`, `str()`, `list()`).

**Implicit vs Explicit**

- **Implicit:** Python automatically converts between compatible types (for example `int` to `float` during arithmetic).
- **Explicit:** You call conversion functions like `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, `dict()`, `bytes()`, `bytearray()`, `complex()`.

**Common Conversions**

- **Number conversions:** `int()`, `float()`, `complex()` — convert between integer, floating-point, and complex numbers. Watch out for truncation when converting `float` to `int`.
- **Text and bytes:** `str()` and `bytes()` / `bytearray()` — encoding matters when converting from `str` to `bytes` (`encode()` / `decode()` or `bytes(s, encoding)`).
- **Boolean:** `bool()` — empty containers/zero/`None` are `False`, most other values are `True`.
- **Collections:** `list()`, `tuple()`, `set()`, `dict()` — convert between iterable container types. Converting to `dict()` requires key/value pairs or another mapping.

**Built-in Conversion Functions**

- `int(x, base=10)` — from numbers or numeric strings. `int('12.9')` raises `ValueError`.
- `float(x)` — from numeric strings or numbers.
- `str(x)` — universal text representation.
- `bool(x)` — truthiness conversion.
- `list(iterable)`, `tuple(iterable)`, `set(iterable)` — collection conversions.
- `dict(mapping_or_iterable)` — from mapping or pairs of two-item iterables.
- `bytes(s, encoding)` / `bytearray(s, encoding)` — convert text to raw bytes.
- `complex(real, imag=0)` or `complex(str)` — construct complex numbers.

**Pitfalls & Notes**

- Converting a `float` to `int` truncates toward zero (precision is lost).
- Passing non-numeric strings to `int()` or `float()` raises `ValueError`.
- `bool('False')` is `True` because non-empty strings are truthy.
- Converting between collections may change ordering (sets) or remove duplicates.
- `bytes()` from a `str` requires specifying encoding or using `encode()`.

**Examples and runnable code**

See the example script: [Typecasting.py](Typecasting.py) for runnable demonstrations of each conversion and common edge cases.

