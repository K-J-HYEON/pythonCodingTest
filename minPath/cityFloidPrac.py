INF = int(1e9)

# 노드 개수 및 갖선ㅇ 개수
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0


# 각 간선에 대한 정보 입력 받고 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


# 최종 목적지 노드 입력받기
x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

# 도달할 수 없다 그러면 -1로 해라
if distance >= INF:
    print("-1")
    
else:
    print(distance)