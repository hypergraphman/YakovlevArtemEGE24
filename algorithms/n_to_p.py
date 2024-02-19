from string import digits, ascii_lowercase


def n_to_p(n, p):
    r = ''
    alp = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        r = alp[n % p] + r
        n //= p
    return r


print(n_to_p(10, 10))
print(n_to_p(194, 5))
print(n_to_p(255, 16))
