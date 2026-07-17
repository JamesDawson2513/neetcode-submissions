class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def finder(left, right):
            middle = (left + right) // 2
            if right - left < 2:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                else:
                    return -1
            elif nums[middle] > target:
                return finder(left, middle)
            else:
                return finder(middle, right)
        res = finder(0,len(nums)-1)
        return res

        