# 인접 행렬
INF = 99999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)


# 인접 리스트
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[2].append((0, 5))

print(graph)


# dfs
def dfs(graph, v, visited):
    visited[v] = True

    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
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

dfs(graph, 1, visited)