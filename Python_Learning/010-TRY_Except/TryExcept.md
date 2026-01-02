This file explains Python's try/except mechanisms, uses, patterns, and includes links to runnable examples in TryExcept.py.

**Overview**

- **What:** `try`/`except` is Python's mechanism for catching and handling exceptions (runtime errors).
- **Why:** Prevents a program from crashing, allows recovery, cleanup, and clearer error reporting.
- **When to use:** When you call code that may fail for reasons outside your control (I/O, network, user input, parsing), or when you want to surface friendly messages and ensure cleanup.

**Basic Syntax**

```python
try:
    # risky operation
    result = 10 / x
except ZeroDivisionError:
    # handle specific exception
    result = None
except Exception as e:
    # fallback for any other exception
    handle(e)
else:
    # runs if try block raised no exceptions
    post_process(result)
finally:
    # always runs (cleanup)
    resource.close()
```

**Key Concepts**

- **Catch specific exceptions first:** Always catch the most specific exceptions you expect. Avoid broad `except:` unless you re-raise or log.
- **Use `else`:** Put code that should run only when no exception occurred in `else` (keeps `try` small).
- **Use `finally`:** Cleanup actions (closing files, releasing locks) belong in `finally` because it runs regardless of errors.
- **Re-raise when appropriate:** If you cannot handle an exception meaningfully, re-raise it so callers can handle it.
- **Create custom exceptions:** For domain-specific errors, subclass `Exception`.

**Patterns & Best Practices**

- Keep `try` blocks small: only wrap the statements that can raise the exception you intend to handle.
- Log exceptions with context (use `logging.exception()` inside an `except` block) instead of silently swallowing them.
- Avoid using exceptions for control flow in hot loops; they are for exceptional conditions.
- Prefer catching explicit exception classes rather than a bare `except:`.

**When Not To Use**

- Don’t wrap large sections of code in a single `try` just to avoid program termination — this hides bugs and makes debugging harder.
- Avoid catching `Exception` everywhere; this can mask unexpected issues.

**Convenience helpers**

- `contextlib.suppress(ExceptionType)` can be useful when you want to ignore specific exceptions for short blocks.

**Examples and runnable demos:** See the example file at [Python_Learning/010-TRY_Except/TryExcept.py](Python_Learning/010-TRY_Except/TryExcept.py).

**Run instructions**

From the repository root run:

```bash
python Python_Learning/010-TRY_Except/TryExcept.py
```

This will execute small demos showing different `try`/`except` patterns and their outputs.
