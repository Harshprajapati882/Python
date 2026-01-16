"""
Lambda Expressions in Python
=====================================
A comprehensive guide to lambda functions with practical examples
"""

print("=" * 70)
print("LAMBDA EXPRESSIONS IN PYTHON")
print("=" * 70)

# ==================== 1. BASIC SYNTAX ====================
print("\n1. BASIC SYNTAX")
print("-" * 70)

# No arguments
greet = lambda: "Hello, World!"
print(f"No args: {greet()}")

# Single argument
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Multiple arguments
add = lambda x, y: x + y
print(f"Add 10 + 20: {add(10, 20)}")

# Three arguments
multiply = lambda a, b, c: a * b * c
print(f"Multiply 2 * 3 * 4: {multiply(2, 3, 4)}")

# ==================== 2. PARAMETERS ====================
print("\n2. PARAMETERS")
print("-" * 70)

# Default parameters
power = lambda x, exp=2: x ** exp
print(f"Square (default): {power(5)}")
print(f"Cube (custom): {power(5, 3)}")

# Variable-length arguments (*args)
sum_all = lambda *args: sum(args)
print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")

# Multiple default parameters
greet_person = lambda name="Guest", greeting="Hello": f"{greeting}, {name}!"
print(f"Default greeting: {greet_person()}")
print(f"Custom greeting: {greet_person('Alice', 'Hi')}")

# ==================== 3. ARITHMETIC EXPRESSIONS ====================
print("\n3. ARITHMETIC EXPRESSIONS")
print("-" * 70)

operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y,
    "power": lambda x, y: x ** y,
    "modulo": lambda x, y: x % y,
}

num1, num2 = 10, 3
for op_name, op_func in operations.items():
    print(f"{num1} {op_name} {num2} = {op_func(num1, num2)}")

# ==================== 4. CONDITIONAL EXPRESSIONS ====================
print("\n4. CONDITIONAL EXPRESSIONS (Ternary)")
print("-" * 70)

# Simple if-else
max_num = lambda x, y: x if x > y else y
print(f"Max of 15 and 8: {max_num(15, 8)}")

# Multiple conditions
grade = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
for score in [95, 85, 75, 65]:
    print(f"Score {score}: Grade {grade(score)}")

# Absolute value using ternary
absolute = lambda x: x if x >= 0 else -x
print(f"Absolute value of -15: {absolute(-15)}")

# ==================== 5. STRING EXPRESSIONS ====================
print("\n5. STRING EXPRESSIONS")
print("-" * 70)

uppercase = lambda s: s.upper()
lowercase = lambda s: s.lower()
capitalize_str = lambda s: s.capitalize()
reverse = lambda s: s[::-1]
count_vowels = lambda s: sum(1 for char in s.lower() if char in 'aeiou')

text = "Python Lambda"
print(f"Original: {text}")
print(f"Uppercase: {uppercase(text)}")
print(f"Lowercase: {lowercase(text)}")
print(f"Capitalized: {capitalize_str(text)}")
print(f"Reversed: {reverse(text)}")
print(f"Vowel count: {count_vowels(text)}")

# String formatting
format_fullname = lambda first, last: f"{first.title()} {last.title()}"
print(f"Formatted name: {format_fullname('john', 'doe')}")

# ==================== 6. LIST/COLLECTION EXPRESSIONS ====================
print("\n6. LIST/COLLECTION EXPRESSIONS")
print("-" * 70)

first_elem = lambda lst: lst[0]
last_elem = lambda lst: lst[-1]
list_sum = lambda lst: sum(lst)
list_avg = lambda lst: sum(lst) / len(lst)
list_length = lambda lst: len(lst)
list_max = lambda lst: max(lst)
list_min = lambda lst: min(lst)

numbers = [10, 20, 30, 40, 50]
print(f"List: {numbers}")
print(f"First: {first_elem(numbers)}")
print(f"Last: {last_elem(numbers)}")
print(f"Sum: {list_sum(numbers)}")
print(f"Average: {list_avg(numbers)}")
print(f"Length: {list_length(numbers)}")
print(f"Max: {list_max(numbers)}")
print(f"Min: {list_min(numbers)}")

# ==================== 7. BOOLEAN EXPRESSIONS ====================
print("\n7. BOOLEAN EXPRESSIONS")
print("-" * 70)

is_positive = lambda x: x > 0
is_negative = lambda x: x < 0
is_even = lambda x: x % 2 == 0
is_odd = lambda x: x % 2 != 0
is_palindrome = lambda s: s == s[::-1]
is_empty = lambda lst: len(lst) == 0

test_num = 7
print(f"Number: {test_num}")
print(f"Is positive: {is_positive(test_num)}")
print(f"Is negative: {is_negative(test_num)}")
print(f"Is even: {is_even(test_num)}")
print(f"Is odd: {is_odd(test_num)}")

test_word = "racecar"
print(f"\nWord: {test_word}")
print(f"Is palindrome: {is_palindrome(test_word)}")

# ==================== 8. MAP() - TRANSFORM DATA ====================
print("\n8. MAP() - TRANSFORM DATA")
print("-" * 70)

numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")

# Double each element
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")

# Square each element
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {squared}")

# Convert to strings
strings = list(map(lambda x: f"num_{x}", numbers))
print(f"Formatted: {strings}")

# Convert string numbers to integers
str_nums = ["1", "2", "3", "4", "5"]
integers = list(map(lambda x: int(x), str_nums))
print(f"String to int: {integers}")

# Convert strings to uppercase
words = ["apple", "banana", "cherry", "date"]
upper_words = list(map(lambda w: w.upper(), words))
print(f"Words uppercase: {upper_words}")

# Complex transformation: dictionary values
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
names = list(map(lambda p: p["name"], people))
ages = list(map(lambda p: p["age"], people))
print(f"Names: {names}")
print(f"Ages: {ages}")

# ==================== 9. FILTER() - SELECT DATA ====================
print("\n9. FILTER() - SELECT DATA")
print("-" * 70)

numbers = list(range(1, 11))
print(f"Original: {numbers}")

# Even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Odd numbers
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Odd numbers: {odds}")

# Numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Greater than 5: {greater_than_5}")

# Filter strings
words = ["apple", "ant", "ball", "bat", "cat", "dog"]
words_with_a = list(filter(lambda w: 'a' in w, words))
print(f"Words containing 'a': {words_with_a}")

# Filter by length
long_words = list(filter(lambda w: len(w) > 4, words))
print(f"Words with length > 4: {long_words}")

# Filter dictionaries
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 16},
    {"name": "Charlie", "age": 25}
]
adults = list(filter(lambda p: p["age"] >= 18, people))
print(f"Adults: {adults}")

# ==================== 10. REDUCE() - AGGREGATE DATA ====================
print("\n10. REDUCE() - AGGREGATE DATA")
print("-" * 70)

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum
total = reduce(lambda x, y: x + y, numbers)
print(f"Numbers: {numbers}")
print(f"Sum (reduce): {total}")

# Product (multiply all)
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")

# Concatenate strings
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda x, y: x + y, words)
print(f"Concatenated: {sentence}")

# Find maximum
max_num = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum: {max_num}")

# Find minimum
min_num = reduce(lambda x, y: x if x < y else y, numbers)
print(f"Minimum: {min_num}")

# Build a sentence from list
words = ["Python", "Lambda", "Expressions", "Rock"]
phrase = reduce(lambda x, y: x + " " + y, words)
print(f"Phrase: {phrase}")

# ==================== 11. SORTED() WITH KEY PARAMETER ====================
print("\n11. SORTED() WITH KEY PARAMETER")
print("-" * 70)

# Sort numbers by absolute value
numbers = [-5, 3, -1, 8, -2]
sorted_by_abs = sorted(numbers, key=lambda x: abs(x))
print(f"Original: {numbers}")
print(f"Sorted by absolute value: {sorted_by_abs}")

# Sort strings by length
words = ["python", "is", "awesome", "code"]
sorted_by_len = sorted(words, key=lambda w: len(w))
print(f"\nWords: {words}")
print(f"Sorted by length: {sorted_by_len}")

# Sort tuples by second element
students = [("Alice", 85), ("Bob", 75), ("Charlie", 90), ("Diana", 80)]
sorted_by_score = sorted(students, key=lambda x: x[1])
print(f"\nStudents: {students}")
print(f"Sorted by score: {sorted_by_score}")

# Sort dictionaries by value
scores = {"Alice": 85, "Bob": 75, "Charlie": 90}
sorted_scores = sorted(scores.items(), key=lambda x: x[1])
print(f"\nScores: {scores}")
print(f"Sorted by score: {sorted_scores}")

# Sort with reverse=True
descending = sorted(numbers, key=lambda x: abs(x), reverse=True)
print(f"\nSorted by absolute value (descending): {descending}")

# Multi-level sort
employees = [
    {"name": "Alice", "dept": "IT", "salary": 50000},
    {"name": "Bob", "dept": "HR", "salary": 60000},
    {"name": "Charlie", "dept": "IT", "salary": 55000},
]
sorted_emp = sorted(employees, key=lambda e: (e["dept"], e["salary"]))
print(f"\nEmployees sorted by dept, then salary: {sorted_emp}")

# ==================== 12. MIN() AND MAX() WITH KEY ====================
print("\n12. MIN() AND MAX() WITH KEY")
print("-" * 70)

students = [("Alice", 85), ("Bob", 75), ("Charlie", 90), ("Diana", 80)]
print(f"Students: {students}")

# Find student with max score
top_student = max(students, key=lambda x: x[1])
print(f"Top student: {top_student}")

# Find student with min score
lowest_student = min(students, key=lambda x: x[1])
print(f"Lowest student: {lowest_student}")

# Find longest word
words = ["python", "is", "awesome", "code"]
longest = max(words, key=lambda w: len(w))
shortest = min(words, key=lambda w: len(w))
print(f"\nWords: {words}")
print(f"Longest: {longest}")
print(f"Shortest: {shortest}")

# ==================== 13. FUNCTIONAL PROGRAMMING PATTERNS ====================
print("\n13. FUNCTIONAL PROGRAMMING PATTERNS")
print("-" * 70)

# Pattern 1: Pipeline Processing
print("Pattern 1: Pipeline Processing")
data = [1, 2, 3, 4, 5]
# Filter even, multiply by 2, sum
result = sum(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, data)))
print(f"Data: {data}")
print(f"Filter even → multiply by 2 → sum: {result}")

# Pattern 2: Currying / Function Factory
print("\nPattern 2: Function Factory")
def multiplier(factor):
    return lambda x: x * factor

times_2 = multiplier(2)
times_5 = multiplier(5)
times_10 = multiplier(10)

print(f"10 * 2 = {times_2(10)}")
print(f"10 * 5 = {times_5(10)}")
print(f"10 * 10 = {times_10(10)}")

# Pattern 3: Composition
print("\nPattern 3: Function Composition")
add_5 = lambda x: x + 5
multiply_2 = lambda x: x * 2
square = lambda x: x ** 2

# Compose: (x + 5) * 2 squared
value = 3
result = square(multiply_2(add_5(value)))
print(f"((({value} + 5) * 2) ^ 2) = {result}")

# Pattern 4: Higher-order functions
print("\nPattern 4: Higher-Order Functions")
def apply_operation(x, y, operation):
    return operation(x, y)

print(f"5 + 3 = {apply_operation(5, 3, lambda a, b: a + b)}")
print(f"5 - 3 = {apply_operation(5, 3, lambda a, b: a - b)}")
print(f"5 * 3 = {apply_operation(5, 3, lambda a, b: a * b)}")
print(f"5 / 3 = {apply_operation(5, 3, lambda a, b: a / b)}")

# ==================== 14. PRACTICAL USE CASES ====================
print("\n14. PRACTICAL USE CASES")
print("-" * 70)

# Use Case 1: Data Validation
print("Use Case 1: Email Validation")
is_valid_email = lambda email: "@" in email and "." in email
emails = ["user@example.com", "invalid.email", "test@gmail.com"]
valid_emails = list(filter(is_valid_email, emails))
print(f"Valid emails: {valid_emails}")

# Use Case 2: Data Cleaning
print("\nUse Case 2: Data Cleaning - Remove None values")
data = [1, None, 3, None, 5, 6]
clean_data = list(filter(lambda x: x is not None, data))
print(f"Original: {data}")
print(f"Cleaned: {clean_data}")

# Use Case 3: Sorting Complex Data
print("\nUse Case 3: Sorting Complex Data")
books = [
    {"title": "Python Guide", "author": "John", "year": 2020},
    {"title": "Learn Lambda", "author": "Alice", "year": 2021},
    {"title": "Advanced Python", "author": "Bob", "year": 2019},
]
sorted_books = sorted(books, key=lambda b: b["year"])
for book in sorted_books:
    print(f"  {book['title']} ({book['year']}) by {book['author']}")

# Use Case 4: Processing API Response
print("\nUse Case 4: Processing Data")
response = [
    {"id": 1, "name": "Alice", "status": "active"},
    {"id": 2, "name": "Bob", "status": "inactive"},
    {"id": 3, "name": "Charlie", "status": "active"},
]
active_users = list(filter(lambda u: u["status"] == "active", response))
user_names = list(map(lambda u: u["name"], active_users))
print(f"Active users: {user_names}")

# ==================== 15. LAMBDA IN COMPREHENSIONS ====================
print("\n15. LAMBDA IN COMPREHENSIONS")
print("-" * 70)

# While lambdas work with comprehensions, list comprehensions are often clearer
numbers = [1, 2, 3, 4, 5]

# Traditional lambda with map
squared_lambda = list(map(lambda x: x ** 2, numbers))
print(f"Lambda approach: {squared_lambda}")

# List comprehension (often preferred)
squared_comp = [x ** 2 for x in numbers]
print(f"Comprehension approach: {squared_comp}")

# Filtered list comprehension
evens_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Lambda filter: {evens_lambda}")

evens_comp = [x for x in numbers if x % 2 == 0]
print(f"Comprehension filter: {evens_comp}")

# ==================== 16. LAMBDA VS REGULAR FUNCTION ====================
print("\n16. LAMBDA VS REGULAR FUNCTION")
print("-" * 70)

# Simple case - Lambda is better
print("Simple case - Lambda preferred:")
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {result}")

# Complex case - Regular function is better
print("\nComplex case - Regular function preferred:")

def process_complex(x):
    """Process with multiple steps"""
    if x < 0:
        return abs(x)
    elif x == 0:
        return 1
    else:
        return x ** 2

# Instead of trying to create complex lambda:
# process = lambda x: abs(x) if x < 0 else 1 if x == 0 else x ** 2
results = [process_complex(x) for x in [-3, 0, 5, -1, 2]]
print(f"Results: {results}")

# ==================== 17. COMMON MISTAKES ====================
print("\n17. COMMON MISTAKES")
print("-" * 70)

# Mistake 1: Trying to use statements in lambda
print("Mistake 1: Lambda doesn't support statements")
print("DON'T: lambda x: y = x + 1  # SyntaxError!")
print("DO: lambda x: x + 1")

# Mistake 2: Reusing lambda when function would be better
print("\nMistake 2: Complex logic in lambda")
print("DON'T: lambda x: (x ** 2) if (x > 0) else ((-x) ** 2) if (x < 0) else 0")
print("DO: Use a regular function for complex logic")

# Mistake 3: Loop variable in lambda (closure issue)
print("\nMistake 3: Loop variable capture (closure)")
funcs = [lambda x, i=i: x + i for i in range(5)]
# Without i=i, all lambdas would capture the same 'i'
results = [f(10) for f in funcs]
print(f"Results: {results}")

# ==================== 18. ADVANCED EXAMPLES ====================
print("\n18. ADVANCED EXAMPLES")
print("-" * 70)

# Example 1: Chaining operations
print("Example 1: Chaining operations")
data = "hello world python"
result = data.upper().replace(" ", "_")
print(f"Result: {result}")

# Example 2: Complex sorting
print("\nExample 2: Complex sorting")
people = [
    {"name": "Alice", "age": 30, "city": "NYC"},
    {"name": "Bob", "age": 25, "city": "LA"},
    {"name": "Charlie", "age": 30, "city": "Chicago"},
]
# Sort by age (ascending), then by name (alphabetically)
sorted_people = sorted(people, key=lambda p: (p["age"], p["name"]))
for person in sorted_people:
    print(f"  {person['name']}, {person['age']}, {person['city']}")

# Example 3: Nested data processing
print("\nExample 3: Nested data processing")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = reduce(lambda x, y: x + y, matrix)
print(f"Flattened matrix: {flattened}")

# Example 4: Counting occurrences
print("\nExample 4: Counting specific elements")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count_3s = sum(map(lambda x: 1 if x == 3 else 0, numbers))
print(f"Count of 3s: {count_3s}")

# ==================== 19. PERFORMANCE CONSIDERATION ====================
print("\n19. PERFORMANCE CONSIDERATION")
print("-" * 70)

import time

numbers = list(range(100000))

# Method 1: Lambda with map
start = time.time()
result1 = list(map(lambda x: x ** 2, numbers))
time1 = time.time() - start

# Method 2: List comprehension
start = time.time()
result2 = [x ** 2 for x in numbers]
time2 = time.time() - start

print(f"Lambda + map time: {time1:.6f}s")
print(f"List comprehension time: {time2:.6f}s")
print(f"Results are equal: {result1 == result2}")

# ==================== 20. KEY TAKEAWAYS ====================
print("\n20. KEY TAKEAWAYS")
print("-" * 70)
print("""
✓ Lambda creates anonymous, single-expression functions
✓ Perfect for use with map(), filter(), sorted()
✓ Useful for short callbacks and temporary functions
✓ Concise and readable for simple operations
✓ Use regular functions for complex logic
✓ Preferred in functional programming patterns
✓ Can have multiple parameters and default values
✓ Always returns the result of its expression implicitly
✓ Best used with built-in higher-order functions
✓ Keep lambdas simple - prioritize readability!
""")

print("\n" + "=" * 70)
print("END OF LAMBDA EXPRESSIONS GUIDE")
print("=" * 70)
