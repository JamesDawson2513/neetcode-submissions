class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n):
            num = nums[i]
            if num <= 0 or num > n:
                nums[i] = n + 1

        for i in range(n):
            num = nums[i]
            if 1 <= abs(num) <= n:
                nums[abs(num)-1] = - abs(nums[abs(num)-1])
            
        for i in range(n):
            if nums[i] >= 0:
                res = i + 1
                return res

        return n + 1
                


    



        