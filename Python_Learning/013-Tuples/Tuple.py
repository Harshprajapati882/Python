"""Tuple examples and quick assertions.

Run this file to see example outputs and to verify behaviors via assertions.
"""

from collections import namedtuple


def examples():
    """Runs through examples of tuple usage."""
    # =================================================================
    # Creating Tuples
    # =================================================================
    print("--- Creating Tuples ---")
    empty_tuple = ()
    t1 = (1, "hello", 3.14)
    t2 = 4, 5, 6  # Implicit tuple (parentheses are optional)
    single_item_tuple = (42,)
    not_a_tuple = (42) # This is just an integer due to order of operations

    assert type(single_item_tuple) is tuple
    assert type(not_a_tuple) is int
    print("Empty tuple:", empty_tuple)
    print("Tuple with mixed types:", t1)
    print("Implicitly created tuple:", t2)
    print("Single item tuple:", single_item_tuple)

    # From an iterable
    tuple_from_list = tuple([1, 2, 3])
    tuple_from_string = tuple("abc")
    assert tuple_from_list == (1, 2, 3)
    assert tuple_from_string == ('a', 'b', 'c')
    print("Tuple from list:", tuple_from_list)


    # =================================================================
    # Access Tuples Items
    # =================================================================
    print("\n--- Accessing Tuple Items ---")
    my_tuple = ('a', 'b', 'c', 'd', 'e')
    assert my_tuple[0] == 'a'  # First item
    assert my_tuple[-1] == 'e' # Last item
    print("First item:", my_tuple[0])
    print("Last item:", my_tuple[-1])

    # Slicing
    assert my_tuple[1:3] == ('b', 'c')
    assert my_tuple[:2] == ('a', 'b')
    assert my_tuple[3:] == ('d', 'e')
    assert my_tuple[::-1] == ('e', 'd', 'c', 'b', 'a') # Reverse
    print("Slice [1:3]:", my_tuple[1:3])
    print("Reversed tuple:", my_tuple[::-1])


    # =================================================================
    # Update Tuples (Immutability)
    # =================================================================
    print("\n--- Updating Tuples (Immutability) ---")
    # Tuples are immutable. The line below would raise a TypeError.
    # my_tuple[0] = 'z' 
    
    # To "update" a tuple, you create a new one.
    # 1. Convert to list, modify, convert back
    temp_list = list(my_tuple)
    temp_list[0] = 'z'
    updated_tuple = tuple(temp_list)
    assert updated_tuple == ('z', 'b', 'c', 'd', 'e')
    print("Original tuple:", my_tuple)
    print("'Updated' tuple:", updated_tuple)

    # 2. Concatenate to "add" items
    new_tuple = my_tuple + ('f', 'g')
    assert new_tuple == ('a', 'b', 'c', 'd', 'e', 'f', 'g')
    print("Extended tuple:", new_tuple)


    # =================================================================
    # Unpack Tuples
    # =================================================================
    print("\n--- Unpacking Tuples ---")
    packed_tuple = ("John", 35, "New York")
    name, age, city = packed_tuple # Unpacking
    assert name == "John" and age == 35

    # Using * to capture multiple items
    numbers = (1, 2, 3, 4, 5)
    first, *middle, last = numbers
    assert first == 1
    assert middle == [2, 3, 4] # The rest are captured as a list
    assert last == 5
    print(f"Unpacked: first={first}, middle={middle}, last={last}")

    # =================================================================
    # Loop Tuples
    # =================================================================
    print("\n--- Looping Through Tuples ---")
    print("Items in t1:")
    for item in t1:
        print(f"- {item}")
    
    print("\nItems with index:")
    for i, item in enumerate(t1):
        print(f"- Index {i}: {item}")


    # =================================================================
    # Join Tuples
    # =================================================================
    print("\n--- Joining Tuples ---")
    t1 = (1, 2)
    t2 = (3, 4)
    # Concatenation
    concatenated = t1 + t2
    assert concatenated == (1, 2, 3, 4)
    print("Concatenated:", concatenated)

    # Repetition
    repeated = t1 * 3
    assert repeated == (1, 2, 1, 2, 1, 2)
    print("Repeated:", repeated)


    # =================================================================
    # Tuple Methods
    # =================================================================
    print("\n--- Tuple Methods ---")
    t = (1, 2, 2, 3, 2)
    # count()
    count_of_2 = t.count(2)
    assert count_of_2 == 3
    print(f"The number 2 appears {count_of_2} times in {t}")

    # index()
    index_of_3 = t.index(3)
    assert index_of_3 == 3
    print(f"The number 3 is first found at index {index_of_3}")
    
    # index() raises ValueError if item is not found
    try:
        t.index(99)
    except ValueError as e:
        print(f"Successfully caught expected error: {e}")


    # =================================================================
    # namedtuple
    # =================================================================
    print("\n--- namedtuple ---")
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(11, y=22)
    assert p.x == 11 and p.y == 22
    assert isinstance(p, tuple)
    print(f"Namedtuple Point: x={p.x}, y={p.y}")
    print(f"Access by index: p[0]={p[0]}, p[1]={p[1]}")

def exercises():
    """Solutions for the exercises in Tuple.md."""
    print("\n--- Tuple Exercises ---")

    # 1. Create a tuple with different data types.
    mixed_tuple = (1, "Python", 3.14, True)
    print("1. Tuple with different data types:", mixed_tuple)
    assert isinstance(mixed_tuple[0], int)
    assert isinstance(mixed_tuple[1], str)
    assert isinstance(mixed_tuple[3], bool)
    
    # 2. Access and print the last item of the tuple.
    last_item = mixed_tuple[-1]
    print("2. Last item of the tuple:", last_item)
    assert last_item is True
    
    # 3. Find the number of times a specific item appears in a tuple.
    t = (1, 2, 3, 2, 4, 2)
    count_of_2 = t.count(2)
    print(f"3. The number 2 appears {count_of_2} times in {t}")
    assert count_of_2 == 3
    
    # 4. Unpack a tuple into several variables.
    person_data = ("Alice", 30, "London")
    name, age, city = person_data
    print(f"4. Unpacked tuple: Name={name}, Age={age}, City={city}")
    assert name == "Alice" and city == "London"

    # 5. Create a namedtuple to represent a Book.
    Book = namedtuple('Book', ['title', 'author', 'ISBN'])
    book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "0-345-39180-2")
    print("5. Namedtuple for a book:", book1)
    assert book1.author == "Douglas Adams"

    # 6. Return a tuple of the largest and smallest number in a list.
    def find_min_max(numbers):
        if not numbers:
            return (None, None)
        return (min(numbers), max(numbers))

    num_list = [5, 1, 9, 3, 7]
    min_val, max_val = find_min_max(num_list)
    print(f"6. Min and max of {num_list} are: ({min_val}, {max_val})")
    assert (min_val, max_val) == (1, 9)


if __name__ == "__main__":
    examples()
    exercises()