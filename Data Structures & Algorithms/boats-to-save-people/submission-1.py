class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        freq = Counter(people)
        lower = 1
        res = 0

        for r in range(max(freq.keys()),0,-1):
            while freq[r] > 0:
                if r + lower > limit:
                    res += 1
                    freq[r] -= 1
                elif freq.get(lower, 0) == 0:
                    lower += 1
                else:
                    freq[r] -= 1
                    freq[lower] -= 1
                    res += 1
        
        return res
            


        