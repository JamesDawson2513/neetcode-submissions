import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        for i in range(math.gcd(n, k)):
            l = i
            temp1 = nums[(l - k) % n]
            repeat = False
            while not repeat:
                temp2 = nums[l]
                nums[l] = temp1
                temp1 = temp2
                l += k
                l = l % n
                if l == i:
                    repeat = True
        return nums




                


        
        