class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1
        while r < len(numbers):
            if numbers[l] + numbers[r] < target:
                r += 1
                l += 1
            elif numbers[l] + numbers[r] > target:
                l -= 1
            else:
                return [l+1, r+1]


