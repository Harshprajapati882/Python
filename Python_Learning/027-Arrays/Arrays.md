# Python Arrays

In Python, "arrays" are not a built-in data type, but the built-in `list` type serves the same purpose. Lists are dynamic, can hold items of different types, and are very flexible.

For more memory-efficient, typed arrays, you can use the `array` module.

## Topics Covered

1.  [Creating an Array](#creating-an-array)
2.  [Accessing Array Items](#accessing-array-items)
3.  [Adding Array Items](#adding-array-items)
4.  [Removing Array Items](#removing-array-items)
5.  [Looping Through an Array](#looping-through-an-array)
6.  [Copying an Array](#copying-an-array)
7.  [Reversing an Array](#reversing-an-array)
8.  [Sorting an Array](#sorting-an-array)
9.  [Joining Arrays](#joining-arrays)
10. [Array/List Methods](#arraylist-methods)
11. [Array Exercises](#array-exercises)

---

## Creating an Array

You can create a list by enclosing a comma-separated sequence of items in square brackets `[]`.

```python
# A list of strings
fruits = ["apple", "banana", "cherry"]

# A list of integers
numbers = [1, 5, 8, 12]
```

To use the `array` module, you need to import it and specify the type of the elements.

```python
import array as arr

# Create an array of integers
a = arr.array('i', [1, 2, 3])
```

## Accessing Array Items

You access an array item by referring to its index number.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Output: banana
```

## Adding Array Items

You can add an item to the end of a list using the `append()` method.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits) # Output: ['apple', 'banana', 'cherry', 'orange']
```

To add an item at a specified index, use the `insert()` method.

```python
fruits.insert(1, "lemon")
print(fruits) # Output: ['apple', 'lemon', 'banana', 'cherry', 'orange']
```

## Removing Array Items

The `remove()` method removes the first occurrence of a specified value.

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits) # Output: ['apple', 'cherry']
```

The `pop()` method removes the item at a specified index, or the last item if the index is not specified.

```python
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits) # Output: ['apple', 'cherry']

fruits.pop()
print(fruits) # Output: ['apple']
```

## Looping Through an Array

You can loop through the items of a list using a `for` loop.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
```

## Copying an Array

You can make a copy of a list with the `copy()` method or by slicing.

```python
fruits = ["apple", "banana", "cherry"]

# Using copy()
new_fruits = fruits.copy()

# Using slicing
another_copy = fruits[:]
```

## Reversing an Array

The `reverse()` method reverses the order of the elements in the list.

```python
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits) # Output: ['cherry', 'banana', 'apple']
```

## Sorting an Array

The `sort()` method sorts the list alphanumerically, ascending, by default.

```python
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars) # Output: ['BMW', 'Ford', 'Volvo']

# Sort in descending order
cars.sort(reverse=True)
print(cars) # Output: ['Volvo', 'Ford', 'BMW']
```

## Joining Arrays

You can join two lists by using the `+` operator.

```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) # Output: ['a', 'b', 'c', 1, 2, 3]
```

## Array/List Methods

Python has a set of built-in methods that you can use on lists.

| Method      | Description                                             |
|-------------|---------------------------------------------------------|
| `append()`  | Adds an element at the end of the list                  |
| `clear()`   | Removes all the elements from the list                  |
| `copy()`    | Returns a copy of the list                              |
| `count()`   | Returns the number of elements with the specified value |
| `extend()`  | Add the elements of a list (or any iterable), to the end of the current list |
| `index()`   | Returns the index of the first element with the specified value |
| `insert()`  | Adds an element at the specified position               |
| `pop()`     | Removes the element at the specified position           |
| `remove()`  | Removes the first item with the specified value         |
| `reverse()` | Reverses the order of the list                          |
| `sort()`    | Sorts the list                                          |

## Array Exercises

1.  Create a list of your 3 favorite fruits.
2.  Add a 4th fruit to the list.
3.  Print the 2nd fruit in the list.
4.  Remove the last fruit from the list.
5.  Sort the list and print it.
