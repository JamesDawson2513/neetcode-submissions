class Solution(object):
    def minWindow(self, s, t):
        res = ""
        tcon = set(t)
        tdic = {}
        cdic = {}
        satisfied = 0
        need = len(tcon)
        for char in t:
            tdic[char] = tdic.get(char, 0) + 1
            cdic[char] = 0
        l = 0
        for r in range(len(s)):
            if s[r] in tcon:
                cdic[s[r]] += 1
                if cdic[s[r]] == tdic[s[r]]:
                    satisfied += 1
            while satisfied == need:
                if res == "":
                    res = r - l + 1
                if res >= r - l + 1:
                    indices = [l,r]
                    res = r - l + 1 
                if s[l] in tcon:
                    cdic[s[l]] -= 1
                    if cdic[s[l]] == tdic[s[l]] - 1:
                        satisfied -= 1
                l += 1
        if res == "":
            return res
        else:
            return s[indices[0]:indices[1]+1]




            



        