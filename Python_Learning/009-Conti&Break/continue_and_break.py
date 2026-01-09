("""Conti&Br examples

Runnable examples demonstrating `break`, `continue`, nested loops, `for-else`, and a short note about `match` as a switch-like alternative.
""")

def demo_break_simple():
	items = [2, 4, 7, 8, 11]
	target = 7
	for i in items:
		if i == target:
			print(f"Found {target} — breaking")
			break
		print(f"Checked {i}")
	else:
		# runs only if loop didn't hit break
		print(f"{target} not found")


def demo_continue_simple():
	values = [1, -1, 2, -5, 3]
	print("Positive values:")
	for v in values:
		if v < 0:
			# skip negatives
			continue
		print(v)


def demo_nested_break():
	matrix = [[1, 2], [3, 4], [5, 6]]
	target = 4
	found = False
	for r_idx, row in enumerate(matrix):
		for c_idx, val in enumerate(row):
			if val == target:
				print(f"Found {target} at {r_idx},{c_idx}")
				found = True
				break
		if found:
			# break outer loop too
			break


def demo_while_continue():
	i = 0
	while i < 6:
		i += 1
		if i % 2 == 0:
			# skip even numbers
			continue
		print(f"Odd: {i}")


def demo_match_switch_like(x):
	# Requires Python 3.10+ for `match`; if unavailable, use if/elif or dict dispatch.
	try:
		match x:
			case 0:
				return "zero"
			case 1 | 2:
				return "one or two"
			case _:
				return "other"
	except Exception:
		# fallback for older Pythons
		if x == 0:
			return "zero"
		if x in (1, 2):
			return "one or two"
		return "other"


def main():
	print("--- demo_break_simple ---")
	demo_break_simple()
	print("--- demo_continue_simple ---")
	demo_continue_simple()
	print("--- demo_nested_break ---")
	demo_nested_break()
	print("--- demo_while_continue ---")
	demo_while_continue()
	print("--- demo_match_switch_like ---")
	for x in [0, 1, 3]:
		print(x, "->", demo_match_switch_like(x))


if __name__ == "__main__":
	main()

