def plus_bit(num):
    count_zero = num.count('0')
    count_one = num.count('1')
    if count_zero > count_one:
        return num + '1'
    if count_zero < count_one:
        return num + '0'
    return num + num[-1]


def f(n):
    s1 = bin(n)[2:]
    s2 = plus_bit(s1)
    s3 = plus_bit(s2)
    s4 = plus_bit(s3)
    return int(s4, 2)


for i in range(132, 200):
    if f(i) % 8 == 0:
        print(i)
        break