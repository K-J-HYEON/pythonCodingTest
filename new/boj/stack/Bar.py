import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    stack.append(int(input()))

last = stack[-1]
count = 1

for i in reversed(range(n)):
    if stack[i] > last:
        count += 1
        last = stack[i]

print(count)