class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        in_nums = set()
        for n in nums:
            if n in in_nums:
                return True
            else:
                in_nums.add(n)
        return False
