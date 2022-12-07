# DFS 메서드 정의
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    # 현재 노드와 연결된 다른 노드 재귀적으로 방문
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
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

dfs(graph, 1, visited)

