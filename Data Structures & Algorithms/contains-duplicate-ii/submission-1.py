class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0
        r = 0
        for r in range(min(len(nums), k + 1)):
            num = nums[r]
            if num in window:
                return True
            window.add(num)
        
        r += 1

        while r < len(nums):
            window.remove(nums[l])
            num = nums[r]
            if num in window:
                return True
            window.add(num)
            l, r = l+1, r+1
        return False