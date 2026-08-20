class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return [[]]

        without_first = self.subsets(nums[1:])
        with_first = [[nums[0]] + sub for sub in without_first]
        
        return without_first + with_first