from collections import deque

def bfs(graph, v, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



graph = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

visited = [False] * 9

bfs(graph, 1, visited)
