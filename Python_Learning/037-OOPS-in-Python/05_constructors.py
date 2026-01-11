# Constructors (`__init__`) and Destructors (`__del__`) in Python

# 1. Parameterized Constructor
class Employee:
    # This is a parameterized constructor
    def __init__(self, name, employee_id, salary):
        print(f"Creating an Employee object for {name}...")
        
        # Initializing instance attributes
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}")

    # The destructor method
    def __del__(self):
        # This is called when the object is garbage collected
        print(f"Destructor called. Deleting the Employee object for {self.name}.")

# Creating an instance of the Employee class
# This automatically calls the __init__ method
emp1 = Employee("Alice", "E123", 70000)
emp1.display_details() # Output: ID: E123, Name: Alice, Salary: $70000

emp2 = Employee("Bob", "E456", 85000)
emp2.display_details() # Output: ID: E456, Name: Bob, Salary: $85000

print("\n--- Deleting objects ---\n")
# The __del__ method is called when the object's reference count becomes zero.
# We can trigger this by using the 'del' keyword.
del emp1
# Output: Destructor called. Deleting the Employee object for Alice.

# emp2 will be deleted automatically when the script finishes.


# 2. Default Constructor Behavior
class Simple:
    # This class has no __init__ method defined.
    # Python provides a default constructor that does nothing.
    def say_hello(self):
        print("Hello from the Simple class!")

# We can still create an instance, even without a custom __init__
s = Simple()
s.say_hello() # Output: Hello from the Simple class!


# 3. Constructor with Default Arguments
class Book:
    def __init__(self, title, author, genre="Fiction"):
        # 'genre' has a default value
        self.title = title
        self.author = author
        self.genre = genre

    def info(self):
        print(f"'{self.title}' by {self.author} ({self.genre})")

# Creating a book and providing all arguments
book1 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy")
book1.info() # Output: 'The Hobbit' by J.R.R. Tolkien (Fantasy)

# Creating a book without the 'genre' argument; it will use the default value
book2 = Book("1984", "George Orwell")
book2.info() # Output: '1984' by George Orwell (Fiction)
