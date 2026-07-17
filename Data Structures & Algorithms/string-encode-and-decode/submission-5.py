class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "£" + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        Bool = False
        counter = 0
        l = 0
        q = -1
        for i in range(len(s)):
            if i == q:
                if k == 0:
                    Bool = False
                    res[l] = ""
                    l += 1
                    counter = 0
            elif Bool == False and s[i+1] == "£":
                p = s[i-counter:i+1]
                k = int(p)
                res.append("")
                Bool = True
                q = i + 1
            elif Bool == False and s[i+1] != "£":
                counter +=1
            elif Bool == True:
                res[l] += (s[i])
                k -= 1
                if k == 0:
                    Bool = False
                    l += 1
                    counter = 0
        return res

                


