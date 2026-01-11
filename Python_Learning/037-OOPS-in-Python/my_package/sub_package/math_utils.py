# A module with math utility functions.

PI = 3.14159

def area_of_circle(radius):
    """Calculates the area of a circle."""
    return PI * (radius ** 2)

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
