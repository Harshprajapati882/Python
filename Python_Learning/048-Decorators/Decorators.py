"""
PYTHON DECORATORS - Function Decorators with Practical Examples
================================================================
A decorator is a function that modifies or enhances another function or class
without permanently changing its source code.
"""

from functools import wraps
import time
from datetime import datetime

print("=" * 70)
print("PYTHON DECORATORS - FUNCTION DECORATORS")
print("=" * 70)

# =============================================================================
# TOPIC 1: BASIC FUNCTION DECORATOR
# =============================================================================
print("\n" + "=" * 70)
print("TOPIC 1: BASIC FUNCTION DECORATOR")
print("=" * 70)

def simple_decorator(func):
    """
    A simple decorator that adds functionality before and after function call.
    
    Args:
        func: The function to be decorated
    
    Returns:
        wrapper: The wrapped function
    """
    def wrapper():
        print("✓ [DECORATOR] Before function execution")
        func()  # Call the original function
        print("✓ [DECORATOR] After function execution")
    
    return wrapper

# Using the decorator with @ syntax
@simple_decorator
def say_hello():
    print("  → Hello, World!")

print("\nExample 1: Simple Decorator")
say_hello()

# Same thing without @ syntax (for understanding)
def say_goodbye():
    print("  → Goodbye!")

say_goodbye = simple_decorator(say_goodbye)
print("\nExample 2: Decorator without @ syntax")
say_goodbye()

# =============================================================================
# TOPIC 2: DECORATORS WITH ARGUMENTS
# =============================================================================
print("\n" + "=" * 70)
print("TOPIC 2: DECORATORS WITH ARGUMENTS (*args, **kwargs)")
print("=" * 70)

def argument_decorator(func):
    """
    Decorator that works with functions having arguments.
    Uses *args and **kwargs to handle any function signature.
    """
    def wrapper(*args, **kwargs):
        print(f"✓ [DECORATOR] Function called with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"✓ [DECORATOR] Function returned: {result}")
        return result
    
    return wrapper

@argument_decorator
def add(a, b):
    """Add two numbers."""
    return a + b

@argument_decorator
def greet(name, greeting="Hello"):
    """Greet a person."""
    return f"{greeting}, {name}!"

print("\nExample 3: Decorator with positional arguments")
result1 = add(5, 3)

print("\nExample 4: Decorator with keyword arguments")
result2 = greet("Alice", greeting="Hi")

# =============================================================================
# TOPIC 3: PRESERVING FUNCTION METADATA WITH @wraps
# =============================================================================
print("\n" + "=" * 70)
print("TOPIC 3: PRESERVING FUNCTION METADATA WITH @wraps")
print("=" * 70)

# WITHOUT @wraps - Function metadata is lost
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        """This is the wrapper function."""
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def calculate(x, y):
    """Calculate sum of two numbers."""
    return x + y

print("\nExample 5: WITHOUT @wraps (metadata lost)")
print(f"Function name: {calculate.__name__}")  # Shows 'wrapper' instead of 'calculate'
print(f"Function doc: {calculate.__doc__}")    # Shows wrapper's doc, not calculate's doc

# WITH @wraps - Function metadata is preserved
def good_decorator(func):
    @wraps(func)  # Preserves metadata
    def wrapper(*args, **kwargs):
        """This is the wrapper function."""
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def multiply(x, y):
    """Multiply two numbers."""
    return x * y

print("\nExample 6: WITH @wraps (metadata preserved)")
print(f"Function name: {multiply.__name__}")  # Shows 'multiply'
print(f"Function doc: {multiply.__doc__}")    # Shows correct doc

# =============================================================================
# TOPIC 4: LOGGING DECORATOR
# =============================================================================
print("\n" + "=" * 70)
print("TOPIC 4: PRACTICAL EXAMPLE - LOGGING DECORATOR")
print("=" * 70)

def log_decorator(func):
    """Decorator that logs function calls with timestamp."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Calling function: {func.__name__}")
        print(f"              Arguments: args={args}, kwargs={kwargs}")
        
        try:
            result = func(*args, **kwargs)
            print(f"              Result: {result}")
            return result
        except Exception as e:
            print(f"              Error: {e}")
            raise
    
    return wrapper

@log_decorator
def divide(a, b):
    """Divide two numbers."""
    return a / b

print("\nExample 7: Logging Decorator in Action")
result = divide(10, 2)
try:
    divide(10, 0)
except ZeroDivisionError:
    print("              Exception was caught and logged!")

# =============================================================================
# TOPIC 5: TIMING/PERFORMANCE DECORATOR
# =============================================================================
print("\n" + "=" * 70)
print("TOPIC 5: PRACTICAL EXAMPLE - TIMING DECORATOR")
print("=" * 70)

def timing_decorator(func):
    """Decorator that measures function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"⏱ Function '{func.__name__}' took {execution_time:.6f} seconds")
        return result
    
    return wrapper

@timing_decorator
def slow_function():
    """Simulate a slow function."""
    time.sleep(0.5)
    return "Done!"

@timing_decorator
def fast_function():
    """Simulate a fast function."""
    return sum(range(1000))

print("\nExample 8: Timing Decorator")
slow_function()
fast_function()

# =============================================================================
# TOPIC 6: DECORATORS WITH PARAMETERS
# =============================================================================
print("\n" + "=" * 70)
print("TOPIC 6: DECORATORS WITH PARAMETERS")
print("=" * 70)

def repeat_decorator(times):
    """
    Decorator that repeats function execution N times.
    This decorator accepts a parameter!
    
    Args:
        times: Number of times to repeat
    
    Returns:
        decorator_wrapper: The actual decorator
    """
    def decorator_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                print(f"  Iteration {i + 1}/{times}")
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator_wrapper

@repeat_decorator(times=3)
def say_hi(name):
    """Say hi to someone."""
    return f"Hi, {name}!"

print("\nExample 9: Decorator with Parameters")
results = say_hi("Bob")
print(f"All results: {results}")

# Another example with customizable repetition
def retry_decorator(max_attempts=3, delay=0.5):
    """
    Decorator that retries function execution on failure.
    
    Args:
        max_attempts: Maximum number of attempts
        delay: Delay between retries in seconds
    """
    def decorator_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        print(f"  ✗ Failed after {max_attempts} attempts")
                        raise
                    print(f"  ⚠ Attempt {attempts} failed, retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator_wrapper

@retry_decorator(max_attempts=3, delay=0.1)
def unstable_operation():
    """Simulate an operation that might fail."""
    import random
    if random.random() < 0.3:
        raise ConnectionError("Operation failed!")
    return "Success!"

print("\nExample 10: Retry Decorator with Parameters")
try:
    result = unstable_operation()
    print(f"  ✓ {result}")
except Exception:
    pass

# =============================================================================
# TOPIC 7: CHAINING DECORATORS
# =============================================================================
print("\n" + "=" * 70)
print("TOPIC 7: CHAINING DECORATORS (Multiple Decorators)")
print("=" * 70)

def uppercase_decorator(func):
    """Decorator that converts output to uppercase."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("  [UPPERCASE] Converting to uppercase")
        return result.upper() if isinstance(result, str) else result
    return wrapper

def exclamation_decorator(func):
    """Decorator that adds exclamation marks."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("  [EXCLAMATION] Adding exclamation marks")
        return result + "!!!" if isinstance(result, str) else result
    return wrapper

# Chaining decorators - decorators are applied bottom to top
@exclamation_decorator  # Applied second (outer)
@uppercase_decorator     # Applied first (inner)
def make_message(text):
    """Create a message."""
    return text

print("\nExample 11: Chaining Decorators")
print("Order: @exclamation_decorator (outer) → @uppercase_decorator (inner)")
message = make_message("hello world")
print(f"Final result: {message}")

# Different order
@uppercase_decorator     # Applied second (outer)
@exclamation_decorator   # Applied first (inner)
def make_message2(text):
    """Create a message."""
    return text

print("\nExample 12: Decorators in Different Order")
print("Order: @uppercase_decorator (outer) → @exclamation_decorator (inner)")
message2 = make_message2("hello world")
print(f"Final result: {message2}")

# =============================================================================
# TOPIC 8: VALIDATION DECORATOR
# =============================================================================
print("\n" + "=" * 70)
print("TOPIC 8: PRACTICAL EXAMPLE - VALIDATION DECORATOR")
print("=" * 70)

def validate_positive(func):
    """Decorator that validates function arguments are positive numbers."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Check positional arguments
        for i, arg in enumerate(args):
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument {i} must be positive, got {arg}")
        
        # Check keyword arguments
        for key, val in kwargs.items():
            if isinstance(val, (int, float)) and val < 0:
                raise ValueError(f"Argument '{key}' must be positive, got {val}")
        
        return func(*args, **kwargs)
    
    return wrapper

@validate_positive
def calculate_area(length, width):
    """Calculate area of rectangle."""
    return length * width

print("\nExample 13: Validation Decorator")
print("Valid input:")
area = calculate_area(5, 3)
print(f"  Area: {area}")

print("\nInvalid input:")
try:
    calculate_area(-5, 3)
except ValueError as e:
    print(f"  ✓ Error caught: {e}")

# =============================================================================
# TOPIC 9: CACHING/MEMOIZATION DECORATOR
# =============================================================================
print("\n" + "=" * 70)
print("TOPIC 9: PRACTICAL EXAMPLE - CACHING DECORATOR")
print("=" * 70)

def simple_cache(func):
    """Decorator that caches function results."""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"  [CACHE HIT] Returning cached result for {args}")
            return cache[args]
        
        print(f"  [CACHE MISS] Computing result for {args}")
        result = func(*args)
        cache[args] = result
        return result
    
    return wrapper

@simple_cache
def fibonacci(n):
    """Calculate fibonacci number (expensive computation)."""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\nExample 14: Caching/Memoization Decorator")
print("First call (computes):")
fib = fibonacci(5)
print(f"  fibonacci(5) = {fib}")

print("\nSecond call (from cache):")
fib = fibonacci(5)
print(f"  fibonacci(5) = {fib}")

# =============================================================================
# TOPIC 10: PERMISSION/AUTHORIZATION DECORATOR
# =============================================================================
print("\n" + "=" * 70)
print("TOPIC 10: PRACTICAL EXAMPLE - AUTHORIZATION DECORATOR")
print("=" * 70)

# Simulated current user
current_user = {"name": "Alice", "role": "admin"}

def require_role(required_role):
    """Decorator that checks if user has required role."""
    def decorator_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.get("role") != required_role:
                print(f"  ✗ Access Denied! User role is '{current_user.get('role')}', "
                      f"but '{required_role}' is required")
                raise PermissionError(f"Requires {required_role} role")
            
            print(f"  ✓ Access Granted for user: {current_user['name']}")
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator_wrapper

@require_role("admin")
def delete_user(user_id):
    """Delete a user (requires admin role)."""
    return f"User {user_id} deleted successfully"

@require_role("user")
def view_profile():
    """View profile (requires user role)."""
    return "Profile displayed"

print("\nExample 15: Authorization Decorator")
print(f"Current user: {current_user}")

print("\nCalling admin-only function:")
try:
    result = delete_user(123)
    print(f"  Result: {result}")
except PermissionError:
    pass

print("\nCalling user-only function:")
try:
    result = view_profile()
    print(f"  Result: {result}")
except PermissionError:
    pass

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 70)
print("SUMMARY OF DECORATORS")
print("=" * 70)

summary = """
✓ WHAT IS A DECORATOR?
  - A function that modifies or enhances another function
  - Doesn't change the original function's source code
  - Returns a modified/wrapped version of the function

✓ KEY CONCEPTS
  - First-class functions: Functions can be assigned to variables
  - Higher-order functions: Functions that take/return functions
  - Closures: Functions with access to outer scope variables

✓ BASIC SYNTAX
  @decorator_name
  def function():
      pass

✓ IMPORTANT PATTERNS
  1. Simple decorator (no parameters)
  2. Decorator with *args, **kwargs
  3. Decorator with parameters (extra nesting level)
  4. Using @wraps to preserve metadata

✓ PRACTICAL USES
  - Logging, Timing, Caching, Validation
  - Authorization, Error Handling, Retries
  - Rate Limiting, Memoization, Debugging

✓ BEST PRACTICES
  1. Always use @wraps from functools
  2. Use *args, **kwargs for flexibility
  3. Document your decorators
  4. Keep decorator logic simple and focused
  5. Remember: decorators are applied bottom-to-top when chained
"""

print(summary)
print("=" * 70)
