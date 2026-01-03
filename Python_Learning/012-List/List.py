
def run_examples():
	print('\n--- Creation ---')
	a = [1, 2, 3]
	b = list(range(4))
	c = list('abc')
	empty = []
	print('a =', a)
	print('b =', b)
	print('c =', c)
	print('empty =', empty)

	print('\n--- Indexing & Slicing ---')
	print('a[0] =', a[0])
	print('a[-1] =', a[-1])
	print('b[1:3] =', b[1:3])

	print('\n--- Mutability ---')
	a[1] = 20
	print('a after a[1]=20 ->', a)

	print('\n--- Methods ---')
	m = [10, 20]
	m.append(30)
	print('append ->', m)
	m.extend([40, 50])
	print('extend ->', m)
	m.insert(1, 15)
	print('insert ->', m)
	m.remove(20)
	print('remove 20 ->', m)
	popped = m.pop()
	print('pop ->', popped, 'remaining', m)
	m.clear()
	print('clear ->', m)

	print('\n--- Searching & Counting ---')
	s = [1, 2, 3, 2, 4]
	print('s.index(2) =', s.index(2))
	print('s.count(2) =', s.count(2))
	print('3 in s ->', 3 in s)

	print('\n--- Sorting & Reversing ---')
	nums = [5, 1, 4, 3]
	print('sorted(nums) ->', sorted(nums))
	nums.sort()
	print('nums.sort() ->', nums)
	nums.reverse()
	print('nums.reverse() ->', nums)

	print('\n--- Copying ---')
	orig = [[1, 2], [3, 4]]
	shallow = orig.copy()
	shallow[0].append(99)
	print('orig after shallow modification ->', orig)
	import copy
	deep = copy.deepcopy(orig)
	deep[0].append(100)
	print('orig after deep modification ->', orig)
	print('deep ->', deep)

	print('\n--- Nested lists ---')
	mat = [[1, 2, 3], [4, 5, 6]]
	print('mat[1][2] ->', mat[1][2])
	flat = [x for row in mat for x in row]
	print('flattened ->', flat)

	print('\n--- List comprehensions ---')
	comps = [x * x for x in range(6) if x % 2 == 0]
	print('squares of even 0..5 ->', comps)

	print('\n--- Iteration patterns ---')
	letters = ['a', 'b', 'c']
	for i, v in enumerate(letters):
		print('index', i, 'value', v)
	for x, y in zip([1, 2, 3], ['x', 'y', 'z']):
		print('zipped', x, y)

	print('\n--- Unpacking ---')
	head, *middle, tail = [1, 2, 3, 4, 5]
	print('head, middle, tail ->', head, middle, tail)

	print('\n--- Built-in helpers ---')
	values = [2, 5, 1]
	print('len ->', len(values))
	print('min ->', min(values))
	print('max ->', max(values))
	print('sum ->', sum(values))
	print('any([0, 1, 2]) ->', any([0, 1, 2]))
	print('all([1, 2]) ->', all([1, 2]))

	print('\n--- Conversions ---')
	print("list('spam') ->", list('spam'))
	print('list(range(3)) ->', list(range(3)))


if __name__ == '__main__':
	run_examples()

