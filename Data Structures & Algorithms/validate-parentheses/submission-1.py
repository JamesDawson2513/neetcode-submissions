class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for char in s:
            if char in bracs.keys():
                stack.append(char)
            else:
                if stack == []:
                    return False
                popped = stack.pop()
                if bracs[popped] == char:
                    continue
                else:
                    return False
        
        if stack == []:
            return True
        else: 
            return False


