# https://www.acmicpc.net/problem/11508
import sys
input = sys.stdin.readline

n = int(input())
price = [int(input()) for _ in range(n)]

price.sort(reverse = True)
ans = 0

for i in range(n):
    if i % 3 != 2:
        ans += price[i]


print(ans)