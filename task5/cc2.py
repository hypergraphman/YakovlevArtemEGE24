def f(n):
    d1, d2, d3, d4, d5 = map(int, str(n))
    a = sorted([d1 + d3 + d5,  d2 + d4])
    return str(a[0]) + str(a[1])


for i in range(10000, 99999 + 1):
    if f(i) == '321':
        print(i)
        break