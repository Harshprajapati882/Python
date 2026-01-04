"""if-else examples and patterns.

Run this file to see short demonstrations of each pattern.
"""
from typing import Any


def simple_if(x: int) -> str:
	if x > 0:
		return "positive"
	# falling through returns None implicitly if no branch


def if_else(x: int) -> str:
	if x % 2 == 0:
		return "even"
	else:
		return "odd"


def if_elif_else(score: int) -> str:
	if score >= 90:
		return "A"
	elif score >= 75:
		return "B"
	elif score >= 60:
		return "C"
	else:
		return "F"


def nested_checks(a: int, b: int) -> str:
	if a > 0:
		if b > 0:
			return "both positive"
		else:
			return "a positive, b non-positive"
	else:
		return "a non-positive"


def ternary_example(a: int, b: int) -> int:
	return a if a >= b else b


def guard_clause_divide(a: float, b: float) -> float:
	if b == 0:
		raise ValueError("division by zero")
	return a / b


def short_circuit(a: Any, b: Any) -> Any:
	# Return a if it's truthy, otherwise b (common python idiom)
	return a or b


def dispatch_example(key: str) -> str:
	# Dictionary dispatch: cleaner than many elifs when mapping values
	def _one():
		return "one"

	def _two():
		return "two"

	dispatch = {
		"1": _one,
		"2": _two,
	}

	func = dispatch.get(key)
	if func:
		return func()
	return "unknown"


def complex_condition(a: int, b: int) -> bool:
	# readability: name parts of the condition
	a_pos = a > 0
	b_pos = b > 0
	return a_pos and b_pos


def main() -> None:
	print("simple_if(3):", simple_if(3))
	print("simple_if(-1):", simple_if(-1))
	print("if_else(4):", if_else(4))
	print("if_else(5):", if_else(5))
	print("if_elif_else(82):", if_elif_else(82))
	print("nested_checks(2,3):", nested_checks(2, 3))
	print("ternary_example(2,5):", ternary_example(2, 5))
	try:
		print("guard_clause_divide(4,2):", guard_clause_divide(4, 2))
	except ValueError as e:
		print("error:", e)
	print("short_circuit('', 'fallback'):", short_circuit('', 'fallback'))
	print("dispatch_example('1'):", dispatch_example('1'))
	print("complex_condition(1,1):", complex_condition(1, 1))


if __name__ == "__main__":
	main()

