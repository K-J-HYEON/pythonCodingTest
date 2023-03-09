# https://www.acmicpc.net/problem/12015

# sol 1
import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
lis = []
ans = 0

for num in a:
    if not lis:
        lis.append(num)
        ans += 1
        continue

    if lis[-1] < num:
        lis.append(num)
        ans += 1

    else:
        index = bisect_left(lis, num)
        lis[index] = num

print(ans)

# sol2
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp = [0]

for i in range(n):
    low = 0
    high = len(dp) - 1

    while low <= high:
        mid = (low + high) // 2
        if dp[mid] < A[i]:
            low = mid + 1
        else:
            high = mid - 1
    if low >= len(dp):

        dp.append(A[i])
    else:
        dp[low] = A[i]

print(len(dp) - 1)
