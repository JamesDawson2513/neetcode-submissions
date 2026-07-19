class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        lengths = {}
        res = 0

        for num in nums:

            if num in lengths:
                continue

            left = lengths.get(num-1, 0)
            right = lengths.get(num+1, 0)

            total = right + left + 1

            if total > res:
                res = total

            lengths[num] = total
            
            lengths[num - left] = total
            lengths[num + right] = total
        
        return res
            

        