class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        indices = defaultdict(set)
        curSum = []
        prefix = 0

        indices[0].add(-1)

        for i in range(len(nums)):
            num = nums[i]
            prefix += num
            indices[prefix].add(i)
            curSum.append(prefix)

        res = 0
        
        for i in range(len(nums)):
            
            current_prefix = curSum[i]
            target = current_prefix - k
            
            for index in indices[target]:
                if index < i:
                    res += 1
        
        return res
            
        
        