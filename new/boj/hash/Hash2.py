# https://www.acmicpc.net/problem/1764

n, m = map(int, input().split())

a = set()
for i in range(n):
    a.add(input())


b = set()
for i in range(m):
    b.add(input())

result = sorted(list(a & b))

print(len(result))

for i in result:
    print(i)