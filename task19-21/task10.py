def f(s, m, ban):
    if s >= 203:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s + 1, m - 1, 0),
         f(s + 2, m - 1, 0)]
    if ban == 0:
        h.append(f(s * 3, m - 1, 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('N19', [s for s in range(1, 203) if f(s, 2, 0)])
print('N20', len([s for s in range(1, 203) if not f(s, 1, 0) and f(s, 3, 0)]))
print('N21', [s for s in range(1, 203) if not f(s, 2, 0) and f(s, 4, 0)])
