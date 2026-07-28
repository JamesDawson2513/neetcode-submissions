class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        contents = set()
        for r in range(len(s)):
            if s[r] in contents:
                res = max(res, r - l)
                while s[l] != s[r]:
                    contents.remove(s[l])
                    l += 1
                contents.remove(s[l])
                l += 1
            contents.add(s[r])
        return max(res, len(s) - l)
                

