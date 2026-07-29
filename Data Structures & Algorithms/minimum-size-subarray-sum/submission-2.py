class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        running = 0
        while r < len(nums):
            running += nums[r]
            while running >= target:
                if res == 0 or r - l + 1 < res:
                    res = r - l + 1
                running -= nums[l]
                l += 1
            r += 1
        return res
