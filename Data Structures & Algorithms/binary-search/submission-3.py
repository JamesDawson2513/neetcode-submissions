class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def finder(left, right):
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif left >= right:
                return -1
            elif nums[middle] > target:
                return finder(left, middle-1)
            else:
                return finder(middle + 1, right)
        res = finder(0,len(nums)-1)
        return res

        