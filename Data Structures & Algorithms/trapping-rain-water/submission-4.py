class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        bef = [-1]*n
        aft = [-1]*n
        res = 0

        for i in range(1,n-1):
            
            bef[i] = max(height[i-1],bef[i-1])
            aft[n-i-1] = max(aft[n-i], height[n-i])

        for i in range(1,n-1):
            res += max(0, min(bef[i],aft[i]) - height[i])

        return res


                



            
        