class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        perms = [[]]
        
        for i in range(len(nums)):
            new_perms = []
            for p in perms:
                for j in range(len(p) + 1):
                    if j > 0 and p[j-1] == nums[i]:
                        break
                    p_copy = p.copy()
                    p_copy.insert(j, nums[i])
                    new_perms.append(p_copy)
            perms = new_perms

        return perms