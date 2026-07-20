class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            left, right = heights[l], heights[r]
            height = min(left, right)
            area = (r - l) * height
            if res < area:
                res = area
            if left < right:
                l += 1
            else:
                r -= 1
        
        return res

        