class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        best = r
        while l <= r:
            m = (l + r) // 2
            if self.numDays(weights, m) > days:
                l = m + 1
            else:
                best = m
                r = m - 1
        return best
    
    def numDays(self, weights: List[int], m: int) -> int:
        res = 1
        carry = 0
        for w in weights:
            if m - carry < w:
                res += 1
                carry = w
            else: 
                carry += w
        return res