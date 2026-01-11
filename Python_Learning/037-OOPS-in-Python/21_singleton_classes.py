# Singleton Pattern Implementation in Python

# The Singleton pattern ensures that a class has only one instance
# and provides a global point of access to it.

# --- Method 1: Using a custom __new__ method ---
print("--- 1. Singleton via __new__ ---")

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # This method is called before __init__ when creating an object.
        if cls._instance is None:
            print("Creating a new DatabaseConnection instance.")
            # If no instance exists, create one using the parent class's __new__
            cls._instance = super().__new__(cls)
        else:
            print("Returning existing DatabaseConnection instance.")
        return cls._instance

    def __init__(self, dsn):
        # The __init__ method will be called every time, so we need to be careful.
        # We can check if the attribute is already set.
        if not hasattr(self, 'dsn'):
            print(f"Initializing connection with DSN: {dsn}")
            self.dsn = dsn

# --- Usage ---
db1 = DatabaseConnection("user:pass@host1:port/db")
db2 = DatabaseConnection("user:pass@host2:port/db") # This DSN will be ignored

# Check if both variables point to the same object
print(f"db1 and db2 are the same object: {db1 is db2}")
print(f"db1 DSN: {db1.dsn}")
print(f"db2 DSN: {db2.dsn}") # Will show the DSN from the first initialization


# --- Method 2: Using a Decorator ---
print("\n--- 2. Singleton via Decorator ---")

def singleton(cls):
    """A decorator that turns a class into a singleton."""
    instances = {}  # Dictionary to store the single instance of each class
    def get_instance(*args, **kwargs):
        if cls not in instances:
            print(f"Creating a new {cls.__name__} instance.")
            instances[cls] = cls(*args, **kwargs)
        else:
            print(f"Returning existing {cls.__name__} instance.")
        return instances[cls]
    return get_instance

@singleton
class AppSettings:
    def __init__(self, theme):
        print(f"Initializing settings with theme: {theme}")
        self.theme = theme
        self.version = "1.0"

# --- Usage ---
settings1 = AppSettings("Dark Mode")
settings2 = AppSettings("Light Mode") # This argument will be ignored

print(f"settings1 and settings2 are the same object: {settings1 is settings2}")
print(f"settings1 theme: {settings1.theme}")
print(f"settings2 theme: {settings2.theme}")


# --- Method 3: Using a Metaclass (Advanced) ---
print("\n--- 3. Singleton via Metaclass ---")

class SingletonMeta(type):
    """A metaclass for creating Singleton classes."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # This method is called when you 'call' the class (e.g., Logger())
        if cls not in cls._instances:
            print(f"Creating a new {cls.__name__} instance via metaclass.")
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            print(f"Returning existing {cls.__name__} instance via metaclass.")
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    def __init__(self, file_name):
        print(f"Initializing logger for file: {file_name}")
        self.file_name = file_name
    
    def log(self, message):
        print(f"Logging to {self.file_name}: {message}")

# --- Usage ---
logger1 = Logger("app.log")
logger2 = Logger("system.log") # This argument will be ignored

print(f"logger1 and logger2 are the same object: {logger1 is logger2}")
logger1.log("This is the first message.")
logger2.log("This is the second message.")
