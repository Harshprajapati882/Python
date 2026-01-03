
# Python Sets

## What is a set?

- A set is an unordered collection of unique, hashable objects.
- Sets are mutable (you can add/remove items), but the elements themselves must be hashable (immutable types like numbers, strings, tuples).
- Use `set()` or curly braces `{}` to create a set. An empty set must be created with `set()` (because `{}` creates an empty dict).

## Key properties

- Unordered: no index, iteration order is arbitrary.
- Unique elements: duplicates are removed automatically.
- Fast membership testing (average O(1)).

## Creating sets

- From literals: `{1, 2, 3}`
- From iterables: `set([1,2,2,3])` or `set('abc')`
- Empty set: `set()`

## Common operations

- Add: `s.add(x)`
- Remove: `s.remove(x)` (raises `KeyError` if missing)
- Discard: `s.discard(x)` (no error if missing)
- Pop: `s.pop()` (removes and returns an arbitrary element)
- Clear: `s.clear()`

## Set algebra

- Union: `a | b` or `a.union(b)`
- Intersection: `a & b` or `a.intersection(b)`
- Difference: `a - b` or `a.difference(b)`
- Symmetric difference: `a ^ b` or `a.symmetric_difference(b)`
- In-place versions: `|=`, `&=`, `-=`, `^=`

## Relationships

- Subset: `a.issubset(b)` or `a <= b`
- Proper subset: `a < b`
- Superset: `a.issuperset(b)` or `a >= b`
- Disjoint: `a.isdisjoint(b)`

## Immutability: `frozenset`

- `frozenset` is an immutable set. Useful as dictionary keys or set elements.

## Use cases

- Remove duplicates from a list: `unique = list(set(lst))`
- Fast membership checks: `if x in s:`
- Set operations for tags, categories, and filtering.

## Examples

See the companion runnable file `Set.py` for concrete examples demonstrating creation, operations, and pitfalls.
