# __str__ vs __repr__ in Python

import datetime

class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

    def __str__(self):
        """
        The __str__ method provides a user-friendly, readable representation.
        It's what the end-user sees when you print the object.
        """
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """
        The __repr__ method provides a developer-friendly, unambiguous representation.
        Ideally, this string should be a valid Python expression that can recreate the object.
        """
        return f"Book(title='{self.title}', author='{self.author}', published_year={self.published_year})"


# --- Create an instance of the Book class ---
book = Book("1984", "George Orwell", 1949)


# --- How the methods are called ---

# 1. print() and str() use __str__
print("--- Using print() and str() ---")
print(book)  # This calls book.__str__()
user_output = str(book)
print(f"Output from str(book): {user_output}")


# 2. repr() and the interactive console use __repr__
print("\n--- Using repr() ---")
print(repr(book)) # This explicitly calls book.__repr__()
developer_output = repr(book)
print(f"Output from repr(book): {developer_output}")


# 3. Inside a collection (like a list), __repr__ is used by default
print("\n--- Objects inside a collection ---")
book_list = [book, Book("Animal Farm", "George Orwell", 1945)]
print(book_list) # This will call __repr__ for each object in the list


# --- What happens if only one is defined? ---

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # This class only defines __repr__
    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}')"

print("\n--- Class with only __repr__ defined ---")
my_car = Car("Toyota", "Corolla")

# print() will fall back to using __repr__ because __str__ is not available.
print(my_car)
print(repr(my_car))


class Person:
    def __init__(self, name):
        self.name = name

    # This class only defines __str__
    def __str__(self):
        return f"Person named {self.name}"

print("\n--- Class with only __str__ defined ---")
person = Person("Alice")

print(person) # Uses the defined __str__
print(repr(person)) # Falls back to the default object repr, which is not very useful.
                    # e.g., <__main__.Person object at 0x...>

# This demonstrates why you should always try to implement __repr__.
