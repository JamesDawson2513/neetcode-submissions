class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        k = n//2 + 1
        numcount = {}
        for num in nums:
            numcount[num] = numcount.get(num, 0) + 1
            if numcount[num] == k:
                return num
        return
        