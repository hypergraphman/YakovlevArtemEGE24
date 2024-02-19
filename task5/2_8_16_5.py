def f(n):
    s1 = bin(n)[2:]
    s2 = int(s1[1:], 2)
    s3 = n - s2
    return s3


print(f(131))


a = set()
for i in range(131, 3131 + 1):
    s1 = bin(i)[2:]
    s2 = int(s1[1:], 2)
    s3 = i - s2
    a.add(s3)
print(len(a))
print(a)
