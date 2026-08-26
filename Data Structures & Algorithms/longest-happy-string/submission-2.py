class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        minHeap = []
        for count, char in [[-a, 'a'], [-b, 'b'], [-c, 'c']]:
            if count < 0:
                heapq.heappush(minHeap, [count, char])
        prev = None
        to_push = None
        while minHeap:
            print("minHeap: ", minHeap, "\n to_push: ", to_push,"\n prev: ", prev,"\n res: ", res)
            cnt, char = heapq.heappop(minHeap)
            if to_push:
                heapq.heappush(minHeap, to_push)
            if prev != char:
                res.append(char)
                if cnt < -1:
                    heapq.heappush(minHeap, [cnt + 1, char])
                to_push = None
            else:
                res.append(char)
                if cnt < -1:
                    to_push = [cnt + 1, char]
            prev = char
        return "".join(res)
        
                
        
                