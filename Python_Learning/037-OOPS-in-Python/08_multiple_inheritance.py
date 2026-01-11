# Multiple Inheritance in Python

# --- Parent Class 1 ---
class CanFly:
    def __init__(self, altitude):
        self.altitude = altitude

    def fly(self):
        print(f"The object is flying at {self.altitude} feet.")

# --- Parent Class 2 ---
class CanSwim:
    def __init__(self, speed):
        self.speed = speed

    def swim(self):
        print(f"The object is swimming at {self.speed} knots.")

# --- Child Class inheriting from both ---
# This class combines the behaviors of CanFly and CanSwim
class AmphibiousVehicle(CanFly, CanSwim):
    def __init__(self, name, altitude, speed):
        self.name = name
        # We need to call the __init__ of both parent classes
        CanFly.__init__(self, altitude)
        CanSwim.__init__(self, speed)
    
    def display_info(self):
        print(f"Vehicle Name: {self.name}")
        self.fly()
        self.swim()

# --- Using the child class ---
print("--- Amphibious Vehicle Example ---")
duck_boat = AmphibiousVehicle("Duck Boat", altitude=1000, speed=8)
duck_boat.display_info()
# Output:
# Vehicle Name: Duck Boat
# The object is flying at 1000 feet.
# The object is swimming at 8 knots.


print("\n" + "="*30 + "\n")


# --- The Diamond Problem and Method Resolution Order (MRO) ---
print("--- Diamond Problem Example ---")

class Grandparent:
    def speak(self):
        print("I am from the Grandparent class.")

class Parent1(Grandparent):
    def speak(self):
        print("I am from Parent1.")

class Parent2(Grandparent):
    def speak(self):
        print("I am from Parent2.")

class Child(Parent1, Parent2):
    pass # Child doesn't override speak()

# Create an instance of the Child class
child_instance = Child()

# Which 'speak' method gets called?
child_instance.speak()  # Output: I am from Parent1.

# Python's MRO determines the order. Let's inspect it.
# The order is: Child -> Parent1 -> Parent2 -> Grandparent -> object
print("\nMethod Resolution Order (MRO) for Child class:")
print(Child.__mro__)
# Output:
# (<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class '__main__.Grandparent'>, <class 'object'>)

# Because Parent1 comes before Parent2 in the MRO, its 'speak' method is used.
