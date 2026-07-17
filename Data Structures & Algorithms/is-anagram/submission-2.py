class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        snums = {}
        for char in s:
            if char in snums:
                snums[char] += 1
            else:
                snums[char] = 1
        for char in t:
            if char in snums:
                snums[char] -= 1
            else:
                return False
        for char in snums:
            if snums[char] != 0:
                return False
        return True
        