# Duck Typing in Python

# The principle of duck typing is that an object's suitability for a role
# is determined by its methods and properties, not its class type.

# --- The "Ducks" ---
# These classes are completely unrelated by inheritance.
# However, they share a common interface by convention: they all have a 'speak()' method.

class Duck:
    def speak(self):
        return "Quack!"
    def swim(self):
        return "The duck is swimming."

class Goose:
    def speak(self):
        return "Honk!"
    def swim(self):
        return "The goose is gracefully swimming."

class Mockingbird:
    def speak(self):
        return "Tweet tweet!"
    # This class does not have a swim() method.

# --- The "Duck Test" Function ---
def make_it_speak(bird):
    """
    This function takes any object and calls its 'speak' method.
    It doesn't care about the object's type, only its behavior.
    """
    try:
        sound = bird.speak()
        print(f"The {type(bird).__name__} says: {sound}")
    except AttributeError:
        print(f"This object of type {type(bird).__name__} cannot speak.")

def make_it_swim(bird):
    """
    This function demonstrates the EAFP principle (Easier to Ask for Forgiveness than Permission).
    We just try to call the method and handle the error if it doesn't exist.
    """
    try:
        action = bird.swim()
        print(f"The {type(bird).__name__} does this: '{action}'")
    except AttributeError:
        print(f"This object of type {type(bird).__name__} cannot swim.")

# --- Using the functions ---

duck = Duck()
goose = Goose()
mockingbird = Mockingbird()

# Create a list of different "bird" objects
birds = [duck, goose, mockingbird]

print("--- Testing the 'speak' behavior ---")
for bird in birds:
    make_it_speak(bird)
# Output:
# The Duck says: Quack!
# The Goose says: Honk!
# The Mockingbird says: Tweet tweet!

print("\n--- Testing the 'swim' behavior ---")
for bird in birds:
    make_it_swim(bird)
# Output:
# The Duck does this: 'The duck is swimming.'
# The Goose does this: 'The goose is gracefully swimming.'
# This object of type Mockingbird cannot swim.

# --- Another classic example: file-like objects ---
# The built-in open() function returns a file object.
# The io.StringIO class creates an in-memory text buffer that *behaves* like a file.
import io

# Both of these objects have a .write() method.
file_obj = open("temp.txt", "w")
string_io_obj = io.StringIO()

def write_to_stream(stream):
    """
    This function can write to any object that has a .write() method.
    It doesn't care if it's a real file or an in-memory buffer.
    """
    stream.write("Hello, World!")

write_to_stream(file_obj)
write_to_stream(string_io_obj)

file_obj.close()

# Clean up the temp file
import os
os.remove("temp.txt")

print(f"\nString IO object content: '{string_io_obj.getvalue()}'")
# This shows that duck typing allows for flexible and interchangeable components.
