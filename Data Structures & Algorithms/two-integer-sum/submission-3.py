class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numhash = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in numhash:
                return [numhash[target-num], i]
            else:
                numhash[num] = i
        
