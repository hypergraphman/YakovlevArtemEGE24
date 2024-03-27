def f(s, e, h):
    if s > e:
        return 0
    if s == e:
        if h.count('B') <= 2:
            return 1
        else:
            return 0
    m = [f(s + 1, e, h + '1')]
    if s % 2 == 0:
        m.append(f(s // 2, e,))
    return f(s + 1, e, h + 'A') + f(s * 2, e, h + 'B') + f(s * 3, e, h + 'C')


print(f(1, 28, ''))