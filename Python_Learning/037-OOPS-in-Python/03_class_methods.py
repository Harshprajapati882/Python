# Class Methods in Python

class Pizza:
    # Class attribute
    slice_size = 8  # inches

    def __init__(self, toppings):
        # Instance attribute
        self.toppings = toppings

    # An instance method
    def display(self):
        print(f"A pizza with {', '.join(self.toppings)}.")
        print(f"Each slice is {self.slice_size} inches.")

    # A class method
    # It takes the class (cls) as the first argument
    @classmethod
    def get_slice_size(cls):
        return cls.slice_size

    # Another class method
    # This one modifies a class attribute
    @classmethod
    def set_slice_size(cls, new_size):
        cls.slice_size = new_size

    # A factory method using a class method
    # This provides an alternative way to create a Pizza object
    @classmethod
    def from_string(cls, pizza_string):
        """Creates a pizza instance from a string like 'pepperoni-onions-mushrooms'."""
        toppings = pizza_string.split('-')
        return cls(toppings)


# --- Using Class Methods ---

# You can call a class method directly on the class
print(f"Default pizza slice size: {Pizza.get_slice_size()}")  # Output: 8

# Let's change the slice size for ALL pizzas
Pizza.set_slice_size(10)
print(f"New pizza slice size: {Pizza.get_slice_size()}")      # Output: 10

# Create two pizza instances
pizza1 = Pizza(["cheese", "pepperoni"])
pizza2 = Pizza(["mushrooms", "olives"])

# The change in the class attribute is reflected in all instances
pizza1.display()
# Output:
# A pizza with cheese, pepperoni.
# Each slice is 10 inches.

pizza2.display()
# Output:
# A pizza with mushrooms, olives.
# Each slice is 10 inches.


# --- Using a Factory Method ---

# Create a pizza using the standard __init__ constructor
veggie_pizza = Pizza(["spinach", "feta", "tomatoes"])
veggie_pizza.display()

# Create another pizza using our 'from_string' factory method
meat_lovers_pizza_string = "sausage-bacon-ham"
meat_lovers_pizza = Pizza.from_string(meat_lovers_pizza_string)
meat_lovers_pizza.display()
# Output:
# A pizza with sausage, bacon, ham.
# Each slice is 10 inches.
