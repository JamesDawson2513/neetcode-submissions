class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = {}
        email2name = {}

        def find(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 1
            elif parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                    rank[root_x] += rank[root_y]
                else:
                    parent[root_x] = root_y
                    rank[root_y] += rank[root_x]
        
        for i in range(len(accounts)):
            name = accounts[i][0]
            for j in range(1, len(accounts[i])):
                email2name[accounts[i][j]] = name
                union(accounts[i][1], accounts[i][j])
    
        groups = defaultdict(list)

        for email in parent:
            root = find(email)
            groups[root].append(email)

        res = []
        
        for root, emails in groups.items():
            name = email2name[root]
            res.append([name] + sorted(emails))

        return res