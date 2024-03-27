def f(c, e, k):
    if k > 4 or c > e:
        return 0
    if c == e:
        if k == 4:
            return 1
        else:
            return 0
    m = [
        f(c + 1, e, k + 1),
        f(c + 3, e, k + 1),
        f(c * 3, e, k + 1)
    ]
    return sum(m)


c = 0
for e in range(2, 1000):
    if f(1, e, 0):
        c += 1
print(c)