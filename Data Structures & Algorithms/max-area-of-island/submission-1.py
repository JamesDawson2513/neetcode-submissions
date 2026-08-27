class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        if not grid:
            return 0
        
        def bfs(i,j) -> int:
            nonlocal area
            area += 1
            visited.add((i,j))
            directions = [(0,1), (1,0), (-1, 0), (0,-1)]
            for di, dj in directions:
                di, dj = i + di, j + dj
                if di in range(len(grid)) and dj in range(len(grid[0])) and (di,dj) not in visited and grid[di][dj] == 1:
                    bfs(di,dj)
                    

            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = 0
                    bfs(i,j)
                    maxArea = max(maxArea, area)
        return maxArea

        