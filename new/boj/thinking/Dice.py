human = int(input())
answer = 0

for _ in range(human):
    a, b, c = map(int, input().split())

    if a == b == c:
        answer = max(answer, 10000 + a * 1000)
    elif a == b:
        answer = max(answer, 10000 + a * 100)
    elif a == c:
        answer = max(answer, 10000 + a * 100)
    elif b == c:
        answer = max(answer, 10000 + b * 1000)
    else:
        answer = max(answer, max(a, b, c) * 100)

print(answer)