class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = defaultdict(list)
        visited = {0}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        q = collections.deque()
        q.append(0)
        while q:
            node = q.popleft()
            for adjnode in adj[node]:
                if adjnode not in visited:
                    visited.add(adjnode)
                    q.append(adjnode)
        return len(visited) == n
        