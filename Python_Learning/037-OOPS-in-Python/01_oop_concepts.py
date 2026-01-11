# Object-Oriented Programming (OOP) Concepts in Python

# 1. Encapsulation
# The Car class encapsulates the data (make, model, year) and methods (display_info)
# that operate on that data.
class Car:
    def __init__(self, make, model, year):
        self._make = make  # Encapsulated data
        self._model = model
        self._year = year

    def display_info(self):
        print(f"Car: {self._year} {self._make} {self._model}")

# 2. Abstraction
# The user of the Car object doesn't need to know the internal details of
# how display_info() works. They just call the method.
my_car = Car("Toyota", "Corolla", 2022)
my_car.display_info() # Output: Car: 2022 Toyota Corolla

# 3. Inheritance
# The ElectricCar class inherits from the Car class.
# It gains the attributes and methods of Car and adds its own.
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year) # Call the constructor of the base class
        self.battery_size = battery_size

    def display_info(self): # Method overriding (Polymorphism)
        print(f"Electric Car: {self._year} {self._make} {self._model} with a {self.battery_size}-kWh battery.")

my_electric_car = ElectricCar("Tesla", "Model S", 2023, 100)
my_electric_car.display_info() # Output: Electric Car: 2023 Tesla Model S with a 100-kWh battery.

# 4. Polymorphism
# Polymorphism allows us to use objects of different classes through a common interface.
# Here, both Car and ElectricCar have a display_info method.

def print_car_details(car_object):
    car_object.display_info()

print_car_details(my_car)
print_car_details(my_electric_car)

# Another example of polymorphism with a list of different objects
cars = [
    Car("Ford", "Focus", 2019),
    ElectricCar("Nissan", "Leaf", 2021, 62)
]

for car in cars:
    car.display_info()
    # Output:
    # Car: 2019 Ford Focus
    # Electric Car: 2021 Nissan Leaf with a 62-kWh battery.
