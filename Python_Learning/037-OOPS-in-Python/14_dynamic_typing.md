# Dynamic Typing

**Typing** in programming refers to how a language handles the data types of variables. There are two main approaches: static typing and dynamic typing.

**Python is a dynamically typed language.**

## Static Typing

In a statically typed language (like Java, C++, or C#), you must explicitly declare the data type of a variable when you create it.

```java
// Java code
String myVar = "Hello"; // myVar must always be a String
int myNum = 10;         // myNum must always be an int
// myVar = 5;           // This would cause a compile-time error!
```

*   **Type checking** is done at **compile-time**.
*   **Pros**: Catches type-related errors early, can lead to better performance, and IDEs can provide better autocompletion and error checking.
*   **Cons**: Can be more verbose and less flexible.

## Dynamic Typing

In a dynamically typed language (like Python, JavaScript, or Ruby), you do not have to declare the data type of a variable. The type is associated with the value the variable holds at runtime, not the variable itself.

This means a single variable can refer to different types of objects (integer, string, list, custom object, etc.) throughout the program's execution.

```python
# Python code
my_variable = "Hello"  # my_variable is a string
print(type(my_variable))

my_variable = 10       # Now it's an integer
print(type(my_variable))

my_variable = [1, 2, 3] # Now it's a list
print(type(my_variable))
```

*   **Type checking** is done at **run-time**.
*   **Pros**: More flexible, faster development, less boilerplate code.
*   **Cons**: Type errors are only caught when the code is executed, which can sometimes be late in the development cycle. It can be harder for IDEs to provide perfect analysis.

## Dynamic Typing vs. Strong Typing

It's important not to confuse dynamic typing with weak typing.

*   **Dynamic vs. Static** is about *when* type checking happens (runtime vs. compile-time).
*   **Strong vs. Weak** is about how strictly the language enforces type rules.

**Python is both dynamically typed and strongly typed.**

"Strongly typed" means that Python will not automatically change the type of an object. For example, you cannot add a string and a number together without explicitly converting one of them.

```python
x = 10
y = "5"
# print(x + y)  # This raises a TypeError!
# Python won't implicitly convert y to an integer or x to a string.

# You must do it explicitly:
print(x + int(y))    # Output: 15
print(str(x) + y)  # Output: "105"
```
In contrast, a weakly typed language like JavaScript *would* implicitly convert the types and return a result (`"105"`).
