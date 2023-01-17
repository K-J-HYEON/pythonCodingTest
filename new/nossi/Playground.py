import sys

input = sys.stdin.readline

w, n = map(int, input().split())
mp = [list(map(int, input().split())) for x in range(n)]
cnt = [0] * (n + 1)

# 리스트 변수에 금속의 무게를 무게당 가격의 크기순으로 넣는다.
for i in range(n):
    cnt[mp[i][1]] += mp[i][0]

result = 0
for i in reversed(range(n + 1)):
    if w < cnt[i]:
        result += w * i
        break

    result += i * cnt[i]
    w -= cnt[i]

print(result)