# Recursion in Python

# 1. Factorial
# The factorial of a non-negative integer n, denoted by n!,
# is the product of all positive integers less than or equal to n.
# Example: 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    """Calculates the factorial of a number using recursion."""
    # Base case: factorial of 0 is 1
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0:
        return 1
    # Recursive step
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5 is: {factorial(5)}")
print(f"Factorial of 0 is: {factorial(0)}")
print(f"Factorial of -3 is: {factorial(-3)}")
print("-" * 20)


# 2. Fibonacci Sequence with Memoization
# A sequence where each number is the sum of the two preceding ones, starting from 0 and 1.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# This version uses memoization to avoid re-calculating the same values.

memo_fib = {}
def fibonacci_memo(n):
    """Calculates the nth fibonacci number using recursion with memoization."""
    if n <= 0:
        return "Input should be a positive integer"
    if n in memo_fib:
        return memo_fib[n]
    # Base cases
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # Recursive step
    else:
        result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
        memo_fib[n] = result
        return result

print(f"10th Fibonacci number is: {fibonacci_memo(10)}")
print(f"30th Fibonacci number is: {fibonacci_memo(30)}")
print("-" * 20)


# 3. Sum of list elements

def sum_list(items):
    """Calculates the sum of elements in a list using recursion."""
    # Base case
    if not items:
        return 0
    # Recursive step
    else:
        return items[0] + sum_list(items[1:])

my_list = [1, 5, 4, 2, 8]
print(f"Sum of {my_list} is: {sum_list(my_list)}")
print("-" * 20)


# 4. Reversing a string

def reverse_string(s):
    """Reverses a string using recursion."""
    # Base case
    if len(s) == 0:
        return s
    # Recursive step
    else:
        return reverse_string(s[1:]) + s[0]

my_string = "hello"
print(f"Reverse of '{my_string}' is: '{reverse_string(my_string)}'")
print("-" * 20)


# 5. Tower of Hanoi

def tower_of_hanoi(n, source, aux, dest):
    """Solves the Tower of Hanoi puzzle."""
    if n > 0:
        # Move n-1 disks from source to auxiliary rod
        tower_of_hanoi(n - 1, source, dest, aux)
        # Move the nth disk from source to destination rod
        print(f"Move disk {n} from {source} to {dest}")
        # Move the n-1 disks from auxiliary to destination rod
        tower_of_hanoi(n - 1, aux, source, dest)

print("Tower of Hanoi with 3 disks:")
tower_of_hanoi(3, 'A', 'B', 'C')
print("-" * 20)


# 6. Merge Sort

def merge_sort(arr):
    """Sorts an array using the merge sort algorithm."""
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

unsorted_list = [12, 11, 13, 5, 6, 7]
print(f"Unsorted list: {unsorted_list}")
sorted_list = merge_sort(unsorted_list.copy()) # use copy to keep original
print(f"Sorted list: {sorted_list}")
print("-" * 20)


# 7. Binary Tree Traversal

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(root):
    """Performs in-order traversal of a binary tree."""
    res = []
    if root:
        res = inorder_traversal(root.left)
        res.append(root.val)
        res = res + inorder_traversal(root.right)
    return res

def preorder_traversal(root):
    """Performs pre-order traversal of a binary tree."""
    res = []
    if root:
        res.append(root.val)
        res = res + preorder_traversal(root.left)
        res = res + preorder_traversal(root.right)
    return res

def postorder_traversal(root):
    """Performs post-order traversal of a binary tree."""
    res = []
    if root:
        res = postorder_traversal(root.left)
        res = res + postorder_traversal(root.right)
        res.append(root.val)
    return res

# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Binary Tree Traversals:")
print(f"In-order: {inorder_traversal(root)}")
print(f"Pre-order: {preorder_traversal(root)}")
print(f"Post-order: {postorder_traversal(root)}")
print("-" * 20)

# 8. Recursive Binary Search

def binary_search_recursive(arr, low, high, target):
    """
    Performs a binary search for a target value in a sorted array using recursion.
    Returns the index of the target, or -1 if not found.
    """
    if low <= high:
        mid = (low + high) // 2
        
        # If element is present at the middle itself
        if arr[mid] == target:
            return mid
        
        # If element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > target:
            return binary_search_recursive(arr, low, mid - 1, target)
        
        # Else the element can only be present in right subarray
        else:
            return binary_search_recursive(arr, mid + 1, high, target)
    else:
        # Element is not present in the array
        return -1

# Test array for binary search must be sorted
test_list = [2, 3, 4, 10, 40]
target_val = 10
print(f"Binary Search Test:")
print(f"Array: {test_list}")
# Function call
result = binary_search_recursive(test_list, 0, len(test_list)-1, target_val)

if result != -1:
    print(f"Element {target_val} is present at index {result}")
else:
    print(f"Element {target_val} is not present in array")

target_val = 99
result = binary_search_recursive(test_list, 0, len(test_list)-1, target_val)
if result != -1:
    print(f"Element {target_val} is present at index {result}")
else:
    print(f"Element {target_val} is not present in array")

print("-" * 20)