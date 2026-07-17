class Solution(object):
    def maxSlidingWindow(self, nums, k):
        output = []
        q = deque()
        l = r = 0
        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            if q[0] < l:
                q.popleft()
            if r-l+1 == k:
                output.append(nums[q[0]])
                l += 1
        return output