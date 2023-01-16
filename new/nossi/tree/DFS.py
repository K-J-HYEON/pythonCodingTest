# DFS
# 깊이 우선 탐색
# def dfs(root):
#     if root is None:
#         return
#     dfs(root.left)
#     dfs(root.right)
#
#     dfs(root)
# root만 나한테 주면 root가 가리키는 tree에 속한 모든노드를 접근해준다라는 뜻

# def dfs(cur_node):
#     if cur_node is None:
#         return
#     dfs(cur_node.left)
#     dfs(cur_node.right)
#
#     dfs(root)