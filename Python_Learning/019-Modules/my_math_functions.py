def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(f"The __name__ of my_math_functions is: {__name__}")

if __name__ == "__main__":
    print("my_math_functions.py is being run directly")
    print(f"Example of add(1,1): {add(1,1)}")
else:
    print("my_math_functions.py is being imported.")
