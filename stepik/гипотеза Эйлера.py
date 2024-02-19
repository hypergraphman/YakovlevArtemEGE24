from time import time

e = 150 ** 5
now = time()
for a in range(2, 151):
    a5 = a ** 5
    for b in range(2, 151):
        b5 = b ** 5
        for c in range(2, 151):
            c5 = c ** 5
            for d in range(2, 151):
                if a5 + b5 + c5 + d ** 5 <= e:
                    k = a + b + c + d
                    if k * 10 == int((a5 + b5 + c5 + d ** 5) ** (1 / 5) * 10):
                        print(a, b, c, d, k)
                    # print(a, b, c, d, k ** (1/5))
                else:
                    break
    print(time() - now)
    now = time()