class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        num_passengers = 0
        onboard = []
        trips.sort(key=lambda x: x[1])
        for passengers, start, end in trips:
            while onboard and onboard[0][0] <= start:
                _, offpassengers = heapq.heappop(onboard)
                num_passengers -= offpassengers
            num_passengers += passengers
            if num_passengers > capacity:
                return False
            heapq.heappush(onboard, [end, passengers])
        return True