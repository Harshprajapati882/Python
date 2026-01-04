"""main.py — examples for basic Python syntax: comments, escape sequences, variables and type casting.
"""

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

def type_casting_examples():
	print("\n--- Type Casting ---")
	print("NUMBER CONVERSIONS")
	print("int('123') ->", int('123'))
	print("int(12.9) ->", int(12.9))
	try:
		print("int('12.9') ->", int('12.9'))
	except ValueError as e:
		print("int('12.9') raises:", e)
	print("float('12.9') ->", float('12.9'))
	print("complex(1,2) ->", complex(1,2))
	print("complex('1+2j') ->", complex('1+2j'))

	print("\nBOOL & STR")
	print("bool('') ->", bool(''))
	print("bool('False') ->", bool('False'))
	print("bool(0) ->", bool(0))
	print("bool(1) ->", bool(1))
	print("str(123) ->", str(123))

	print("\nCOLLECTIONS")
	print("list((1,2,3)) ->", list((1,2,3)))
	print("tuple([1,2,3]) ->", tuple([1,2,3]))
	print("set([1,1,2]) ->", set([1,1,2]))
	print("dict([('a',1),('b',2)]) ->", dict([('a',1),('b',2)]))
	try:
		print("dict([1,2,3]) ->", dict([1,2,3]))
	except Exception as e:
		print("dict([1,2,3]) raises:", e)

	print("\nBYTES")
	s = "hello"
	b = s.encode('utf-8')
	print("s.encode('utf-8') ->", b)
	print("bytes('hi','utf-8') ->", bytes('hi','utf-8'))
	ba = bytearray(b)
	print("bytearray(b) ->", ba)

	print("\nEDGE CASES")
	f = 3.999
	print("int(3.999) ->", int(f))
	print("float('nan') ->", float('nan'))
	print("bool([]) ->", bool([]))
	print("bool({})
 ->", bool({}))
	print("None ->", type(None))


def demo_all():
	print('--- Comments ---')
	comments_examples()
	print('\n--- Escape sequences ---')
	escape_sequence_examples()
	print('\n--- Variable types ---')
	variable_types_examples()
	type_casting_examples()


if __name__ == '__main__':
	demo_all()