#!/usr/bin/env python3

def demo_numbers():
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


def demo_bool_str():
	print("\nBOOL & STR")
	print("bool('') ->", bool(''))
	print("bool('False') ->", bool('False'))
	print("bool(0) ->", bool(0))
	print("bool(1) ->", bool(1))
	print("str(123) ->", str(123))


def demo_collections():
	print("\nCOLLECTIONS")
	print("list((1,2,3)) ->", list((1,2,3)))
	print("tuple([1,2,3]) ->", tuple([1,2,3]))
	print("set([1,1,2]) ->", set([1,1,2]))
	print("dict([('a',1),('b',2)]) ->", dict([('a',1),('b',2)]))
	try:
		print("dict([1,2,3]) ->", dict([1,2,3]))
	except Exception as e:
		print("dict([1,2,3]) raises:", e)


def demo_bytes():
	print("\nBYTES")
	s = "hello"
	b = s.encode('utf-8')
	print("s.encode('utf-8') ->", b)
	print("bytes('hi','utf-8') ->", bytes('hi','utf-8'))
	ba = bytearray(b)
	print("bytearray(b) ->", ba)


def demo_edge_cases():
	print("\nEDGE CASES")
	f = 3.999
	print("int(3.999) ->", int(f))
	print("float('nan') ->", float('nan'))
	print("bool([]) ->", bool([]))
	print("bool({}) ->", bool({}))
	print("None ->", type(None))


if __name__ == "__main__":
	demo_numbers()
	demo_bool_str()
	demo_collections()
	demo_bytes()
	demo_edge_cases()

