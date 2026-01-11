# A module with string utility functions.

def reverse_string(s):
    """Returns the reversed version of a string."""
    return s[::-1]

def count_vowels(s):
    """Counts the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
