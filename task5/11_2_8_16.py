def f(n):
    s1 = bin(n)[2:]
    count_one = s1[1::2].count('1')
    count_zero = s1[::2].count('0')
    res = abs(count_zero - count_one)
    return res


print(f(131))

k = 0
for i in range(1000, 5000 + 1):
    if f(i) >= 5:
        k += 1
print(k)