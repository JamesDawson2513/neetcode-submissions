class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        res = []
        wordDict = set(wordDict)

        def dfs(i, running, cur):

            if i == len(s):
                if cur == "":
                    res.append(" ".join(running))
                return

            cur += s[i]

            if cur in wordDict:
                running.append(cur)
                dfs(i+1, running, "")
                running.pop()
            
            dfs(i+1, running, cur)
        
        dfs(0, [], "")
        return res

