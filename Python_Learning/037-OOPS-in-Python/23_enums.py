# Enumerations (Enums) in Python
from enum import Enum, auto

# --- 1. Defining a simple Enum ---
print("--- 1. Simple Enum ---")
class Status(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

# --- 2. Accessing Enum members ---
print("\n--- 2. Accessing Enum members ---")
current_status = Status.IN_PROGRESS

print(f"Current status object: {current_status}")
# You can access the name and value of a member
print(f"Name: {current_status.name}")
print(f"Value: {current_status.value}")

# You can also access members by their value or key
print(f"Status from value 'completed': {Status('completed')}")
print(f"Status from key 'FAILED': {Status['FAILED']}")

# --- 3. Comparing Enum members ---
print("\n--- 3. Comparing Enum members ---")
if current_status == Status.IN_PROGRESS:
    print("The process is currently in progress.")

# Identity checks also work
if current_status is Status.IN_PROGRESS:
    print("Identity check confirms: The process is in progress.")

# You cannot compare an Enum member to its value directly (this is good!)
if current_status == "in_progress":
    print("This will not be printed, which prevents bugs.")
else:
    print("Enum members are not equal to their raw values.")


# --- 4. Using Enums in functions ---
print("\n--- 4. Using Enums in functions ---")
def process_task(status: Status):
    """
    A function that takes a Status enum member as an argument.
    This provides type safety and readability.
    """
    if status == Status.PENDING:
        print("Task is pending. Starting now...")
    elif status == Status.COMPLETED:
        print("Task is already complete. Nothing to do.")
    else:
        print(f"Handling task with status: {status.name}")

process_task(Status.PENDING)
process_task(Status.COMPLETED)
# process_task("pending") # A type checker like mypy would flag this as an error.


# --- 5. Iterating and automatic values ---
print("\n--- 5. Iteration and Auto Values ---")
class Color(Enum):
    RED = auto()    # Gets value 1
    GREEN = auto()  # Gets value 2
    BLUE = auto()   # Gets value 3
    YELLOW = auto() # Gets value 4

print("All available colors:")
for color in Color:
    print(f"  - {color.name} (value: {color.value})")

# The auto() function assigns incremental integer values by default.
print(f"The value of Color.BLUE is: {Color.BLUE.value}")
