import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

li = []
for _ in range(n):
    li.append(int(input()))


li.sort(reverse=True)
count = 0

for i in li:
    if k // i > 0:
        count += k // i
        k = k % i

print(count)