# Python Sets

## Sets
A set is a collection which is both unordered and unindexed.
Sets are written with curly brackets.

- A set is an unordered collection of unique, hashable objects.
- Sets are mutable (you can add/remove items), but the elements themselves must be hashable (immutable types like numbers, strings, tuples).
- Use `set()` or curly braces `{}` to create a set. An empty set must be created with `set()` (because `{}` creates an empty dict).

### Key properties

- Unordered: no index, iteration order is arbitrary.
- Unique elements: duplicates are removed automatically.
- Fast membership testing (average O(1)).

### Creating sets

- From literals: `{1, 2, 3}`
- From iterables: `set([1,2,2,3])` or `set('abc')`
- Empty set: `set()`

## Access Set Items
You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a `for` loop, or ask if a specified value is present in a set, by using the `in` keyword.

## Add Set Items
To add one item to a set use the `add()` method.
To add more than one item to a set use the `update()` method.

## Remove Set Items
To remove an item in a set, use the `remove()`, or the `discard()` method.
- `s.remove(x)` (raises `KeyError` if missing)
- `s.discard(x)` (no error if missing)
- `s.pop()` (removes and returns an arbitrary element)
- `s.clear()` (empties the set)

## Loop Sets
You can loop through the set items by using a `for` loop:

```python
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
```

## Join Sets
There are several ways to join two or more sets in Python.
You can use the `union()` method that returns a new set containing all items from both sets, or the `update()` method that inserts all the items from one set into another.

## Copy Sets
You cannot copy a set simply by typing `set2 = set1`, because: `set2` will only be a reference to `set1`, and changes made in `set1` will automatically also be made in `set2`.
There are ways to make a copy, one way is to use the built-in `copy()` method.
Another way is to use the `set()` constructor.

## Set Operators
- Union: `a | b`
- Intersection: `a & b`
- Difference: `a - b`
- Symmetric difference: `a ^ b`

## Set Methods
Python has a set of built-in methods that you can use on sets.

| Method | Description |
|---|---|
| `add()` | Adds an element to the set |
| `clear()` | Removes all the elements from the set |
| `copy()` | Returns a copy of the set |
| `difference()` | Returns a set containing the difference between two or more sets |
| `difference_update()` | Removes the items in this set that are also included in another, specified set |
| `discard()` | Remove the specified item |
| `intersection()` | Returns a set, that is the intersection of two other sets |
| `intersection_update()` | Removes the items in this set that are not present in other, specified set(s) |
| `isdisjoint()` | Returns whether two sets have a intersection or not |
| `issubset()` | Returns whether another set contains this set or not |
| `issuperset()` | Returns whether this set contains another set or not |
| `pop()` | Removes an element from the set |
| `remove()` | Removes the specified element |
| `symmetric_difference()` | Returns a set with the symmetric differences of two sets |
| `symmetric_difference_update()` | inserts the symmetric differences from this set and another |
| `union()` | Return a set containing the union of sets |
| `update()` | Update the set with the union of this set and others |

## Immutability: `frozenset`
`frozenset` is an immutable set. Useful as dictionary keys or set elements.

## Set Exercises

1. Create a set with the following elements: 1, 2, 3, 4, 5.
2. Add the element 6 to the set.
3. Remove the element 3 from the set.
4. Check if the element 4 is in the set.
5. Find the union of the set with another set: {5, 6, 7, 8}.
6. Find the intersection of the set with another set: {5, 6, 7, 8}.
7. Find the difference of the set with another set: {5, 6, 7, 8}.

## Examples
See the companion runnable file `Set.py` for concrete examples demonstrating creation, operations, and pitfalls.