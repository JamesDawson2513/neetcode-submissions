class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        flows = defaultdict(tuple)
        p_q, a_q = collections.deque(), collections.deque()
        p_visited, a_visited = set(), set()
        res = []
        for r in range(rows):
            p_q.append((r, 0))
            p_visited.add((r, 0))
            
            a_q.append((r, cols - 1))
            a_visited.add((r, cols - 1))

        for c in range(cols):
            p_q.append((0, c))
            p_visited.add((0, c))
            
            a_q.append((rows - 1, c))
            a_visited.add((rows - 1, c))
        
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        while p_q:
            r, c = p_q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr in range(rows) 
                and nc in range(cols) 
                and (nr,nc) not in p_visited 
                and heights[nr][nc] >= heights[r][c]):
                    p_q.append((nr,nc))
                    p_visited.add((nr,nc))

        while a_q:
            r, c = a_q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr in range(rows) 
                and nc in range(cols) 
                and (nr,nc) not in a_visited 
                and heights[nr][nc] >= heights[r][c]):
                    a_q.append((nr,nc))
                    a_visited.add((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if (r,c) in a_visited and (r,c) in p_visited:
                    res.append([r,c])

        return res



            