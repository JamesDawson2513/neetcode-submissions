class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []
        if n < 3:
            return output
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            if nums[i] > 0:
                break
            while left < right:
                Sum = nums[i] + nums[left] + nums[right]
                if Sum < 0:
                    left += 1
                elif Sum > 0:
                    right -= 1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return output

            
        