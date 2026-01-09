# Tuples in Python

## What are Tuples?
- **Definition:** Tuples are ordered, immutable sequences in Python. They are used to store multiple items in a single variable.
- Items can be of mixed types.
- **Literal syntax:** Use parentheses `()` or comma-separated values. 
- For a single-item tuple, you must include a trailing comma: `(1,)`.

### Creating Tuples
- **Empty tuple:** `empty_tuple = ()`
- **With items:** `my_tuple = (1, "hello", 3.14)`
- **Implicitly:** `another_tuple = 1, "hello", 3.14` (the parentheses are optional in many cases)
- **From an iterable:** `tuple_from_list = tuple([1, 2, 3])`, `tuple_from_string = tuple("abc")`
- **Single-item tuple:** `single_item_tuple = (42,)` 
- `not_a_tuple = (42)` is just the integer `42`.

## Access Tuples Items
- **Indexing:** Access elements by their zero-based position. `my_tuple[0]` returns the first item.
- **Negative Indexing:** Access elements from the end. `my_tuple[-1]` returns the last item.
- **Slicing:** Extract a portion of a tuple. `my_tuple[1:3]` returns a new tuple with elements from index 1 up to (but not including) index 3.
  - `my_tuple[:2]` gets items from the beginning up to index 2.
  - `my_tuple[1:]` gets items from index 1 to the end.
  - `my_tuple[::-1]` returns a new tuple with the elements in reverse order.

## Update Tuples
Tuples are **immutable**, which means you cannot change, add, or remove items after the tuple has been created. However, you can create *new* tuples based on existing ones.

- **"Updating" by creating a new tuple:** Convert the tuple to a list, modify the list, and then convert it back to a tuple. This is the standard workaround.
- **Adding items:** Since you can't add items to a tuple, you can concatenate two tuples to create a new one. `new_tuple = old_tuple + (item1, item2)`

## Unpack Tuples
- **Packing:** When you create a tuple, you are "packing" values into it: `my_tuple = 1, "hello", True`
- **Unpacking:** You can extract the values back into variables. This is called "unpacking": `number, greeting, is_real = my_tuple`. The number of variables must match the number of items in the tuple.
- **Asterisk `*` for unpacking:** If the number of variables is less than the number of values, you can add an `*` to a variable name, and the remaining values will be assigned to that variable as a list: `first, *rest, last = (1, 2, 3, 4, 5)`

## Loop Tuples
- **For loop**: The most common way to iterate over the items of a tuple.
  ```python
  for item in my_tuple:
      print(item)
  ```
- **Looping with index**: Use `enumerate()` to get both the index and the value.
  ```python
  for i, item in enumerate(my_tuple):
      print(f"Index {i}: {item}")
  ```

## Join Tuples
- **Concatenation:** You can join two or more tuples using the `+` operator to create a new tuple.
- **Repetition:** You can multiply a tuple by an integer to create a new tuple with repeated elements. `repeated_tuple = (1, 2) * 3` will result in `(1, 2, 1, 2, 1, 2)`.

## Tuple Methods
Tuples have only two methods, as they are immutable.
- `count(value)`: Returns the number of times a specified value occurs in a tuple.
- `index(value)`: Searches the tuple for a specified value and returns the position of where it was found. Raises a `ValueError` if the value is not found.

## `namedtuple`
For more complex data, `collections.namedtuple` is a factory function that allows you to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable. It makes your code more readable.

```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p.x, p.y)  # Output: 11 22
```

## Tuple Use Cases
- **Fixed collections:** When you have a collection of items that should not change, such as days of the week or coordinates.
- **Function returns:** Functions can return multiple values as a tuple.
- **Dictionary keys:** Tuples can be used as keys in a dictionary because they are hashable (immutable). Lists cannot.

## Performance
- **Memory:** Tuples are slightly more memory-efficient than lists.
- **Time:** Tuples are slightly faster to create and access than lists.

## Tuple Exercises

Here are some exercises to practice working with tuples.

1.  Create a tuple with different data types.
2.  Access and print the last item of the tuple.
3.  Find the number of times a specific item appears in a tuple.
4.  Unpack a tuple into several variables.
5.  Create a `namedtuple` to represent a `Book` with fields `title`, `author`, and `ISBN`.
6.  Return a tuple of the largest and smallest number in a list of integers.

See `Tuple.py` for example code and solutions to these exercises.

---

## Further reading
- Official docs: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences