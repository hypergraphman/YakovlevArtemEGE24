def f(c, e, k):
    if c > e or k > 7:
        return 0
    if c == e:
        return 1
    m = [
        f(c + 2, e, k + 1),
        f(c + 3, e, k + 1),
        f(c * 2, e, k + 1)
    ]
    return sum(m)


print(f(1, 130, 0))