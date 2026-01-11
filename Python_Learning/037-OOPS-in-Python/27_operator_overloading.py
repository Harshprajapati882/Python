# Operator Overloading in Python

class Vector:
    """A simple class representing a 2D vector."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # --- Overloading Arithmetic Operators ---
    def __add__(self, other):
        """Overloads the + operator."""
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Overloads the - operator."""
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)
        
    def __mul__(self, scalar):
        """Overloads the * operator for scalar multiplication."""
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)

    # --- Overloading Comparison Operators ---
    def __eq__(self, other):
        """Overloads the == operator."""
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y

    # To implement comparisons like < or >, we usually need a way to
    # represent the vector's "magnitude".
    def __abs__(self):
        """Overloads the abs() function to return the vector's magnitude."""
        return (self.x**2 + self.y**2)**0.5

    def __lt__(self, other):
        """Overloads the < operator based on magnitude."""
        if not isinstance(other, Vector):
            return NotImplemented
        return abs(self) < abs(other)

    # --- Overloading Built-in Functions ---
    def __len__(self):
        """Overloads the len() function. A bit unusual for a vector, but for demonstration."""
        # For a vector, perhaps len() could mean the number of dimensions.
        return 2

    def __repr__(self):
        """A developer-friendly representation."""
        return f"Vector({self.x}, {self.y})"
        
    def __str__(self):
        """A user-friendly representation."""
        return f"({self.x}, {self.y})"


# --- Using the overloaded operators ---

v1 = Vector(2, 3)
v2 = Vector(5, 1)

print(f"v1 = {v1}")
print(f"v2 = {v2}")

# Using '+' from __add__
v_sum = v1 + v2
print(f"v1 + v2 = {v_sum}")

# Using '-' from __sub__
v_diff = v1 - v2
print(f"v1 - v2 = {v_diff}")

# Using '*' from __mul__
v_scaled = v1 * 3
print(f"v1 * 3 = {v_scaled}")

# Using '==' from __eq__
v3 = Vector(2, 3)
print(f"Is v1 == v2? {v1 == v2}") # False
print(f"Is v1 == v3? {v1 == v3}") # True

# Using '<' from __lt__ and abs() from __abs__
print(f"Magnitude of v1: {abs(v1):.2f}")
print(f"Magnitude of v2: {abs(v2):.2f}")
print(f"Is v1 < v2? {v1 < v2}") # True, because 2.65 < 5.1

# Using len() from __len__
print(f"Dimensions in v1: {len(v1)}")
