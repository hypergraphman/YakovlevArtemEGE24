def f(n):
    s1 = bin(n)[3:]
    return int(s1, 2)


s = set()
for i in range(131, 3131 + 1):
    s.add(i - f(i))
print(len(s))