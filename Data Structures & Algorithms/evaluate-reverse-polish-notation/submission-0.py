class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for char in tokens:
            if char.lstrip('-').isdigit():
                stack.append(int(char))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if char == '+':
                    stack.append(num2 + num1)
                elif char == '-':
                    stack.append(num2 - num1)
                elif char == '*':
                    stack.append(num2 * num1)
                elif char == '/':
                    stack.append(int(num2 / num1))       
        return stack[0]