def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b

    
# 노드의 개수와 간선(union)의 개수 입력받기
v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트 / 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서 부소를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
# 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선
last = 0

# 간선 하나씩 확인하고
for edge in edges:
    cost, a, b = edge
    # 사이클 발생하지 않으면 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)
