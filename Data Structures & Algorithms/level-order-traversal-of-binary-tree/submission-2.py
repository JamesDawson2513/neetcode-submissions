# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        else:
            left_array = self.levelOrder(root.left)
            right_array = self.levelOrder(root.right)
            llen, rlen = len(left_array), len(right_array)
            maxlen = max(llen, rlen)
            res = [[] for _ in range(maxlen + 1)]
            res[0].append(root.val)
            for i in range(1, maxlen + 1):
                if i <= llen:
                    for j in range(len(left_array[i-1])):
                        res[i].append(left_array[i-1][j])
                if i <= rlen:
                    for j in range(len(right_array[i-1])):
                        res[i].append(right_array[i-1][j])
            return res


