def dfs(graph, v, visited):
    visited[v] = True

    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

visited = [False] * 9

dfs(graph, 1, visited)
