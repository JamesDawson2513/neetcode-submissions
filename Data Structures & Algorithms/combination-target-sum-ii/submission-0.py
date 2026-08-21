class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        avoid = float('-inf')
        nums.sort()

        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(nums):
                return
            cur.append(nums[i])
            dfs(i+1, total + nums[i])
            cur.pop()
            avoid = nums[i]
            while i < len(nums) and nums[i] == avoid:
                i += 1
            dfs(i, total)
        
        dfs(0,0)
        return res

        