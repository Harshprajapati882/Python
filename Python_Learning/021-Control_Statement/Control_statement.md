# Python Control Statements - Complete Notes

## Table of Contents
1. [Introduction](#introduction)
2. [Sequential Statements](#sequential-statements)
3. [Selection/Conditional Statements](#selection-statements)
4. [Iteration/Loop Statements](#iteration-statements)
5. [Loop Control Statements](#loop-control-statements)
6. [Best Practices](#best-practices)

---

## Introduction

**Control statements** manage the flow of program execution. Instead of executing code line by line, control statements allow us to make decisions, repeat actions, and jump to different parts of code.

### Three Categories:
1. **Sequential** - Default top-to-bottom execution
2. **Selection** - Conditional execution (if, elif, else)
3. **Iteration** - Repeated execution (for, while)

---

## Sequential Statements

By default, Python executes statements sequentially from top to bottom.

```
Statement 1
Statement 2
Statement 3
```

Each statement executes in order, one after another.

---

## Selection Statements

### 1. IF Statement

Executes a code block only when a condition is **True**.

**Syntax:**
```
if condition:
    statement(s)
```

**Key Points:**
- Condition must evaluate to True or False
- Indentation (4 spaces) defines the code block
- If condition is False, the block is skipped

### 2. IF-ELSE Statement

Provides two paths: one for True, one for False.

**Syntax:**
```
if condition:
    statement(s)
else:
    statement(s)
```

**Use Cases:**
- Even/odd checking
- Pass/fail decisions
- Binary choices

### 3. IF-ELIF-ELSE Statement (Ladder)

Checks multiple conditions sequentially. Only the first True condition executes.

**Syntax:**
```
if condition1:
    statement(s)
elif condition2:
    statement(s)
elif condition3:
    statement(s)
else:
    statement(s)
```

**Advantages over nested if-else:**
- More readable
- Better performance
- Easier to maintain

**Use Cases:**
- Grade calculation
- Menu selection
- Traffic light systems
- Category classification

### 4. Nested IF Statements

An if statement inside another if statement.

**Syntax:**
```
if condition1:
    if condition2:
        statement(s)
    else:
        statement(s)
else:
    statement(s)
```

**When to Use:**
- Multiple dependent conditions
- Complex decision trees

**Warning:** Too many nested levels reduce readability. Consider elif instead.

### 5. Ternary Operator (Conditional Expression)

A compact one-line if-else statement.

**Syntax:**
```
value_if_true if condition else value_if_false
```

**Examples:**
- `result = "Pass" if marks >= 40 else "Fail"`
- `max_val = a if a > b else b`

**Best Practice:** Use for simple conditions only. Complex logic should use regular if-else.

---

## Iteration Statements

### 1. FOR Loop

Iterates over a sequence (list, tuple, string, range, dictionary, etc.)

**Syntax:**
```
for variable in sequence:
    statement(s)
```

**Common Uses:**

**With range():**
- `range(n)` - 0 to n-1
- `range(start, stop)` - start to stop-1
- `range(start, stop, step)` - with custom increment

**With sequences:**
- Lists: `for item in my_list:`
- Strings: `for char in my_string:`
- Tuples: `for element in my_tuple:`
- Dictionary: `for key, value in my_dict.items():`

**enumerate():** Get both index and value
```
for index, value in enumerate(sequence):
```

**zip():** Iterate multiple sequences together
```
for item1, item2 in zip(list1, list2):
```

### 2. WHILE Loop

Repeats as long as a condition remains True.

**Syntax:**
```
while condition:
    statement(s)
    # Must update condition variable to avoid infinite loop
```

**Key Differences from FOR:**
- FOR: Known number of iterations
- WHILE: Unknown iterations, depends on condition

**Common Uses:**
- User input validation
- Game loops
- Processing until specific condition
- Menu-driven programs

**Warning:** Always ensure the condition will eventually become False to avoid infinite loops.

### 3. Nested Loops

A loop inside another loop.

**Syntax:**
```
for i in outer_sequence:
    for j in inner_sequence:
        statement(s)
```

**Use Cases:**
- 2D arrays/matrices
- Pattern printing
- Combinations and permutations
- Nested data structures

**Performance Note:** Be cautious with nested loops on large datasets. Time complexity multiplies (O(n²), O(n³), etc.)

---

## Loop Control Statements

### 1. BREAK Statement

Immediately exits the loop, regardless of the condition.

**Syntax:**
```
for/while loop:
    if condition:
        break
```

**Use Cases:**
- Found what you're searching for
- Error condition detected
- User wants to exit

**In Nested Loops:** Break only exits the innermost loop.

### 2. CONTINUE Statement

Skips the rest of the current iteration and moves to the next one.

**Syntax:**
```
for/while loop:
    if condition:
        continue
    statement(s)  # Skipped if continue executes
```

**Use Cases:**
- Skip invalid data
- Filter specific values
- Skip processing certain items

### 3. PASS Statement

Does nothing. Acts as a placeholder.

**Syntax:**
```
if condition:
    pass  # TODO: implement later
```

**Use Cases:**
- Empty function/class definitions during development
- Syntactically required code blocks
- Placeholder for future implementation

### 4. ELSE with Loops

The else block executes when the loop completes normally (not interrupted by break).

**Syntax:**
```
for/while loop:
    if condition:
        break
else:
    # Executes only if loop wasn't broken
    statement(s)
```

**Use Cases:**
- Search operations (found vs. not found)
- Validation checks
- Prime number testing

---

## Comparison Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal | `a >= b` |
| `<=` | Less than or equal | `a <= b` |

---

## Logical Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | Both conditions must be True | `a > 5 and b < 10` |
| `or` | At least one condition must be True | `a > 5 or b < 10` |
| `not` | Negates the condition | `not (a > 5)` |

**Short-Circuit Evaluation:**
- `and`: If first is False, second isn't evaluated
- `or`: If first is True, second isn't evaluated

---

## Membership Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `in` | Element exists in sequence | `'a' in 'apple'` |
| `not in` | Element doesn't exist | `'z' not in 'apple'` |

---

## Truthy and Falsy Values

**Falsy Values (evaluate to False):**
- `False`
- `None`
- `0`, `0.0`, `0j`
- Empty sequences: `''`, `[]`, `()`, `{}`
- Empty sets and dictionaries

**Truthy Values:**
- Everything else evaluates to True
- Non-zero numbers
- Non-empty sequences/collections

---

## Best Practices

### 1. Indentation
- Use 4 spaces (not tabs)
- Consistent indentation is crucial
- Incorrect indentation causes `IndentationError`

### 2. Condition Simplification
```python
# Bad
if condition == True:

# Good
if condition:
```

### 3. Avoid Deep Nesting
```python
# Bad - too many nested levels
if a:
    if b:
        if c:
            if d:
                do_something()

# Good - use elif or return early
if not a:
    return
if not b:
    return
if not c:
    return
if d:
    do_something()
```

### 4. Use Appropriate Loop Type
- **FOR**: When iterations are known or iterating sequences
- **WHILE**: When iterations depend on a condition

### 5. Meaningful Variable Names
```python
# Bad
for i in students:
    print(i)

# Good
for student in students:
    print(student)
```

### 6. Avoid Modifying List While Iterating
```python
# Bad
for item in my_list:
    my_list.remove(item)

# Good
my_list = [item for item in my_list if condition]
```

### 7. Use List Comprehensions
```python
# Instead of:
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x**2)

# Use:
result = [x**2 for x in range(10) if x % 2 == 0]
```

### 8. Infinite Loop Prevention
Always ensure loop conditions will eventually become False:
```python
# Bad - infinite loop
while True:
    print("Forever")

# Good
count = 0
while count < 10:
    print(count)
    count += 1
```

### 9. Use `enumerate()` Instead of Manual Indexing
```python
# Bad
for i in range(len(items)):
    print(i, items[i])

# Good
for i, item in enumerate(items):
    print(i, item)
```

### 10. DRY Principle (Don't Repeat Yourself)
Extract repeated conditions or code into functions or variables.

---

## Common Patterns

### Pattern 1: Input Validation
```python
while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        break
    print("Invalid input!")
```

### Pattern 2: Search and Exit
```python
for item in collection:
    if item == target:
        print("Found!")
        break
else:
    print("Not found!")
```

### Pattern 3: Menu-Driven Program
```python
while True:
    print("1. Option A")
    print("2. Option B")
    print("3. Exit")
    choice = input("Choose: ")
    
    if choice == '1':
        # Do A
        pass
    elif choice == '2':
        # Do B
        pass
    elif choice == '3':
        break
    else:
        print("Invalid choice")
```

### Pattern 4: Nested Loop with Flag
```python
found = False
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == target:
            found = True
            break
    if found:
        break
```

---

## Summary

**Control Statements** are fundamental to programming, allowing you to:
- Make decisions with **if/elif/else**
- Repeat tasks with **for/while loops**
- Control flow with **break/continue/pass**
- Handle multiple conditions efficiently

Mastering these concepts is essential for writing efficient, readable, and maintainable Python code.

---

## Practice Exercises

1. Write a program to check if a year is a leap year
2. Print all prime numbers between 1 and 100
3. Create a multiplication table for numbers 1-10
4. Implement a simple calculator using if-elif-else
5. Generate the Fibonacci sequence up to n terms
6. Check if a string is a palindrome
7. Find the largest element in a list without using max()
8. Count vowels and consonants in a string
9. Print various patterns (triangles, diamonds, etc.)
10. Implement a number guessing game

---

**Remember:** Practice is key to mastering control statements. Try modifying the examples and creating your own programs!