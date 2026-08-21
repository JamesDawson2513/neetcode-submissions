class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total_sum = sum(nums)
        if total_sum % k != 0 or len(nums) < k:
            return False

        target = total_sum // k

        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        boxes = [0]*k

        def dfs(i) -> bool:
            if i == len(nums):
                return True

            for j in range(k):

                if boxes[j] + nums[i] <= target:
                    boxes[j] += nums[i]
                    if dfs(i+1):
                        return True
                    boxes[j] -= nums[i]
                
                if boxes[j] == 0:
                    break

            return False

        return dfs(0)