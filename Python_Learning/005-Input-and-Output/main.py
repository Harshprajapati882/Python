"""main.py — examples for basic Python input and output.
"""

def print_examples():
	print('a', 'b', 'c', sep=' - ', end='\n')
	x = 42
	print(f'formatted (f-string): x = {x}')
	print('no newline ', end='')
	print('continued')


def safe_input(prompt: str, default: str = '') -> str:
	"""Try to read input, but return default if running non-interactively."""
	try:
		return input(prompt)
	except EOFError:
		return default

def input_examples():
	# Use defaults so the script can run in automated environments
	name = safe_input('Enter your name: ', default='Alice')
	age_str = safe_input('Enter your age: ', default='30')
	try:
		age = int(age_str)
	except ValueError:
		age = None
	print('Hello', name, '- age parsed as', age)

def demo_all():
	print('\n--- Print examples ---')
	print_examples()
	print('\n--- Input examples ---')
	input_examples()


if __name__ == '__main__':
	demo_all()
