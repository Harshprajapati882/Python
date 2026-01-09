# Python Lists as Arrays
# In Python, lists are commonly used to perform array-like operations.

# For typed arrays, you can use the 'array' module.
import array as arr

print("--- Creating an Array ---")
# A list of strings
fruits = ["apple", "banana", "cherry"]
print("List of fruits:", fruits)

# A list of integers
numbers = [1, 5, 8, 12]
print("List of numbers:", numbers)

# Using the array module for an array of integers
typed_array = arr.array('i', [1, 2, 3, 4, 5])
print("Typed array of integers:", typed_array)


print("\n--- Accessing Array Items ---")
# Accessing an item by its index
print("Second fruit is:", fruits[1])  # Output: banana


print("\n--- Adding Array Items ---")
# Appending an item to the end of the list
fruits.append("orange")
print("Fruits after append:", fruits)

# Inserting an item at a specific index
fruits.insert(1, "lemon")
print("Fruits after insert:", fruits)


print("\n--- Removing Array Items ---")
# Removing a specific item by value
fruits.remove("banana")
print("Fruits after removing 'banana':", fruits)

# Removing an item by its index (pop)
popped_item = fruits.pop(1)
print(f"Popped item at index 1: {popped_item}")
print("Fruits after pop(1):", fruits)

# Pop the last item
last_item = fruits.pop()
print(f"Popped last item: {last_item}")
print("Fruits after pop():", fruits)


print("\n--- Looping Through an Array ---")
# Using a for loop to iterate over the list
print("All fruits:")
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)


print("\n--- Copying an Array ---")
original_list = [1, 2, 3, 4, 5]
# Using the copy() method
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)

# Using slicing to create a copy
sliced_copy = original_list[:]
print("Sliced copy:", sliced_copy)
# Modifying the original list to show that the copy is independent
original_list.append(6)
print("Original list after modification:", original_list)
print("Copied list remains unchanged:", copied_list)


print("\n--- Reversing an Array ---")
# Reversing the order of elements
numbers_to_reverse = [1, 2, 3, 4, 5]
print("Original numbers:", numbers_to_reverse)
numbers_to_reverse.reverse()
print("Reversed numbers:", numbers_to_reverse)


print("\n--- Sorting an Array ---")
# Sorting a list of strings
cars = ['Ford', 'BMW', 'Volvo', 'Audi']
print("Original car list:", cars)
cars.sort()
print("Sorted car list (ascending):", cars)

# Sorting in descending order
cars.sort(reverse=True)
print("Sorted car list (descending):", cars)

# Sorting a list of numbers
num_list = [5, 2, 8, 1, 9]
print("Original number list:", num_list)
num_list.sort()
print("Sorted number list:", num_list)


print("\n--- Joining Arrays ---")
# Joining two lists using the + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
joined_list = list1 + list2
print("List 1:", list1)
print("List 2:", list2)
print("Joined list:", joined_list)


print("\n--- Array Exercises ---")
# 1. Create a list of your 3 favorite fruits.
favorite_fruits = ["mango", "strawberry", "pineapple"]
print("1. My favorite fruits:", favorite_fruits)

# 2. Add a 4th fruit to the list.
favorite_fruits.append("grape")
print("2. Added a 4th fruit:", favorite_fruits)

# 3. Print the 2nd fruit in the list.
print("3. The 2nd fruit is:", favorite_fruits[1])

# 4. Remove the last fruit from the list.
favorite_fruits.pop()
print("4. Removed the last fruit:", favorite_fruits)

# 5. Sort the list and print it.
favorite_fruits.sort()
print("5. Sorted list:", favorite_fruits)
