class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t = strs[0]
        j = len(t)
        for s in strs:
            if j > len(s):
                j = len(s)
            for i in range(j):
                if t[i] != s[i]:
                    j = i
                    break
        return t[0:j]



        