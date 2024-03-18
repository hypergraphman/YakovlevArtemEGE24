for x in range(24):
    is_y = True
    for y in range(24):
        a = 3 * 24**3 + x * 24**2 + y * 24 + 3
        b = 1 * 24**3 + y * 24**2 + 3 * 24 + 1
        s = a + b
        if s % 5 != 0:
            is_y = False
            break
    if is_y:
        a = 3 * 24 ** 3 + x * 24 ** 2 + 7 * 24 + 3
        b = 1 * 24 ** 3 + 7 * 24 ** 2 + 3 * 24 + 1
        s = a + b
        print(x, s // 5)
