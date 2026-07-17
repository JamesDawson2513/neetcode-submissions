class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        index = 0
        height = 1
        res = 0
        for r in range(len(heights)):
            currentindex = r
            while stack != [] and heights[r] <= stack[-1][height]:
                area = (stack[-1][height])*(r-stack[-1][index])
                res = max(res,area)
                currentindex = stack[-1][index]
                stack.pop()
            stack.append([currentindex, heights[r]])
        while stack != []:
            area = (stack[-1][height])*(r + 1 - stack[-1][index])
            res = max(res,area)
            stack.pop()
        return res
