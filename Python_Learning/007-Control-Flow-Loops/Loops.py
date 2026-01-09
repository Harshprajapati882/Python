("""Loops examples for learning.

Run this file to see concise demonstrations of Python loop types and behaviors.
""")

def for_over_list():
	items = ['apple', 'banana', 'cherry']
	print('\nfor_over_list:')
	for it in items:
		print('-', it)


def for_with_range():
	print('\nfor_with_range:')
	for i in range(5):
		print(i, end=' ')
	print()


def for_enumerate_zip_dict():
	print('\nfor_enumerate_zip_dict:')
	colors = ['red', 'green', 'blue']
	for idx, color in enumerate(colors, start=1):
		print(idx, color)

	a = [1, 2, 3]
	b = ['one', 'two', 'three']
	print('zip:')
	for n, w in zip(a, b):
		print(n, '->', w)

	print('dict iteration:')
	d = {'x': 10, 'y': 20}
	for k, v in d.items():
		print(k, v)


def while_loop_demo():
	print('\nwhile_loop_demo:')
	n = 3
	while n > 0:
		print('countdown', n)
		n -= 1


def break_continue_demo():
	print('\nbreak_continue_demo:')
	for i in range(6):
		if i == 3:
			print('skip 3')
			continue
		if i == 5:
			print('stop at 5')
			break
		print('i =', i)


def nested_loops_demo():
	print('\nnested_loops_demo:')
	for i in range(1, 4):
		for j in range(1, 3):
			print(f'({i},{j})', end=' ')
		print()


def loop_else_demo():
	print('\nloop_else_demo:')
	for i in range(3):
		print(i)
	else:
		print('completed for without break')

	for i in range(3):
		if i == 1:
			break
	else:
		print('this will not run because loop broke')


def list_comprehension_demo():
	print('\nlist_comprehension_demo:')
	squares = [x * x for x in range(6)]
	print('squares:', squares)


def iterate_string_demo():
	print('\niterate_string_demo:')
	for ch in 'hello':
		print(ch, end=' ')
	print()


def main():
	for_over_list()
	for_with_range()
	for_enumerate_zip_dict()
	while_loop_demo()
	break_continue_demo()
	nested_loops_demo()
	loop_else_demo()
	list_comprehension_demo()
	iterate_string_demo()


if __name__ == '__main__':
	main()

