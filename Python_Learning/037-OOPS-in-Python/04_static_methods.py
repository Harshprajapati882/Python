# Static Methods in Python

class MathUtils:
    # This class groups together related mathematical functions.
    # It doesn't need to be instantiated because all its methods are static.

    def __init__(self):
        # The __init__ method is not necessary here, but we include it
        # to show that even if you create an instance, the static methods
        # don't depend on it.
        print("MathUtils instance created (but not needed for static methods).")

    @staticmethod
    def add(x, y):
        """A static method to add two numbers."""
        # This method doesn't use 'self' or 'cls'.
        # It only works with the arguments it receives.
        return x + y

    @staticmethod
    def multiply(x, y):
        """A static method to multiply two numbers."""
        return x * y

    @staticmethod
    def is_even(num):
        """A static method to check if a number is even."""
        return num % 2 == 0


# --- Using Static Methods ---

# You can call static methods directly on the class without creating an instance.
sum_result = MathUtils.add(5, 10)
print(f"The sum is: {sum_result}")  # Output: The sum is: 15

product_result = MathUtils.multiply(4, 6)
print(f"The product is: {product_result}")  # Output: The product is: 24

# --- Example with a more practical class ---

class TemperatureConverter:
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Converts Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Converts Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5/9

# No instance is needed. We can use the class as a namespace for our functions.
celsius_temp = 25
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")
# Output: 25°C is equal to 77.0°F

fahrenheit_temp = 68
celsius_temp = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is equal to {celsius_temp}°C")
# Output: 68°F is equal to 20.0°C


# You can also call static methods on an instance, but it's less common
# and doesn't provide any additional benefit.
math_instance = MathUtils() # "MathUtils instance created..." is printed
check_num = math_instance.is_even(7)
print(f"Is 7 even? {check_num}") # Output: Is 7 even? False
