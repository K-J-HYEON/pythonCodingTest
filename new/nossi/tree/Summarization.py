from collections import deque

# 트리의 기본 구조
def levelOrder(root):
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

# 전위 순회
def traversal(root):
    if root is None:
        return
    traversal(root.left)
    traversal(root.right)

def preorder(root):
    if root is None:
        return
    print(root)
    preorder(root.left)
    preorder(root.right)

# 중위 순회
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root)
    inorder(root.right)

# 후위 순회
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root)