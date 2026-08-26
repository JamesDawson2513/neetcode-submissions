class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = []
        time = 0
        num_passengers = 0
        onboard = []
        for passengers, start, end in trips:
            heapq.heappush(minHeap, [start, end, passengers])
        while minHeap:
            start, end, passengers = heapq.heappop(minHeap)
            while onboard and onboard[0][0] <= start:
                _, _, offpassengers = heapq.heappop(onboard)
                num_passengers -= offpassengers
            num_passengers += passengers
            if num_passengers > capacity:
                return False
            heapq.heappush(onboard, [end, start, passengers])
        return True