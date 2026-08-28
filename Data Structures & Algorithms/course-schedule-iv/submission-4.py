class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pres, trackr, posts = defaultdict(set), defaultdict(set),defaultdict(set)
        for a, b in prerequisites:
            pres[a].add(b)
            trackr[a].add(b)
            posts[b].add(a)
        q = collections.deque()
        for i in range(numCourses):
            if len(pres[i]) == 0:
                q.append(i)
        while q: 
            course = q.popleft()
            for post in posts[course]:
                for c in pres[course]:
                    pres[post].add(c)
                trackr[post].remove(course)
                if len(trackr[post]) == 0:
                    q.append(post)
        res = []
        for a, b in queries:
            if b in pres[a]: res.append(True)
            else: res.append(False)
        return res
