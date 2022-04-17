def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(grapj, i, visited)


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

