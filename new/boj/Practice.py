import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

maxNumber = max(m)
minNumber = min(m)

print(maxNumber * minNumber)