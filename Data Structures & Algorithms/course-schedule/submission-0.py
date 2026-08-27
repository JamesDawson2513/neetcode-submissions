class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        p_count = [0]*n
        post = defaultdict(set)
        num_courses = 0
        for after, before in prerequisites:
            p_count[after] += 1
            post[before].add(after)
        q = collections.deque()
        for i in range(n):
            if p_count[i] == 0:
                num_courses += 1
                q.append(i)
        while q:
            course = q.popleft()
            for dec in post[course]:
                p_count[dec] -= 1
                if p_count[dec] == 0:
                    q.append(dec)
                    num_courses += 1
        if num_courses == numCourses:
            return True
        else:
            return False

