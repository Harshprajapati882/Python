# Dictionaries in Python

# Creating a Dictionary
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Original dictionary:", my_dict)

# Accessing Dictionary Items
model = my_dict["model"]
print("\nModel of the car:", model)

model_get = my_dict.get("model")
print("Model using get():", model_get)

# Change Dictionary Items
my_dict["year"] = 2024
print("\nDictionary after changing year:", my_dict)

my_dict.update({"year": 2022, "color": "red"})
print("Dictionary after update:", my_dict)


# Add Dictionary Items
my_dict["seats"] = 4
print("\nDictionary after adding seats:", my_dict)

# Remove Dictionary Items
removed_item = my_dict.pop("model")
print("\nDictionary after removing model:", my_dict)
print("Removed item:", removed_item)

last_item = my_dict.popitem()
print("Dictionary after popitem:", my_dict)
print("Removed item (popitem):", last_item)

del my_dict["year"]
print("Dictionary after deleting year:", my_dict)

my_dict_to_clear = {"a": 1, "b": 2}
my_dict_to_clear.clear()
print("Cleared dictionary:", my_dict_to_clear)


# Dictionary View Objects
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("\nOriginal dictionary for views:", my_dict)

keys = my_dict.keys()
print("Keys view:", keys) 

values = my_dict.values()
print("Values view:", values)

items = my_dict.items()
print("Items view:", items)

# The view object will reflect changes in the dictionary
my_dict["color"] = "white"
print("\nDictionary after adding color:", my_dict)
print("Updated keys view:", keys)
print("Updated values view:", values)
print("Updated items view:", items)


# Loop Dictionaries
print("\nLooping through dictionary:")
# Print all key names in the dictionary
print("Keys:")
for key in my_dict:
  print(key)

# Print all values in the dictionary
print("\nValues (method 1):")
for key in my_dict:
  print(my_dict[key])

# You can also use the values() method
print("\nValues (method 2):")
for value in my_dict.values():
  print(value)

# Loop through both keys and values, by using the items() method
print("\nKeys and Values:")
for key, value in my_dict.items():
  print(key, "->", value)


# Copy Dictionaries
print("\nCopying dictionaries:")
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict2 = dict1.copy()
print("Copied dictionary (copy()):", dict2)

dict3 = dict(dict1)
print("Copied dictionary (dict()):", dict3)

# Nested Dictionaries
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
print("\nNested dictionary:", my_family)
print("Accessing nested dictionary:", my_family["child2"]["name"])


# Dictionary Methods
print("\nDictionary Methods in action:")
car = {"brand": "Tesla", "model": "Model S", "year": 2022}
print("Original car dictionary:", car)

# fromkeys()
keys = {'a', 'b', 'c'}
value = 0
fromkeys_dict = dict.fromkeys(keys, value)
print("fromkeys() example:", fromkeys_dict)

# get()
model = car.get("model")
print("get() example:", model)
# get() with default value
color = car.get("color", "white")
print("get() with default value:", color)

# setdefault()
color = car.setdefault("color", "black")
print("setdefault() example (new key):", car)
model = car.setdefault("model", "Model 3")
print("setdefault() example (existing key):", car)

# Dictionary Exercises
print("\n--- Dictionary Exercises ---")
# 1. Create a dictionary representing a car
car_exercise = {"brand": "Honda", "model": "Civic", "year": 2020}
print("1. Car dictionary:", car_exercise)

# 2. Access the "model" of the car.
print("2. Model:", car_exercise["model"])

# 3. Change the "year" of the car to 2023.
car_exercise["year"] = 2023
print("3. Updated car:", car_exercise)

# 4. Add a new key "color" with the value "blue" to the car dictionary.
car_exercise["color"] = "blue"
print("4. Added color:", car_exercise)

# 5. Remove the "model" key from the dictionary.
del car_exercise["model"]
print("5. Removed model:", car_exercise)

# 6. Loop through the dictionary and print all the keys.
print("6. Keys:")
for key in car_exercise:
    print(key)

# 7. Loop through the dictionary and print all the values.
print("7. Values:")
for value in car_exercise.values():
    print(value)

# 8. Create a copy of the car dictionary.
car_copy = car_exercise.copy()
print("8. Copied car:", car_copy)

# 9. Create a nested dictionary for a family with 2 members.
family_exercise = {
    "parent1": {"name": "Alex", "age": 35},
    "parent2": {"name": "Beth", "age": 32}
}
print("9. Family dictionary:", family_exercise)

# 10. Use the `get()` method to get the value of a key that does not exist and provide a default value.
engine_type = car_exercise.get("engine", "electric")
print("10. Engine type:", engine_type)

