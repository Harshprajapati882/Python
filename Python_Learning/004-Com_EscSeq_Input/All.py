"""All.py — examples for comments, escape sequences, print, input, and variable types.

This script is safe to run non-interactively: input examples use defaults when input isn't available.
"""

import sys
from typing import Any


def comments_examples():
	# Single-line comment: this line is ignored by the interpreter
	'''
	Triple-quoted strings can act like multi-line comments or docstrings.
	They are real strings, so normally used for docstrings.
	'''
	print('comments: shown via source, no runtime effect')


def escape_sequence_examples():
	s = "First Line\nSecond Line"
	print('escape newline:')
	print(s)

	path = r"C:\Users\name\docs"  # raw string keeps backslashes
	print('raw path:', path)

	quote = "She said \"hi\""
	print('quotes escaped:', quote)

	print('unicode heart: \u2764')


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


def variable_types_examples():
	i = 10               # int
	f = 3.14             # float
	s = 'text'           # str
	b = True             # bool
	lst = [1, 2, 3]      # list
	tpl = (1, 2)         # tuple
	d = {'k': 'v'}       # dict
	st = {1, 2, 3}       # set
	none_val = None      # NoneType
	by = b'bytes'        # bytes
	comp = 1 + 2j        # complex

	items = [i, f, s, b, lst, tpl, d, st, none_val, by, comp]
	for v in items:
		print(type(v).__name__, ':', v)


def type_conversion_examples():
	print('int(3.9) ->', int(3.9))
	print('float("2.5") ->', float('2.5'))
	print('str(10) ->', str(10))
	print('bool(0) ->', bool(0))
	print('list((1,2)) ->', list((1, 2)))


def demo_all():
	print('--- Comments ---')
	comments_examples()
	print('\n--- Escape sequences ---')
	escape_sequence_examples()
	print('\n--- Print examples ---')
	print_examples()
	print('\n--- Input examples ---')
	input_examples()
	print('\n--- Variable types ---')
	variable_types_examples()
	print('\n--- Type conversions ---')
	type_conversion_examples()


if __name__ == '__main__':
	demo_all()

