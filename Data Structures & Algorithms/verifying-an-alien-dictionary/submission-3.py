class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        chardict = {char: index for index, char in enumerate(order)}
        prev = []
        for word in words:
            cur = []
            same = True
            for i in range(len(word)):
                char = word[i]
                val = chardict[char]
                cur.append(val)
                if same and i < len(prev) and val < prev[i]:
                    return False
                elif i < len(prev) and val > prev[i]:
                    same = False
            if same and len(prev) > len(cur):
                return False
            prev = cur
        return True    
            
            




