class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L = 0
        for R in range(1,len(prices)):
            if prices[R] < prices[L]:
                L = R
            else:
                res = max(prices[R] - prices[L], res)
        return res


        