## deque 사용
from collections import deque

n = int(input())
cards = deque(list(range(1, n+1)))
res = []

while cards:
    card = cards.popleft()
    res.append(card)
    if cards:
        card = cards.popleft()
        cards.append(card)

print(*res)

## deque 사용 x
n = int(input())
cards = list(range(1, n + 1))
res = []
while len(cards) > 1:
    res.append(cards[0])
    cards = cards[2:] + [cards[1]]
res.append(cards[0])

print(*res)