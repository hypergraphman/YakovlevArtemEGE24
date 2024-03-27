def f(c, e, k):
    if c > e or k > 7:
        return 0
    if c == e:
        return 1
    m = []
    if (c + 1) % 2 == 0:
        m.append(f(c + 1, e, k + 1))
    else:
        m.append(f(c + 1, e, k))
    if (c * 2) % 2 == 0:
        m.append(f(c * 2, e, k + 1))
    else:
        m.append(f(c * 2, e, k))
    if (c * 3) % 2 == 0:
        m.append(f(c * 3, e, k + 1))
    else:
        m.append(f(c * 3, e, k))
    return sum(m)


print(f(1, 131, 0))