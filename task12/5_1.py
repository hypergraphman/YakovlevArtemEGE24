def divs(n):
    s = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            s.add(d)
            s.add(n // d)
    return sorted(s)


for n in range(1, 100):
    s = 103 + n * 7
    if len(divs(s)) == 2:
        print(n, s)
        break