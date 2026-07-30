# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def isDescendant(root, p) -> bool:
            if not root:
                return False
            elif p == root.right or p == root.left or p == root:
                return True
            else:
                return isDescendant(root.right, p) or isDescendant(root.left, p)

        if root.right and isDescendant(root.right, p) and isDescendant(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.left and isDescendant(root.left, p) and isDescendant(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root





        