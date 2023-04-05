# https://www.acmicpc.net/problem/5568

from itertools import permutations

n = int(input())
k = int(input())
cards = []

for _ in range(n):
    number = input()
    cards.append(number)

result = set()

for i in permutations(cards, k):
    result.add(''.join(i))

print(len(result))