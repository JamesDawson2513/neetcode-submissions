class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        def dfs(i,j):
            if grid[i][j] == "1":
                grid[i][j] = "2"
                if i > 0: dfs(i-1,j)
                if j > 0: dfs(i, j-1)
                if i < len(grid) - 1: dfs(i+1, j)
                if j < len(grid[0]) - 1: dfs(i, j+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)

        return res


