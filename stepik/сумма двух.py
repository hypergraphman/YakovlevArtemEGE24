n = int(input())
b = []
pre = int(input())
for i in range(n - 1):
    cur = int(input())
    b.append(pre + cur)
    pre = cur
print(b)
