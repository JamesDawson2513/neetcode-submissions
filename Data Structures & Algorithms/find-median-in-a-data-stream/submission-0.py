class MedianFinder:

    def __init__(self):
        self.lowerHalf = [] # should be a maxHeap
        self.upperHalf = [] # should be a minHeap
        self.even = True
        

    def addNum(self, num: int) -> None:
        if self.even:
            if self.upperHalf and self.upperHalf[0] >= num:
                heapq.heappush(self.lowerHalf, -num)
            else:
                heapq.heappush(self.upperHalf, num)
                heapq.heappush(self.lowerHalf, -heapq.heappop(self.upperHalf))
            self.even = False
        else:
            if self.lowerHalf[0] >= - num:
                heapq.heappush(self.upperHalf, num)
            else:
                heapq.heappush(self.lowerHalf, - num)
                heapq.heappush(self.upperHalf, -heapq.heappop(self.lowerHalf))
            self.even = True

    def findMedian(self) -> float:
        if self.even:
            return (- self.lowerHalf[0] + self.upperHalf[0]) / 2
        else:
            return -self.lowerHalf[0]
        
        