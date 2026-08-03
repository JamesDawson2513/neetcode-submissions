# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = None
        def dfs(node: Optional[TreeNode]):
            nonlocal count
            nonlocal res
            if not node or res:
                return
            if node.left:
                dfs(node.left)
            count += 1
            if count == k:
                res = node.val
            if node.right:
                dfs(node.right)
        dfs(root)
        return res

             
                
