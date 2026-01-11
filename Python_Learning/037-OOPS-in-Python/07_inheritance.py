# Single Inheritance in Python

# --- Parent Class (Superclass) ---
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True

    def speak(self):
        # A generic sound, to be overridden by subclasses
        return "The animal makes a sound."

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

# --- Child Class (Subclass) ---
# The Dog class inherits from the Animal class
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the constructor of the parent class (Animal)
        # We pass "Dog" as the species
        super().__init__(name, species="Dog")
        self.breed = breed

    # Overriding the 'speak' method from the parent class
    def speak(self):
        return "Woof! Woof!"

    # Adding a new method specific to the Dog class
    def fetch(self, item):
        return f"{self.name} is fetching the {item}."

# --- Another Child Class ---
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    # Overriding the 'speak' method
    def speak(self):
        return "Meow."
    
    # Adding a new method
    def purr(self):
        return f"{self.name} is purring."


# --- Using the classes ---

# Create an instance of the parent class
generic_animal = Animal("Creature", "Unknown")
print(f"Generic Animal: {generic_animal.name}, Species: {generic_animal.species}")
print(generic_animal.speak()) # Output: The animal makes a sound.
print(generic_animal.eat())   # Output: Creature is eating.

print("\n" + "="*20 + "\n")

# Create an instance of the Dog subclass
my_dog = Dog("Buddy", "Golden Retriever")
print(f"Dog's Name: {my_dog.name}")
print(f"Dog's Species: {my_dog.species}") # Inherited from Animal
print(f"Dog's Breed: {my_dog.breed}")   # Specific to Dog

# Calling methods
print(my_dog.speak()) # Output: Woof! Woof! (Overridden method)
print(my_dog.eat())   # Output: Buddy is eating. (Inherited method)
print(my_dog.fetch("ball")) # Output: Buddy is fetching the ball. (New method)

print("\n" + "="*20 + "\n")

# Create an instance of the Cat subclass
my_cat = Cat("Whiskers", "Gray")
print(f"Cat's Name: {my_cat.name}")
print(f"Cat's Species: {my_cat.species}") # Inherited

# Calling methods
print(my_cat.speak()) # Output: Meow. (Overridden method)
print(my_cat.sleep()) # Output: Whiskers is sleeping. (Inherited method)
print(my_cat.purr())  # Output: Whiskers is purring. (New method)

# The 'isinstance()' function can be used to check the relationship
print(f"\nIs 'my_dog' an instance of Dog? {isinstance(my_dog, Dog)}")       # True
print(f"Is 'my_dog' an instance of Animal? {isinstance(my_dog, Animal)}") # True
print(f"Is 'generic_animal' an instance of Dog? {isinstance(generic_animal, Dog)}") # False
