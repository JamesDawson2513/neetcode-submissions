class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = nums[0]
        for num in nums:
            if num == res:
                count += 1
            else:
                count -= 1
                if count == -1:
                    res = num
                    count = 1
        return res

        