from math import ceil

class Solution:
    def numHours(self, piles: List[int], m: int) -> int:
        res = 0 
        for i in range(len(piles)):
            res += ceil(piles[i]/m)
        return res
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = -1
        while l <= r:
            m = (l + r) // 2
            hours = self.numHours(piles, m)
            if hours > h:
                l = m + 1
            else:
                best = m
                r = m - 1
        return best
    
