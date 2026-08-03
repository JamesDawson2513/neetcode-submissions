"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n,r,c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allSame = False
            if allSame == True:
                val = grid[r][c]
                return Node(val,True, None, None, None, None)
            else:
                val = grid[r][c]
                return Node(val, False, dfs(n//2,r,c), dfs(n//2, r, c+n//2), dfs(n//2,r + n//2,c), dfs(n//2, r + n//2, c + n//2))
        return dfs(len(grid),0,0)