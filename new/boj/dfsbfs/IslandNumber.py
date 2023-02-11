# https://www.acmicpc.net/problem/4963

from collections import deque

w, h = int(), int()
arr, visited = list(), list()
count = 0
d = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]  # ↑ ← ↓ → ←↑ ←↓ ↓→ →↑


def bfs(a, b):
    global w, h, arr, count

    if not arr[a][b] or visited[a][b]: return

    queue = deque([(a, b)])
    count += 1

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx, ny = x + d[i][0], y + d[i][1]
            if nx in range(h) and ny in range(w) and not visited[nx][ny] and arr[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


def solution():
    global w, h, arr, count, visited

    while True:
        # init
        count = 0

        # user_input
        w, h = map(int, input().split())
        if w == h == 0: break

        visited = [[False] * w for _ in range(h)]
        arr = [list(map(int, input().split())) for _ in range(h)]

        # logic
        for x in range(h):
            for y in range(w):
                bfs(x, y)
        print(count)


solution()