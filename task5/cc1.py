def f(n):
    d1, d2, d3 = n // 100, n // 10 % 10, n % 10
    a = sorted([d1 + d2, d2 + d3])[::-1]
    res = str(a[0]) + str(a[1])
    return res


for i in range(100, 999 + 1):
    if f(i) == '145':
        print(i)