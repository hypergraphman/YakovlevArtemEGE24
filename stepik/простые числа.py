a = int(input())
b = int(input())
for x in range(a, b + 1):
    k = 0
    for d in range(1, x + 1):
        if x % d == 0:
            k += 1
    if k == 2:
        print(x)
