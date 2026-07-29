class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        r,l = 0,0
        for i in range(len(s1)):
            count[s1[i]] = 1 + count.get(s1[i], 0)
        running = len(count.keys())
        while r < len(s2):
            print(r, count)
            if r > len(s1) - 1:
                if s2[l] in count.keys():
                    count[s2[l]] += 1
                    if count[s2[l]] == 0:
                        running -= 1
                    elif count[s2[l]] == 1:
                        running += 1
                l += 1
            if s2[r] in count.keys():
                count[s2[r]] -= 1
                if count[s2[r]] == 0:
                    running -= 1
                elif count[s2[r]] == -1:
                    running += 1
            r += 1
            if running == 0:
                return True
        print(r, count)
        return False