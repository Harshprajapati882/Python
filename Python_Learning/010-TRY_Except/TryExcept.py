"""TryExcept.py

Small, runnable examples demonstrating Python try/except patterns.
Run from repo root:

    python Python_Learning/010-TRY_Except/TryExcept.py

"""
from contextlib import suppress


def example_division(x):
    """Shows catching a specific exception."""
    try:
        return 10 / x
    except ZeroDivisionError:
        return 'division by zero'


def multiple_except(value):
    """Demonstrates multiple except clauses and exception object access."""
    try:
        if value == 'k':
            raise KeyError('missing key')
        if value == 'v':
            raise ValueError('bad value')
        return 'ok'
    except KeyError as e:
        return f'key error handled: {e}'
    except ValueError as e:
        return f'value error handled: {e}'
    except Exception as e:
        return f'generic handler: {type(e).__name__}: {e}'


def else_and_finally(flag):
    """Shows use of else and finally."""
    try:
        if flag == 'err':
            raise RuntimeError('whoops')
        result = 'worked'
    except RuntimeError as e:
        return ('caught', str(e))
    else:
        # runs only if no exception
        return ('else', result)
    finally:
        # always runs
        pass


def raise_and_reraise():
    """Shows raising and re-raising an exception with context."""
    try:
        try:
            int('not-int')
        except ValueError as e:
            # add context and re-raise
            raise RuntimeError('conversion failed') from e
    except RuntimeError as e:
        return f're-raised: {e.__class__.__name__} caused by {e.__cause__.__class__.__name__}'


class MyError(Exception):
    pass


def custom_exception_demo(x):
    """Shows raising a custom exception for domain-specific logic."""
    if x < 0:
        raise MyError('negative not allowed')
    return x * 2


def suppress_demo(path):
    """Shows contextlib.suppress to ignore a specific exception."""
    with suppress(FileNotFoundError):
        with open(path, 'r') as f:
            return f.read()
    return None


def main():
    print('example_division(2) ->', example_division(2))
    print('example_division(0) ->', example_division(0))

    print("multiple_except('k') ->", multiple_except('k'))
    print("multiple_except('v') ->", multiple_except('v'))
    print("multiple_except('x') ->", multiple_except('x'))

    print("else_and_finally('ok') ->", else_and_finally('ok'))
    print("else_and_finally('err') ->", else_and_finally('err'))

    print('raise_and_reraise() ->', raise_and_reraise())

    try:
        print('custom_exception_demo(-1) ->', custom_exception_demo(-1))
    except MyError as e:
        print('caught custom exception:', e)

    print('suppress_demo(nonexistent) ->', suppress_demo('this_file_does_not_exist.txt'))


if __name__ == '__main__':
    main()
