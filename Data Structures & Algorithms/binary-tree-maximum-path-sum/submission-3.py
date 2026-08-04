# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float('-inf')
        def dfs(node) -> int:
            nonlocal maxsum
            if node == None:
                return 0
            maxright = dfs(node.right)
            maxleft = dfs(node.left)
            split_max = node.val + max(maxright,0) + max(maxleft,0)
            if split_max > maxsum:
                maxsum = split_max
            return node.val + max(maxright, maxleft, 0)
        dfs(root)
        return maxsum