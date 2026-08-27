class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        q = collections.deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c,0))
                    visited.add((r,c))
        
        while q:
            r, c, dist = q.popleft()
            grid[r][c] = dist
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc] > 0:
                    q.append((nr,nc,dist+1))
                    visited.add((nr,nc))



        
        
