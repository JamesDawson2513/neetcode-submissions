class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
            
        res = []
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def dfs(i, running):

            if i == len(digits):
                return res.append("".join(running))
            
            for char in phone[digits[i]]:
                running += [char]
                dfs(i+1, running)
                running.pop()
        dfs(0,[])
        return res

            