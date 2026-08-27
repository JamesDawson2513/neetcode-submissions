class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited = set()

        def bfs(r: int, c: int) -> int:
            area = 0
            q = deque([(r, c)])
            visited.add((r, c))
            
            while q:
                curr_r, curr_c = q.popleft()
                area += 1
                
                for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))
                    
        return max_area
        