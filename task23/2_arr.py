a = [0] * 1000
a[3] = 1
for i in range(4, 1000):
    if i != 12:
        a[i] += a[i - 1]
        if i % 2 == 0:
            a[i] += a[i // 2]
        if i ** 0.5 == int(i ** 0.5):
            a[i] += a[int(i ** 0.5)]

print(a[20])
print(a[500])