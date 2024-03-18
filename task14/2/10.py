k = 0
for x in range(6, 100):
    a = 1 * x ** 4 + 3 * x ** 3 + 1 * x ** 2 + 5 * x + 2
    b = 7 * 100 ** 3 + x * 100 ** 2 + 2 * 100 + 5
    s = a + b
    if s % 9 == 0:
        k += 1
print(k)