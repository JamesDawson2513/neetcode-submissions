class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0]*3
        for num in nums:
            count[num] += 1
        i = 0
        for colour in range(3):
            for _ in range(count[colour]):
                nums[i] = colour
                i += 1
        

            