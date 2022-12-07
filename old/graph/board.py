def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    
    else:
        parent[a] = b


g = int(input())
p = int(input())


#  부모 테이블 초기화
parent = [0] * (g + 1)

for i in range(1, g + 1):
    parent[i] = i


result = 0

for _ in range(p):
    # 현재 탑승구의 루트 확인
    data = find_parent(parent, int(input()))
    if data == 0:
        break

    union_parent(parent, data, data - 1)
    result += 1

print(result)
