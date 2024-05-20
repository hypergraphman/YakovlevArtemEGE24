line = open('24.txt').readline()

max_len = 0
cur_len = 1
for i in range(len(line) - 1):
    c1, c2 = line[i], line[i + 1]
    if c1 == c2:
        cur_len += 1
    else:
        cur_len = 1
    if cur_len > max_len:
        max_len = cur_len
print(max_len)