class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2): return False
        d1 = {}
        d2 = {}
        for i in range(26):
            d1[i] = 0
            d2[i] = 0
        for i in range(len(s1)):
            d1[ord(s1[i]) - ord('a')] += 1
            d2[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            if d1[i] == d2[i]:
                matches += 1
        if matches == 26:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            old = ord(s2[l]) - ord('a')
            if d1[old] == d2[old]:
                matches -= 1
            d2[old] -= 1
            if d1[old] == d2[old]:
                matches += 1
            l += 1
            new = ord(s2[r]) - ord('a')
            if d1[new] == d2[new]:
                matches -= 1
            d2[new] += 1
            if d1[new] == d2[new]:
                matches += 1
            if matches == 26:
                return True
        return False