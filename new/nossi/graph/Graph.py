# 방향그래프 vs 무향그래프(코테 많이 등장)
# 다중 그래프 vs 단순 그래프 (중요)
# 가중치 그래프 => 다익스트라

# 그래프 활용
# 현실 세계의 사물이나 추상적인 개념 간의 연결 관계를 표현
# 그래프는 현실의 문제를 해결하기 위한 도구 => 문제 많이 나옴

# 인접행렬
graph = [
    [],
    [],
    [],
    [],
    []
]

# 인접리스트(많이 씀)
graph = {
    1: [3, 5],
    2: [],
    3: [],
    4: [],
    5: [1,2,3,4]
}
# 암시적 그래프


# https://leetcode.com/problems/number-of-islands/
# brute force
from collections import deque

visit = []
class Solution:
    def bfs(self, v, grid):
        global visit
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        q = deque()
        q.append(v)
        visit[v[0]][v[1]] = 1

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == "1" and not visit[nx][ny]:
                        visit[nx][ny] = 1
                        q.append([nx, ny])

    def numIslands(self, grid):
        global visit
        visit = [[0] * len(grid[0]) for _ in range(len(grid))]
        islandCnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visit[i]:

                    Solution.bfs(self, [i, j], grid)
                    islandCnt += 1
                    return islandCnt


