class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        res = [0]*len(T)     
        stack = []

        for i in range(len(T)):
            cur = T[i]
            while stack and stack[-1][0] < T[i]:
                popped = stack.pop()
                res[popped[1]] = i - popped[1]
            stack.append([cur, i])

        return res



        
        