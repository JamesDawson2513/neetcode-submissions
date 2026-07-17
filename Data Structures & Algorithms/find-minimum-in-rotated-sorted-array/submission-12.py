class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if nums[l] <= nums[r]:
            return nums[l]
        while r-l > 1:
            m = (l + r) // 2
            if nums[r] < nums[m] > nums[l]:
                l = m + 1
            else:
                r = m
        return min(nums[l],nums[r])

        