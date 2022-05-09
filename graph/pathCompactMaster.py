
# 특정 원소가 속한 집합을 찾고
def find_parent(parent, x):
    # 루트 노드가 아니면, 루트 노드 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]
