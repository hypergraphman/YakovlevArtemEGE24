from fnmatch import fnmatch

for i in range(47, 10**10, 47):
    if fnmatch(str(i), '9*4*0'):
        f = True
        for p1, p2 in zip(str(i), str(i)[1:]):
            if p1 <= p2:
                f = False
                break
        if f:
            print(i, i // 47)