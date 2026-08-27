class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        pres = [0]*numCourses
        posts = defaultdict(set)
        q = collections.deque()
        for after, before in prerequisites:
            pres[after] += 1
            posts[before].add(after)
        for i in range(numCourses):
            if pres[i] == 0:
                res.append(i)
                q.append(i)
        while q:
            course = q.popleft()
            for post in posts[course]:
                pres[post] -= 1
                if pres[post] == 0:
                    q.append(post)
                    res.append(post)
        if len(res) == numCourses:
            return res
        else:
            return []
