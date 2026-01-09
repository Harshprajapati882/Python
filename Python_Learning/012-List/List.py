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

    print('\n--- Accessing list items ---')
    print('a[0] =', a[0])
    print('a[-1] =', a[-1])
    print('b[1:3] =', b[1:3])
    print('c[:2] =', c[:2])
    print('a[1:] =', a[1:])
    print('a[::-1] =', a[::-1])


    print('\n--- Change list items ---')
    a[1] = 20
    print('a after a[1]=20 ->', a)
    a[0:2] = [100, 200, 300]
    print('a after slice assignment ->', a)

    print('\n--- Add list items ---')
    m = [10, 20]
    m.append(30)
    print('append ->', m)
    m.extend([40, 50])
    print('extend ->', m)
    m.insert(1, 15)
    print('insert ->', m)

    print('\n--- Remove list items ---')
    m.remove(20)
    print('remove 20 ->', m)
    popped = m.pop()
    print('pop ->', popped, 'remaining', m)
    del m[0]
    print('del m[0] ->', m)
    m.clear()
    print('clear ->', m)


    print('\n--- Loop lists ---')
    letters = ['a', 'b', 'c']
    print('For loop:')
    for letter in letters:
        print(letter, end=' ')
    print('\nEnumerate:')
    for i, v in enumerate(letters):
        print(f'index {i}, value {v}')


    print('\n--- List comprehensions ---')
    comps = [x * x for x in range(6) if x % 2 == 0]
    print('squares of even 0..5 ->', comps)
    # More complex comprehension
    words = ['hello', 'world', 'python']
    upper_words = [word.upper() for word in words]
    print('Upper case words ->', upper_words)


    print('\n--- Sorting & Reversing ---')
    nums = [5, 1, 4, 3, 2]
    print('Original list:', nums)
    print('sorted(nums) ->', sorted(nums))
    nums.sort(reverse=True)
    print('nums.sort(reverse=True) ->', nums)
    # Sort with a key
    words = ['banana', 'apple', 'cherry']
    words.sort(key=len)
    print('Sorted by length ->', words)


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

    print('\n--- Join lists ---')
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    joined_list = list1 + list2
    print('Joined with + ->', joined_list)
    list1.extend(list2)
    print('Extended list1 ->', list1)


    print('\n--- Other Built-in helpers ---')
    values = [2, 5, 1, 8, 3]
    print('len ->', len(values))
    print('min ->', min(values))
    print('max ->', max(values))
    print('sum ->', sum(values))
    print('any([0, 1, 2]) ->', any([0, 1, 2]))
    print('all([1, 2, 0]) ->', all([1, 2, 0]))

def run_exercises():
    print('\n--- List Exercises ---')

    # 1. Find the largest number
    numbers = [10, 20, 4, 45, 99]
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    print('1. Largest number in', numbers, 'is', largest)

    # 2. Remove duplicates
    my_list = [1, 2, 3, 2, 4, 5, 4]
    unique_list = []
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
    print('2. List with duplicates:', my_list)
    print('   List without duplicates:', unique_list)
    # Alternative using sets
    # unique_list_alt = list(set(my_list))


    # 3. Check if a list is empty
    empty_list = []
    non_empty_list = [1, 2, 3]
    if not empty_list:
        print('3. The list', empty_list, 'is empty.')
    if non_empty_list:
        print('3. The list', non_empty_list, 'is not empty.')

    # 4. Merge two lists and sort it
    list1 = [1, 5, 3]
    list2 = [2, 4, 6]
    merged_list = list1 + list2
    merged_list.sort()
    print('4. Merged and sorted list:', merged_list)

    # 5. Count occurrences
    my_list = [1, 2, 3, 2, 4, 2, 5]
    element_to_count = 2
    count = my_list.count(element_to_count)
    print(f'5. The element {element_to_count} appears {count} times in the list.')


if __name__ == '__main__':
    run_examples()
    run_exercises()

