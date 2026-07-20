class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        b = 0
        while b < len(nums):
            a = b + 1
            while a < len(nums):
                target2 = -nums[a] - nums[b] + target
                l, r = a + 1, len(nums) - 1
                while l < r:
                    left, right = nums[l], nums[r]
                    if left + right == target2:
                        res.append([nums[b], nums[a], left, right])
                        while l < len(nums) and nums[l] == left:
                            l +=1
                    elif left + right < target2:
                        while l < len(nums) and nums[l] == left:
                            l += 1
                    else: 
                        while r >= 0 and nums[r] == right:
                            r -= 1
                anum = nums[a]
                while a < len(nums) and nums[a] == anum:
                    a += 1
            bnum = nums[b]
            while b < len(nums) and nums[b] == bnum:
                    b += 1

        return res