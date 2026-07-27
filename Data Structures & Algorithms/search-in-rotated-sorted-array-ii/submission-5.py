class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        l, r = 0, len(nums) - 1
        
        while l <= r:
            while l < r and nums[r] == nums[l]:
                r -= 1
            mid = (l+r)//2
            if target == nums[mid]:
                return True
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False

