# https://www.acmicpc.net/problem/1158
import sys
input = sys.stdin.readline

from collections import deque
queue = deque()

n, k = map(int, input().split())

for i in range(n):
    queue.append(i+1)

result = []

i = 1
while queue:
    if i % k == 0:
        result.append(queue.popleft())
    else:
        queue.append(queue.popleft())

    i = i + 1

print('<' +', '.join(map(str, result))+'>')