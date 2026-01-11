# Encapsulation in Python

# --- Example 1: Using Getters and Setters ---
print("--- 1. Using traditional Getters and Setters ---")
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        # This attribute is 'protected' by convention.
        # We don't want it to be changed directly without validation.
        self._balance = initial_balance

    # A 'getter' method to securely retrieve the balance.
    def get_balance(self):
        # In a real app, you might add security checks here.
        print("Verifying access rights...")
        return self._balance

    # A 'setter' method for depositing money.
    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
        self._balance += amount
        print(f"Deposited ${amount}. New balance: ${self._balance}")

    # Another 'setter' method for withdrawing money.
    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return
        if self._balance < amount:
            print(f"Error: Insufficient funds. Current balance: ${self._balance}")
            return
        self._balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self._balance}")

# --- Usage ---
acc1 = BankAccount("John Doe", 500)

# We interact with the object through its public methods, not by direct access.
print(f"Account Holder: {acc1.account_holder}")
acc1.deposit(200)
acc1.withdraw(150)
current_balance = acc1.get_balance()
print(f"Final retrieved balance: ${current_balance}")

# Trying to set a negative deposit fails due to the validation in the method.
acc1.deposit(-50) 

# While possible, direct access to '_balance' is discouraged by the underscore convention.
# Bypassing the methods means we can put the object in an invalid state.
# acc1._balance = -1000 # This is bad practice!


# --- Example 2: Using @property for a more Pythonic approach ---
print("\n--- 2. Using the @property decorator ---")
class Student:
    def __init__(self, name, age):
        self.name = name
        # The actual data is stored in a 'private' attribute.
        self.__age = age

    @property
    def age(self):
        """This is the 'getter'. It's accessed like a public attribute."""
        return self.__age

    @age.setter
    def age(self, new_age):
        """This is the 'setter'. It provides controlled access."""
        if 10 <= new_age <= 100:
            self.__age = new_age
        else:
            print("Error: Age must be between 10 and 100.")

# --- Usage ---
s1 = Student("Jane Smith", 18)

# Accessing the age using the @property (looks like a public attribute)
print(f"{s1.name}'s age is {s1.age}") # The age() getter is called automatically.

# Changing the age using the setter
s1.age = 19 # The age() setter is called automatically.
print(f"Jane's new age is {s1.age}")

# Trying to set an invalid age is prevented by the setter's logic.
s1.age = 120 # Output: Error: Age must be between 10 and 100.
print(f"Jane's age remains {s1.age}")
