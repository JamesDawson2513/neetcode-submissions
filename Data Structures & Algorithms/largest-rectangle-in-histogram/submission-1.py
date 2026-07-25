class Solution:
    def largestRectangleArea(self, H: List[int]) -> int:
        stack = []
        res = -1
        for r in range(len(H)):
            cur_i = r
            while stack and H[r] < stack[-1][1]:
                area = (stack[-1][1])*(r-stack[-1][0])
                res = max(res, area)
                cur_i = stack[-1][0]
                stack.pop()
            stack.append([cur_i, H[r]])
        r = len(H)
        while stack:
            area = (stack[-1][1])*(r - stack[-1][0])
            res = max(res, area)
            stack.pop()
        return res
        