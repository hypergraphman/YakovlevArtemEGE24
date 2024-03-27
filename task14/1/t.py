def sum_digit_p(n, p):
    data = []
    n = abs(n)
    while n:
        data.append(n % p)
        n //= p
    return sum(data)


print(sum_digit_p(18*7**108 - 5 * 49**76 + 343**35 - 50, 49))