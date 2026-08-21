class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(running, cur, i):
            if i == len(s):
                if cur == "":
                    res.append(running.copy())
                return
            
            cur += s[i]

            if cur == cur[::-1]:
                running.append(cur)
                dfs(running, "", i+1)
                running.pop()

            dfs(running, cur, i + 1)

        dfs([],"",0)
        return res