# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p or not q:
                if not p and not q:
                    return True
                return False
            else:
                return (p.val == q.val and 
                    isSameTree(p.right, q.right) and isSameTree(p.left,q.left))

        if not root:
            return False
        elif isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        