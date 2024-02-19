from string import digits, ascii_lowercase


def n_to_p(n, p):
    r = ''
    alp = digits + ascii_lowercase
    while n:
        r = alp[n % p] + r
        n //= p
    return r


def f(n):
    s1 = n_to_p(n // 2, 16)
    if n % 4 != 0:
        s2 = 'F' + s1 + 'A0'
    else:
        s2 = '15' + s1 + 'C'
    return int(s2, 16)


for i in range(1000):
    if f(i) < 65535:
        print(i)