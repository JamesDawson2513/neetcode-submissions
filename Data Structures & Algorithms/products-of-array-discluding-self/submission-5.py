class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = 0
        res = []
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                product *= num
        if zeroCount > 1:
            res = [0] * len(nums)
            return res
        if zeroCount > 0:
            for num in nums:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
            return res
        else:
            for num in nums:
                res.append(product // num)
            return res
        
        