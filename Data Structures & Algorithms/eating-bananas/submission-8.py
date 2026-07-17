
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r  # Start with the maximum possible speed as the initial result
        while l <= r:
            k = (l + r) // 2  # Middle speed to check
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k  # Equivalent to math.ceil(p / k)
            if hours <= h:
                res = min(res, k)  # Update res to the smallest valid speed
                r = k - 1  # Try a lower speed
            else:
                l = k + 1  # Try a higher speed
        return res
