class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        start = 0
        length = 0
        for i in range(len(s)):
            char = s[i]
            if char in chars:
                if start <= chars[char]:
                    start = chars[char] + 1
            chars[char] = i  
            if i - start + 1 > length:
                length += 1
        return length    



            
