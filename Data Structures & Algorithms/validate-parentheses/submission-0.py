class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        openchars = {'(','{','['}
        closed = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in openchars:
                check.append(char)
            else:
                if len(check) == 0 or closed[check[-1]] != char:
                    return False
                else:
                    check.pop()
        if len(check) == 0:
            return True
        else:
            return False