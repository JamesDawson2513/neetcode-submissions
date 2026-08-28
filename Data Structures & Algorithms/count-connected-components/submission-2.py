class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visited = set()
        res = 0

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            visited.add(node)
            for adjnode in adj[node]:
                if adjnode not in visited:
                    dfs(adjnode)
        
        for i in range(n):
            if i not in visited:
                res +=1 
                dfs(i)
        
        return res

            
                