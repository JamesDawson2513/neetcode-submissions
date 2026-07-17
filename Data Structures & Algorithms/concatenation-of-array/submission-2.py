class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n= len(nums)
        for i in range(n):
            ans.append(nums[i])
        for i in range (n):
            ans.append(nums[i-n])
        return ans
    



        