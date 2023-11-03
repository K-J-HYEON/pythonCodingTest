# https://www.acmicpc.net/problem/10816

# 해시 풀이
import sys
input = sys.stdin.readline
N = int(input())
a = map(int, input().split())

# 1. hash에 num에 개수 반영
hash = {}
for num in a:
    hash[num] = hash.setdefault(num, 0) + 1

# 2.hash에서 num 개수 출력
M = int(input())
b = map(int, input().split())
for num in b:
    print(hash.setdefault(num, 0), end = ' ')


# 배열 풀이
import sys
input = sys.stdin.readline
MAX = 20000000 + 10
cnt = [0] * MAX

N = int(input())
a = map(int, input().split())
for num in a:
    cnt[num + 10000000] += 1

M = int(input())
b = map(int, input())
for num in b:
    print(cnt[num + 10000000], end = ' ')