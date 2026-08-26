class Solution:
    def reorganizeString(self, s: str) -> str:
        minHeap = []
        res = ""
        count = Counter(s)
        for char in count:
            heapq.heappush(minHeap, [-count[char], char])
        while minHeap:
            print(minHeap, res)
            count, char = heapq.heappop(minHeap)
            res += char
            if not minHeap:
                if count != -1:
                    return ""
                else: return res
            count2, char2 = heapq.heappop(minHeap)
            res += char2
            if count != -1:
                heapq.heappush(minHeap, [count + 1, char])
            if count2 != -1:
                heapq.heappush(minHeap, [count2 + 1, char2])
        return res



