# bfs
# 트리 순회할려는 그림 => 1분 안되서 외우기

from collections import deque

def bfs(root):
    visited = []
    if root is None:
        return 0
    q = deque()
    q.append(root)
    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)

    return visited

    bfs(root)