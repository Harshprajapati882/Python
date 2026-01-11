# Multilevel Inheritance in Python

# Level 1: Grandparent Class
class Vehicle:
    def __init__(self, make, year):
        self.make = make
        self.year = year
        print("Vehicle constructor called.")

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

# Level 2: Parent Class (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, make, year, number_of_doors):
        # Call the constructor of the immediate parent (Vehicle)
        super().__init__(make, year)
        self.number_of_doors = number_of_doors
        print("Car constructor called.")

    def drive(self):
        print(f"The {self.make} is driving.")

# Level 3: Child Class (inherits from Car)
class ElectricCar(Car):
    def __init__(self, make, year, number_of_doors, battery_capacity):
        # Call the constructor of the immediate parent (Car)
        super().__init__(make, year, number_of_doors)
        self.battery_capacity = battery_capacity
        print("ElectricCar constructor called.")

    # Overriding a method from the Grandparent class
    def start_engine(self):
        print("Electric motor is now active (no engine sound).")

    def charge_battery(self):
        print(f"Charging the {self.battery_capacity}kWh battery.")


# --- Using the classes ---

print("--- Creating a Vehicle object ---")
v = Vehicle("Generic", 2000)
v.start_engine() # Output: Engine started.

print("\n" + "="*30 + "\n")

print("--- Creating a Car object ---")
# This calls constructors for Vehicle and Car
my_car = Car("Honda", 2021, 4)
my_car.start_engine() # Inherited from Vehicle
my_car.drive()        # From Car class

print("\n" + "="*30 + "\n")

print("--- Creating an ElectricCar object ---")
# This calls constructors for Vehicle, Car, and ElectricCar
my_tesla = ElectricCar("Tesla", 2023, 4, 100)

# Calling methods from all levels of the hierarchy:
my_tesla.start_engine()   # Overridden in ElectricCar
my_tesla.drive()          # Inherited from Car
my_tesla.stop_engine()    # Inherited from Vehicle
my_tesla.charge_battery() # Specific to ElectricCar

print("\n--- Inspecting the MRO ---")
# The Method Resolution Order shows the chain of inheritance
print(ElectricCar.__mro__)
# Output:
# (<class '__main__.ElectricCar'>, <class '__main__.Car'>, <class '__main__.Vehicle'>, <class 'object'>)
