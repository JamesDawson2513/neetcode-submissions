class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for op in operations:
            if op == "+":
                term = stack[-1] + stack[-2]
                total += term
                stack.append(term)
            elif op == "D":
                term = stack [-1]*2
                total += term
                stack.append(term)
            elif op == "C":
                term = stack.pop()
                total -= term
            else:
                term = int(op)
                total += term
                stack.append(term)
        return total
        