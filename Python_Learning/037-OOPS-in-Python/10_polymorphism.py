# Polymorphism in Python

# --- 1. Polymorphism with Class Inheritance ---
print("--- 1. Polymorphism with Class Inheritance ---")

class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        # A generic shape doesn't have a specific area calculation
        raise NotImplementedError("Subclass must implement this method")

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    # Overriding the area method
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
        
    # Overriding the area method
    def area(self):
        return 3.14159 * (self.radius ** 2)

# Create a list of different Shape objects
shapes = [
    Rectangle(10, 5),
    Circle(7)
]

# We can iterate through the list and call the same 'area' method on each object.
# The correct version of the method is called for each object based on its class.
for shape in shapes:
    print(f"The area of the {shape.name} is: {shape.area()}")
# Output:
# The area of the Rectangle is: 50
# The area of the Circle is: 153.93791


# --- 2. Polymorphism with Duck Typing ---
print("\n--- 2. Polymorphism with Duck Typing ---")

class Report:
    def __init__(self, content):
        self.content = content
    
    def render(self):
        print(f"Rendering Report: {self.content}")

class AudioFile:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def render(self):
        print(f"Playing audio file: {self.file_path}")

class VideoFile:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def render(self):
        print(f"Displaying video file: {self.file_path}")

# Note: Report, AudioFile, and VideoFile do not share a common parent class (other than object).
# But they all have a 'render' method.

media_objects = [
    Report("Annual Financials"),
    AudioFile("/media/song.mp3"),
    VideoFile("/media/movie.mp4")
]

# This function works with any object that has a 'render' method.
def process_media(media_list):
    for media in media_list:
        media.render() # Duck typing in action!

process_media(media_objects)
# Output:
# Rendering Report: Annual Financials
# Playing audio file: /media/song.mp3
# Displaying video file: /media/movie.mp4


# --- 3. Polymorphism with Operators ---
print("\n--- 3. Polymorphism with Operators ---")

# The '+' operator behaves differently for different types
num1 = 10
num2 = 20
print(f"Addition of numbers: {num1 + num2}") # Performs addition

str1 = "Hello"
str2 = " World"
print(f"Concatenation of strings: {str1 + str2}") # Performs concatenation

list1 = [1, 2, 3]
list2 = [4, 5]
print(f"Merging of lists: {list1 + list2}") # Performs list merging
