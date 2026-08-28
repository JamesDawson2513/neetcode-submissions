class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def dfs(curr, target, visited) -> bool:
            if curr == target:
                return True
            visited.add(curr)
            for neighbour in adj[curr]:
                if neighbour not in visited:
                    if dfs(neighbour, target, visited):
                        return True
            return False

        for u, v in edges:
            if dfs(u, v, set()):
                return [u,v]
            adj[u].append(v)
            adj[v].append(u)

        return []