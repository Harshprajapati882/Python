# Python Closures

A closure is a function object that remembers values in the enclosing scope even if they are not present in memory. It is a record that stores a function together with an environment.

## Key Concepts

### 1. Nested Functions
A function defined inside another function is called a nested function. Nested functions can access variables of the enclosing scope.

### 2. Accessing Enclosing Scope
The nested function can access variables from its enclosing (non-global) scope. This is what makes closures possible.

### 3. Retention of State
This is the most important feature of closures. The inner function remembers the state of its environment when it was created. Even after the outer function has finished executing, the inner function (the closure) retains access to the outer function's variables.

### 4. Variable Scope (LEGB Rule)
Python's scope resolution follows the LEGB rule:
- **L**ocal: Variables defined within the function.
- **E**nclosing: Variables in the scope of any enclosing functions (e.g., in nested functions).
- **G**lobal: Variables defined at the top level of a module.
- **B**uilt-in: Names that are pre-assigned in Python (e.g., `print`, `len`).

### 5. Creating a Closure
To create a closure, you must have:
1.  A nested function.
2.  The nested function must refer to a value defined in the enclosing function.
3.  The enclosing function must return the nested function.

### 6. The `nonlocal` Keyword
The `nonlocal` keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function. It is used to declare that a variable is not local to the current function but is in the enclosing scope. This allows you to modify the variable's value.
