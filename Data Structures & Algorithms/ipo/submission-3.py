class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capitalHeap = []
        profitsHeap = []
        cur_capital = w
        for i in range(len(profits)):
            heapq.heappush(capitalHeap, [capital[i], profits[i]])
        for i in range(k):
            while capitalHeap and cur_capital >= capitalHeap[0][0]:
                _, push_profit = heapq.heappop(capitalHeap)
                heapq.heappush(profitsHeap, -push_profit)
            if profitsHeap:
                add_capital = - heapq.heappop(profitsHeap)
                cur_capital += add_capital
            else: 
                return cur_capital
        return cur_capital


