class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = set()
        x = 0
        y = 0
        output = []
        for i in nums:
            if target - i in num:
                s = i
                t = target - i
                break
            num.add(i)
        output.append(nums.index(t, 0))
        output.append(nums.index(s, output[0] + 1))
        return output
        
            
        
        