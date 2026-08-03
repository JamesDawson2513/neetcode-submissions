# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            to_add = 0
            if not node:
                return 0
            elif node.val >= max_val:
                max_val = node.val
                to_add = 1
            return to_add + dfs(node.left, max_val) + dfs(node.right, max_val)
        return dfs(root, float('-inf'))
        