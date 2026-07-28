class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = sum(nums)
        while l <= r:
            mid = (l + r) // 2
            count = 1
            running = 0
            for i in range(len(nums)):
                running += nums[i]
                if running > mid:
                    count += 1
                    running = nums[i]
            if count <= k:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

            


            
            
                


            
            