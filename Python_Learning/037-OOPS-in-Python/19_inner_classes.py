# Inner Classes (Nested Classes) in Python

class Person:
    """Represents a person with a name and a list of addresses."""

    def __init__(self, name):
        self.name = name
        self.addresses = [] # A list to hold Address objects

    def add_address(self, street, city, postal_code, address_type="Home"):
        """
        Method to create and add an Address object to the person's list of addresses.
        """
        # We create an instance of the inner class here.
        address = self.Address(street, city, postal_code, address_type)
        self.addresses.append(address)
        print(f"Added new address for {self.name}.")

    def list_addresses(self):
        """Displays all addresses associated with the person."""
        print(f"\nAddresses for {self.name}:")
        if not self.addresses:
            print("  No addresses on file.")
        for address in self.addresses:
            # We call the 'display' method of the inner class object.
            address.display()

    # --- This is the Inner Class ---
    class Address:
        """
        Represents a physical address. It is nested within Person because
        an address is logically associated with a person in this context.
        """
        def __init__(self, street, city, postal_code, address_type):
            self.street = street
            self.city = city
            self.postal_code = postal_code
            self.type = address_type

        def display(self):
            """Prints the formatted address."""
            print(f"  - Type: {self.type}")
            print(f"    Street: {self.street}")
            print(f"    City: {self.city}, {self.postal_code}")


# --- Using the Outer and Inner Classes ---

# Create an instance of the outer class
p1 = Person("Alice")
p1.list_addresses() # Shows no addresses initially

# Use the outer class's method to create instances of the inner class
p1.add_address("123 Main St", "Anytown", "12345", "Home")
p1.add_address("456 Work Ave", "Busytown", "67890", "Work")

# Display the collected addresses
p1.list_addresses()

# You can also create an instance of the inner class directly,
# but this is often less intuitive for this kind of relationship.
print("\n--- Creating an Inner Class instance directly ---")
# The inner class is accessed like a static member of the outer class.
freestanding_address = Person.Address("999 Lost Rd", "Nowhere", "00000", "Cabin")
freestanding_address.display()
