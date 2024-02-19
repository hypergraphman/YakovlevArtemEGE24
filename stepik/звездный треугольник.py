n = int(input())
for i in range(n):
    for j in range((n + 1) // 2 - abs(i - n // 2)):
        print('*', end='')
    print()
