class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        if n < 3:
            return 0
        lmax = [0]*n
        rmax = [0]*n
        lmax[0],rmax[n-1] = height[0], height[n-1]
        for i in range(1, n-1):
            lmax[i] = max(lmax[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], height[i])
        for i in range(1,n-1):
            res += max(0, min(rmax[i],lmax[i]) - height[i])
        return res