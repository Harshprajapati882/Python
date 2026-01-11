# Dynamic Binding (Late Binding) in Python

# All method binding in Python is dynamic.

class EnglishSpeaker:
    def greet(self):
        print("Hello!")

class FrenchSpeaker:
    def greet(self):
        print("Bonjour!")

class SpanishSpeaker:
    def greet(self):
        print("Hola!")

def introduce(speaker):
    """
    This function takes any object and calls the greet() method on it.
    The decision of which greet() method to call is not made until this
    function is actually running. This is dynamic binding.
    """
    print("An introduction...")
    speaker.greet()
    print("...end of introduction.\n")


# --- Demonstration ---

# Create instances of different classes
eng = EnglishSpeaker()
fr = FrenchSpeaker()
spa = SpanishSpeaker()

# Call the same function with objects of different types
introduce(eng)
# Output:
# An introduction...
# Hello!
# ...end of introduction.

introduce(fr)
# Output:
# An introduction...
# Bonjour!
# ...end of introduction.

introduce(spa)
# Output:
# An introduction...
# Hola!
# ...end of introduction.


# --- A more dynamic example ---
print("--- A more dynamic example ---")

# The type of 'speaker_obj' can change during runtime
speaker_obj = EnglishSpeaker()
introduce(speaker_obj) # Binds to EnglishSpeaker.greet()

speaker_obj = FrenchSpeaker()
introduce(speaker_obj) # Binds to FrenchSpeaker.greet()

# We can even use a list to show this
speakers = [SpanishSpeaker(), EnglishSpeaker(), FrenchSpeaker()]
import random

print("\n--- Randomly introducing speakers ---")
for _ in range(3):
    # The 'chosen_speaker' is different in each iteration.
    # The binding of 'chosen_speaker.greet()' happens dynamically inside the
    # 'introduce' function each time it's called.
    chosen_speaker = random.choice(speakers)
    introduce(chosen_speaker)
