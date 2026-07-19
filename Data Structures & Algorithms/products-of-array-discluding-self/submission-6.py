class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProd, rightProd, res = [1]*(n+2), [1]*(n+2), [1]*n
        for i in range(n):
            leftProd[i+1] = leftProd[i] * nums[i]
            rightProd[n-i] = rightProd[n-i+1] * nums[n-i-1]
        for i in range(n):
            res[i] = leftProd[i] * rightProd[i+2]
        return res


        

