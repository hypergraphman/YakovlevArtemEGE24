def f(n):
    d1, d2, d3 = map(int, str(n))
    b = [d1 * 10 + d2, d1 * 10 + d3,
         d2 * 10 + d1, d2 * 10 + d3,
         d3 * 10 + d1, d3 * 10 + d2]
    a = []
    for el in b:
        if el > 9:
            a.append(el)
    return max(a) - min(a)


for i in range(100, 999 + 1):
    if f(i) == 80:
        print(i)