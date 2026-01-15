# Python Generators Examples

# 1. Simple Generator Function
def simple_generator():
    """A simple generator function that yields three numbers."""
    print("Starting generator...")
    yield 1
    yield 2
    yield 3
    print("...Generator finished.")

# To use the generator, you first create a generator object
gen_obj = simple_generator()

print("Created generator object.")

# You can iterate over it using a for loop
print("\nIterating with a for loop:")
for value in simple_generator():
    print(value)

# Or by using next()
gen_obj = simple_generator()
print("\nIterating with next():")
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
# The next line would raise a StopIteration exception because the generator is exhausted
# print(next(gen_obj))


# 2. Generator Expression
print("\n--- Generator Expression ---")
# List comprehension
list_comp = [i * i for i in range(5)]
print("List comprehension:", list_comp)

# Generator expression
gen_exp = (i * i for i in range(5))
print("Generator expression object:", gen_exp)
print("Values from generator expression:")
for value in gen_exp:
    print(value)


# 3. yield vs return
def yield_example():
    yield "yielded value"
    return "returned value" # This will be the StopIteration value

print("\n--- yield vs return ---")
y_gen = yield_example()
print(next(y_gen))
try:
    next(y_gen)
except StopIteration as e:
    print(f"StopIteration has value: {e.value}")


# 4. Exception Handling in Generators
def generator_with_exception():
    """A generator that handles exceptions."""
    print("Generator started")
    try:
        yield 10
        # An exception can be thrown into the generator
        yield 20
        yield 30
    except ValueError:
        print("Caught a ValueError inside the generator!")
        yield "Handled error"
    finally:
        print("Generator is closing.")

print("\n--- Exception Handling ---")
gwe = generator_with_exception()
print(f"next(): {next(gwe)}")

# Using throw() to inject an exception into the generator
print("Throwing ValueError into generator...")
print(f"next() after throw: {gwe.throw(ValueError)}")

# Using close() to stop the generator
gwe2 = generator_with_exception()
print(f"\nnext(): {next(gwe2)}")
print("Closing generator...")
gwe2.close()


# 5. send() method
def counter_generator():
    """A generator that can receive values using send()."""
    count = 0
    while True:
        # The 'yield' expression returns the value sent by send()
        received = yield count
        if received is not None:
            print(f"Received: {received}")
            count = received
        else:
            count += 1

print("\n--- send() method ---")
cg = counter_generator()
print(f"next(): {next(cg)}") # Start the generator
print(f"next(): {next(cg)}")
print(f"send(10): {cg.send(10)}") # Send a value
print(f"next(): {next(cg)}")


# 6. Async Generator
import asyncio

async def async_generator():
    """An asynchronous generator."""
    for i in range(3):
        await asyncio.sleep(0.5)
        yield i * i

async def run_async_gen():
    print("\n--- Async Generator ---")
    print("Iterating over async generator:")
    async for value in async_generator():
        print(value)

# Running the async example
if __name__ == "__main__":
    asyncio.run(run_async_gen())
