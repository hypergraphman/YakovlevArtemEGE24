line = input()
mx_count_char = 0
mx_char = None
for char in set(line):
    if line.count(char) > mx_count_char:
        mx_count_char = line.count(char)
        mx_char = char
print(mx_char)