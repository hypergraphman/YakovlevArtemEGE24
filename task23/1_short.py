def f(s, e):
    if s >= e:
        return s == e
    return f(s + 1, e) + f(s * 2, e) + f(s * 3, e)


print(f(1, 15))