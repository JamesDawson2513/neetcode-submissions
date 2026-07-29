class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q = collections.deque()
        r = 0

        for _ in range(k):
            q.append(arr[r])
            r += 1

        while r < len(arr):
            if x - q[0] <= arr[r] - x:
                return list(q)
            else:
                q.popleft()
                q.append(arr[r])
                r += 1
        
        return list(q)