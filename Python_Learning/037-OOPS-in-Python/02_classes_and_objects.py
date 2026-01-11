# Classes and Objects in Python

# Define a class called 'Dog'
class Dog:
    # Class attribute - shared by all instances of the class
    species = "Canis familiaris"

    # The __init__ method is the constructor. It's called when an object is created.
    # 'self' refers to the instance being created.
    # 'name' and 'age' are parameters for the new object.
    def __init__(self, name, age):
        # Instance attributes - specific to each object
        self.name = name
        self.age = age
        self.is_sitting = False

    # A method of the class
    def bark(self):
        print(f"{self.name} says Woof!")

    def sit(self):
        if self.is_sitting:
            print(f"{self.name} is already sitting.")
        else:
            self.is_sitting = True
            print(f"{self.name} sits down.")

    def stand(self):
        if self.is_sitting:
            self.is_sitting = False
            print(f"{self.name} stands up.")
        else:
            print(f"{self.name} is already standing.")
            
    def description(self):
        return f"{self.name} is {self.age} years old."

# --- Creating Objects (Instances) of the Dog class ---

# Create an object named 'my_dog'
# This calls the __init__ method with name="Buddy" and age=3
my_dog = Dog("Buddy", 3)

# Create another object named 'your_dog'
your_dog = Dog("Lucy", 5)


# --- Accessing Attributes and Calling Methods ---

# Accessing instance attributes
print(f"{my_dog.name} is a good boy.")  # Output: Buddy is a good boy.
print(f"His friend is {your_dog.name}.") # Output: His friend is Lucy.
print(f"They are both of the species {Dog.species}.") # Accessing class attribute

# Calling methods on the objects
my_dog.bark()      # Output: Buddy says Woof!
your_dog.bark()    # Output: Lucy says Woof!

print(my_dog.description()) # Output: Buddy is 3 years old.

# Manipulating the state of an object
my_dog.sit()       # Output: Buddy sits down.
my_dog.sit()       # Output: Buddy is already sitting.
my_dog.stand()     # Output: Buddy stands up.
