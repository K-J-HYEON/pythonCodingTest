def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visted[i]:
            dfs(grapn, i, visited)



graph = [
    [],
    [2, 3, 8],ㅇ
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9

dfs(graph, 1, visited)
