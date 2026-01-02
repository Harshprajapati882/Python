"""DS.py — compact examples for Python data structures.

Run this file to see example outputs demonstrating common operations.
"""

from collections import deque, defaultdict, Counter, namedtuple
from array import array
import heapq
import bisect
from typing import List, Dict


def list_examples():
	a = [1, 2, 3]
	a.append(4)
	a.insert(0, 0)
	print("list:", a)


def tuple_examples():
	t = (1, 2, 3)
	x, y, z = t
	print("tuple unpack:", x, y, z)


def set_examples():
	s = {1, 2, 2, 3}
	s.add(4)
	print("set unique:", s)


def dict_examples():
	d = {'a': 1, 'b': 2}
	d['c'] = 3
	print("dict items:", list(d.items()))


def deque_and_defaultdict_examples():
	dq = deque([1, 2, 3])
	dq.appendleft(0)
	dq.pop()
	print("deque:", list(dq))

	dd = defaultdict(int)
	dd['x'] += 1
	print("defaultdict:", dict(dd))


def counter_namedtuple_examples():
	words = ["apple", "banana", "apple", "orange"]
	c = Counter(words)
	print("counter most common:", c.most_common())

	Point = namedtuple('Point', ['x', 'y'])
	p = Point(1, 2)
	print("namedtuple:", p.x, p.y)


def heap_and_bisect_examples():
	h = []
	for val in [5, 1, 3]:
		heapq.heappush(h, val)
	print("heap pop order:", [heapq.heappop(h) for _ in range(len(h))])

	sorted_list = [1, 3, 4, 7]
	bisect.insort(sorted_list, 5)
	print("bisect insort:", sorted_list)


def array_example():
	# compact numeric array (homogeneous)
	a = array('i', [1, 2, 3])
	a.append(4)
	print("array:", a.tolist())


def typing_example(data: List[int]) -> Dict[int, int]:
	# count frequencies using plain dict (typing hint example)
	freq: Dict[int, int] = {}
	for v in data:
		freq[v] = freq.get(v, 0) + 1
	return freq


def demo_all():
	print("--- Lists ---")
	list_examples()
	print("--- Tuples ---")
	tuple_examples()
	print("--- Sets ---")
	set_examples()
	print("--- Dicts ---")
	dict_examples()
	print("--- deque/defaultdict ---")
	deque_and_defaultdict_examples()
	print("--- Counter/namedtuple ---")
	counter_namedtuple_examples()
	print("--- heap/bisect ---")
	heap_and_bisect_examples()
	print("--- array ---")
	array_example()
	print("--- typing example ---")
	print(typing_example([1, 2, 2, 3]))


if __name__ == '__main__':
	demo_all()

