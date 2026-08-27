class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    grid[r][c] = -1
        while q:
            r, c = q.popleft()
            directions = ((1,0), (-1,0), (0,1), (0,-1))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                    q.append((nr,nc))
                    grid[nr][nc] = grid[r][c] -1 
                    res = max(res, -(grid[nr][nc]+1))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: return -1
        return res
