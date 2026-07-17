class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        pre = strs[0]
        for i in range(len(pre)):
            for s in strs:
                if i == len(s) or pre[i] != s[i]:
                    return res
            res += pre[i]
        return res

        



        