class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        bef = [-1]*n
        aft = [-1]*n
        res = 0

        for i in range(1,n):

            if height[i-1] > bef[i-1]:
                bef[i] = height[i-1]
            else:
                bef[i] = bef[i-1]
            
            if height[n - i] > aft[n - i]:
                aft[n-i-1] = height[n-i]
            else:
                aft[n-i-1] = aft[n-i]
        
        for i in range(1,n-1):
            res += max(0, min(bef[i],aft[i]) - height[i])

        return res

                



            
        