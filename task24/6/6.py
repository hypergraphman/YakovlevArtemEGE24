line = open('24.txt').readline().strip()

max_len = 0
cur_len = 1
max_i = 0
for i in range(len(line) - 1):
    c1, c2 = line[i], line[i + 1]
    if c1 != c2:
        cur_len += 1

    else:
        cur_len = 1

    if cur_len >= max_len:
        max_len = cur_len
        max_i = i + 1
print(line[max_i - max_len - 2:max_i + 4])
