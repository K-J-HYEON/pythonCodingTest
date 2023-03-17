    # 1은 땅 0은 물
    # 시간 복잡도 300 * 300 = > 90000 -> 10**5 o(n**2) 하지말고 o(n) / o(nlogn)으로 작성
    # 2차원에서 dfs bfs 정석 코드 외우고 / 문제 형태 외우기 / 시간 복잡도 걍 생각해내기
    # 그래프 표현방식 1. 인접행렬 -> 매트릭스 / 2. 인접 리스트 / 3. 암시적
    # 벌텍스 - 엣지로 연결
    # 벌텍스와 모든 벌텍스를 연결
    # 2차원 배열 => 모든 곳을 탐방해야 하는 문제 => 걍 외우기

# https://leetcode.com/problems/number-of-islands/
# for 반복문 두개
# 땅일때 dfs bfs 돌기

# 동서남북 체크

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

from collections import deque

def numIslands(grid):
    number_of_islands = 0
    row = len(grid)
    col = len(grid[0])
    # 방문안햇을 때가 n x n이 있어야 한다.
    visited = [[False] * col for _ in range(row)]

    def bfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited[x][y] = True
        queue = deque()
        queue.append((x, y))
        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if next_x >= 0 and next_x < row and next_y >= 0 and next_y <col:
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1" and visited[i][j]:
                bfs(i, j)
                number_of_islands += 1
                # dfs()
    return number_of_islands

print(numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

