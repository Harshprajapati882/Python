def show_types():
    a = 10
    b = 3.5
    c = 1 + 2j
    s = 'hello'
    l = [1, 2, 3]
    d = {'k': 'v'}

    print('Types:')
    print(type(a), type(b), type(c), type(s), type(l), type(d))
    print('Conversions: int(3.5)->', int(b), 'float(10)->', float(a), 'str(10)->', str(a))


def arithmetic_ops():
    x, y = 7, 3
    print('\nArithmetic:')
    print('x + y =', x + y)
    print('x - y =', x - y)
    print('x * y =', x * y)
    print('x / y =', x / y)
    print('x // y =', x // y)
    print('x % y =', x % y)
    print('x ** y =', x ** y)


def assignment_ops():
    print('\nAssignment:')
    n = 5
    print('initial n =', n)
    n += 2
    print('after n += 2 ->', n)
    n *= 3
    print('after n *= 3 ->', n)


def comparison_ops():
    a, b = 4, 5
    print('\nComparison:')
    print('a == b ->', a == b)
    print('a != b ->', a != b)
    print('a < b ->', a < b)
    print('1 < a <= 10 ->', 1 < a <= 10)


def logical_ops():
    a, b = True, False
    print('\nLogical:')
    print('a and b ->', a and b)
    print('a or b ->', a or b)
    print('not a ->', not a)


def bitwise_ops():
    x, y = 5, 3  # 5:0b101, 3:0b011
    print('\nBitwise:')
    print('x & y ->', x & y)
    print('x | y ->', x | y)
    print('x ^ y ->', x ^ y)
    print('~x ->', ~x)
    print('x << 1 ->', x << 1)
    print('x >> 1 ->', x >> 1)


def membership_identity():
    seq = [1, 2, 3]
    a = seq
    b = list(seq)
    print('\nMembership & Identity:')
    print('2 in seq ->', 2 in seq)
    print('5 not in seq ->', 5 not in seq)
    print('a is b ->', a is b)
    print('a == b ->', a == b)


def ternary_precedence():
    val = 10
    result = 'big' if val > 100 else 'small'
    print('\nTernary & Precedence:')
    print("val=", val, "->", result)
    print('Precedence example: 2 + 3 * 4 =', 2 + 3 * 4)


def main():
    show_types()
    arithmetic_ops()
    assignment_ops()
    comparison_ops()
    logical_ops()
    bitwise_ops()
    membership_identity()
    ternary_precedence()


if __name__ == '__main__':
    main()
