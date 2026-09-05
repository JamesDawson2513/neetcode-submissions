class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = {}
        rank = {}
        multiple = {}

        def find(x) -> Tuple[str, float]:
            if x not in parent:
                parent[x] = x
                rank[x] = 1
                multiple[x] = 1
            elif x != parent[x]:
                root, parent_mult_to_root = find(parent[x])
                multiple[x] = multiple[x] * parent_mult_to_root 
                parent[x] = root
            return (parent[x], multiple[x])

        def union(x,y, val):
            parx, multx = find(x)
            pary, multy = find(y)
            if parx != pary:
                if rank[parx] >= rank[pary]:
                    parent[pary] = parx
                    rank[parx] += rank[pary]
                    multiple[pary] = multx/(val*multy)
                else:
                    parent[parx] = pary
                    rank[pary] += rank[parx]
                    multiple[parx] = (val*multy)/multx
        
        for i in range(len(values)):
            a, b, val = equations[i][0], equations[i][1], values[i]
            union(a,b,val)

        res = []
        
        for x, y in queries:
            if x not in parent or y not in parent:
                res.append(-1)
                continue
            parx, multx, pary, multy = find(x)[0], find(x)[1], find(y)[0], find(y)[1]
            if parx != pary:
                res.append(-1)
            else:
                res.append(multx/multy)
        return res


        

