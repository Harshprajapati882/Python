# Access Modifiers in Python

class Gadget:
    def __init__(self, name, version):
        # Public attribute
        self.name = name
        
        # Protected attribute (by convention)
        self._version = version
        
        # Private attribute (name mangling will happen)
        self.__serial_number = f"SN{hash(name)}"

    # Public method
    def display_info(self):
        print(f"Gadget: {self.name}, Version: {self._version}")

    # A method to access the private attribute within the class
    def get_serial_number(self):
        return f"Serial Number (accessed from within the class): {self.__serial_number}"
        
    def _protected_method(self):
        print("This is a protected method.")

    def __private_method(self):
        print("This is a private method.")

# --- Inheriting from the Gadget class ---
class AdvancedGadget(Gadget):
    def __init__(self, name, version, feature):
        super().__init__(name, version)
        self.feature = feature

    def show_version(self):
        # Subclasses can access protected members
        print(f"Version from subclass: {self._version}")
        self._protected_method() # Can call protected methods

    def try_access_private(self):
        # Subclasses cannot directly access private members of the parent
        try:
            print(self.__serial_number)
        except AttributeError as e:
            print(f"Error accessing private attribute: {e}")
        # Error: 'AdvancedGadget' object has no attribute '_AdvancedGadget__serial_number'
        # Note that it's looking for a different name than the original.


# --- Creating an instance and accessing members ---

gadget = Gadget("SmartWatch", "2.1")

# 1. Accessing Public members (Allowed)
print(f"Public attribute: {gadget.name}")
gadget.display_info()

# 2. Accessing Protected members (Discouraged, but possible)
print(f"Protected attribute (direct access): {gadget._version}")
gadget._protected_method() # This also works, but is not recommended

# 3. Accessing Private members (Causes an error)
try:
    print(gadget.__serial_number)
except AttributeError as e:
    print(f"Error accessing private attribute directly: {e}")

# You can access private members via "name mangling" (strongly discouraged)
print(f"Private attribute (via name mangling): {gadget._Gadget__serial_number}")

# Accessing private attribute via a public method (the correct way)
print(gadget.get_serial_number())


print("\n--- Testing Subclass Access ---")
adv_gadget = AdvancedGadget("SmartGlasses", "3.0", "AR Display")
adv_gadget.show_version()
adv_gadget.try_access_private()
