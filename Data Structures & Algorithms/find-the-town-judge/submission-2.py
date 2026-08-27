class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_scores = [0]*n
        for a, b in trust:
            trust_scores[a-1] -= 1
            trust_scores[b-1] += 1
        for i in range(n):
            if trust_scores[i] == n-1: return i + 1
        return -1
                       
            