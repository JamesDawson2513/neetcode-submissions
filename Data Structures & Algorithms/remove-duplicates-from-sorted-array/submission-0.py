class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        cur = nums[0]
        pointer = 1

        for num in nums:
            if num == cur:
                continue
            else:
                nums[pointer] = num
                cur = num
                pointer += 1

        return pointer





