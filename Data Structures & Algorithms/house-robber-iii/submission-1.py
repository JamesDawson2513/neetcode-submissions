# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node) -> tuple[robbed: int, skipped: int]:
            if not node:
                return (0,0)
            else:
                left_rob, left_skip = dfs(node.left)
                right_rob, right_skip = dfs(node.right)
                rob_skip = max(left_rob, left_skip) + max(right_rob, right_skip)
                rob_this = node.val + left_skip + right_skip
                return (max(rob_this, rob_skip), rob_skip)
        return max(dfs(root))