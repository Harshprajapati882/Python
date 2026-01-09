
# Python Lists — Notes

## What is a list?
- A list is an ordered, mutable collection of items. Items can be of mixed types.
- Lists are one of the most versatile and commonly used data structures in Python.

## Creating lists
- **Literal**: `[]`, `[1, 2, 3]`, `['apple', 'banana', 'cherry']`
- **From iterable**: `list('abc')`, `list(range(5))`
- **Empty list**: `[]` or `list()`

## Accessing list items
- **Indexing**: `a[0]` (first item), `a[-1]` (last item).
- **Slicing**: `a[start:stop]`, `a[start:stop:step]` — returns a new list.
  - `a[1:3]` gets items from index 1 up to (but not including) index 3.
  - `a[:3]` gets items from the beginning up to index 3.
  - `a[1:]` gets items from index 1 to the end.
  - `a[::-1]` reverses the list.

## Change list items
- Lists are mutable, so you can change their content.
- **Assignment**: `a[1] = 'blueberry'`
- **Slice assignment**: `a[1:3] = ['x', 'y']`. This can also be used to change the size of the list.

## Add list items
- `append(x)` — add a single item to the end of the list.
- `extend(iterable)` — add all items from an iterable (like another list) to the end.
- `insert(i, x)` — insert an item at a specific index `i`.

## Remove list items
- `remove(x)` — remove the first occurrence of a specific value `x`. Raises a `ValueError` if the item is not found.
- `pop([i])` — remove and return the item at a specific index `i`. If no index is specified, it removes and returns the last item.
- `clear()` — remove all items from the list, making it empty.
- `del` keyword:
  - `del a[0]` removes the item at index 0.
  - `del a[1:3]` removes a slice.
  - `del a` deletes the entire list variable.

## Loop lists
- **For loop**: The most common way to iterate over the items of a list.
  ```python
  for item in my_list:
      print(item)
  ```
- **Looping with index**: Use `enumerate()` to get both the index and the value.
  ```python
  for i, item in enumerate(my_list):
      print(f"Index {i}: {item}")
  ```
- **While loop**: You can also use a `while` loop with an index.
  ```python
  i = 0
  while i < len(my_list):
      print(my_list[i])
      i += 1
  ```

## List comprehension
- A short and elegant way to create lists.
- **Syntax**: `[expression for item in iterable if condition]`
- **Example**: `squares = [x * x for x in range(10)]`
- **Example with condition**: `even_squares = [x * x for x in range(10) if x % 2 == 0]`

## Sort lists
- `sort(key=None, reverse=False)` — sorts the list in-place. It modifies the original list.
  - `key` can be a function to specify a custom sorting criterion.
  - `reverse=True` sorts in descending order.
- `sorted(iterable, key=None, reverse=False)` — returns a new sorted list, leaving the original unchanged.

## Copy lists
- You cannot copy a list simply by typing `list2 = list1`, because `list2` will only be a *reference* to `list1`. Changes made in `list1` will automatically be made in `list2`.
- **Shallow copies**: `a.copy()`, `list(a)`, `a[:]`. This creates a new list, but if the list contains other mutable objects (like other lists), the inner objects are still shared.
- **Deep copy**: `import copy; copy.deepcopy(a)`. This creates a fully independent copy of the list and all its nested objects.

## Join lists
- **Concatenation**: `list1 + list2` creates a new list containing all items from `list1` followed by all items from `list2`.
- **`extend()` method**: `list1.extend(list2)` adds all items from `list2` to the end of `list1` (in-place).

## List methods
- `append(x)`: Adds an element `x` to the end of the list.
- `extend(iterable)`: Extends the list by appending all the items from the iterable.
- `insert(i, x)`: Inserts an element `x` at a given position `i`.
- `remove(x)`: Removes the first item from the list whose value is `x`.
- `pop([i])`: Removes the item at the given position in the list, and returns it. If no index is specified, `pop()` removes and returns the last item in the list.
- `clear()`: Removes all items from the list.
- `index(x[, start[, end]])`: Returns the index of the first occurrence of `x`.
- `count(x)`: Returns the number of times `x` appears in the list.
- `sort(key=None, reverse=False)`: Sorts the items of the list in place.
- `reverse()`: Reverses the elements of the list in place.
- `copy()`: Returns a shallow copy of the list.

## List Exercises

Here are a few exercises to test your understanding of Python lists.

1.  **Find the largest number**: Write a program to find the largest number in a list without using the built-in `max()` function.
2.  **Remove duplicates**: Write a program to remove duplicate elements from a list.
3.  **Check if a list is empty**: Write a program to check if a list is empty or not.
4.  **Merge two lists and sort it**: Write a program to merge two lists and sort it.
5.  **Count occurrences**: Write a program to count the occurrences of a specific element in a list.

---

## Further reading
- Official docs: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
