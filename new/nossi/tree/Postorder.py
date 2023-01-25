# def LCA(root, p, q):
#     if root == None:
#         return None
#
#     left  = LCA(root.left, p, q)
#     right = LCA(root.right, p, q)
#     if root == p or root == q:
#         return root
#     elif left and right:
#         return root
#     return left or right
#
# LCA([3,5,1,6,2,0,8, None, None, 7, 4], 6, 4)


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if root == p or root == q:
            return root

        elif left and right:
            return root

        elif left:
            return left

        elif right:
            return right