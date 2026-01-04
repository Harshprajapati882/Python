"""Basics example: data types, control flow, functions."""

def greet(name: str) -> str:
    return f"Hello, {name}!"


def factorial(n: int) -> int:
    if n < 2:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == '__main__':
    print(greet('World'))
    print('5! =', factorial(5))
    nums = [1, 2, 3, 4]
    squares = [x * x for x in nums]
    print('squares:', squares)
