class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(Close, Open):
            if Close == Open == n:
                res.append(''.join(stack))
            
            if Open < n:
                stack.append('(')
                backtrack(Close, Open + 1)
                stack.pop()
            
            if Close < Open:
                stack.append(')')
                backtrack(Close + 1, Open)
                stack.pop()
        backtrack(0,0)
        return res



        