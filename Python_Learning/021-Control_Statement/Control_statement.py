# ============================================================================
#                   PYTHON CONTROL STATEMENTS - CODE EXAMPLES
# ============================================================================

print("=" * 80)
print("PYTHON CONTROL STATEMENTS - PRACTICAL CODE EXAMPLES")
print("=" * 80)

# ============================================================================
#                        1. SEQUENTIAL STATEMENTS
# ============================================================================
print("\n1. SEQUENTIAL STATEMENTS")
print("-" * 80)

print("First statement")
print("Second statement")
print("Third statement")
print("Statements execute line by line from top to bottom")

# ============================================================================
#                     2. SELECTION/CONDITIONAL STATEMENTS
# ============================================================================

# ----------------------------------------------------------------------------
# 2.1 IF STATEMENT
# ----------------------------------------------------------------------------
print("\n2.1 IF STATEMENT")
print("-" * 80)

age = 18
if age >= 18:
    print(f"Age {age}: You are eligible to vote")

temperature = 35
if temperature > 30 and temperature < 40:
    print(f"Temperature {temperature}°C: It's hot outside!")

# ----------------------------------------------------------------------------
# 2.2 IF-ELSE STATEMENT
# ----------------------------------------------------------------------------
print("\n2.2 IF-ELSE STATEMENT")
print("-" * 80)

number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Nested if-else
marks = 85
if marks >= 90:
    grade = 'A+'
else:
    if marks >= 80:
        grade = 'A'
    else:
        if marks >= 70:
            grade = 'B'
        else:
            grade = 'C'
print(f"Marks: {marks}, Grade: {grade}")

# ----------------------------------------------------------------------------
# 2.3 IF-ELIF-ELSE STATEMENT (Ladder)
# ----------------------------------------------------------------------------
print("\n2.3 IF-ELIF-ELSE STATEMENT")
print("-" * 80)

score = 75

if score >= 90:
    grade = 'A+'
    message = "Outstanding!"
elif score >= 80:
    grade = 'A'
    message = "Excellent!"
elif score >= 70:
    grade = 'B'
    message = "Good job!"
elif score >= 60:
    grade = 'C'
    message = "Average"
elif score >= 50:
    grade = 'D'
    message = "Below average"
else:
    grade = 'F'
    message = "Failed"

print(f"Score: {score}, Grade: {grade}, {message}")

# Traffic light system
light = "yellow"
print(f"\nTraffic Light: {light}")
if light == "red":
    print("STOP! Do not cross.")
elif light == "yellow":
    print("CAUTION! Prepare to stop.")
elif light == "green":
    print("GO! You can cross safely.")
else:
    print("Invalid traffic light color!")

# ----------------------------------------------------------------------------
# 2.4 TERNARY OPERATOR
# ----------------------------------------------------------------------------
print("\n2.4 TERNARY OPERATOR")
print("-" * 80)

x = 10
result = "Greater" if x > 5 else "Smaller or equal"
print(f"x = {x}, Result: {result}")

# Nested ternary
age = 25
category = "Child" if age < 13 else "Teen" if age < 20 else "Adult"
print(f"Age {age}: {category}")

num = -5
status = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(f"{num} is {status}")

# ============================================================================
#                     3. ITERATION/LOOP STATEMENTS
# ============================================================================

# ----------------------------------------------------------------------------
# 3.1 FOR LOOP
# ----------------------------------------------------------------------------
print("\n3.1 FOR LOOP")
print("-" * 80)

# Basic for loop with range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# Iterating over a list
fruits = ["apple", "banana", "cherry", "date"]
print("\nFruits:")
for fruit in fruits:
    print(f"- {fruit}")

# Iterating over a string
word = "Python"
print(f"\nLetters in '{word}':")
for letter in word:
    print(letter, end=" ")
print()

# Using enumerate()
print("\nEnumerated fruits:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Nested for loops - Multiplication table
print("\nMultiplication Table (2 to 4):")
for i in range(2, 5):
    for j in range(1, 6):
        print(f"{i}×{j}={i*j:2d}", end="  ")
    print()

# Iterating over dictionary
student = {"name": "Alice", "age": 20, "grade": "A"}
print("\nStudent Information:")
for key, value in student.items():
    print(f"{key}: {value}")

# ----------------------------------------------------------------------------
# 3.2 WHILE LOOP
# ----------------------------------------------------------------------------
print("\n3.2 WHILE LOOP")
print("-" * 80)

count = 1
print("Counting with while loop (1 to 5):")
while count <= 5:
    print(count, end=" ")
    count += 1
print()

# While loop - withdrawal simulation
balance = 100
withdrawal = 30
print(f"\nInitial balance: ${balance}")
while balance >= withdrawal and balance > 0:
    balance -= withdrawal
    print(f"Withdrew ${withdrawal}. Remaining: ${balance}")

# While loop - sum until condition
number = 1
total = 0
print("\nSum of numbers until total exceeds 50:")
while total < 50:
    total += number
    print(f"Added {number}, Total: {total}")
    number += 1

# ----------------------------------------------------------------------------
# 3.3 NESTED LOOPS & PATTERNS
# ----------------------------------------------------------------------------
print("\n3.3 NESTED LOOPS - PATTERNS")
print("-" * 80)

# Rectangle pattern
print("Rectangle Pattern:")
for i in range(4):
    for j in range(6):
        print("*", end=" ")
    print()

# Right triangle
print("\nRight Triangle:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Number pyramid
print("\nNumber Pyramid:")
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Inverted triangle
print("\nInverted Triangle:")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# ============================================================================
#                     4. LOOP CONTROL STATEMENTS
# ============================================================================

# ----------------------------------------------------------------------------
# 4.1 BREAK STATEMENT
# ----------------------------------------------------------------------------
print("\n4.1 BREAK STATEMENT")
print("-" * 80)

# Finding first multiple of 7
print("Finding first multiple of 7 between 20-50:")
for num in range(20, 51):
    if num % 7 == 0:
        print(f"Found: {num}")
        break

# Breaking from nested loop
print("\nSearching in 2D grid:")
found = False
for i in range(1, 4):
    for j in range(1, 4):
        print(f"Checking ({i}, {j})", end=" ")
        if i == 2 and j == 2:
            print("\nTarget found at (2, 2)!")
            found = True
            break
    if found:
        break

# ----------------------------------------------------------------------------
# 4.2 CONTINUE STATEMENT
# ----------------------------------------------------------------------------
print("\n4.2 CONTINUE STATEMENT")
print("-" * 80)

# Print only odd numbers
print("Odd numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num, end=" ")
print()

# Skip multiples of 3
print("\nNumbers except multiples of 3 (1 to 15):")
for num in range(1, 16):
    if num % 3 == 0:
        continue
    print(num, end=" ")
print()

# ----------------------------------------------------------------------------
# 4.3 PASS STATEMENT
# ----------------------------------------------------------------------------
print("\n4.3 PASS STATEMENT")
print("-" * 80)

print("Demonstrating pass statement:")
for i in range(5):
    if i == 2:
        pass  # Placeholder - does nothing
    else:
        print(i, end=" ")
print("\n(Number 2 was processed but pass did nothing)")

# ----------------------------------------------------------------------------
# 4.4 ELSE WITH LOOPS
# ----------------------------------------------------------------------------
print("\n4.4 ELSE WITH LOOPS")
print("-" * 80)

# for-else example
print("Searching for even number in list [1, 3, 5, 7, 9]:")
numbers = [1, 3, 5, 7, 9]
for num in numbers:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break
else:
    print("No even number found in the list")

# while-else - prime number check
num = 17
print(f"\nChecking if {num} is prime:")
i = 2
while i < num:
    if num % i == 0:
        print(f"{num} is not prime (divisible by {i})")
        break
    i += 1
else:
    print(f"{num} is prime!")

# ============================================================================
#                     5. PRACTICAL EXAMPLES
# ============================================================================
print("\n5. PRACTICAL EXAMPLES")
print("=" * 80)

# ----------------------------------------------------------------------------
# Example 1: Password Validator
# ----------------------------------------------------------------------------
print("\nExample 1: Password Validator")
print("-" * 80)

password = "SecurePass123"
has_upper = has_lower = has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

print(f"Password: {password}")
print(f"Has uppercase: {has_upper}")
print(f"Has lowercase: {has_lower}")
print(f"Has digit: {has_digit}")
print(f"Length >= 8: {len(password) >= 8}")

if has_upper and has_lower and has_digit and len(password) >= 8:
    print("✓ Password is strong!")
else:
    print("✗ Password is weak. Needs uppercase, lowercase, digit, and 8+ chars.")

# ----------------------------------------------------------------------------
# Example 2: Fibonacci Sequence
# ----------------------------------------------------------------------------
print("\nExample 2: Fibonacci Sequence (first 10 terms)")
print("-" * 80)

n = 10
a, b = 0, 1
count = 0
print("Fibonacci sequence:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()

# ----------------------------------------------------------------------------
# Example 3: Number Guessing Game Simulation
# ----------------------------------------------------------------------------
print("\nExample 3: Number Guessing Game (Automated)")
print("-" * 80)

secret_number = 42
guesses = [25, 50, 35, 40, 42]
attempts = 0
max_attempts = 5

print(f"Secret number is {secret_number} (hidden from player)")
for guess in guesses:
    attempts += 1
    print(f"\nAttempt {attempts}: Guessed {guess}")
    
    if guess == secret_number:
        print(f"🎉 Correct! Found in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! ↑")
    else:
        print("Too high! ↓")
    
    if attempts >= max_attempts:
        print(f"Game over! The number was {secret_number}")
        break

# ----------------------------------------------------------------------------
# Example 4: Prime Numbers in Range
# ----------------------------------------------------------------------------
print("\nExample 4: Prime Numbers between 10 and 30")
print("-" * 80)

primes = []
for num in range(10, 31):
    if num < 2:
        continue
    
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        primes.append(num)

print(f"Prime numbers: {primes}")

# ----------------------------------------------------------------------------
# Example 5: Sum of Digits
# ----------------------------------------------------------------------------
print("\nExample 5: Sum of Digits")
print("-" * 80)

number = 12345
digit_sum = 0
temp = number

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp //= 10

print(f"Number: {number}")
print(f"Sum of digits: {digit_sum}")

# ----------------------------------------------------------------------------
# Example 6: Factorial Calculation
# ----------------------------------------------------------------------------
print("\nExample 6: Factorial Calculation")
print("-" * 80)

n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# ----------------------------------------------------------------------------
# Example 7: Reverse a Number
# ----------------------------------------------------------------------------
print("\nExample 7: Reverse a Number")
print("-" * 80)

original = 12345
reversed_num = 0
temp = original

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

print(f"Original: {original}")
print(f"Reversed: {reversed_num}")

# ----------------------------------------------------------------------------
# Example 8: Count Vowels and Consonants
# ----------------------------------------------------------------------------
print("\nExample 8: Count Vowels and Consonants")
print("-" * 80)

text = "Hello World"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Text: '{text}'")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")

# ----------------------------------------------------------------------------
# Example 9: Palindrome Checker
# ----------------------------------------------------------------------------
print("\nExample 9: Palindrome Checker")
print("-" * 80)

word = "radar"
is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[len(word) - 1 - i]:
        is_palindrome = False
        break

print(f"Word: '{word}'")
if is_palindrome:
    print(f"✓ '{word}' is a palindrome")
else:
    print(f"✗ '{word}' is not a palindrome")

# ----------------------------------------------------------------------------
# Example 10: List Comprehension with Conditions
# ----------------------------------------------------------------------------
print("\nExample 10: List Comprehension")
print("-" * 80)

# Squares of numbers
squares = [x**2 for x in range(1, 11)]
print(f"Squares (1-10): {squares}")

# Even squares only
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Labels for odd/even
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 11)]
print(f"Odd/Even labels: {labels}")

# Nested list comprehension - multiplication table
mult_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("\nMultiplication table (nested list comprehension):")
for row in mult_table:
    print(row)

# ============================================================================
#                     6. ADVANCED PATTERNS
# ============================================================================
print("\n6. ADVANCED PATTERNS")
print("=" * 80)

# Diamond pattern
print("\nDiamond Pattern:")
n = 5
# Upper half
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
# Lower half
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Floyd's Triangle
print("\nFloyd's Triangle:")
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# ============================================================================
print("\n" + "=" * 80)
print("✓ ALL EXAMPLES COMPLETED SUCCESSFULLY!")
print("=" * 80)
print("\nKey Takeaways:")
print("1. Use IF-ELIF-ELSE for multiple conditions")
print("2. Choose FOR for known iterations, WHILE for conditions")
print("3. Use BREAK to exit loops, CONTINUE to skip iterations")
print("4. ELSE with loops executes when loop completes normally")
print("5. Practice makes perfect - try modifying these examples!")
print("=" * 80)