class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = str()
        res = True
        for char in s:
            if char.isalnum():
                forward += char.lower()
        n = len(forward)
        for i in range(n//2):
            if forward[i] != forward[n-i-1]:
                res = False
        return res
            


        