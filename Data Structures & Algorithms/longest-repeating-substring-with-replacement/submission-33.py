class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = res = 0
        chars = {}
        while r < len(s):
            char = s[r]
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
            maxf = 1
            for i in chars:
                maxf = max(chars[i],maxf)
            if (r - l + 1) - maxf > k:
                    chars[s[l]] -= 1
                    l += 1
            elif r-l+1 > res:
                res = r-l+1
            print(l,r,maxf,char)
            r += 1
        return res
             

        