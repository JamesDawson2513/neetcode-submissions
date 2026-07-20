class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a = 0
        res = []
        while a < len(nums) and nums[a] <= 0:
            target = -nums[a]
            l, r = a + 1, len(nums) - 1
            while l < r:
                left, right = nums[l], nums[r]
                if left + right == target:
                    res.append([-target, left, right])
                    while l < len(nums) and nums[l] == left:
                        l +=1
                elif left + right < target:
                    while l < len(nums) and nums[l] == left:
                        l += 1
                else: 
                    while r >= 0 and nums[r] == right:
                        r -= 1
            while a < len(nums) and nums[a] == -target:
                a += 1

        return res
        