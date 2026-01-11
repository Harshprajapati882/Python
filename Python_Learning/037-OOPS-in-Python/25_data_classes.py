# Data Classes in Python
from dataclasses import dataclass, field
from typing import List

# --- 1. A Basic Data Class vs. a Regular Class ---
print("--- 1. Basic Data Class ---")

# The "old" way of creating a class to hold data
class OldProduct:
    def __init__(self, name: str, price: float, sku: str):
        self.name = name
        self.price = price
        self.sku = sku
    
    def __repr__(self):
        return f"OldProduct(name='{self.name}', price={self.price}, sku='{self.sku}')"

    def __eq__(self, other):
        if not isinstance(other, OldProduct):
            return False
        return (self.name == other.name and 
                self.price == other.price and 
                self.sku == other.sku)

# The modern way using the @dataclass decorator
@dataclass
class Product:
    name: str
    price: float
    sku: str

# Let's see what the decorator gives us for free.

# __init__ is automatically created
p1 = Product("Laptop", 1200.50, "LT-123")
p2 = Product("Laptop", 1200.50, "LT-123")
p3 = Product("Mouse", 25.00, "MS-456")

# __repr__ is automatically created and is great for debugging
print(f"Product representation: {p1}")

# __eq__ is automatically created
print(f"Are p1 and p2 equal? {p1 == p2}") # True
print(f"Are p1 and p3 equal? {p1 == p3}") # False


# --- 2. Data Class with Sorting (`order=True`) ---
print("\n--- 2. Data Class with Sorting ---")
@dataclass(order=True)
class Employee:
    # The comparison will be based on 'priority' first, then 'name'.
    priority: int
    name: str

e1 = Employee(1, "Alice")
e2 = Employee(3, "Bob")
e3 = Employee(1, "Charlie")

print(f"Is e1 < e2? {e1 < e2}") # True, because 1 < 3
print(f"Is e1 < e3? {e1 < e3}") # True, because priorities are equal, so 'Alice' < 'Charlie'

# We can now sort a list of these objects
employees = [e2, e1, e3]
employees.sort()
print(f"Sorted employees: {employees}")


# --- 3. Immutable Data Classes (`frozen=True`) ---
print("\n--- 3. Immutable (Frozen) Data Class ---")
@dataclass(frozen=True)
class Configuration:
    host: str
    port: int
    is_https: bool

config = Configuration("api.example.com", 443, True)
print(f"Initial config: {config}")

# Trying to change a value will raise an error
try:
    config.port = 8080
except Exception as e:
    print(f"Error as expected: {e}")


# --- 4. Data Class with Default Values and Field Customization ---
print("\n--- 4. Data Class with Default Values ---")
@dataclass
class InventoryItem:
    name: str
    unit_price: float
    # Use `field` to provide default values for mutable types like lists
    tags: List[str] = field(default_factory=list)
    quantity_on_hand: int = 0

item1 = InventoryItem("Book", 15.99, tags=["fiction", "sci-fi"])
item2 = InventoryItem("Pen", 1.25)
print(item1)
print(item2)
