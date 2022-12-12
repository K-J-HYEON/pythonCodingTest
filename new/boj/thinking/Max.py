max_num = 0
col = 0
row = 0
for i in range(9):
    line = list(map(int, input().split()))
    if max(line) > max_num:
        max_num = max(line)
        col = i+1
        row = line.index(max_num) + 1

print(max_num)
print(col, row)