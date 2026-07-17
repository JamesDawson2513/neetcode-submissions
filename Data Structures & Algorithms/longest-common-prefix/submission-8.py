class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        pre = strs[0]
        for i in range(len(pre)):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res

        



        