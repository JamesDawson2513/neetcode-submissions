class Solution:
    def decodeString(self, s: str) -> str:
        stack = [["",1]]
        i = 0
        while i < len(s):
            if s[i].isnumeric() == True:
                integer_str = s[i]
                i += 1
                while s[i] != "[":
                    integer_str = integer_str + s[i]
                    i += 1
                integer = int(integer_str)
                stack.append(["",integer])
                i += 1
            elif s[i] == "]":
                popped = stack.pop()
                add_str = popped[0] * popped[1]
                stack[-1][0] = stack[-1][0] + add_str
                i += 1
            else:
                stack[-1][0] = stack[-1][0] + s[i]
                i += 1
        return stack[0][0]