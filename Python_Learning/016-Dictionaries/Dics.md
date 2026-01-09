# Dictionaries in Python

Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicate keys.

## Creating a Dictionary

You can create a dictionary by placing a comma-separated list of key:value pairs in curly braces `{}`.

```python
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(my_dict)
```

## Accessing Dictionary Items

You can access the items of a dictionary by referring to its key name, inside square brackets `[]`.

```python
# Get the value of the "model" key
model = my_dict["model"]
print(model)
```

You can also use the `get()` method:

```python
model = my_dict.get("model")
print(model)
```

## Change Dictionary Items

You can change the value of a specific item by referring to its key name.

```python
my_dict["year"] = 2024
print(my_dict)
```

The `update()` method can also be used to update the dictionary with items from another dictionary or from an iterable of key:value pairs.

```python
my_dict.update({"year": 2022, "color": "red"})
print(my_dict)
```

## Add Dictionary Items

You can add an item to the dictionary by using a new index key and assigning a value to it.

```python
my_dict["color"] = "red"
print(my_dict)
```

## Remove Dictionary Items

There are several methods to remove items from a dictionary:

- `pop()`: Removes the item with the specified key name.
- `popitem()`: Removes the last inserted item.
- `del`: Removes the item with the specified key name. `del` can also delete the dictionary completely.
- `clear()`: Empties the dictionary.

```python
# Remove "model"
my_dict.pop("model")
print(my_dict)

# Remove the last item
my_dict.popitem()
print(my_dict)

# Delete the "year" item
del my_dict["year"]
print(my_dict)

# Clear the dictionary
my_dict.clear()
print(my_dict)
```

## Dictionary View Objects

Dictionary view objects provide a dynamic view of the dictionary's entries. When the dictionary changes, the view reflects these changes. The view objects are:

- `keys()`: Returns a view object containing the dictionary's keys.
- `values()`: Returns a view object containing the dictionary's values.
- `items()`: Returns a view object containing the dictionary's key-value tuple pairs.

```python
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

keys = my_dict.keys()
print(keys) 

values = my_dict.values()
print(values)

items = my_dict.items()
print(items)

# The view object will reflect changes in the dictionary
my_dict["color"] = "white"
print(keys)
print(values)
print(items)
```

## Loop Dictionaries

You can loop through a dictionary by using a `for` loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

```python
# Print all key names in the dictionary
for key in my_dict:
  print(key)

# Print all values in the dictionary
for key in my_dict:
  print(my_dict[key])

# You can also use the values() method
for value in my_dict.values():
  print(value)

# Loop through both keys and values, by using the items() method
for key, value in my_dict.items():
  print(key, value)
```

## Copy Dictionaries

You cannot copy a dictionary simply by typing `dict2 = dict1`, because `dict2` will only be a *reference* to `dict1`, and changes made in `dict1` will automatically also be made in `dict2`.

There are ways to make a copy, one way is to use the built-in `copy()` method.

```python
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict2 = dict1.copy()
print(dict2)
```

Another way to make a copy is to use the built-in `dict()` function.

```python
dict3 = dict(dict1)
print(dict3)
```

## Nested Dictionaries

A dictionary can contain dictionaries, this is called nested dictionaries.

```python
my_family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(my_family)
```

## Dictionary Methods

Python has a set of built-in methods that you can use on dictionaries.

| Method      | Description                                                                                               |
|-------------|-----------------------------------------------------------------------------------------------------------|
| `clear()`   | Removes all the elements from the dictionary                                                              |
| `copy()`    | Returns a copy of the dictionary                                                                          |
| `fromkeys()`| Returns a dictionary with the specified keys and value                                                    |
| `get()`     | Returns the value of the specified key                                                                    |
| `items()`   | Returns a list containing a tuple for each key value pair                                                 |
| `keys()`    | Returns a list containing the dictionary's keys                                                           |
| `pop()`     | Removes the element with the specified key                                                                |
| `popitem()` | Removes the last inserted key-value pair                                                                  |
| `setdefault()`| Returns the value of the specified key. If the key does not exist: insert the key, with the specified value|
| `update()`  | Updates the dictionary with the specified key-value pairs                                                 |
| `values()`  | Returns a list of all the values in the dictionary                                                        |

## Dictionary Exercises

1. Create a dictionary representing a car with "brand", "model", and "year" keys.
2. Access the "model" of the car.
3. Change the "year" of the car to 2023.
4. Add a new key "color" with the value "blue" to the car dictionary.
5. Remove the "model" key from the dictionary.
6. Loop through the dictionary and print all the keys.
7. Loop through the dictionary and print all the values.
8. Create a copy of the car dictionary.
9. Create a nested dictionary for a family with 2 members.
10. Use the `get()` method to get the value of a key that does not exist and provide a default value.
