class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i, length, avoided):
            print(cur)
            if length == k:
                res.append(cur.copy())
                return
            if avoided < n - k:
                dfs(i+1, length, avoided + 1)
            cur.append(i)
            dfs(i + 1, length + 1, avoided)
            cur.pop()
        
        dfs(1,0,0)
        return res
            


        