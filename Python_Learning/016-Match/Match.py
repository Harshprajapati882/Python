"""Examples for structural pattern matching (Python 3.10+).

Run with: python3 Match.py
"""

from dataclasses import dataclass


def literal_examples(value):
	match value:
		case 0:
			return "zero"
		case 1:
			return "one"
		case _:
			return "other"


def sequence_examples(point):
	match point:
		case (0, y):
			return f"On y-axis at {y}"
		case (x, y):
			return f"Point at x={x}, y={y}"
		case _:
			return "Not a point"


def list_rest_example(seq):
	match seq:
		case [first, *rest]:
			return (first, rest)
		case []:
			return None


def mapping_example(data):
	match data:
		case {"type": "point", "x": x, "y": y}:
			return f"Point {x},{y}"
		case {"type": "person", "name": name}:
			return f"Person: {name}"
		case _:
			return "Unknown"


@dataclass
class P:
	x: int
	y: int


def class_pattern_example(obj):
	match obj:
		case P(0, y):
			return f"P on y-axis {y}"
		case P(x, y):
			return f"P at {x},{y}"
		case _:
			return "Not a P"


def guard_or_examples(value):
	match value:
		case x if x > 0:
			return "positive"
		case 0 | 1:
			return "zero-or-one"
		case _:
			return "other"


def nested_example(data):
	match data:
		case {"user": {"id": uid, "roles": [first, *rest]}}:
			return (uid, first, rest)
		case _:
			return None


if __name__ == "__main__":
	print("literal_examples(0)", literal_examples(0))
	print("literal_examples(5)", literal_examples(5))

	print("sequence_examples((0,3))", sequence_examples((0, 3)))
	print("sequence_examples((2,4))", sequence_examples((2, 4)))

	print("list_rest_example([1,2,3])", list_rest_example([1, 2, 3]))
	print("mapping_example({'type':'point','x':1,'y':2})", mapping_example({"type": "point", "x": 1, "y": 2}))

	p = P(5, 6)
	print("class_pattern_example(P(5,6))", class_pattern_example(p))

	print("guard_or_examples(10)", guard_or_examples(10))
	print("guard_or_examples(1)", guard_or_examples(1))

	nested = {"user": {"id": 42, "roles": ["admin", "user"]}}
	print("nested_example", nested_example(nested))
