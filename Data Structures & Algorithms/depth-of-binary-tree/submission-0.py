# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.right:
            maxr = self.maxDepth(root.right)
        else:
            maxr = 0
        if root.left:
            maxl = self.maxDepth(root.left)
        else:
            maxl = 0
        return max(maxr, maxl) + 1