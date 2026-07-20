class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:
        stack = []
        for i in range(len(A)):
            cur = A[i]
            while stack and stack[-1] > 0 and cur < 0:
                if stack[-1] + cur == 0:
                    cur = 0
                    stack.pop()
                elif stack[-1] + cur < 0:
                    stack.pop()
                else:
                    cur = 0
            if cur != 0:
                stack.append(cur)
        
        return stack



        