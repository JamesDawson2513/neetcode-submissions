class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        res = ""
        for char in t:
            count[char] = count.get(char, 0) + 1
        running = len(count)
        if len(t) > len(s):
            return res
        l,r = 0,0
        while r < len(s) and s[r] not in count:
            l,r = l+1, r+1
        while r < len(s):
            if s[r] in count:
                count[s[r]] -= 1
                if count[s[r]] == 0:
                    running -= 1
            
            while running == 0:
                print(count,s[l:r+1], running)
                if r-l+1 < len(res) or res == "":
                    res = s[l:r+1]
                if s[l] in count.keys():
                    count[s[l]] += 1
                    if count[s[l]] == 1:
                        running += 1
                l += 1
            while l < len(s) and s[l] not in count:
                l += 1
            r += 1

        return res