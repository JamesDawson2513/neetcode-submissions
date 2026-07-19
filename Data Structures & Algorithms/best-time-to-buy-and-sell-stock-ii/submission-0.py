class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tracker = 0
        total = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                tracker += 1
            elif prices[i+1] < prices[i] and tracker > 0:
                total += prices[i] - prices[i - tracker]
                tracker = 0
        if tracker > 0:
            i = len(prices)-1
            total += prices[i] - prices[i - tracker]
        return total


                
        