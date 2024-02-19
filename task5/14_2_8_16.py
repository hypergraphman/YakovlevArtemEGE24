def edit_bin(num):
    if num.count('1') % 2 == 0:
        return num[1:].lstrip('0')
    return num.replace('0', '') + '1'


def f(n):
    s1 = bin(n)[2:]
    s2 = edit_bin(s1)
    s3 = edit_bin(s2)
    return int(s3, 2)


k = 1
for i in range(1, 1000 + 1):
    if f(i) == 7:
        k += 1
print(k)

