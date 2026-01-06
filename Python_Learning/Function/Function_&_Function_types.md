# Functions in Python

A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

## Defining a Function

You can define functions to provide the required functionality. Here are simple rules to define a function in Python.

-   Function blocks begin with the keyword `def` followed by the function name and parentheses `()`.
-   Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
-   The first statement of a function can be an optional statement - the documentation string of the function or docstring.
-   The code block within every function starts with a colon (`:`) and is indented.
-   The statement `return [expression]` exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as `return None`.

### Syntax

```python
def function_name(parameters):
   """docstring"""
   statement(s)
   return [expression]
```

## Calling a Function

Defining a function only gives it a name, specifies the parameters that are to be included in the function and structures the blocks of code.

Once the basic structure of a function is finalized, you can execute it by calling it from another function or directly from the Python prompt.

## Function Arguments

You can call a function by using the following types of formal arguments:

-   Required arguments
-   Keyword arguments
-   Default arguments
-   Variable-length arguments

### Required arguments

Required arguments are the arguments passed to a function in correct positional order. Here, the number of arguments in the function call should match exactly with the function definition.

### Keyword arguments

Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name.

### Default arguments

A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.

### Variable-length arguments

You may need to process a function for more arguments than you specified while defining the function. These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.

#### `*args` (Non-Keyword Arguments)

The special syntax `*args` in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-key worded, variable-length argument list.

#### `**kwargs` (Keyword Arguments)

The special syntax `**kwargs` in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name `kwargs` with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).

## The `return` Statement

The statement `return [expression]` exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as `return None`.

## Anonymous Functions (Lambda Functions)

These functions are called anonymous because they are not declared in the standard manner by using the `def` keyword. You can use the `lambda` keyword to create small anonymous functions.

-   Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.
-   An anonymous function cannot be a direct call to `print` because `lambda` requires an expression.
-   Lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.

### Syntax

```python
lambda [arg1 [,arg2,.....argn]]:expression
```

## Types of Functions

There are two types of functions:
1.  **Built-in functions:** These are the functions that are built into Python.
2.  **User-defined functions:** These are the functions that are defined by the user.

### Built-in functions

Some examples of built-in functions are: `print()`, `len()`, `type()`, `int()`, `float()`, `str()`, `list()`, `tuple()`, `dict()`, `set()`, etc.

### User-defined functions

The functions which we define ourselves to do certain specific task are referred as user-defined functions.

---

## Advanced Function Concepts

### Scope and Lifetime of Variables (LEGB Rule)

The scope of a variable is the part of the program where the variable is recognized. Python uses the LEGB rule to decide the order in which the namespaces are to be searched to execute a statement.

-   **L (Local):** Variables defined inside a function.
-   **E (Enclosing):** Variables in the local scope of enclosing functions (for nested functions).
-   **G (Global):** Variables defined at the top level of a module.
-   **B (Built-in):** Names pre-assigned in Python.

### Closures

A closure is a function object that remembers values in enclosing scopes even if they are not present in memory. It is a record that stores a function together with an environment.

### Decorators

Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behavior of a function or class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.

### Generators

A generator is a special type of function which does not return a single value, instead, it returns an iterator object with a sequence of values. In a generator function, a `yield` statement is used rather than a `return` statement.

### Type Hinting

Python is a dynamically typed language, which means we don't have to declare the type of a variable. But from Python 3.5, we can provide type hints. Type hints are a special syntax that allow declaring the type of a variable.

### Recursion

Recursion is the process of defining something in terms of itself. In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.
