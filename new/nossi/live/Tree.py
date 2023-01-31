# 1. Tree 구현
# 2. 트리 순회
# postorder

# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from collections import deque
# root = [3, 9, 20, None, None, 15, 7]
#
# class TreeNode(self, l, r):
#     def __init__(self):
#         left = l
#         right = r


# levelorder
# from collections import deque
#
# class TreeNode():
#     def __init__(self, v, l=None, r=None):
#         self.value = v
#         self.left = l
#         self.right = r
#
# root = TreeNode(v=3)
# root.left = TreeNode(v=9)
# root.right = TreeNode(v=20)
# root.right.left = TreeNode(v=15)
# root.right.right = TreeNode(v=7)
#
#
# def maxDepth(root):
#     max_depth = 0
#     if root is None:
#         return 0
#     q = deque()
#     q.append((root, 1))
#     while q:
#         cur_node, cur_depth = q.popleft()
#         if cur_node.left:
#             q.append((cur_node.left, cur_depth + 1))
#         if cur_node.right:
#             q.append((cur_node.right, cur_depth + 1))
#         max_depth = max(max_depth, cur_depth)
#     return max_depth
#
# print(maxDepth(root))



# postorder
from collections import deque

class TreeNode():
    def __init__(self, v, l=None, r=None):
        self.value = v
        self.left = l
        self.right = r

root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)


def maxDepth(root):
    if root is None:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)


    # 맥스뎁스 결정 => left right 중 어떤게 더 깊은지
    # left vs right
    cur_depth = max(left_depth, right_depth) + 1
    return cur_depth

print(maxDepth(root))