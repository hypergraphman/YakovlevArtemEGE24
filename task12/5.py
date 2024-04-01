def divs(n):
    s = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            s.add(d)
            s.add(n // d)
    return sorted(s)


for n in range(1, 100):
    line = '>' + '1' * 14 + '2' * 11 + '3' * n
    while '>1' in line or '>2' in line or '>3' in line:
        if '>1' in line:
            line = line.replace('>1', '23>', 1)
        if '>2' in line:
            line = line.replace('>2', '21>', 1)
        if '>3' in line:
            line = line.replace('>3', '7>', 1)
    if len(divs(sum(map(int, line[:-1])))) == 2:
        print(n, sum(map(int, line[:-1])))
        break