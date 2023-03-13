# Level Order Traversal

from collections import deque

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

# preorder
def traversal(root):
    if root is None:
        return
    print(root)
    traversal(root.left)
    traversal(root.right)


# inorder
def traversal(root):
    if root is None:
        return
    traversal(root.left)
    print(root)
    traversal(root.right)


# postorder
def traversal(root):
    if root is None:
        return
    traversal(root.left)
    traversal(root.right)
    print(root)

