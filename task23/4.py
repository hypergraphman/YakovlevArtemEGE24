def f(s, e, h):
    if s > e:
        return 0
    if s == e:
        if h[-2] == '2':
            return 1
        else:
            return 0
    return f(s + 1, e, h + '1') + f(s * 2, e, h + '2') + f(s * 3, e, h + '2')


print(f(1, 28, ''))