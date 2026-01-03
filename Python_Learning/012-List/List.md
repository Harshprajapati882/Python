
# Python Lists — Notes

## What is a list?
- A list is an ordered, mutable collection of items. Items can be of mixed types.

## Creating lists
- Literal: `[]`, `[1, 2, 3]`
- From iterable: `list('abc')`, `list(range(5))`
- Empty list: `[]` or `list()`

## Accessing elements
- Indexing: `a[0]`, `a[-1]`
- Slicing: `a[start:stop]`, `a[start:stop:step]` — returns a new list

## Mutability
- Lists are mutable: assignment `a[1] = value`, slice assignment `a[1:3] = [x, y]`.

## Common operations
- Concatenation: `a + b`
- Repetition: `a * 3`
- Membership: `x in a`, `x not in a`
- Length: `len(a)`

## Important list methods
- `append(x)` — add item to end
- `extend(iterable)` — extend by items from iterable
- `insert(i, x)` — insert before index `i`
- `remove(x)` — remove first occurrence of `x` (raises `ValueError` if not found)
- `pop([i])` — remove and return item at index `i` (default last)
- `clear()` — remove all items
- `index(x[, start[, end]])` — return index of first occurrence
- `count(x)` — return number of occurrences
- `sort(key=None, reverse=False)` — sort in-place
- `reverse()` — reverse list in-place
- `copy()` — shallow copy of the list

## Built-in functions commonly used with lists
- `sorted(iterable, key=None, reverse=False)` — returns a new sorted list
- `min(a)`, `max(a)`, `sum(a)` — for numeric lists
- `any(a)`, `all(a)` — boolean checks
- `enumerate(a)` — yields pairs `(index, value)`
- `zip(a, b, ...)` — iterate in parallel

## List comprehensions
- Compact syntax for building lists: `[expr for item in iterable if condition]`
- Can include nested comprehensions for nested lists.

## Nested lists (lists of lists)
- Use for matrices, trees, etc. Access with `a[i][j]`.
- Beware of shallow copies for nested lists — copying the outer list still references inner lists.

## Copying lists
- Shallow copies: `a.copy()`, `list(a)`, `a[:]` — inner mutable elements are shared.
- Deep copy: `import copy; copy.deepcopy(a)` — duplicates nested structures.

## Performance notes
- Appending to the end is amortized O(1).
- Inserting or deleting at arbitrary positions (start or middle) is O(n) due to shifting.
- Use `collections.deque` for fast appends/pops at both ends when needed.

## Common idioms
- Swap two elements: `a[i], a[j] = a[j], a[i]`
- Reverse copy: `a[::-1]` or `list(reversed(a))`
- Flatten one level: `[x for sub in nested for x in sub]`

## Example use-cases
- Storing sequences of values, buffers, stacks (using `append` and `pop`), queues (use `deque`), and simple matrices.

## Further reading
- Official docs: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
