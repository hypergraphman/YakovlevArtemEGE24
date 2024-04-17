*a, = map(int, open('17.txt').read().split())

x = sum(a) / len(a)

b = []
for p1, p2 in zip(a, a[1:]):
    if (p1 < x or p2 < x) and (p1 + p2) % 100 == 13:
        b.append(p1 + p2)
print(len(b), min(b))